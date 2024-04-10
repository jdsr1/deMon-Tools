#!/bin/bash

#
## Script     : Plot optimization energies and forces from a deMon output.
##            : Plot MD temperature, energies and pressure. 
## Maintainer : JDSR <https://github.com/jdsr1>
## Last Change: 2024 Feb 16
#


# Starting time/step for plotting.
# Average for MD properties will be recalculated from this time on.
typeset -i time_0=0


# Parse program arguments.
while true; do
    case $1 in
       (-help|-h) echo -e " "
                  echo -e " Get help.\n"
                  exit;;
        (-opt|-o) shift
                  mode="optimization"
                  continue;;
         (-md|-m) shift
                  mode="dynamics"
                  mdtype=$(echo $1 | tr a-z A-Z)
                  shift
                  continue;;
      (-start|-s) shift
                  time_0=$1
                  shift
                  continue;;
      (-title|-t) shift
                  title=$1
                  shift
                  continue;;
             (-*) echo -e "\n Invalid option!\n"
                  exit 1;;
              (*) break;;
    esac
done

input=$1
if [[ -e $input ]]; then
    f=${input##*/}
    if [[ -z $title ]]; then
        title=${f/%.*}
    fi
else
    echo -e "\n File $input does not exists.\n"
    exit 2
fi


# Print runtype information.
echo -e "\n Input file: $input"

if [[ $mode == "optimization" ]]; then
    echo -e " Plotting OPT - Total energy and forces."
elif [[ $mode == "dynamics" ]]; then
    if [[ $mdtype == "NVE" || $mdtype == "NVT" ]]; then
        echo -e " Plotting MD $mdtype - Temperature and energies."
    elif [[ $mdtype == "NPT" ]]; then
        echo -e " Plotting MD $mdtype - Temperature, pressure and energies."
    else
        echo -e " Unknown MD ensemble: $mdtype. Switching to NVE."
        mdtype="NVE"
    fi
    if [[ $time_0 -gt 0 ]]; then
        echo -e " Average values calculated for t >= $time_0 fs."
    fi
fi


# Make temporary working directory.
curdir=$(pwd)
wrkdir="/tmp/Plotter.$$"
mkdir $wrkdir

cp $input $wrkdir/.
cd $wrkdir


# File names.
gdat=${f/out/dat}
grms=${f/out/rms}
gmax=${f/out/max}
gawk=${f/out/awk}
ggpl=${f/out/gpl}
gpng=${f/out/png}


# Get plotting information.
if [[ $mode == "optimization" ]]; then
    awk '/TOTAL ENERGY/ {print $4}' $f > $gdat
    awk '/RMSQ FORCE/   {print $4}' $f > $grms
    awk '/MAX FORCE/    {print $4}' $f > $gmax
elif [[ $mode == "dynamics" ]]; then
    if [[ $mdtype == "NVE" || $mdtype == "NVT" ]]; then
        cat >$gawk <<-***
        /^ TIME\\>/ {time = 1}
        /^ [ 0-9]+\\.[0-9]+/ { 
            if (\$1 >= $time_0) {
                entry = 1 
                count = count + 1
                sum6 = sum6 + \$2
                sum7 = sum7 + \$5
                sum62 = sum62 + \$2^2
                sum72 = sum72 + \$5^2
                \$6 = sum6/count
                \$7 = sum7/count
            }
            }
        { if (time || entry) printf("%s\\n", \$0) }
        time = 0
        entry = 0
        END {
          a6 = sum6/count
          a7 = sum7/count
          s6 = sqrt(sum62/count - a6^2)
          s7 = sqrt(sum72/count - a7^2)
          printf(" Average and standard deviations over %d data points:\\n", count)
          printf(" T %20.6f %20.6f\\n", a6, s6)
          printf(" E %20.6f %20.6f\\n", a7, s7)
        }
***
    awk -f $gawk $f > $gdat
    tail -3 $gdat
    elif [[ $mdtype == "NPT" ]]; then
        cat >$gawk <<-***
        /^ TIME\\>/ {time = 1}
        /^ [ 0-9]+\\.[0-9]+/ { 
            if (\$1 >= $time_0) {
                entry = 1 
                count = count + 1
                sum7 = sum7 + \$2
                sum8 = sum8 + \$3
                sum9 = sum9 + \$6
                sum72 = sum72 + \$2^2
                sum82 = sum82 + \$3^2
                sum92 = sum92 + \$6^2
                \$7 = sum7/count
                \$8 = sum8/count
                \$9 = sum9/count
            }
            }
        { if (time || entry) printf("%s\\n", \$0) }
        time = 0
        entry = 0
        END {
          a7 = sum7/count
          a8 = sum8/count
          a9 = sum9/count
          s7 = sqrt(sum72/count - a7^2)
          s8 = sqrt(sum82/count - a8^2)
          s9 = sqrt(sum92/count - a9^2)
          printf(" Average and standard deviations over %d data points:\\n", count)
          printf(" T %20.6f %20.6f\\n", a7, s7)
          printf(" p %20.6f %20.6f\\n", a8, s8)
          printf(" E %20.6f %20.6f\\n", a9, s9)
        }
***
    awk -f $gawk $f > $gdat
    tail -4 $gdat
    fi
fi


# Write gnuplot script.
if [[ $mode == "optimization" ]]; then
    cat >$ggpl <<-***
    #!/usr/bin/gnuplot
    set terminal png size 640,640
    set size square
    set output "$gpng"
    #    
    set title "$title. OPT"
    set xlabel "Step" textcolor rgb "blue"
    set ylabel "Energy [a.u.]" textcolor rgb "blue"
    set y2label "Force [a.u.]" textcolor rgb "blue"
    #
    set ytics nomirror
    set y2tics
    set format y  "%.2f"
    set format y2 "%.2f"
    #
    plot "$gdat" axes x1y1 with lines linewidth 3 title "Energy",\
         "$grms" axes x1y2 with lines linewidth 3 title "RMS Force",\
         "$gmax" axes x1y2 with lines linewidth 3 title "MAX Force"
***
elif [[ $mode == "dynamics" ]]; then
    if [[ $mdtype == "NVE" || $mdtype == "NVT" ]]; then
        cat >$ggpl <<-***
        #!/usr/bin/gnuplot
        set terminal png size 1000,500 font "sans-serif,10"
        set output "$gpng"
        #    
        set multiplot layout 1,2 title "$title. MD $mdtype"
        set xlabel "Time [fs]"
        #
        ntics = 4
        stats "$gdat" using 1 name "time" nooutput
        set xtics time_max/ntics
        #
        set title "Temperature [K]" textcolor rgb "blue"
        plot "$gdat" using 1:2 with lines title "T(t)",\
             "" using 1:6 with lines linewidth 2.0 title "<T>"
        set title "Kinetic, Potential and System Energies [a.u.]"
        plot "$gdat" using 1:3 with lines title "E_{KIN}(t)",\
             "" using 1:4 with lines title "E_{POT}(t)",\
             "" using 1:5 with lines title "E_{SYS}(t)"
***
    elif [[ $mdtype == "NPT" ]]; then
        cat >$ggpl <<-***
        #!/usr/bin/gnuplot
        set terminal png size 800,800 font "sans-serif,10"
        set output "$gpng"
        #    
        set multiplot layout 2,2 title "$title. MD $mdtype"
        set xlabel "Time [fs]"
        #
        ntics = 4
        stats "$gdat" using 1 name "time" nooutput
        set xtics time_max/ntics
        #
        set title "Temperature [K]" textcolor rgb "blue"
        plot "$gdat" using 1:2 with lines title "T(t)",\
             "" using 1:7 with lines linewidth 2.0 title "<T>"
        set title "Pressure [bar]"
        plot "$gdat" using 1:3 with lines title "p(t)",\
             "" using 1:8 with lines linewidth 2.0 title "<p>"
        set title "Kinetic, Potential and Total Energies [a.u.]"
        plot "$gdat" using 1:4 with lines title "E_{KIN}(t)",\
             "" using 1:5 with lines title "E_{POT}(t)",\
             "" using 1:(\$4+\$5) with lines title "E_{TOT}(t)",\
             "" using 1:6 with lines title "E_{SYS}(t)"
        set title "System Energy [a.u.]"
        plot "$gdat" using 1:6 with lines title "E_{SYS}(t)",\
             "" using 1:9 with lines linewidth 2.0 title "<E_{SYS}>"
***
    fi
fi


# Generate png file.
gnuplot $ggpl >/dev/null 2>Plotter.log

if [[ $? -eq 0 ]]; then
    cp $gpng $curdir/.
    cd $curdir 
    rm -rf $wrkdir
    display $gpng 
else
    echo -e "\n png file could not be generated. gnuplot says:\n"
    cat Plotter.log
    cd $curdir 
    rm -rf $wrkdir
    exit 3
fi

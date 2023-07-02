#!/bin/bash

#
## Script     : Plot optimization energies and forces from a deMon output.
## Maintainer : JDSR <https://github.com/jdsr1>
## Last Change: 2023 Jul 02
#

# Process script arguments
if [[ -e $1 ]]; then
    echo -e "\n Generating png file for $1"
    f=${1##*/}
else
    echo -e "\n ERROR: File $1 does not exists.\n"
    exit 1
fi

title=$f
[[ -n "$2" ]] && title=$2

# Make temporary working directory
curdir=$(pwd)
wrkdir="/tmp/Plotter.$$"
mkdir $wrkdir
echo -e " Creating temporary directory at $wrkdir"

# Copy file into working directory and go there
cp $1 $wrkdir/.
cd $wrkdir

# File names with plotting data, gnuplot script and png file
gdat=${f/out/dat}
grms=${f/out/rms}
gmax=${f/out/max}
ggpl=${f/out/gpl}
gpng=${f/out/png}

# Get energies and forces
awk '/TOTAL ENERGY/ {print $4}' $f > $gdat
awk '/RMSQ FORCE/   {print $4}' $f > $grms
awk '/MAX FORCE/    {print $4}' $f > $gmax

# Get final energy and total time
ef=$(tail -n 1 $gdat)
tt=$(awk '/TOTAL TIME/ {print $NF}' $f | tail -1)

# Write gnuplot script
cat >$ggpl <<-***
#!/usr/bin/gnuplot
set terminal png size 640,640
set size square
set output "$gpng"
#    
set title   "$title\n{/*0.8 E=$ef ($tt s)}"
set xlabel  "Step"   textcolor rgb "red"
set ylabel  "Energy" textcolor rgb "red"
set y2label "Force"  textcolor rgb "red"
#
set ytics nomirror
set y2tics
set format y  '%.4f'
set format y2 '%.4f'
#
plot '$gdat' axes x1y1 with lines linewidth 3 title 'Energy',\
     '$grms' axes x1y2 with lines linewidth 3 title 'RMS Force',\
     '$gmax' axes x1y2 with lines linewidth 3 title 'MAX Force'
#
***

# Generate png file
gnuplot $ggpl >/dev/null 2>Plotter.log

# Check gnuplot exit status
if [[ $? -eq 0 ]]; then
    cp $gpng $curdir/.
    echo -e " File $gpng saved in $curdir"
    cd $curdir 
    rm -rf $wrkdir
    echo -e " Directory $wrkdir deleted\n"
else
    echo -e "\n ERROR: png file could not be generated. gnuplot says:\n"
    cat Plotter.log
    cd $curdir 
    rm -rf $wrkdir
    echo -e "\n Directory $wrkdir deleted\n"
    exit 2
fi


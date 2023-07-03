#!/usr/bin/python

# Physical constants and conversion factors as defined in deMon2k
# version 6.2.0.

import math

MAXMOM = 3 # Maximum rank of electrostatic moments. From parameter.h

# ----------------------------------------------------------------------

#
#     Purpose: Initialization of physical constants.
#
#     Lit.: CODATA constants from http://www.codata.org (2002)
#           Periodic Table from http://pearl1.lanl.gov/periodic (2004)
#
#     History: - Creation (28.05.97, MK)
#                         (04.09.04, RFM)
#                         (03.05.05, AG)
#                         (03.10.17, MA)
#                         (15.07.20, AMK)
#
#     ******************************************************************
#
#     List of variables:
#
#     ABC     : Frequency labels.
#     ABOHR   : Bohr radius [m].
#     AFINE   : Fine-structure constant.
#     AMU     : Conversion factor [amu] -> [atomic units].
#     AMUKG   : Conversion factor [amu] -> [kg].
#     AOSYM   : Atomic orbital symbols.
#     BOHR    : Conversion factor [Angstrom] -> [Bohr].
#     CLIGHT  : Speed of light in vacuum [m/s].
#     CMM     : Coulomb type constant for MM [kcal/mol].
#     COVRAD  : Atomic covalent radii [Angstrom] -> [Bohr].
#     D3CR    : Atomic covalent radii used by D3 dispersion
#               [Angstrom] -> [Bohr].
#     ECHARGE : Elementary charge [C].
#     ELCONF  : Element configuration.
#     ELGRP   : Element group.
#     ELSYM   : Element symbols.
#     EMASS   : Electron mass [kg].
#     EPSI0   : Electric field constant [F/m].
#     ESU     : Conversion factors [Hartree] -> [esu].
#     EVOLT   : Conversion factor [Hartree] -> [eV].
#     FSEC    : Conversion factor [fsec] -> [atomic units].
#     HPLANCK : Planck constant [J*s].
#     HZ      : Conversion factor [Hartree] -> [Hz].
#     KBOLTZ  : Boltzmann constant [J/K].
#     KCALMOL : Conversion factor [Hartree] -> [kcal/mol].
#     KJMOL   : Conversion factor [Hartree] -> [kJ/mol].
#     JOULE   : Conversion factor [Hartree] -> [J].
#     MHZ     : Conversion factor [Hartree] -> [MHz].
#     MUPERM  : Permeability of vacuum [N/A**2].
#     NAVOG   : Avogrado constant [1/mol].
#     NOS     : Labels for matrix numbers.
#     PASCAL  : Conversion factor [a.u.] -> [Pa].
#     PPM     : Parts per million [ppm].
#     PRESSURE: Standard pressure [Pa].
#     RGAS    : Gas constant [J/(K*mol)].
#     RYDBERG : Rydberg constant [1/m].
#     STDMATOM: Standard atomic masses.
#     VDWRAD  : Atomic van der Waals radii [Angstrom] -> [Bohr].
#     VIBFAC  : Conversion factor [Hartree/Bohr**2] -> [1/cm].
#     WAVENUM : Conversion factor [Hartree] -> [1/cm] (wave numbers).
#     WAVESEC : Conversion factor [1/cm] -> [1/sec].
#     XYZ     : Labels for the Cartesian components.
#
#     ------------------------------------------------------------------
#
#
#     ------------------------------------------------------------------
#
## Definition of standard covalent radii [Angstrom]        
## Lit.: R.T. Sanderson, Inorganic Chemistry, Reinhold 1967
#
COVRAD = []
COVRAD.append(0.00)
COVRAD.append(0.32)
COVRAD.append(0.93)
COVRAD.append(1.23)
COVRAD.append(0.90)
COVRAD.append(0.82)
COVRAD.append(0.77)
COVRAD.append(0.75)
COVRAD.append(0.73)
COVRAD.append(0.72)
COVRAD.append(0.71)
COVRAD.append(1.54)
COVRAD.append(1.36)
COVRAD.append(1.18)
COVRAD.append(1.11)
COVRAD.append(1.06)
COVRAD.append(1.02)
COVRAD.append(0.99)
COVRAD.append(0.98)
COVRAD.append(2.03)
COVRAD.append(1.74)
COVRAD.append(1.44)
COVRAD.append(1.32)
COVRAD.append(1.22)
COVRAD.append(1.18)
COVRAD.append(1.17)
COVRAD.append(1.17)
COVRAD.append(1.16)
COVRAD.append(1.15)
COVRAD.append(1.17)
COVRAD.append(1.25)
COVRAD.append(1.26)
COVRAD.append(1.22)
COVRAD.append(1.20)
COVRAD.append(1.16)
COVRAD.append(1.14)
COVRAD.append(1.12)
COVRAD.append(2.16)
COVRAD.append(1.91)
COVRAD.append(1.62)
COVRAD.append(1.45)
COVRAD.append(1.34)
COVRAD.append(1.30)
COVRAD.append(1.27)
COVRAD.append(1.25)
COVRAD.append(1.25)
COVRAD.append(1.28)
COVRAD.append(1.34)
COVRAD.append(1.48)
COVRAD.append(1.44)
COVRAD.append(1.41)
COVRAD.append(1.40)
COVRAD.append(1.36)
COVRAD.append(1.33)
COVRAD.append(1.31)
COVRAD.append(2.35)
COVRAD.append(1.98)
COVRAD.append(1.69)
COVRAD.append(1.65)
COVRAD.append(1.65)
COVRAD.append(1.64)
COVRAD.append(1.63)
COVRAD.append(1.62)
COVRAD.append(1.85)
COVRAD.append(1.61)
COVRAD.append(1.59)
COVRAD.append(1.59)
COVRAD.append(1.58)
COVRAD.append(1.57)
COVRAD.append(1.56)
COVRAD.append(1.74)
COVRAD.append(1.56)
COVRAD.append(1.44)
COVRAD.append(1.34)
COVRAD.append(1.30)
COVRAD.append(1.28)
COVRAD.append(1.26)
COVRAD.append(1.27)
COVRAD.append(1.30)
COVRAD.append(1.34)
COVRAD.append(1.49)
COVRAD.append(1.48)
COVRAD.append(1.47)
COVRAD.append(1.46)
COVRAD.append(1.46)
COVRAD.append(1.45)
COVRAD.append(1.90)
COVRAD.append(1.65)
COVRAD.append(1.42)
COVRAD.append(1.34)
COVRAD.append(1.55)
COVRAD.append(1.89)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
COVRAD.append(2.00)
#
## Definition of covalent radii used in D3 [Angstrom]     
## Lit.: P. Pyykko, M. Atsumi, Chem. Eur. J. 15,186 (2009)
## All covalent radii for metals are decreased by 10%     
#
D3CR = []
D3CR.append(0.00)
D3CR.append(0.32)
D3CR.append(0.46)
D3CR.append(1.20)
D3CR.append(0.94)
D3CR.append(0.77)
D3CR.append(0.75)
D3CR.append(0.71)
D3CR.append(0.63)
D3CR.append(0.64)
D3CR.append(0.67)
D3CR.append(1.40)
D3CR.append(1.25)
D3CR.append(1.13)
D3CR.append(1.04)
D3CR.append(1.10)
D3CR.append(1.02)
D3CR.append(0.99)
D3CR.append(0.96)
D3CR.append(1.76)
D3CR.append(1.54)
D3CR.append(1.33)
D3CR.append(1.22)
D3CR.append(1.21)
D3CR.append(1.10)
D3CR.append(1.07)
D3CR.append(1.04)
D3CR.append(1.00)
D3CR.append(0.99)
D3CR.append(1.01)
D3CR.append(1.09)
D3CR.append(1.12)
D3CR.append(1.09)
D3CR.append(1.15)
D3CR.append(1.10)
D3CR.append(1.14)
D3CR.append(1.17)
D3CR.append(1.89)
D3CR.append(1.67)
D3CR.append(1.47)
D3CR.append(1.39)
D3CR.append(1.32)
D3CR.append(1.24)
D3CR.append(1.15)
D3CR.append(1.13)
D3CR.append(1.13)
D3CR.append(1.08)
D3CR.append(1.15)
D3CR.append(1.23)
D3CR.append(1.28)
D3CR.append(1.26)
D3CR.append(1.26)
D3CR.append(1.23)
D3CR.append(1.32)
D3CR.append(1.31)
D3CR.append(2.09)
D3CR.append(1.76)
D3CR.append(1.62)
D3CR.append(1.47)
D3CR.append(1.58)
D3CR.append(1.57)
D3CR.append(1.56)
D3CR.append(1.55)
D3CR.append(1.51)
D3CR.append(1.52)
D3CR.append(1.51)
D3CR.append(1.50)
D3CR.append(1.49)
D3CR.append(1.49)
D3CR.append(1.48)
D3CR.append(1.53)
D3CR.append(1.46)
D3CR.append(1.37)
D3CR.append(1.31)
D3CR.append(1.23)
D3CR.append(1.18)
D3CR.append(1.16)
D3CR.append(1.11)
D3CR.append(1.12)
D3CR.append(1.13)
D3CR.append(1.32)
D3CR.append(1.30)
D3CR.append(1.30)
D3CR.append(1.36)
D3CR.append(1.31)
D3CR.append(1.38)
D3CR.append(1.42)
D3CR.append(2.01)
D3CR.append(1.81)
D3CR.append(1.67)
D3CR.append(1.58)
D3CR.append(1.52)
D3CR.append(1.53)
D3CR.append(1.54)
D3CR.append(1.55)
D3CR.append(1.66)
D3CR.append(1.66)
D3CR.append(1.68)
D3CR.append(1.68)
D3CR.append(1.65)
D3CR.append(1.67)
D3CR.append(1.73)
D3CR.append(1.76)
D3CR.append(1.61)
D3CR.append(1.57)
D3CR.append(1.49)
D3CR.append(1.43)
D3CR.append(1.41)
D3CR.append(1.34)
D3CR.append(1.29)
D3CR.append(1.28)
D3CR.append(1.21)
#
## Definition of standard van der Waals radii [Angstrom] 
## Lit.: A. Bondi, J. Phys. Chem. 68, 441 (1964)         
#
VDWRAD = []
VDWRAD.append(0.00)
VDWRAD.append(1.20)
VDWRAD.append(1.40)
VDWRAD.append(1.82)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(1.70)
VDWRAD.append(1.55)
VDWRAD.append(1.52)
VDWRAD.append(1.47)
VDWRAD.append(1.54)
VDWRAD.append(2.27)
VDWRAD.append(1.73)
VDWRAD.append(2.00)
VDWRAD.append(2.10)
VDWRAD.append(1.80)
VDWRAD.append(1.80)
VDWRAD.append(1.75)
VDWRAD.append(1.88)
VDWRAD.append(2.75)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(1.63)
VDWRAD.append(1.40)
VDWRAD.append(2.00)
VDWRAD.append(1.87)
VDWRAD.append(2.00)
VDWRAD.append(1.85)
VDWRAD.append(1.90)
VDWRAD.append(1.85)
VDWRAD.append(2.02)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(1.63)
VDWRAD.append(1.72)
VDWRAD.append(1.58)
VDWRAD.append(1.93)
VDWRAD.append(2.17)
VDWRAD.append(2.00)
VDWRAD.append(2.06)
VDWRAD.append(1.98)
VDWRAD.append(2.16)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(1.72)
VDWRAD.append(1.66)
VDWRAD.append(1.55)
VDWRAD.append(1.96)
VDWRAD.append(2.02)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(1.86)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
VDWRAD.append(2.00)
#
## Definition of empirical atomic C6 coefficients [a.u.]    
## The formal oxidation number (FON) are given as comment   
## C6 coefficients for H, C, N, O are taken from:           
## Lit.: Q. Wu, W. Yang, J. Chem. Phys. 116, 515 (2002)     
## All other C6 coefficients are taken from UFF:            
## Lit.: A. Rappe et al., J. Am. Chem. Soc 114, 10024 (1992)
#
CSIX = []
CSIX.append(0.000)
CSIX.append(2.845)       # FON =  0
CSIX.append(1.109)       # FON =  0
CSIX.append(0.787)       # FON =  0
CSIX.append(5.278)       # FON =  0
CSIX.append(121.048)     # FON =  0
CSIX.append(26.360)      # FON =  0
CSIX.append(19.480)      # FON =  0
CSIX.append(12.415)      # FON =  0
CSIX.append(10.518)      # FON =  0
CSIX.append(7.092)       # FON =  0
CSIX.append(3.068)       # FON =  0
CSIX.append(12.247)      # FON = +2
CSIX.append(607.850)     # FON =  0
CSIX.append(366.281)     # FON =  0
CSIX.append(225.171)     # FON =  0
CSIX.append(171.641)     # FON =  0
CSIX.append(124.577)     # FON =  0
CSIX.append(89.929)      # FON =  0
CSIX.append(15.588)      # FON =  0
CSIX.append(53.271)      # FON = +2
CSIX.append(3.529)       # FON = +3
CSIX.append(2.528)       # FON = +4
CSIX.append(2.243)       # FON = +5
CSIX.append(1.662)       # FON = +3
CSIX.append(1.272)       # FON = +2
CSIX.append(1.151)       # FON = +2
CSIX.append(1.140)       # FON = +3
CSIX.append(1.128)       # FON = +2
CSIX.append(1.323)       # FON = +1
CSIX.append(8.008)       # FON = +2
CSIX.append(427.057)     # FON = +3
CSIX.append(338.151)     # FON =  0
CSIX.append(256.927)     # FON =  0
CSIX.append(233.506)     # FON =  0
CSIX.append(196.854)     # FON =  0
CSIX.append(161.014)     # FON =  0
CSIX.append(28.148)      # FON =  0
CSIX.append(79.470)      # FON = +2
CSIX.append(14.639)      # FON = +3
CSIX.append(9.309)       # FON = +2
CSIX.append(8.608)       # FON = +5
CSIX.append(6.569)       # FON = +6
CSIX.append(5.059)       # FON = +5
CSIX.append(5.500)       # FON = +2
CSIX.append(4.857)       # FON = +3
CSIX.append(4.136)       # FON = +2
CSIX.append(5.085)       # FON = +1
CSIX.append(17.660)      # FON = +2
CSIX.append(687.064)     # FON = +3
CSIX.append(590.699)     # FON =  0
CSIX.append(485.947)     # FON = +3
CSIX.append(460.826)     # FON = +2
CSIX.append(408.586)     # FON =  0
CSIX.append(351.585)     # FON =  0
CSIX.append(55.478)      # FON =  0
CSIX.append(136.217)     # FON = +2
CSIX.append(4.710)       # FON = +3
CSIX.append(3.815)       # FON = +3
CSIX.append(3.191)       # FON = +3
CSIX.append(3.030)       # FON = +3
CSIX.append(2.610)       # FON = +3
CSIX.append(2.209)       # FON = +3
CSIX.append(2.109)       # FON = +3
CSIX.append(1.907)       # FON = +3
CSIX.append(1.716)       # FON = +3
CSIX.append(1.649)       # FON = +3
CSIX.append(1.595)       # FON = +3
CSIX.append(1.545)       # FON = +3
CSIX.append(1.285)       # FON = +3
CSIX.append(47.195)      # FON = +3
CSIX.append(13.842)      # FON = +3
CSIX.append(10.036)      # FON = +4
CSIX.append(11.930)      # FON = +5
CSIX.append(8.126)       # FON =  0
CSIX.append(6.365)       # FON = +5
CSIX.append(4.954)       # FON = +6
CSIX.append(5.560)       # FON = +3
CSIX.append(5.066)       # FON = +2
CSIX.append(7.218)       # FON = +3
CSIX.append(21.891)      # FON = +2
CSIX.append(665.972)     # FON = +3
CSIX.append(605.780)     # FON =  0
CSIX.append(523.633)     # FON = +3
CSIX.append(514.357)     # FON = +2
CSIX.append(473.466)     # FON =  0
CSIX.append(421.345)     # FON =  0
CSIX.append(100.451)     # FON =  0
CSIX.append(144.928)     # FON = +2
CSIX.append(8.478)       # FON = +3
CSIX.append(5.789)       # FON = +4
CSIX.append(5.146)       # FON = +4
CSIX.append(4.890)       # FON = +4
CSIX.append(4.444)       # FON = +4
CSIX.append(3.742)       # FON = +4
CSIX.append(3.035)       # FON = +4
CSIX.append(2.554)       # FON = +3
CSIX.append(2.615)       # FON = +3
CSIX.append(2.495)       # FON = +3
CSIX.append(2.245)       # FON = +3
CSIX.append(2.193)       # FON = +3
CSIX.append(1.966)       # FON = +3
CSIX.append(1.875)       # FON = +3
CSIX.append(1.833)       # FON = +3
CSIX.append(1.833)       # FON = +3
CSIX.append(1.833)       # FON = +3
CSIX.append(1.833)       # FON = +3
CSIX.append(1.833)       # FON = +3
CSIX.append(1.833)       # FON = +3
CSIX.append(1.833)       # FON = +3
CSIX.append(1.833)       # FON = +3
CSIX.append(1.833)       # FON = +3
#
## Empirical atomic values of multipole expectation values  
## ratio <r^4>/<r^2>  derived from atomic densities  [a.u.] 
## Lit.: S. Grimme et al., J. Chem. Phys. 132, 154104 (2010)
#
R2R4 = []
R2R4.append(8.0589)
R2R4.append(3.4698)
R2R4.append(29.0974)
R2R4.append(14.8517)
R2R4.append(11.8799)
R2R4.append(7.8715)
R2R4.append(5.5588)
R2R4.append(4.7566)
R2R4.append(3.8025)
R2R4.append(3.1036)
R2R4.append(26.1552)
R2R4.append(17.2304)
R2R4.append(17.7210)
R2R4.append(12.7442)
R2R4.append(9.5361)
R2R4.append(8.1652)
R2R4.append(6.7463)
R2R4.append(5.6004)
R2R4.append(29.2012)
R2R4.append(22.3934)
R2R4.append(19.0598)
R2R4.append(16.8590)
R2R4.append(15.4023)
R2R4.append(12.5589)
R2R4.append(13.4788)
R2R4.append(12.2309)
R2R4.append(11.2809)
R2R4.append(10.5569)
R2R4.append(10.1428)
R2R4.append(9.4907)
R2R4.append(13.4606)
R2R4.append(10.8544)
R2R4.append(8.9386)
R2R4.append(8.1350)
R2R4.append(7.1251)
R2R4.append(6.1971)
R2R4.append(30.0162)
R2R4.append(24.4103)
R2R4.append(20.3537)
R2R4.append(17.4780)
R2R4.append(13.5528)
R2R4.append(11.8451)
R2R4.append(11.0355)
R2R4.append(10.1997)
R2R4.append(9.5414)
R2R4.append(9.0061)
R2R4.append(8.6417)
R2R4.append(8.9975)
R2R4.append(14.0834)
R2R4.append(11.8333)
R2R4.append(10.0179)
R2R4.append(9.3844)
R2R4.append(8.4110)
R2R4.append(7.5152)
R2R4.append(32.7622)
R2R4.append(27.5708)
R2R4.append(23.1671)
R2R4.append(21.6003)
R2R4.append(20.9615)
R2R4.append(20.4562)
R2R4.append(20.1010)
R2R4.append(19.7475)
R2R4.append(19.4828)
R2R4.append(15.6013)
R2R4.append(19.2362)
R2R4.append(17.4717)
R2R4.append(17.8321)
R2R4.append(17.4237)
R2R4.append(17.1954)
R2R4.append(17.1631)
R2R4.append(14.5716)
R2R4.append(15.8758)
R2R4.append(13.8989)
R2R4.append(12.4834)
R2R4.append(11.4421)
R2R4.append(10.2671)
R2R4.append(8.3549)
R2R4.append(7.8496)
R2R4.append(7.3278)
R2R4.append(7.482)
R2R4.append(13.5124)
R2R4.append(11.6554)
R2R4.append(10.0959)
R2R4.append(9.7340)
R2R4.append(8.8584)
R2R4.append(8.0125)
R2R4.append(29.8135)
R2R4.append(26.3157)
R2R4.append(19.1885)
R2R4.append(15.8542)
R2R4.append(16.1305)
R2R4.append(15.6161)
R2R4.append(15.1226)
R2R4.append(16.1576)
#
#
## Definition of element configuration
## http://pearl1.lanl.gov/periodic    
#
ELCONF = []
ELCONF.append('1s^1')
ELCONF.append('1s^1')
ELCONF.append('1s^2')
ELCONF.append('[He] 2s^1')
ELCONF.append('[He] 2s^2')
ELCONF.append('[He] 2s^2 2p^1')
ELCONF.append('[He] 2s^2 2p^2')
ELCONF.append('[He] 2s^2 2p^3')
ELCONF.append('[He] 2s^2 2p^4'  )
ELCONF.append('[He] 2s^2 2p^5')
ELCONF.append('[He] 2s^2 2p^6')
ELCONF.append('[Ne] 3s^1')
ELCONF.append('[Ne] 3s^2')
ELCONF.append('[Ne] 3s^2 3p^1')
ELCONF.append('[Ne] 3s^2 3p^2')
ELCONF.append('[Ne] 3s^2 3p^3')
ELCONF.append('[Ne] 3s^2 3p^4')
ELCONF.append('[Ne] 3s^2 3p^5')
ELCONF.append('[Ne] 3s^2 3p^6')
ELCONF.append('[Ar] 4s^1')
ELCONF.append('[Ar] 4s^2')
ELCONF.append('[Ar] 4s^2 3d^1')
ELCONF.append('[Ar] 4s^2 3d^2')
ELCONF.append('[Ar] 4s^2 3d^3')
ELCONF.append('[Ar] 3d^5 4s^1')
ELCONF.append('[Ar] 4s^2 3d^5')
ELCONF.append('[Ar] 4s^2 3d^6')
ELCONF.append('[Ar] 4s^2 3d^7')
ELCONF.append('[Ar] 4s^2 3d^8')
ELCONF.append('[Ar] 3d^10 4s^1')
ELCONF.append('[Ar] 3d^10 4s^2')
ELCONF.append('[Ar] 3d^10 4s^2 4p^1')
ELCONF.append('[Ar] 3d^10 4s^2 4p^2')
ELCONF.append('[Ar] 3d^10 4s^2 4p^3')
ELCONF.append('[Ar] 3d^10 4s^2 4p^4')
ELCONF.append('[Ar] 3d^10 4s^2 4p^5')
ELCONF.append('[Ar] 3d^10 4s^2 4p^6')
ELCONF.append('[Kr] 5s^1')
ELCONF.append('[Kr] 5s^2')
ELCONF.append('[Kr] 5s^2 4d^1')
ELCONF.append('[Kr] 5s^2 4d^2')
ELCONF.append('[Kr] 4d^4 5s^1')
ELCONF.append('[Kr] 4d^5 5s^1')
ELCONF.append('[Kr] 5s^2 4d^5')
ELCONF.append('[Kr] 4d^7 5s^1')
ELCONF.append('[Kr] 4d^8 5s^1')
ELCONF.append('[Kr] 4d^10 5s^0')
ELCONF.append('[Kr] 4d^10 5s^1')
ELCONF.append('[Kr] 4d^10 5s^2')
ELCONF.append('[Kr] 4d^10 5s^2 5p^1')
ELCONF.append('[Kr] 4d^10 5s^2 5p^2')
ELCONF.append('[Kr] 4d^10 5s^2 5p^3')
ELCONF.append('[Kr] 4d^10 5s^2 5p^4')
ELCONF.append('[Kr] 4d^10 5s^2 5p^5')
ELCONF.append('[Kr] 4d^10 5s^2 5p^6')
ELCONF.append('[Xe] 6s^1')
ELCONF.append('[Xe] 6s^2')
ELCONF.append('[Xe] 6s^2 5d^1')
ELCONF.append('[Xe] 4f^1 6s^2 5d^1')
ELCONF.append('[Xe] 4f^3 6s^2')
ELCONF.append('[Xe] 4f^4 6s^2')
ELCONF.append('[Xe] 4f^5 6s^2')
ELCONF.append('[Xe] 4f^6 6s^2')
ELCONF.append('[Xe] 4f^7 6s^2')
ELCONF.append('[Xe] 4f^7 6s^2 5d^1')
ELCONF.append('[Xe] 4f^9 6s^2')
ELCONF.append('[Xe] 4f^10 6s^2')
ELCONF.append('[Xe] 4f^11 6s^2')
ELCONF.append('[Xe] 4f^12 6s^2')
ELCONF.append('[Xe] 4f^13 6s^2')
ELCONF.append('[Xe] 4f^14 6s^2')
ELCONF.append('[Xe] 4f^14 6s^2 5d^1')
ELCONF.append('[Xe] 4f^14 6s^2 5d^2')
ELCONF.append('[Xe] 4f^14 6s^2 5d^3')
ELCONF.append('[Xe] 4f^14 6s^2 5d^4')
ELCONF.append('[Xe] 4f^14 6s^2 5d^5')
ELCONF.append('[Xe] 4f^14 6s^2 5d^6')
ELCONF.append('[Xe] 4f^14 6s^2 5d^7')
ELCONF.append('[Xe] 4f^14 5d^9 6s^1')
ELCONF.append('[Xe] 4f^14 5d^10 6s^1')
ELCONF.append('[Xe] 4f^14 5d^10 6s^2')
ELCONF.append('[Xe] 4f^14 5d^10 6s^2 6p^1')
ELCONF.append('[Xe] 4f^14 5d^10 6s^2 6p^2')
ELCONF.append('[Xe] 4f^14 5d^10 6s^2 6p^3')
ELCONF.append('[Xe] 4f^14 5d^10 6s^2 6p^4')
ELCONF.append('[Xe] 4f^14 5d^10 6s^2 6p^5')
ELCONF.append('[Xe] 4f^14 5d^10 6s^2 6p^6')
ELCONF.append('[Rn] 7s^1')
ELCONF.append('[Rn] 7s^2')
ELCONF.append('[Rn] 7s^2 6d^1')
ELCONF.append('[Rn] 7s^2 6d^2')
ELCONF.append('[Rn] 5f^2 7s^2 6d^1')
ELCONF.append('[Rn] 5f^3 7s^2 6d^1')
ELCONF.append('[Rn] 5f^4 7s^2 6d^1')
ELCONF.append('[Rn] 5f^6 7s^2')
ELCONF.append('[Rn] 5f^7 7s^2')
ELCONF.append('[Rn] 5f^7 7s^2 6d^1')
ELCONF.append('[Rn] 5f^9 7s^2')
ELCONF.append('[Rn] 5f^10 7s^2')
ELCONF.append('[Rn] 5f^11 7s^2')
ELCONF.append('[Rn] 5f^11 7s^2 6d^1')
ELCONF.append('[Rn] 5f^13 7s^2')
ELCONF.append('[Rn] 5f^14 7s^2')
ELCONF.append('[Rn] 5f^14 7s^2 6d^1')
ELCONF.append('[Rn] 5f^14 7s^2 6d^2')
ELCONF.append('[Rn] 5f^14 7s^2 6d^3')
ELCONF.append('[Rn] 5f^14 7s^2 6d^4')
ELCONF.append('[Rn] 5f^14 7s^2 6d^5')
ELCONF.append('[Rn] 5f^14 7s^2 6d^6')
ELCONF.append('[Rn] 5f^14 7s^2 6d^7')
ELCONF.append('[Rn] 5f^14 6d^9 7s^1')
ELCONF.append('[Rn] 5f^14 7s^2 6d^9')
#
## Definition of element group
#
ELGRP = []
ELGRP.append(' NONE')
ELGRP.append('   IA')
ELGRP.append('VIIIA')
ELGRP.append('   IA')
ELGRP.append('  IIA')
ELGRP.append(' IIIA')
ELGRP.append('  IVA')
ELGRP.append('   VA')
ELGRP.append('  VIA')
ELGRP.append(' VIIA')
ELGRP.append('VIIIA')
ELGRP.append('   IA')
ELGRP.append('  IIA')
ELGRP.append(' IIIA')
ELGRP.append('  IVA')
ELGRP.append('   VA')
ELGRP.append('  VIA')
ELGRP.append(' VIIA')
ELGRP.append('VIIIA')
ELGRP.append('   IA')
ELGRP.append('  IIA')
ELGRP.append(' IIIB')
ELGRP.append('  IVB')
ELGRP.append('   VB')
ELGRP.append('  VIB')
ELGRP.append(' VIIB')
ELGRP.append('VIIIB')
ELGRP.append('VIIIB')
ELGRP.append('VIIIB')
ELGRP.append('   IB')
ELGRP.append('  IIB')
ELGRP.append(' IIIA')
ELGRP.append('  IVA')
ELGRP.append('   VA')
ELGRP.append('  VIA')
ELGRP.append(' VIIA')
ELGRP.append('VIIIA')
ELGRP.append('   IA')
ELGRP.append('  IIA')
ELGRP.append(' IIIB')
ELGRP.append('  IVB')
ELGRP.append('   VB')
ELGRP.append('  VIB')
ELGRP.append(' VIIB')
ELGRP.append('VIIIB')
ELGRP.append('VIIIB')
ELGRP.append('VIIIB')
ELGRP.append('   IB')
ELGRP.append('  IIB')
ELGRP.append(' IIIA')
ELGRP.append('  IVA')
ELGRP.append('   VA')
ELGRP.append('  VIA')
ELGRP.append(' VIIA')
ELGRP.append('VIIIA')
ELGRP.append('   IA')
ELGRP.append('  IIA')
ELGRP.append(' IIIB')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append(' LANS')
ELGRP.append('  IVB')
ELGRP.append('   VB')
ELGRP.append('  VIB')
ELGRP.append(' VIIB')
ELGRP.append('VIIIB')
ELGRP.append('VIIIB')
ELGRP.append('VIIIB')
ELGRP.append('   IB')
ELGRP.append('  IIB')
ELGRP.append(' IIIA')
ELGRP.append('  IVA')
ELGRP.append('   VA')
ELGRP.append('  VIA')
ELGRP.append(' VIIA')
ELGRP.append('VIIIA')
ELGRP.append('   IA')
ELGRP.append('  IIA')
ELGRP.append(' IIIB')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append(' ACTS')
ELGRP.append('  IVB')
ELGRP.append('   VB')
ELGRP.append('  VIB')
ELGRP.append(' VIIB')
ELGRP.append('VIIIB')
ELGRP.append('VIIIB')
ELGRP.append('VIIIB')
ELGRP.append('   IB')
#
## Definition of element symbols
#
ELSYM = []
ELSYM.append(' X')
ELSYM.append(' H')
ELSYM.append('He')
ELSYM.append('Li')
ELSYM.append('Be')
ELSYM.append(' B')
ELSYM.append(' C')
ELSYM.append(' N')
ELSYM.append(' O')
ELSYM.append(' F')
ELSYM.append('Ne')
ELSYM.append('Na')
ELSYM.append('Mg')
ELSYM.append('Al')
ELSYM.append('Si')
ELSYM.append(' P')
ELSYM.append(' S')
ELSYM.append('Cl')
ELSYM.append('Ar')
ELSYM.append(' K')
ELSYM.append('Ca')
ELSYM.append('Sc')
ELSYM.append('Ti')
ELSYM.append(' V')
ELSYM.append('Cr')
ELSYM.append('Mn')
ELSYM.append('Fe')
ELSYM.append('Co')
ELSYM.append('Ni')
ELSYM.append('Cu')
ELSYM.append('Zn')
ELSYM.append('Ga')
ELSYM.append('Ge')
ELSYM.append('As')
ELSYM.append('Se')
ELSYM.append('Br')
ELSYM.append('Kr')
ELSYM.append('Rb')
ELSYM.append('Sr')
ELSYM.append(' Y')
ELSYM.append('Zr')
ELSYM.append('Nb')
ELSYM.append('Mo')
ELSYM.append('Tc')
ELSYM.append('Ru')
ELSYM.append('Rh')
ELSYM.append('Pd')
ELSYM.append('Ag')
ELSYM.append('Cd')
ELSYM.append('In')
ELSYM.append('Sn')
ELSYM.append('Sb')
ELSYM.append('Te')
ELSYM.append(' I')
ELSYM.append('Xe')
ELSYM.append('Cs')
ELSYM.append('Ba')
ELSYM.append('La')
ELSYM.append('Ce')
ELSYM.append('Pr')
ELSYM.append('Nd')
ELSYM.append('Pm')
ELSYM.append('Sm')
ELSYM.append('Eu')
ELSYM.append('Gd')
ELSYM.append('Tb')
ELSYM.append('Dy')
ELSYM.append('Ho')
ELSYM.append('Er')
ELSYM.append('Tm')
ELSYM.append('Yb')
ELSYM.append('Lu')
ELSYM.append('Hf')
ELSYM.append('Ta')
ELSYM.append(' W')
ELSYM.append('Re')
ELSYM.append('Os')
ELSYM.append('Ir')
ELSYM.append('Pt')
ELSYM.append('Au')
ELSYM.append('Hg')
ELSYM.append('Tl')
ELSYM.append('Pb')
ELSYM.append('Bi')
ELSYM.append('Po')
ELSYM.append('At')
ELSYM.append('Rn')
ELSYM.append('Fr')
ELSYM.append('Ra')
ELSYM.append('Ac')
ELSYM.append('Th')
ELSYM.append('Pa')
ELSYM.append(' U')
ELSYM.append('Np')
ELSYM.append('Pu')
ELSYM.append('Am')
ELSYM.append('Cm')
ELSYM.append('Bk')
ELSYM.append('Cf')
ELSYM.append('Es')
ELSYM.append('Fm')
ELSYM.append('Md')
ELSYM.append('No')
ELSYM.append('Lr')
ELSYM.append('Rf')
ELSYM.append('Db')
ELSYM.append('Sg')
ELSYM.append('Bh')
ELSYM.append('Hs')
ELSYM.append('Mt')
ELSYM.append('Ds')
ELSYM.append('Rg')
#
## Definition of standard isotopic masses           
## Lit.: CRC Handbook of Chemistry and Physics, 1989
#
STDMATOM = []
STDMATOM.append(0.000000)
STDMATOM.append(1.007940)
STDMATOM.append(4.002602)
STDMATOM.append(6.941000)
STDMATOM.append(9.012182)
STDMATOM.append(10.811000)
STDMATOM.append(12.011000)
STDMATOM.append(14.006740)
STDMATOM.append(15.999400)
STDMATOM.append(18.998400)
STDMATOM.append(20.179700)
STDMATOM.append(22.989768)
STDMATOM.append(24.305000)
STDMATOM.append(26.981539)
STDMATOM.append(28.085500)
STDMATOM.append(30.973762)
STDMATOM.append(32.066000)
STDMATOM.append(35.452700)
STDMATOM.append(39.948000)
STDMATOM.append(39.098300)
STDMATOM.append(40.078000)
STDMATOM.append(44.955910)
STDMATOM.append(47.880000)
STDMATOM.append(50.941500)
STDMATOM.append(51.996100)
STDMATOM.append(54.938050)
STDMATOM.append(55.847000)
STDMATOM.append(58.933200)
STDMATOM.append(58.693400)
STDMATOM.append(63.546000)
STDMATOM.append(65.390000)
STDMATOM.append(69.723000)
STDMATOM.append(72.610000)
STDMATOM.append(74.921590)
STDMATOM.append(78.960000)
STDMATOM.append(79.904000)
STDMATOM.append(83.800000)
STDMATOM.append(85.467800)
STDMATOM.append(87.620000)
STDMATOM.append(88.905850)
STDMATOM.append(91.224000)
STDMATOM.append(92.906380)
STDMATOM.append(95.940000)
STDMATOM.append(98.000000)
STDMATOM.append(101.070000)
STDMATOM.append(102.905500)
STDMATOM.append(106.420000)
STDMATOM.append(107.868200)
STDMATOM.append(112.411000)
STDMATOM.append(114.820000)
STDMATOM.append(118.710000)
STDMATOM.append(121.757000)
STDMATOM.append(127.600000)
STDMATOM.append(126.904470)
STDMATOM.append(131.290000)
STDMATOM.append(132.905430)
STDMATOM.append(137.327000)
STDMATOM.append(138.905500)
STDMATOM.append(140.115000)
STDMATOM.append(140.907650)
STDMATOM.append(144.240000)
STDMATOM.append(145.000000)
STDMATOM.append(150.360000)
STDMATOM.append(151.965000)
STDMATOM.append(157.250000)
STDMATOM.append(158.925340)
STDMATOM.append(162.500000)
STDMATOM.append(164.930320)
STDMATOM.append(167.260000)
STDMATOM.append(168.934210)
STDMATOM.append(173.040000)
STDMATOM.append(174.967000)
STDMATOM.append(178.490000)
STDMATOM.append(180.947900)
STDMATOM.append(183.850000)
STDMATOM.append(186.207000)
STDMATOM.append(190.200000)
STDMATOM.append(192.220000)
STDMATOM.append(195.080000)
STDMATOM.append(196.966540)
STDMATOM.append(200.590000)
STDMATOM.append(204.383300)
STDMATOM.append(207.200000)
STDMATOM.append(208.980370)
STDMATOM.append(209.000000)
STDMATOM.append(210.000000)
STDMATOM.append(222.000000)
STDMATOM.append(223.000000)
STDMATOM.append(226.000000)
STDMATOM.append(227.000000)
STDMATOM.append(232.038100)
STDMATOM.append(231.035880)
STDMATOM.append(238.028900)
STDMATOM.append(237.000000)
STDMATOM.append(244.000000)
STDMATOM.append(243.000000)
STDMATOM.append(247.000000)
STDMATOM.append(247.000000)
STDMATOM.append(251.000000)
STDMATOM.append(252.000000)
STDMATOM.append(257.000000)
STDMATOM.append(258.000000)
STDMATOM.append(259.000000)
STDMATOM.append(262.000000)
STDMATOM.append(267.000000)
STDMATOM.append(268.000000)
STDMATOM.append(271.000000)
STDMATOM.append(270.000000)
STDMATOM.append(277.000000)
STDMATOM.append(276.000000)
STDMATOM.append(281.000000)
STDMATOM.append(280.000000)
#
#     ------------------------------------------------------------------
#
## Definition of atomic orbital symbols
#
AOSYM = []
AOSYM.append('s')
AOSYM.append('p')
AOSYM.append('d')
AOSYM.append('f')
AOSYM.append('g')
AOSYM.append('h')
AOSYM.append('i')
AOSYM.append('j')
AOSYM.append('k')
AOSYM.append('l')
AOSYM.append('m')
AOSYM.append('n')
AOSYM.append('o')
#
## Basic labels for the generation of Cartesian components
#
XYZ = []
XYZ.append('x')
XYZ.append('y')
XYZ.append('z')
#
## Frequency labels
#
ABC = []
ABC.append('a')
ABC.append('b')
ABC.append('c')
#
## Labels for matrix numbering
#
NOS = []
NOS.append('1')
NOS.append('2')
NOS.append('3')
#
#     ------------------------------------------------------------------
PI = 4.0*math.atan(1.0)
#
## P.J. Mohr, B.N. Taylor, The 2002 CODATA Recommended 
## Values of the Fundamental Physical Constants, Web   
## Version 4.0, available at physics.nist.gov/constants
#
## Speed of light in vacuum [m/s]
#
CLIGHT = 2.99792458E8
#
## Elementary charge [C]
#
ECHARGE = 1.6021765314E-19
#
## Electron mass [kg]
#
EMASS = 9.109382616E-31
#
## Electric field constant [F/m]
#
EPSI0 = 8.854187817E-12
#
## Planck constant [J*s]
#
HPLANCK = 6.626069311E-34
#
## Boltzmann constant [J/K]
#
KBOLTZ = 1.380650524E-23
#
## Permeability of vacuum [N/A**2]
#
MUPERM = 4.0*PI*1.0E-7
#
## Avogadro constant [1/mol]
#
NAVOG = 6.022141510E23
#
## Parts per million [ppm]
#
PPM = 1.0/1000000.0
#
## Standard pressure [Pa]
#
PRESSURE = 100000.0
#
## Fine-structure constant
#
AFINE = 0.5*MUPERM*CLIGHT*ECHARGE**2/HPLANCK
#
## Gas constant
#
RGAS = NAVOG*KBOLTZ
#
## Rydberg constant [1/m]
#
RYDBERG = 0.5*EMASS*CLIGHT*AFINE**2/HPLANCK
#
## Bohr radius [m]
#
ABOHR = AFINE/(4.0*PI*RYDBERG)
#
## MM Coulomb constant [kcal/mol]
#
CMM = ECHARGE**2*NAVOG*1.0E7/(4.184*4.0*PI*EPSI0)
#
#     ------------------------------------------------------------------
#
## Conversion factors
#
## [amu] -> [kg]
#
AMUKG = 1.66053886E-27
#
## [amu] -> [atomic units]
#
AMU = AMUKG/EMASS
#
## [Angstrom] -> [Bohr]
#
BOHR = 1.0E-10/ABOHR
#
## [fsec] -> [atomic units]
#
FSEC = 4.0*PI*RYDBERG*CLIGHT*1.0E-15
#
## [Hartree] -> [J]
#
JOULE = 2.0*RYDBERG*HPLANCK*CLIGHT
#
## [Hartree] -> [kJ/mol]
#
KJMOL = 0.001*JOULE*NAVOG
#
## [Hartree] -> [kcal/mol]
#
KCALMOL = KJMOL/4.184
#
## [Hartree] -> [eV]
#
EVOLT = JOULE/ECHARGE
#
## [Hartree] -> [Hz]
#
HZ = JOULE/HPLANCK
MHZ = 1.0E-6*HZ
#
## [Hartree] -> [1/cm] (wave numbers)
#
WAVENUM = 0.02*RYDBERG
#
## [1/cm] -> [1/sec]
#
WAVESEC = 100*CLIGHT
#
## [Hartree/Bohr**2] -> [1/cm] (wave numbers)
#
VIBFAC = 5.0*math.sqrt(KJMOL)/(PI*ABOHR*CLIGHT)
#
## [Hartree] -> [esu] (electrostatic units)
#
ESU = list()
ESU.append(1.0E21*ABOHR*CLIGHT*ECHARGE)
for LM in range(1,max(1,MAXMOM)):
    ESU.append(ESU[LM-1]/BOHR)
#
## [a.u.] -> [Pa]
#
PASCAL = 1.0E30*EMASS*FSEC**2/ABOHR
#
#     ------------------------------------------------------------------
#
## Transform covalent radii [Angstrom] -> [Bohr]
#
COVRAD = list(map(lambda x: x*BOHR, COVRAD))
D3CR = list(map(lambda x: x*BOHR, D3CR))
#
## Transform van der Waals radii [Angstrom] -> [Bohr]
#
VDWRAD = list(map(lambda x: x*BOHR, VDWRAD))
#
#     ------------------------------------------------------------------
#
## End of SUBROUTINE PHYSCON
#
#     END

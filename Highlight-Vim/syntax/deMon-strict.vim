" Vim syntax file
" 
" Language:    deMon input file
" Maintainer:  Juan Samaniego (https://github.com/jota-de)
" Last Change: 2021 Apr 05
"
" ----------------------------------------------------------------------

" Don't load this file if a custom syntax file has been loaded already.
if exists('b:current_syntax')
    finish
endif

" Ignore case.
syntax case ignore

" KEYWORDS
" ----------------------------------------------------------------------


" Molecular geometry input:
syn keyword dKeyword GEOMETRY REACTANT PRODUCT
syn keyword dOption CARTESIAN ZMATRIX MIXED ANGSTROM BOHR

syn keyword dKeyword SYMMETRY
syn keyword dOption NONE ON OFF

syn keyword dKeyword ALIGNMENT
syn keyword dOption ENANTIOMER EXCLUDE CONNECT UNIFORM
syn match dOption / \(CUBE\|TOL\)=/me=e-1

syn keyword dKeyword CONSTANTS CONSTRAINTS VARIABLES PATTERN


" Methodology selection:
" TODO Add vxctype missing options
syn keyword dKeyword VXCTYPE
syn keyword dOption VWN PZ81 PW92 PW86 BLYP OLYP PW91 PW91SSF PBE
syn keyword dOption PBESSF PBESOL KT1 KT2 KT3 CAP SO11 N12 GAM VS98
syn keyword dOption PKZB TPSS M06L M11L MN12 B3LYP PBE0 M062X M06HF M06
syn keyword dOption XALPHA FOCK
syn match dOption / \(BASIS\|AUXIS\)\>/

syn keyword dKeyword DISPERSION
syn match dOption / \(S6\)=/me=e-1

syn keyword dKeyword FORCEFIELD
syn match dOption / \(FF\)=/me=e-1

syn match dKeyword /^\<QM\/MM\>/
syn keyword dOption CHARMM NOPOLES

syn keyword dKeyword EMBED
syn keyword dOption FILE READ

syn keyword dKeyword EFIELD


" Atom specific input:
syn keyword dKeyword GRID
syn keyword dOption ADAPTIVE FIXED MEDIUM COARSE FINE REFERENCE
syn keyword dOption DIRECT
syn match dOption / \(SCF\|GUESS\)\>/
syn match dOption / RAD=/me=e-1

syn keyword dKeyword FREEZE
syn keyword dOption CUSP CORE VALENCE

syn match dKeyword /^\(BASIS\|AUXIS\)/
syn keyword dKeyword AUGMENT ECPS MCPS 


" Electronic state control:
syn keyword dKeyword FIXMOS
syn keyword dOption ITERATIVE

syn keyword dKeyword MULTIPLICITY CHARGE MOEXCHANGE MOMODIFY
syn keyword dKeyword SMEAR

syn keyword dKeyword CONFIGURE
syn keyword dOption OCCUPY
syn match dOption / MAX=/me=e-1


" SCF control and stabilization:
syn keyword dKeyword SCFTYPE
syn keyword dOption RKS UKS ROKS CUKS NOTIGHTEN
syn match dOption / CDF=/me=e-1

syn keyword dKeyword ORBITALS
syn keyword dOption SPHERICAL

syn keyword dKeyword ERIS
syn keyword dOption MULTIPOLE CONVENTIONAL
syn match dOption / RAM=/me=e-1

syn match dKeyword /^GUESS/
syn keyword dOption TB CORE FERMI RESTART ONLY PROJECTED

syn keyword dKeyword MIXING
syn keyword dOption OMA

syn keyword dKeyword SHIFT
syn match dOption / MIN=/me=e-1

syn keyword dKeyword PHASE DIIS


" Optimization, interpolation and transition state search:
syn keyword dKeyword OPTIMIZATION OPTIMIZE
syn keyword dOption REDUNDANT INTERVAL TS
syn match dOption / \(STEP\|MOD\)=/me=e-1

syn keyword dKeyword SADDLE
syn match dOption / INT=/me=e-1

syn keyword dKeyword SCAN
syn keyword dOption ADIABATIC VERTICAL
syn match dOption / END=/me=e-1

syn keyword dKeyword IRC
syn keyword dOption FORWARD REVERSE MASS NOMASS EXTEND
syn match dOption / EVIB=/me=e-1

syn keyword dKeyword HESSIAN
syn keyword dOption BAKER FISHER UNITY INTERNAL LINDH CALCULATE
syn keyword dOption PLAIN DEMON
syn match dOption / VIB=/me=e-1

syn keyword dKeyword UPDATE
syn keyword dOption BFGS POWELL BERNY DFP MSP SR1 EXACT

syn keyword dKeyword STEPTYPE
syn keyword dOption LEVENBERG RFO WALK DESCENT


" Born-Oppenheimer molecular dynamics:
syn keyword dKeyword DYNAMICS
syn match dOption / R=/me=e-1

syn keyword dKeyword TRAJECTORY
syn keyword dOption FORCES
syn match dOption / \(PART\|PLOT\|MOS\)=/me=e-1
syn match dOption / CUT[<>]\{1}/me=e-1

syn keyword dKeyword SIMULATION
syn keyword dOption ANALYZE DIPOLE MOMENTA SIMILARITY ANGLE
syn keyword dOption LINDEMANN MEANDIS PROLATE LENGHT DIHEDRAL
syn match dOption / E=\(STA\|KIN\|POT\|TOT\|SYS\)\a*/
syn match dOption / POLARIZABILITY/
syn match dOption / MAGNETIZABILITY/
syn match dOption / PHASESPACE/
syn match dOption / \(NMR\|RDF\)=/me=e-1

syn keyword dKeyword LPCONSERVE
syn match dOption / VELOCITIES/

syn keyword dKeyword VELOCITIES
syn keyword dOption RANDOM ZERO
syn match dOption / LP=0/
syn match dOption / P=0/
syn match dOption / T=/me=e-1

syn keyword dKeyword BATH
syn keyword dOption SCALING BERENDSEN HOOVER NOSE
syn match dOption / \(TAU\|FREQ\|NHC\)=/me=e-1

syn match dKeyword /^RDF/
syn match dOption / WIDTH=/me=e-1


" Molecular property control:
syn keyword dKeyword FREQUENCY
syn keyword dOption RAMAN

syn keyword dKeyword THERMO
syn keyword dOption VIBONLY

syn match dKeyword /^POLARIZABILITY/
syn keyword dOption ALPHA BETA GAMMA NIACPKS NUMERICAL DD DQ SHG OR
syn keyword dOption SHG EOPE EFISH FALDA GALDA FDKERNEL ANALYTICAL
syn match dOption / \(W\|W2\|FFS\)=/me=e-1

syn keyword dKeyword EXCITATION
syn keyword dOption RS DSYEV JACOBI TDA 
syn match dOption / DAVIDSON/
syn match dOption / D&C/

syn keyword dKeyword XRAY
syn keyword dOption XAS XES

syn match dKeyword /^NMR/
syn keyword dOption NICS SPINROT

syn match dKeyword /^MAGNETIZABILITY/
syn keyword dOption GTENSOR

syn keyword dKeyword NQR
syn keyword dOption BARN
syn match dOption / FM^2/

syn keyword dKeyword NONCOLLINEAR FUKUI


" XXX Electronic structure analysis:
syn keyword dKeyword POPULATION


syn keyword dKeyword DOS SIGPI LOCALIZATION


" Visualization and topological analysis:
syn keyword dKeyword VISUALIZATION TOPOLOGY CPSEARCH ISOSURFACE
syn keyword dKeyword GEOSURFACE BOX POINTS


" Performance and accuracy settings:
syn keyword dKeyword PARALLEL MATDIA MATINV DAVIDSON WEIGHTING
syn keyword dKeyword QUADRATURE CFPINTEGRATION


" Miscellaneous keywords:
syn keyword dKeyword TITLE PRINT


" MISCELLANEOUS
" ----------------------------------------------------------------------

" Basis, auxis, etc. parenthesized options:
syn region dOption start=/(/ms=e+1 end=/)/me=e-1


" Comments including todos:
syn match dTodo contained /\(TODO\|NOTE\|XXX\):*/
syn match dComment /#.*/ contains=dTodo


" Errors:
syn match dError /\( \+=\|=\( \|$\)\+\)/


" Atom labels:
syn match dAtom /^\a\{1,2}\d* /


" HIGHLIGHT
" ----------------------------------------------------------------------

hi link dKeyword Identifier

hi link dOption Statement

hi link dTodo Todo

hi link dComment Comment

hi link dError Error

hi link dAtom Typedef


" END
" ----------------------------------------------------------------------
" Set current syntax
let b:current_syntax = 'deMon'

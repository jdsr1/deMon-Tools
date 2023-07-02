" Vim syntax file
" Language:    deMon
" Maintainer:  Juan Diego Samaniego Rojas <https://github.com/jdsr1>
" Last Change: 2023 Jul 02
" Remark:      This file complies with deMon's five-character-keyword rule.

" Quit when a (custom) syntax file was already loaded.
if exists('b:current_syntax')
    finish
endif

" Ignore case.
syntax case ignore

" Some keywords and options may have unusual characters
setlocal iskeyword+=-
setlocal iskeyword+=/
setlocal iskeyword+=&


" Section: Molecular geometry input
syntax keyword deMonKey GEOME[TRY] REACT[ANT] PRODU[CT]
syntax keyword deMonOpt CARTE[SIAN] ZMATR[IX] Z-MAT[RIX] MIXED ANGST[ROM] BOHR

syntax keyword deMonKey SYMME[TRY]
syntax keyword deMonOpt NONE ON OFF

syntax keyword deMonKey ALIGN[MENT]
syntax keyword deMonOpt ENANT[IOMER] EXCLU[DE] CONNE[CT] UNIFO[RM]

syntax keyword deMonKey CONST[ANTS] CONST[RAINTS] VARIA[BLES] PATTE[RN]


" Section: Methodology selection 
syntax keyword deMonKey VXCTY[PE]
syntax keyword deMonOpt VWN PZ81 PW92 PW86 BLYP OLYP PW91 PW91S[SF] PBE
syntax keyword deMonOpt PBESS[F] PBESO[L] KT1 KT2 KT3 CAP SO11 N12 GAM VS98
syntax keyword deMonOpt PKZB TPSS M06L M11L MN12 B3LYP PBE0 M062X M06HF M06
syntax keyword deMonOpt XALPH[A] FOCK
syntax keyword deMonOpt BASIS AUXIS containedin=deMonKey contained

syntax keyword deMonKey DISPE[RSION]
syntax keyword deMonOpt READ

syntax keyword deMonKey FORCE[FIELD]

syntax keyword deMonKey QM/MM
syntax keyword deMonOpt CHARM[M] NOPOL[ES]

syntax keyword deMonKey EMBED
syntax keyword deMonOpt FILE

syntax keyword deMonKey EFIEL[D]


" Section: Atom specific input
syntax keyword deMonKey GRID
syntax keyword deMonOpt ADAPT[IVE] FIXED MEDIU[M] COARS[E] FINE REFER[ENCE]
syntax keyword deMonOpt SCF GUESS DIREC[T]

syntax keyword deMonKey FREEZE
syntax keyword deMonOpt CUSP CORE VALEN[CE]

syntax keyword deMonKey BASIS AUGME[NT] AUXIS ECPS MCPS


" Section: Electronic state control
syntax keyword deMonKey FIXMO[S]
syntax keyword deMonOpt ITERA[TIVE]

syntax keyword deMonKey MULTI[PLICITY] CHARG[E] MOEXC[HANGE] MOMOD[IFY]
syntax keyword deMonKey SMEAR

syntax keyword deMonKey CONFI[GURE]
syntax keyword deMonOpt OCCUP[Y]


" Section: SCF control and stabilization
syntax keyword deMonKey SCFTY[PE]
syntax keyword deMonOpt RKS UKS ROKS CUKS NOTIG[HTEN]

syntax keyword deMonKey ORBIT[ALS]
syntax keyword deMonOpt SPHER[ICAL]

syntax keyword deMonKey ERIS
syntax keyword deMonOpt MULTI[POLE] CONVE[NTIONAL]

syntax match   deMonKey /^GUESS/
syntax keyword deMonOpt TB CORE FERMI RESTA[RT] ONLY PROJE[CTED]

syntax keyword deMonKey MIXIN[G]
syntax keyword deMonOpt OMA

syntax keyword deMonKey SHIFT

syntax keyword deMonKey PHASE DIIS


" Section: Optimization, interpolation and transition state search
syntax keyword deMonKey OPTIM[IZATION]
syntax keyword deMonOpt REDUN[DANT] INTER[VAL] TS

syntax keyword deMonKey SADDL[E]

syntax keyword deMonKey SCAN
syntax keyword deMonOpt ADIAB[ATIC] VERTI[CAL]

syntax keyword deMonKey IRC
syntax keyword deMonOpt FORWA[RD] REVER[SE] MASS NOMAS[S] EXTEN[D]

syntax keyword deMonKey HESSI[AN]
syntax keyword deMonOpt BAKER FISHE[R] UNITY INTER[NAL] LINDH CALCU[LATE]
syntax keyword deMonOpt PLAIN DEMON

syntax keyword deMonKey UPDAT[E]
syntax keyword deMonOpt BFGS POWEL[L] BERNY DFP MSP SR1 EXACT

syntax keyword deMonKey STEPT[YPE]
syntax keyword deMonOpt LEVEN[BERG] RFO WALK DESCE[NT]


" Section: Born-Oppenheimer molecular dynamics
syntax keyword deMonKey DYNAM[ICS]

syntax keyword deMonKey TRAJE[CTORY]
syntax keyword deMonOpt FORCE[S]

syntax keyword deMonKey SIMUL[ATION]
syntax keyword deMonOpt ANALY[ZE] DIPOL[E] MOMEN[TA] SIMIL[ARITY] ANGLE
syntax keyword deMonOpt LINDE[MANN] MEAND[IS] PROLA[TE] LENGH[T] DIHED[RAL]
syntax keyword deMonOpt POLAR[IZABILITY] MAGNE[TIZABILITY] PHASE[SPACE]

syntax keyword deMonKey LPCON[SERVE]
syntax keyword deMonOpt VELOC[ITIES]

syntax keyword deMonKey VELOC[ITIES]
syntax keyword deMonOpt RANDO[M] ZERO

syntax keyword deMonKey BATH
syntax keyword deMonOpt SCALI[NG] BEREN[DSEN] HOOVE[R] NOSE

syntax match   deMonKey /^RDF/


" Section: Molecular property control
syntax keyword deMonKey FREQU[ENCY]
syntax keyword deMonOpt RAMAN

syntax keyword deMonKey THERM[O]
syntax keyword deMonOpt VIBON[LY]

syntax keyword deMonKey POLAR[IZABILITY]
syntax keyword deMonOpt ALPHA BETA GAMMA NIACP[KS] NUMER[ICAL] DD DQ SHG OR
syntax keyword deMonOpt SHG EOPE EFISH FALDA GALDA FDKER[NEL] ANALY[TICAL]

syntax keyword deMonKey EXCIT[ATION]
syntax keyword deMonOpt RS DSYEV JACOB[I] TDA 
syntax keyword deMonOpt DAVID[SON] D&C

syntax keyword deMonKey XRAY
syntax keyword deMonOpt XAS XES

syntax keyword deMonKey NMR
syntax keyword deMonOpt NICS SPINR[OT]

syntax keyword deMonKey MAGNE[TIZABILITY]
syntax keyword deMonOpt GTENS[OR]

syntax keyword deMonKey NQR
syntax keyword deMonOpt BARN

syntax keyword deMonKey NONCO[LLINEAR] FUKUI


" Section: Electronic structure analysis
syntax keyword deMonKey POPUL[ATION]
syntax keyword deMonKey DOS SIGPI LOCAL[IZATION]


" Section: Visualization and topological analysis
syntax keyword deMonKey VISUA[LIZATION] TOPOL[OGY] CPSEA[RCH] ISOSU[RFACE]
syntax keyword deMonKey GEOSU[RFACE] BOX POINTS


" Section: Performance and accuracy settings
syntax keyword deMonKey PARAL[LEL] MATDI[A] MATIN[V] DAVID[SON] WEIGH[TING]
syntax keyword deMonKey QUADR[ATURE] CFPIN[TEGRATION]


" Section: Miscellaneous keywords
syntax keyword deMonKey TITLE PRINT


" Other: Match options inside paranthesis
syntax match   deMonOpt /(.*)/

" Other: Match options with special signs
syntax match   deMonOpt / \(CDF\|CUBE\|END\|EVIB\|FF\|FFS\|FREQ\|INT\)=/me=e-1
syntax match   deMonOpt / \(MAX\|MIN\|MOD\|MOS\|NHC\|NMR\|P\|PART\)=/me=e-1
syntax match   deMonOpt / \(PLOT\|R\|RAD\|RAM\|RDF\|S6\|STEP\|T\|TAU\)=/me=e-1
syntax match   deMonOpt / \(TOL\|VIB\|W\|W2\|WIDTH\)=/me=e-1

syntax match   deMonOpt / CUT[<>]\{1}/me=e-1
syntax match   deMonOpt / E=\(STA\|KIN\|POT\|TOT\|SYS\)/
syntax match   deMonOpt / \(FM^2\|LP=0\)/

" Other: Comments include todo
syntax match   deMonXXX contained /\(TODO\|NOTE\|XXX\):*/
syntax match   deMonCom /#.*/ contains=deMonXXX

" Other: Spaces around signs should not be left empty
syntax match   deMonErr /\( \+=\|=\( \|$\)\+\)/
syntax match   deMonErr /\( \+<\|<\( \|$\)\+\)/
syntax match   deMonErr /\( \+>\|>\( \|$\)\+\)/

" Other: Atom labels
syntax match   deMonAtm /^\a\{1,2}\d*/


" Highlight: Link deMon groups to standard Vim names
highlight link deMonKey Identifier
highlight link deMonOpt Statement
highlight link deMonXXX Todo
highlight link deMonCom Comment
highlight link deMonErr Error
highlight link deMonAtm Typedef


" End: Set current syntax
let b:current_syntax = 'deMon'

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:05:11 2022

@author: SamuelJames
"""
from random import randint
import argparse
import time
parser = argparse.ArgumentParser(description='show some ascii stuff')


logos = []

logo = '''
    ##############&###############%####%**,#####%##########%(#######(#####((((((((((
    ############&%########%#####&@%####****#####%@####&%#####%############&####(((((
    ######%####&&#######@%####@@#,####******#####/@&#####@&####&##########%%#####(((
    &%########&@######@@%###&@/***###********(####*#@&####**@@##&@########%@#%##(#((
    @@@@@@@@@@@@####%@@(%##&/***,,(#&@/*******,###/%@#@&###%*,,@%&@&######&@#@##@@@@
    @@@@@@@@@@@@###&@&**##&********((*(**********##(,**,,%@%##**,@#@@#####@%@@%@@@@@
    @@@@@@@@@@@@##%@@***#####(#####%#*************,/%#(((((((%&%(#%/@@###@@@@@@@@@@@
    @@@@@@@@@@@@@#&@*##%#%%%%%%%%#%%(##(#*******/(#######%%%#%#####(@@#&@@@@@@@@@@@@
    #.*.(@@@@@#**,%@#%#%((((((((((((//(%%(#****####(((((((((((((((#%@#&@/#**@@@@@@@@
    ,.%@@@@@@*/##%@&%%#(((#(((((((#(((((/%(/**#(##((((((((((((((((((#%@@###*%@@@@@@%
    .&@%     *****&&#@***/%#/(/#/#%#%&@&&&#&%&@%@@@@@&&@@@&@@&&/(&%%&&&&&//(@@@@@@@@
    %,       #*****/#&@(/,(/,/,#./((%%&&%%%%%%%(#&/(/%(/((#/(#%&&&&&&@%%,,/@@((**/@@
         %&    /,(***%&&&##&*&&%&%&&&#%%&%*****,%&@@/***&%#&#%&&/&%%**/,%&@@&%/(%/&,
    *&(          ,(***#(%&@&&&%#((#&&&#,************&@%((((((#@&&&##*#####&#&,*/***,
                 *****%**/(((((((***********************,/((((((**%########****/,,,,
                  ****#%/****************************************%########*,***/,,, 
                  ,****#%#*************************************(%#######(**,*,//,,  
                   /***/##%#*********************************/%########******,((,   
                    ****/####%%/**********%######**********##########*******,,/(    
                     *****#######%#********************(%##########***********/     
      .           *   ******##########%************#############*************//    .
      *           .*    */*****###########%#//#%%############*************/ */     ,
      *.           *,,    .  /****/######################/****/(*,*****,/  ./.   .,,
      *,.          .**,.    .    ./***#############%#(***//************    /*   ., 
    '''

logo1 = '''
 __________________
| | ___________ |o|
| | ___________ | |
| | ___________ | |
| | ___________ | |
| |_____________| |
|     _______     |
|    |       |   ||
|    |       |   V|
|____|_______|____|
'''

logo2 = '''
    ________
   /_______/\
   \n   \ \    / /
 ___\ \__/_/___
/____\ \______/
\\ \   \/ /   / /
 \ \  / /\  / /
  \ \/ /\ \/ /
   \_\/  \_\/
'''

logo3 = '''
     _      _      _      _      _      _      _
   _( )__ _( )__ _( )__ _( )__ _( )__ _( )__ _( )__
 _|     _|     _|     _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|
 |_     |_     |_     |_     |_     |_     |_     |_
  _) _   _) _   _) _   _) _   _) _   _) _   _) _   _)
 |__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|
 _|     _|     _|     _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|
 |_     |_     |_     |_     |_     |_     |_     |_
  _) _   _) _   _) _   _) _   _) _   _) _   _) _sj _)
 |__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|
'''

logo4 = '''
                      gggrgM**M#mggg__
                __wgNN@"B*P""mp""@d#"@N#Nw__
              _g#@0F_a*F#  _*F9m_ ,F9*__9NG#g_
           _mN#F  aM"    #p"    !q@    9NL "9#Qu_
          g#MF _pP"L  _g@"9L_  _g""#__  g"9w_ 0N#p
        _0F jL*"   7_wF     #_gF     9gjF   "bJ  9h_
       j#  gAF    _@NL     _g@#_      J@u_    2#_  #_
      ,FF_#" 9_ _#"  "b_  g@   "hg  _#"  !q_ jF "*_09_
      F N"    #p"      Ng@       `#g"      "w@    "# t
     j p#    g"9_     g@"9_      gP"#_     gF"q    Pb L
     0J  k _@   9g_ j#"   "b_  j#"   "b_ _d"   q_ g  ##
     #F  `NF     "#g"       "Md"       5N#      9W"  j#
     #k  jFb_    g@"q_     _*"9m_     _*"R_    _#Np  J#
     tApjF  9g  J"   9M_ _m"    9%_ _*"   "#  gF  9_jNF
      k`N    "q#       9g@        #gF       ##"    #"j
      `_0q_   #"q_    _&"9p_    _g"`L_    _*"#   jAF,'
       9# "b_j   "b_ g"    *g _gF    9_ g#"  "L_*"qNF
        "b_ "#_    "NL      _B#      _I@     j#" _#"
          NM_0"*g_ j""9u_  gP  q_  _w@ ]_ _g*"F_g@
           "NNh_ !w#_   9#g"    "m*"   _#*" _dN@"
              9##g_0@q__ #"4_  j*"k __*NF_g#@P"
                "9NN#gIPNL_ "b@" _2M"Lg#N@F"
                    ""P@*NN#gEZgNN@#@P""
'''

logo5 ='''
                ..e=******=e..                         
              .r""    .F        ^"4.                     
           .@"        $           .d$b.                  
         z$b.        J"        .d$$$$$$$c                
       .$$$$$$bc.    $    .e$$$$$$$$$$$$$$c              
      d$$$$$$$$$$$$bdbe$$$$$$$$$$$$$$$$$$$$$.            
     d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b           
    $$$$$$$$$$$$$$$$$$$$$$$$$$$F*$$$$$$$$$$$$$$          
   $$$$$$$$$$$$$$$$$$$$$$$$$$$%3   ^"**$$$$$$$$$.        
  d$$$$$$$$$$$$$$$$$$$$$$$$$$"  L         .^$$$$$        
 4$$$$$$$$$$$$$$$$$$$$$$$$$"    4          "^$$$$$       
 $$$$$$$$$$$$$$$$$$$$$$$*"       b           ^$$$$L      
4$$$$$$$$$$$$$$$$$$$$"           'r            "$*"      
$$$$$$$$$$$$$$$$$$$$$             $        .=""          
 "*$$$$$$$$$$$$$$$$$$             ^F  .r^"               
    ^*$$$$$$$$$$$$$$$            ..*"                    
        "$$$$$$$$$$$P        .=""                        
           "*$$$$$$$    ./^"                             
              "*$$$L.="      
'''

logo6 = '''
                        ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     || ||             '-'
     '-''-'
'''

logo7 ='''
             _         _
  __   ___.--'_`.     .'_`--.___   __
 ( _`.'. -   'o` )   ( 'o`   - .`.'_ )
 _\.'_'      _.-'     `-._      `_`./_
( \`. )    //\`         '/\\    ( .'/ )
 \_`-'`---'\\__,       ,__//`---'`-'_/
  \`        `-\         /-'        '/
   `                               ' 
'''

logo8 = '''
  o
                             o$$      oo
                 $o         o$ $     o$
               $  $         $" $    o$    ooo
               $o "$       o"  $    $"   o$""
               $"  "o     o$   $   o    o"
               $    $     $$   $   $   o"
               $$    $   $$"    $ $"  $"       oo "
       $   o   $$     oo"$      " "   $o oooo"""   ooo
        $   "o $$      "  oo       oo  """     oo"""
         $   "$$$       o"  "     "  "      o "
         $$                                 "ooooo
 o        $                         ooo        """"""oooo
  "o      $           ooo   o    o"    ""
o   "oo   "         o"       "o "        "o     oooo
 "o   ""          o"          $           "
   "oo           o"           $$           $     $$$$""
 oooo"           $         oo $  oo        $       """"
 ooooo   "       $        $"$ $ o"$$       $   ooooooo
"""  "$ "        $        "$" $ $$"        "   $$""""
   oo $          "o          o$ ""        o    $$ooo
 o$"""""          "o          "o         o     """""$
 $$                  "ooooo$     o     o            $
 "$                      $      $o"" ""             $
   "o    o                 o   o$"                 "
     ""oo$o                 """"             $ooo"
          "oo                               o$"
            "oo                           oo"
              ""oo        """          oo""
                 """ oo            o  ""
                      o"$" oooo """
                     o"   $""""" o
                     $o   o$     $o
                    o$ooo  $ooooo$"
                    $"     $       "
                    $""""" $""""""$
                    "o$$""$$oooooo$o$
                     o"$  $        $
                     $o$  $"""" "  $$
                o    "    $    """""$
                $oo       $ooooooo  $
                 $""  o  o"         "$
                 $$""$$$$$$$$$$$$$o$$$
                    o$$$$$$$$$$$$$$$$$  o
                ooo$""$$$$$"""""""$$""""""""o
               $""$oooo$$$         $         $o
          """""$o                 o"        o"""
               ""$$oooooooooooooo""" ooo$$
'''

logo9='''
  ,-~~-.___.
 / |  '     \         
(  )         0  
 \_/-, ,----'            
    ====           // 
   /  \-'~;    /~~~(O)
  /  __/~|   /       |     
=(  _____| (_________|
'''

logo10 = '''
       .-.,     ,.-.
 '-.  /:::\\   //:::\  .-'
 '-.\|':':' `"` ':':'|/.-'
 `-./`. .-=-. .-=-. .`\.-`
   /=- /     |     \ -=\
  \n  ;   |      |      |   ;
  |=-.|______|______|.-=|
  |==  \  0 /_\ 0  /  ==|
  |=   /'---( )---'\   =|
   \   \:   .'.   :/   /
    `\= '--`   `--' =/'
      `-=._     _.=-'
           `"""`'''

logo11 = '''
 ___________________________________________
|  _______________________________________  |
| / .-----------------------------------. \ |
| | | /\ :                        90 min| | |
| | |/--\:....................... NR [ ]| | |
| | `-----------------------------------' | |
| |      //-\\   |         |   //-\\      | |
| |     ||( )||  |_________|  ||( )||     | |
| |      \\-//   :....:....:   \\-//      | |
| |       _ _ ._  _ _ .__|_ _.._  _       | |
| |      (_(_)| |(_(/_|  |_(_||_)(/_      | |
| |               low noise   |           | |
| `______ ____________________ ____ ______' |
|        /    []             []    \        |
|       /  ()                   ()  \       |
!______/_____________________________\______!
'''

logo12 = '''
`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"
   `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/
     y==/        y==/        y==/        y==/
   ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.
,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_
'''

logo13 = '''
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \
  \n  /`       .-'~"-.       `\
 \n ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\        ;
 ;  INGODWE /      \\)P    ;
  \  TRUST '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
       `'-..,,,..-'`
'''

logo14 = '''
              _________
             {_________}
              )=======(
             /         \
            \n            | _________ |
            ||   _     ||
            ||  |_)    ||
            ||  | \/   ||
      __    ||    /\   ||
 __  (_|)   |'---------'|
(_|)        `-.........-'
'''

logo15 = '''
    __
    ||
   ====
   |  |__
   |  |-.\
   \n   |__|  \\
    ||   ||
  ======__|
 ________||__
/____________\
'''

logo16='''
  -----                                                               -----
1 | H |                                                               |He |
  |---+----                                       --------------------+---|
2 |Li |Be |                                       | B | C | N | O | F |Ne |
  |---+---|                                       |---+---+---+---+---+---|
3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
  |---+---+---------------------------------------+---+---+---+---+---+---|
4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
  |---+---+---+------------------------------------------------------------
7 |Fr |Ra |ACT|
  -------------
              -------------------------------------------------------------
   Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
              |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
   Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
              -------------------------------------------------------------
'''

logo17='''
       ________________
     |'-.--._ _________:
     |  /    |  __    __\
     \n     | |  _  | [\_\= [\_\
     \n     | |.' '. \.........|
     | ( <)  ||:       :|_
      \ '._.' | :.....: |_(o
       '-\_   \ .------./
       _   \   ||.---.||  _
      / \  '-._|/\ ~~\ ' | \
     \n     (| []=.--[===[()]===[) |
     <\_/  \_______/ _.' /_/
     ///            (_/_/
     |\\            [\\
     ||:|           | I|
     |::|           | I|
     ||:|           | I|
     ||:|           : \:
     |\:|            \I|
     :/\:            ([])
     ([])             [|
      ||              |\_
     _/_\_            [ -'-.__
sj  <]   \>            \_____.>
     \__/
'''

logo18 = '''
 .-.
(o o) boo!
| O |
|   |
`~~~'
'''

logo19 = '''
            _,.-------------.._
         ,-'        j          `-.
       ,'        .-'               `.
      /          |                   '
     /         ,-'                    `
    .         j                         \
   .          |                          \
   : ._       |   _....._                 .
   |   -.     L-''       `.               :
   | `.  \  .'             `.             |
  /.\  `, Y'                 :           ,|
 /.  :  | \                  |         ,' |
\.    " :  `\                |      ,--   |
 \    .'     '-..___,..      |    _/      :
  \  `.      ___   ...._     '-../        '
.-'    \    /| \_/ | | |      ,'         /
|       `--' |    '' |'|     /         .'
|            |      /. |    /       _,'
|-.-.....__..|     Y-dp`...:...-----
|_|_|_L.L.T._/     |
\_|_|_L.T-''/      |
 |                /
/             _.-'
:         _..'
\__...----
'''

logo20 = '''
\.
 \\      .
  \\ _,.+;)_
  .\\;~%:88%%.
 (( a   `)9,8;%.
 /`   _) ' `9%%%?
(' .-' j    '8%%'
 `"+   |    .88%)+._____..,,_   ,+%$%.
       :.   d%9`             `-%*'"'~%$.
    ___(   (%C                 `.   68%%9
  ."        \7                  ;  C8%%)`
  : ."-.__,'.____________..,`   L.  \86' ,
  : L    : :            `  .'\.   '.  %$9%)
  ;  -.  : |             \  \  "-._ `. `~"
   `. !  : |              )  >     ". ?
     `'  : |            .' .'       : |
         ; !          .' .'         : |
        ,' ;         ' .'           ; (
       .  (         j  (            `  \
       \n       """'          ""'             `"" 
'''

logo21 = '''
           ^^                   @@@@@@@@@
      ^^       ^^            @@@@@@@@@@@@@@@
                           @@@@@@@@@@@@@@@@@@              ^^
                          @@@@@@@@@@@@@@@@@@@@
~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~
~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~
  ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~ 
  ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~ 
~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~
      ~             ~        ~      ~      ~~   ~             ~
'''

logo22 = '''
             o\\
   _________/__\\__________
  |                  - (  |
 ,'-.                 . `-|
(____".       ,-.    '   ||
  |          /\\,-\\   ,-.  |
  |      ,-./     \\ /'.-\\ |
  |     /-.,\\      /     \\|
  |    /     \\    ,-.     \\
  |___/_______\\__/___\\_____\\
'''

logo23 = '''
 _._______
| _______ |
||,-----.||
|||     |||
|||_____|||
|`-------'| hjw
| +     O | `97
|      O  |
| / /  ##,"
 `------"
'''

logo24 = '''
           *-*,
       ,*\/|`| \\
       \'  | |'| *,
        \ `| | |/ )
         | |'| , /
         |'| |, /
       __|_|_|_|__
      [___________]
       |         |
       |         |
       |         |
       |_________|
'''

logo25 = '''
                       //   __..--~~~~--..__    \\
                      ||___/  |  |   |  |   \ __/ |
                      ||  /   ___________    \    |
                      ||_/   /.......... \    |   |
                      | |   /..........   \   |   |
 _____________________| |  /...........    \  |   |________________
  ;   . . .   .       |_| |...........      | |   | .''."...  ... .
 ___   ..~.         _.' | |..........       | |   |         . ~
  .      '     .   / \_.| |..........       | |   |\\ ~.   ._..---._
                  |. /| \ \............     / /   |/ .    /\      /\\
    '""" ... ~~~  | \|| _\ \............   / /-.__|      // ~-._./ -\\
  ..~             |  |_.~\\ \_____________/ /// '.|     /__       __.\\
  ___   ..~.      |_.~   .\\_______________//   _ ~-.  ~~~~..  ~~~~~.
                 .~ -.     \__.---.________/   ______\\.
 .''."...  ... ./\        _|      |---|  = |__ \__\===\\   '""" ... ~~~
               /  '.  .  |_|=     |---|    | _| \======\\ ___   ..~.
   ..~        / .   \      |=     |___|    ||       __. \\
             /           _ |_______________|   _.        \\
 .''."...  ./                /   \___    ~~  \            \\  '" ..   ~~
'''

logo26 = '''
        ___
_______(_@_)_______
| POLICE      BOX |
|_________________|
 | _____ | _____ |
 | |###| | |###| |
 | |###| | |###| | 
 | _____ | _____ |
 | || || | || || |
 | ||_|| | ||_|| |
 | _____ |$_____ |
 | || || | || || |
 | ||_|| | ||_|| |
 | _____ | _____ |
 | || || | || || | 
 | ||_|| | ||_|| | 
 |       |       | 
 *****************
'''

logo27 = '''
   nHHHHHHnHHHn
       dHHHHHHHHHHHHHHb
      dHHHHHHHHHHHHHHHHb
     dHHHHHH~~  '~~9HHHHb               ....._________    _____.........__
     HHHHH~         ~9HHH             .'              :  :                :
     HHHH:           ~HHH             `.__..--.   :~--'   ~-.       __....'
     HHHP:_nnnn   .nn.HHP                     `-. `.         :   .-~
     `HH|:^^@ >) (- @>|P                        :. `.        :  :
      |^|:       :    |      %::$$HHHHHnn        `._:      .'  :
      :`|:       |    :    $$$$H$HH$HH$HHHHn        ..     :  :
       ~|:.   ((_))  .:  $:$$H:::H:HH:HHHHHHHb     :  `  _:  '
        ::`.   ^ ^   ': $:$:$H):(::: :  ~HH$HHn     -. ~~  .'
         ::   -^-^- . 'H$::$H((: : :  '   HH:H$       :   :
         `::   ~~~  '/ H$$$$H\: )`  `      H$H$      .'  :
         .|::..__..-~|HHDrSH:)_..._   .===.H$HH$    .' _ `.
       _:::::::      HHH$HHH: . _ .:  . _-.:HHH$   .' : `.`.
    ..::::::::_    _HHHHHHHH: ` ^ '   ` ^-':H$$$H :  .'  : `.
 .::::::::::../XxxX\.HHHHH^|:              :H::::H .-'    : `.
 ::::::...\../\XXXX/\HHHHH\:::      ._)    :HH$$$H :       : `-.
 ..........\/..\XX/..HHHHHHn::`.          ':HHHHHH ;       :    :
 ..............|XX|.HHHHHHHH$:     .=-=.   :HH$HH :        `.   :
 ..............XXXXHHH$HHH$HH::    `...'  .$HHH$H$'          :   :
 ..............XXXHHHH$HH:$HH$::.       ..H$HHHH$H          '.    :
 .............|XXXHHHHHH$$HHH$H:::..   .':HHHHH$H$n--.   .---'     `.__.--.
 .............|XXXXHHHHHHHHH$HH:::::~~~ :HHHHHHHHHHHn :  :                 :
 .............|XHHHHHHHHHHHHHHHH:::    :HHHHHHHHHHHHHHn   -.___.-.___..DrS.'
'''

logo28 = '''

                                    /@
                     __        __   /\\/
                    /==\\      /  \\_/\\/   
                  /======\\    \\/\\__ \\__
                /==/\\  /\\==\\    /\\_|__ \\
             /==/    ||    \\=\\ / / / /_/
           /=/    /\\ || /\\   \\=\\/ /     
        /===/   /   \\||/   \\   \\===\\
      /===/   /_________________ \\===\\
   /====/   / |                /  \\====\\
 /====/   /   |  _________    /  \\   \\===\\     
 /==/   /     | /   /  \\ / / /  __________\\_____      ______       ___
|===| /       |/   /____/ / /   \\   _____ |\\   /      \\   _ \\      \\  \\
 \\==\\             /\\   / / /     | |  /= \\| | |        | | \\ \\     / _ \\
 \\===\\__    \\    /  \\ / / /   /  | | /===/  | |        | |  \\ \\   / / \\ \\
   \\==\\ \\    \\\\ /____/   /_\\ //  | |_____/| | |        | |   | | / /___\\ \\
   \\===\\ \\   \\\\\\\\\\\\\\/   /////// /|  _____ | | |        | |   | | |  ___  |
     \\==\\/     \\\\\\\\/ / //////   \\| |/==/ \\| | |        | |   | | | /   \\ |
     \\==\\     _ \\\\/ / /////    _ | |==/     | |        | |  / /  | |   | |
       \\==\\  / \\ / / ///      /|\\| |_____/| | |_____/| | |_/ /   | |   | |
       \\==\\ /   / / /________/ |/_________|/_________|/_____/   /___\\ /___\\
         \\==\\  /               | /==/
         \\=\\  /________________|/=/   
           \\==\\     _____     /==/ 
          / \\===\\   \\   /   /===/
         / / /\\===\\  \\_/  /===/
        / / /   \\====\\ /====/
       / / /      \\===|===/
       |/_/         \\===/
                      =
'''

logo29 = '''
                                           /
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \\.\\
       ____      |___._.  |       __               \\ `.
     .'    `---""       ``"-.--"'`  \\               .  \\
    .  ,            __               `              |   .
    `,'         ,-"'  .               \\             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'\\'   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \\ `        `.    .      .'/
 j|:D  \\          `--'  ' ,'_  . .         `.__, \\   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  """""'                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) \\`._        ___....----"'  ,'   .'  \\ |   '  \\  .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\\ ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''"""""`.,^.`.--'
'''

logo30 = '''
        .--.       .--.
    _  `    \     /    `  _
     `\.===. \.^./ .===./`
            \/`"`\/
         ,  | y2k |  ,
        / `\|;-.-'|/` \\
       /    |::\\  |    \\
    .-' ,-'`|:::; |`'-, '-.
        |   |::::\\|   | 
        |   |::::;|   |
        |   \:::://   |
        |    `.://'   |
jgs    .'             `.
    _,'                 `,_
'''

logo31 = '''
             _____
          .-'.  ':'-.
        .''::: .:    '.
       /   :::::'      \\
      ;.    ':' `       ;
      |       '..       |
      ; '      ::::.    ;
       \       '::::   /
        '.      :::  .'
jgs        '-.___'_.-'
'''

logo32 = '''
   __J"L__
  ,-'`--...--'`-.
 /  /\\  ___  /\\  \\
J   ""  \\_/  ""   L
|                 |
J    /\\/VWV\\/\\    F
 \\  (/\\/\\_/\\/\\)  /
  "-._       _,-"
      """""""
'''

logos.append(logo)
logos.append(logo1)
logos.append(logo2)
logos.append(logo3)
logos.append(logo4)
logos.append(logo5)
logos.append(logo6)
logos.append(logo7)
logos.append(logo8)
logos.append(logo9)
logos.append(logo10)
logos.append(logo11)
logos.append(logo12)
logos.append(logo13)
logos.append(logo14)
logos.append(logo15)
logos.append(logo16)
logos.append(logo17)
logos.append(logo18)
logos.append(logo19)
logos.append(logo20)
logos.append(logo21)
logos.append(logo22)
logos.append(logo23)
logos.append(logo24)
logos.append(logo25)
logos.append(logo26)
logos.append(logo27)
logos.append(logo28)
logos.append(logo29)
logos.append(logo30)
logos.append(logo31)
logos.append(logo32)

quotes = []

q1 = 'When your only tool is a hammer, all problems start looking like nails.'
q2 = 'Artificial intelligence is no match for natural stupidity.'
q3 = 'The last thing I want to do is insult you. But it IS on the list.'
q4 = 'I don\'t have a solution, but I do admire the problem.'
q5 = 'The only substitute for good manners is fast reflexes.'
q6 = 'Support bacteria - they\'re the only culture some people have.'
q7 = 'Letting the cat out of the bag is a whole lot easier than putting it back in.'
q8 = 'Well, here I am! What are your other two wishes?'
q9 = 'Always remember you\'re unique, just like everyone else.'
q10 = 'Everybody repeat after me: \"We are all individuals.\"'
q11 = 'Confession is good for the soul, but bad for your career.'
q12 = 'A bartender is just a pharmacist with a limited inventory.'
q13 = 'I want patience - AND I WANT IT NOW!!!!'
q14 = 'A day for firm decisions! Or is it?'
q15 = 'Am I ambivalent? Well, yes and no.'
q16 = 'Bombs don\'t kill people, explosions kill people.'
q17 = 'Bureaucrats cut red tape, lengthwise.'
q18 = 'Help stamp out, eliminate and abolish redundancy!'
q19 = 'How many of you believe in telekinesis? Raise MY hand!'
q20 = 'A dog has an owner. A cat has a staff.'
q21 = 'Every organisation is perfectly designed to get the results they are getting.'
q22 = 'Which one of these is the non-smoking lifeboat?'
q23 = 'Treat each day as your last; one day you will be right.'
q24 = 'Red meat is not bad for you. Fuzzy green meat is bad for you.'
q25 = 'The early bird may get the worm, but the second mouse gets the cheese.'
q26 = 'The problem with sex in the movies is, that the popcorn usually spills.'
q27 = 'Living on Earth is expensive, but it does include a free trip around the sun.'
q28 = 'Despite the cost of living, have you noticed how popular it remains?'
q29 = 'All power corrupts. Absolute power is pretty neat, though.'
q30 = 'I might be an asshole, but being nice is something dumb people do to hedge their bets.'
q31 = 'Blasphemy is a victimless crime.'
q32 = 'Immortality was created by christians to sell crosses, the fuck outta here'

quotes.append(q1)
quotes.append(q2)
quotes.append(q3)
quotes.append(q4)
quotes.append(q5)
quotes.append(q6)
quotes.append(q7)
quotes.append(q8)
quotes.append(q9)
quotes.append(q10)
quotes.append(q11)
quotes.append(q12)
quotes.append(q13)
quotes.append(q14)
quotes.append(q15)
quotes.append(q16)
quotes.append(q17)
quotes.append(q18)
quotes.append(q19)
quotes.append(q20)
quotes.append(q21)
quotes.append(q22)
quotes.append(q23)
quotes.append(q24)
quotes.append(q25)
quotes.append(q26)
quotes.append(q27)
quotes.append(q28)
quotes.append(q29)
quotes.append(q30)
quotes.append(q31)
quotes.append(q32)


parser.add_argument('-a','--ascii', help='show me some ascii goodness', required=False)
parser.add_argument('-r','--random', help='show me some random ascii goodness', required=False)
parser.add_argument('-n','--num', help='specify art by number', required=False)
parser.add_argument('-l','--loop_em', type = int, help='loop the art randomly X amount of times', required=False)

args = vars(parser.parse_args())

try:
    if args['ascii'] != None:
        print(logos[0])
        print(quotes[0])

    elif args['random'] == 'rando':
        val = randint(0, 30)
        print(logos[val])
        print(quotes[val])
    
    elif args['num'] != None and int(args['num']) > 0:
        print(logos[int(args['num'])])
    
    elif int(args['loop_em']) > 0:
        for i in range(int(args['loop_em'])):
            val2 = randint(0, 30)
            print(logos[val2])
            print(quotes[val2])
            time.sleep(1)

    else:
        print('Invalid Choice')
except KeyboardInterrupt:
    print('Leaving Program... Goodbye')

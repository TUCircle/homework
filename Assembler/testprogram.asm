;Unterfunktionensammlung
;Dies ist eine Sammlung von Funktionen die ich mal
;für die Mikroone geschrieben habe.
;Den Mikroone-Assembler Emulator findet man hier:
; http://d24a.de/mikroone/index.php/home/


;==============
;Multiplikation
;==============
mul:
POP R[7]
POP R[3]
POP R[2]

ADD R[4], R[0], R[0]

mul_begin:
ADD R[2], R[0], R[2]
JZ mul_end
ADD R[4], R[4], R[3]
SUB R[2], R[2], R[1]
JMP mul_begin

mul_end:
PSH R[4]
PSH R[7]
RTS
;==============
;Division
;==============
div:
POP R[7]
POP R[3]
POP R[2]

ADD R[4], R[0], R[0]

div_begin:
ADD R[2], R[0], R[2]
JZ div_end
SUB R[2], R[2], R[3]
JC div_end
ADD R[4], R[4], R[1]
JMP div_begin

div_end:
PSH R[4]
PSH R[7]
RTS
;==============
;Modulo
;==============
mod:
LDL R[4], 0
POP R[7]
POP R[3]
POP R[2]


mod_begin:
JC mod_end
ADD R[4], R[0], R[2]
JZ mod_end
SUB R[2], R[2], R[3]
JMP mod_begin

mod_end:
PSH R[4]
PSH R[7]
RTS


;=========
;Fakultät Iterativ
;=========

fakit:
POP R[6]
POP R[2]
LDL R[3], 1 ; Return-Wert
LDL R[4], 2 ;Iterationsvariable

fakit_loop:
PSH R[2]
PSH R[4]
SUB R[5],R[2], R[4]
JC fakit_end
PSH R[3]
PSH R[4]
JS mul
POP R[3]
POP R[4]
POP R[2]
ADD R[4], R[4], R[1]
JMP fakit_loop

fakit_end:
PSH R[3]
PSH R[6]
RTS


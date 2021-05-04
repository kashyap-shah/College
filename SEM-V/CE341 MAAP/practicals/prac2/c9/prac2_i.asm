
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

MOV Al, 41
MOV Bl, 5
MOV CL, 9

SUB AL, 32
MUL BL
DIV CL

ret







; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

MOV [4000H], 1111H
MOV [4002H], 1111H   
MOV [4004H], 2222H
MOV [4006H], 2222H

MOV AX, [4000H]
MOV BX, [4002H]
MOV CX, [4004H]
MOV DX, [4006H]

SBB AX, CX 
SBB BX, DX

MOV [7000H], AX 
MOV [7002H], BX   

ret





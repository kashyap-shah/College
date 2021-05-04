
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

MOV [4000H], 0000110B   ;149

MOV AX, [4000H]
SHL AX ,1  
MOV [4001H], AX 
SHR AX ,1
MOV [4002H], AX

ret






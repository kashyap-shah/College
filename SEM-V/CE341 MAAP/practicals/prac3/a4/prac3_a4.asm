
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h
             
MOV [2000H], 10010101B   ;149
MOV [2001H], 01010010B   ;82

MOV AL, [2000H]  
XOR AL, [2001H]

MOV [2002H], AL 

ret






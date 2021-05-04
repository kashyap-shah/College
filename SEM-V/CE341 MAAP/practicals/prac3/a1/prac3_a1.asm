
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

MOV [4000H], 10010101B
MOV [4001H], 01010010B

MOV AL, [4000H]  
OR AL, [4001H]

MOV [4002H], AL 

ret





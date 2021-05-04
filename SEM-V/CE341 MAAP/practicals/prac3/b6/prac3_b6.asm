
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

MOV [4001H], 0110B   ;149
MOV [4002H], 0110B   ;82

MOV AL, [4001H] 
MOV BL, [4002H] 

NOT BL

ADD AL, BL
MOV [4003H], AL 

ret






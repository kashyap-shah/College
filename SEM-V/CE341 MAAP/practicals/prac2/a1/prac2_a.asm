
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

; add your code here 

mov ax, 5000h
mov ds, ax
mov [4000h], 32h

ret





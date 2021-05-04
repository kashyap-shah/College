
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

; add your code here

mov ax, 4000h
mov ds, ax   

mov [2000h], 40h
mov [4000h], 10h   

mov bl, [2000h] ; transfer data of 2000 location to the register bl

xchg bl, [4000h] ; exchanging values of reg bl and 4000 location 
         
mov [2000h], bl ;
         
ret





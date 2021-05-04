
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

mov [2000h], 15h
mov [4000h], 18h
mov al, [2000h]
mov bl, [4000h]

sub bl,al
mov [4002h], bl
ret





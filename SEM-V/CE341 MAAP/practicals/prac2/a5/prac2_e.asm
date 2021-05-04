
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

mov [4000h],10h
mov [4001h],20h
mov [4002h],30h
mov [4003h],40h

mov al,[4000h]
mov ah,[4001h]
mov bl,[4002h]
mov bh,[4003h]
                
add ax,bx
mov [4004h],al
mov [4005h],ah


ret





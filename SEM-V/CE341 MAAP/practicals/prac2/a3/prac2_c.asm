
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

mov ax, 3000h
mov ds, ax   

mov al, 20h
mov bl, 25h
mov cl, 15h
mov dl, 30h

add al,bl ; adding al and bl result will be stored in al

sub al,cl ; subtractingg al and cl result will be stored in al 

adc al,dl ; adding al and dl result will be stored in al 

mov bh,al ;
         
ret





; EMU8086 - Afficher un nombre 16 bits en décimal
; Compilez et exécutez directement dans emu8086

org 100h

start:
    mov ax, 12345    ; Nombre à afficher - CHANGEZ ICI !
    call print_num    ; Appel de la routine
    
    ; Attendre une touche
    mov ah, 1
    int 21h
    
    ret              ; Retour au DOS

; ================================================
; Routine pour afficher le nombre dans AX
; ================================================
print_num proc
    push ax
    push bx
    push cx
    push dx
    
    ; Gestion du zéro
    cmp ax, 0
    jne not_zero
    mov dl, '0'
    mov ah, 2
    int 21h
    jmp fin_affichage
    
not_zero:
    mov cx, 0        ; Compteur de chiffres
    mov bx, 10       ; Base décimale

empiler_chiffres:
    xor dx, dx       ; DX = 0
    div bx           ; AX = quotient, DX = reste
    push dx          ; Empiler le chiffre
    inc cx           ; Un chiffre de plus
    
    test ax, ax      ; Quotient = 0 ?
    jnz empiler_chiffres ; Non, continuer

afficher_chiffres:
    pop dx           ; Dépiler un chiffre
    add dl, '0'      ; Convertir en ASCII
    mov ah, 2        ; Fonction afficher caractère
    int 21h
    loop afficher_chiffres

fin_affichage:
    pop dx
    pop cx
    pop bx
    pop ax
    ret
print_num endp

end start
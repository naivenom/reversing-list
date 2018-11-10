; Assemble:       nasm -f elf64 -l reto.lst  reto.asm
; Link:           gcc -m64 -o reto  reto.o
section .text
    global main
main:
    mov ecx, 41       ;Mueve 0x29 a ECX
lop:                  ;Bucle
    mov eax, msg      ;Mueve la direccion de memoria de msg a EAX
    add eax, ecx      ;Suma 0x29 a EAX
    mov edx, 0        ;Mueve 0 a EDX
    mov edx, [eax]    ;Mueve el contenido de EAX a EDX
    xor edx, 0xb      ;Operacion XOR de 0xb con EDX
    mov [eax], edx    ;Mueve EDX, al contenido de EAX 
    mov edx, 0        ;Mueve 0 a EDX
    mov dx, [eax]     ;Mueve el contenido de EAX a DX (Parte baja de EDX, 16 bytes)
    rol dx, 0x5       ;Rota 5 bits a la izquierda a DX (16 bits)       binary  0b0000000101100000
    mov edx, 0        ;Mueve a EDX 0
    mov dl, [eax]     ;Mueve el contenido de EAX a DL (Parte baja de DX, 8 bytes)
    ror dl, 0x9d      ;Rota 157 bits a la derecha a DL (8 bits)
    sub ecx, 1        ;Contador decrementa valor de msg
    cmp ecx, 0        ;Compara si es 0, si es 0 salta
    jge lop           ;Salto condicional
    mov edx, 41
    mov ecx, msg
    mov ebx, 1
    mov eax, 4
    int 0x80
    mov eax, 1
    int 0x80

section .data
   msg  db  0x63, 0x64, 0x65, 0x6e, 0x72, 0x68, 0x64, 0x65, 0x39, 0x40, 0x3a, 0x33, 0x70, 0x3a, 0x54, 0x67, 0x3b, 0x7d, 0x38, 0x54, 0x73, 0x33, 0x3d, 0x54, 0x3f, 0x78, 0x78, 0x38, 0x66, 0x69, 0x67, 0x72, 0x54, 0x68, 0x3f, 0x69, 0x38, 0x78, 0x63, 0x3b, 0x76

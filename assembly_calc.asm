;adding two numbers

section .text
global _start
_start:
  
    mov eax,4
    mov ebx,2
    
    ;adding
    add eax,ebx
    add eax,'0'
    mov [sum],eax
    
    ;printing the message
    mov edx,len
    mov ecx,msg
    mov ebx,1
    mov eax,4
    int 0x80
    
    ;printing the sum
    mov edx,1
    mov ecx,sum
    mov ebx,1
    mov eax,4
    int 0x80
    
    ;exiting
    mov ebx,0 
    mov eax,1
    int 0x80
    
section .data
msg db "The sum is : "
len equ $ - msg

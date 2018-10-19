section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;; rdx is length
	;; rsi is byte to copy
	;; rdi is dest to copy to

	mov rcx, rdx
	mov al, sil
	mov rsi, rdi
	

	rep stosb		; copy one byte of al to rsi.  al is lowest byte of rax
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

	;; rdx is length
	;; rsi is source string
	;; rdi is dest to copy to

	mov rcx, rdx
	mov rdx, 0
copy_loop:
	mov rax, [rsi + rdx] 
	inc rdx
	
	stosb			;copy next byte (stored in al) to rdi

	loop copy_loop

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!

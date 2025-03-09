;-------------------------------------------------------------------------------------------------------------------------------------------------------
data	segment							; data segment. Keyword db means define byte. You can also define word (dw)
		iNum	db  225					;Define input number
		userinput db 21, ?,  21 dup("$")  ; Declaring userinput as mentioned in int 21.A 

data	ends

										; stack segment
stack1  segment	stack 		
		db	100 dup(?)      			; This is the stack of 100 bytes
stack1  ends


code    segment
        assume  cs:code, ds:data, ss:stack1

start: 
										;Perform initialization 
		mov ax, data					;Put the starting address of the data segment into the ax register (must do this first)
		mov ds, ax						;Put the starting address of the data segment into the ds register (where it belongs)
		
		mov ax, stack1					;Put the starting address of the stack into the ax register (must do this first)
		mov ss, ax						;Put the starting address of the stack segment into the ss register (where it belongs)
;-------------------------------------------------------------------------------------------------------------------------------------------------------		
;****************** Perform Newton's Algorithm ******************

		mov ah, 0Ah     ;loading subroutine that input from user as mentioned in slide 5
		lea dx,userinput  ; dx contains the starting memory address of string ‘userinput’
		int 21h ; Return control to dos prompt

		
;-------------------------------------------------------------------------------------------------------------------------------------------------------										
		mov ah, 4ch 					;Set up code to specify return to dos
        int 21h							;Interpt number 21 (Return control to dos prompt)

code    ends

end     start
;-------------------------------------------------------------------------------------------------------------------------------------------------------




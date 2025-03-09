;-------------------------------------------------------------------------------------------------------------------------------------------------------
data	segment							; data segment. Keyword db means define byte. You can also define word (dw)
		iNum	db  225					;Define input number
		userinput db 21, ?,  21 dup("$") ; Declaring userinput as mentioned in int 21.A
		newline db 10,13, '$'  ; clearing input buffer by a new line
		var1 db "Enter a string (max 20 char.)", 10,13, "$" ; first string declartion with cursor pointing to next line and carriage return
		str_output db "The string you entered is:",10,13, "$" ; second string declartion with cursor pointing to next line and carriage return
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


		mov ah, 09h ; loading subroutine that prints the string
		lea dx, var1 ; dx contains the starting memory address string var1 as mentioned in slide 5 page 56
		int 21h ; Return control to dos prompt

		mov ah, 0Ah     ;loading subroutine that input from user as mentioned in slide 5
		lea dx,userinput  ; dx contains the starting memory address of string ‘userinput’
		int 21h ; Return control to dos prompt

		mov ah, 09h ; loading subroutine that prints the string
		lea dx, newline ;dx contains the starting memory address newline
		int 21h; Return control to dos prompt

		mov ah, 09h; loading subroutine that prints the string
		lea dx, str_output; dx contains the starting memory address string str_output
		int 21h	;  Return control to dos prompt

		; Display user input
		mov ah, 09h; loading subroutine that prints the string
		lea dx, userinput+2 ; dx contains the starting memory address string userinput and with offset 2 so that it points toward the user entered string
		int 21h ;Return control to dos prompt
	
		


;-------------------------------------------------------------------------------------------------------------------------------------------------------										
		mov ah, 4ch 					;Set up code to specify return to dos
        int 21h							;Interpt number 21 (Return control to dos prompt)

code    ends

end     start
;-------------------------------------------------------------------------------------------------------------------------------------------------------




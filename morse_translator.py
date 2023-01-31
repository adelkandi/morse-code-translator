def translate_to_morse(inp):
                    
                    #morse dictionary of : alphabets and numbers and codes
                    M_CODE_DCT = {
'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
'F':'..-.', 'G':'--.', 'H':'....', 
'I':'..', 'J':'.---', 'K':'-.-', 
'L':'.-..', 'M':'--', 'N':'-.', 
'O':'---', 'P':'.--.', 'Q':'--.-', 
'R':'.-.', 'S':'...', 'T':'-', 
'U':'..-', 'V':'...-', 'W':'.--', 
'X':'-..-', 'Y':'-.--', 'Z':'--..', 
'1':'.----', '2':'..---', '3':'...--', 
'4':'....-', '5':'.....', '6':'-....', 
'7':'--...', '8':'---..', '9':'----.', 
'0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..',
 '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-',
                    }

                    inp = inp.upper()
                    m_c = ""
                    
                    for i in range(len(inp)):
                    	# if value of inp is existing in the dictionary ...
                    	if inp[i] in M_CODE_DCT:
                    		# every index in variable inp is changed by the value of every key in ( M_CODE_DCT )
                    		m_c = M_CODE_DCT[inp[i]] + m_c
                    
                    	else:
                    		print("Try Again ^-^")
                    		
                    print(inp, " : " ,m_c)
                   
                    	
# run :)
message = input("Enter the message you wanna translate: ")
translate_to_morse(message)

print("\nWANNA ENCODE AGAIN?\nENTER YES || Y\nENTER NO  || N")
		encod_again = input("\nENTER YOUR RESPONSE:").upper()
		if encod_again == "YES" or encod_again == "Y":
			print("\nENCODING COUNTER:",encoder_counter)
			user_word2 = input("ENTER YOUR ENCODING WORD: ")
			encoding (user_word2)
			encoder_counter+=1
		elif encoder_counter > 3:
			print("\nYOUR DECODING LIMIT EXCEEDED")
			break
		elif encod_again == "NO" or encod_again == "N":
			print("\nOKAY NO ENCODING ")
			break
		else:
			print("WRONG PROMPT (YES/Y)(NO/N)")
			break
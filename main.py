
      # SECRET LANGUAGE
import random
import string
from colorama import Fore
from time import sleep

chars = string.ascii_letters
digits = string.digits
combination= chars + digits

# print(chars)
# print(digits)
# print(combination)

#starting_3_random_word_producer
def s_r_w_p():
	chars = string.ascii_letters
	digits = string.digits
	combination = chars + digits
	lenOfFword = 3
	threeFword = "".join(random.sample(combination,lenOfFword))
	#print(threeFword)
	return threeFword

#ending_3random_word_producer
def e_r_w_p():
	chars = string.ascii_letters
	digits = string.digits
	combination = chars + digits
	lenOfLword = 3
	threeLword = "".join(random.sample(combination,lenOfLword))
	#print(threeLword)
	return threeLword


def encoding(eword):
	try:
		#eword_encodingWORD
		if len(eword) >= 3:
			print("\nYOUR ENCODING WORD=> ",eword)
			#fWord_firstWORD//taking first word
			fWord = eword[0]
			#sWord = startingWORD// initialise the starting word
			sWord = eword[1:]
			#print(sWord)
			#fWord = sWord[0]
			#print(fWord)
			#lWord=lastWord//now adding those two words.
			lWord = sWord+fWord
			#print(lWord)
			#F_first,L_last//calling func to get three random char
			threeFword1 = s_r_w_p()
			threeLword1 = e_r_w_p()
			#FL_first,last//now adding all words into one final word
			FLEFinalWord = threeFword1+lWord+threeLword1
			print("\nYOUR ENCODED WORD=> ",FLEFinalWord)
			return FLEFinalWord
		else:
			print("\nYOUR ENCODING WORD=> ",eword)
			#if word less than 3, just reverse it.here reversing
			reverse_word = eword[::-1]
			print("\nYOUR ENCODED WORD=> ",reverse_word)
			return reverse_word
			
	except TypeError as TE:
		#print(TE)
		print("TO PERFORM THE ENCODING\nENTER A (STRING) CHAR!")

def decoding(dword):
	try:
		if len(dword)<3:
			print("\nYOUR DECODING WORD=> ",dword)
			yourDWord = dword[::-1]
			print("\nYOUR DECODED WORD=> ",yourDWord)
			return yourDWord
		else:
			print("\nYOUR DECODING WORD=> ",dword)
			#R_remove,S_starring_D_decoding,Word
			rSDWord = dword[3:]
			#print(rSDWord)
			#R_remove,L_last,D_decoding,word
			rLDWord = rSDWord[:-3]
			#print(rLDWord)

			#s_store,L_last,char
			sLChar = rLDWord[-1]
			'''
			print(rLDWord[len(
			rLDWord)-1])
	    '''
			#print(sLChar)

			#r_remove,l_last,char
			rLchar = rLDWord[:-1]
			#print(rLchar)

			#append sLchar 2 rLchar
			#Fisrt,Last,Decoding
			FLDFinalWord = sLChar+rLchar
			print("\nYOUR DECODED WORD=> ",FLDFinalWord)
			return FLDFinalWord
			
	except TypeError as TE:
		#print(TE)
		print("TO PERFORM DECODING\nENTER ANY STRING")


if __name__ == "__main__":
	pass
#start
print("\n")
print("-"*43)
print(Fore.CYAN+"ENCODER AND DECODER BY AHMED-ORACLE".center(43)+Fore.RESET)
print("-"*43)
print(Fore.RED+"\nWHAT YOU WANNA DO?"+Fore.CYAN+"\nENCODING || DECODING"+Fore.BLACK+"\nFOR ENCODING ENTER "+Fore.MAGENTA+"E"+Fore.BLACK+"\nFOR DECODING ENTER "+Fore.MAGENTA+"D",Fore.RESET)

user_choice = input("\nENTER YOUR CHOICE:").upper()
encoder_counter = 1
decoder_counter = 1
while True:
	if user_choice == "E":
		user_word = input("\nENTER YOUR ENCODING WORD:")
		sleep(0.69)
		encoding(user_word)
		print("\nWANNA ENCODE AGAIN?\nENTER YES || Y\nENTER NO  || N")
		encod_again = input("\nENTER YOUR RESPONSE:").upper()
		if encod_again == "YES" or encod_again == "Y":
			user_word = input("\nENTER YOUR ENCODING WORD: ")
			encoding (user_word)
		elif encod_again == "NO" or encod_again == "N":
			print("\nOKAY NO ENCODING ")
			break
		else:
			print("WRONG PROMPT (YES/Y)(NO/N)")
			break
	elif user_choice == "D":
		print("\nDECODER COUNTER:",decoder_counter)
		user_word = input("ENTER YOUR DECODING WORD:")
		sleep(0.69)
		decoding(user_word)
		decoder_counter+=1
		if decoder_counter > 3:
			break
	else:
		print("WRONG PROMPT!")
		break
		


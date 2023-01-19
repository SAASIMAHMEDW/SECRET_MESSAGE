
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

#generating three ramdom word
#starting_3_random_word_producer
def s_r_w_p():
	'''THIS FUNCTION GENERATE THREE RANDOM CHAR FOR APPENDING IN THE GIVEN ENCODING WORD. (AT BEGINNING)'''
	chars = string.ascii_letters
	digits = string.digits
	combination = chars + digits
	lenOfFword = 3
	threeFword = "".join(random.sample(combination,lenOfFword))
	#print(threeFword)
	return threeFword

#generating three random word
#ending_3random_word_producer
def e_r_w_p():
	'''THIS FUNCTION GENERATE THREE RANDOM CHAR FOR APPENDING IN THE GIVEN ENCODING WORD. (AT ENDING)'''
	chars = string.ascii_letters
	digits = string.digits
	combination = chars + digits
	lenOfLword = 3
	threeLword = "".join(random.sample(combination,lenOfLword))
	#print(threeLword)
	return threeLword


def encoding(eword):
	"""THIS FUNCTION TAKES ONLY ONE ARGUMENT. AND THEN GENERATE THE ENCRYPTED OR ENCODED WORD OF THE GIVEN WORD"""
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
	"""THIS FUNCTION ALSO TAKES ONLY ONE ARGUMENT AND GENERATE THE DECRIPTED OR DECODED WORD OF THE GIVEN WODD"""
	try:
		if len(dword)<3:
			print("\nYOUR DECODING WORD=> ",dword)
			#len is less thab 3 so here reversing.
			yourDWord = dword[::-1]
			print("\nYOUR DECODED WORD=> ",yourDWord)
			return yourDWord
		else:
			print("\nYOUR DECODING WORD=> ",dword)
			#R_remove,S_starring_D_decoding,Word===removing the starting three word
			rSDWord = dword[3:]
			#print(rSDWord)
			#R_remove,L_last,D_decoding,word===removing the last three word
			rLDWord = rSDWord[:-3]
			#print(rLDWord)

			#s_store,L_last,char===taking last one letter and adding in sLChar varriable
			sLChar = rLDWord[-1]
			'''
			print(rLDWord[len(
			rLDWord)-1])
	    '''
			#print(sLChar)

			#r_remove,l_last,char===removing last one word and appending rest of the word in rLChar variable
			rLchar = rLDWord[:-1]
			#print(rLchar)

			#append sLchar 2 rLchar to produce final word
			#Fisrt,Last,Decoding
			FLDFinalWord = sLChar+rLchar
			print("\nYOUR DECODED WORD=> ",FLDFinalWord)
			return FLDFinalWord
			
	except TypeError as TE:
		#print(TE)
		print("TO PERFORM DECODING\nENTER ANY STRING")

#ignore
if __name__ == "__main__":
	#encoding ()
	pass
	
#start
print("\n")
print("-"*43)
print(Fore.CYAN+"ENCODER AND DECODER BY AHMED-ORACLE".center(43)+Fore.RESET)
print("-"*43)
print(Fore.MAGENTA+"\nREAD CAREFULLY!!!"+Fore.RESET)
print(Fore.RED+"WHAT YOU WANNA DO?"+Fore.CYAN+"\nENCODING || DECODING"+Fore.BLACK+"\nFOR ENCODING ENTER "+Fore.MAGENTA+"E"+Fore.BLACK+"\nFOR DECODING ENTER "+Fore.MAGENTA+"D\n"+Fore.BLACK+"ENTER "+Fore.MAGENTA+"EXIT "+Fore.BLACK+"FOR EXIT"+Fore.RESET)

user_choice = input("\nENTER YOUR CHOICE:").upper()

encoder_counter = 1
decoder_counter = 1
while True:
	#encoding
	if user_choice == "E":
		if encoder_counter == 1:
			print(Fore.RED+"\nYOU CAN ENCODE THREE TIMES!"+Fore.RESET)
		print("\n-ENCODING COUNTER:",encoder_counter)
		user_word1 = input("•ENTER YOUR ENCODING WORD:")
		sleep(0.69)
		encoding(user_word1)
		encoder_counter+=1
		if encoder_counter > 3:
			print("\n!YOUR DECODING LIMIT EXCEEDED")
			break
			
	#decoding	
	elif user_choice == "D":
		if decoder_counter == 1:
			print(Fore.RED+"\nYOU CAN DECODE THREE TIMES!"+Fore.RESET)
		print("\n-DECODER COUNTER:",decoder_counter)
		user_word = input("•ENTER YOUR DECODING WORD:")
		sleep(0.69)
		decoding(user_word)
		decoder_counter+=1
		
		if decoder_counter > 3:
			print("\nYOUR DECODING LIMIT EXCEEDED")
			break
			
	elif user_choice == "EXIT":
		print(Fore.RED+"\nYOU HAVE BEEN EXITED")
		break
	else:
		print(Fore.RED+"\nWRONG PROMPT!")
		break
		


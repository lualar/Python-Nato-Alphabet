from pickle import TRUE
import pandas as pd
import datetime 

#Dict comprehension from PandasDataframe
#t1 = datetime.datetime.now()
dfNato = pd.read_csv("./Alphabet/nato_phonetic_alphabet.csv")
dNatoAlphabet2 = {row.letter:row.code for index, row in dfNato.iterrows()}
#t2 = datetime.datetime.now()
#delta = t2 - t1
#print (f"Method 1 Time: {delta.microseconds} seconds")
#print (f"NATO Alphabet: {dNatoAlphabet2}")

sExit = False
while sExit == False:
    try:
        #ask for a word
        sUserInput = input("\nEnter a single word:")
        sUserInput = sUserInput.replace(" ", "").upper()
 
        #Method 1 (fastest -- correct)
        lWords = [dNatoAlphabet2[letter] for letter in sUserInput]
        sExit = True
    except BaseException:
        lWords  = "Sorry, only letters in the word please."
    else:
        print(f"\nNato Alphabet Results: {lWords}")




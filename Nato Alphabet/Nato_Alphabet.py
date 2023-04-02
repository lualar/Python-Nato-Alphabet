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

#ask for a word
sUserInput = input("\nEnter a single word:")
sUserInput = sUserInput.replace(" ", "").upper()
 
#Method 1 (fastest -- correct)
lWords = [dNatoAlphabet2[letter] for letter in sUserInput]
print(f"\nMethod 1: {lWords}")

#Method 2 (my way !!!)
#t1 = datetime.datetime.now()
#lWords = []
#for letter in sUserInput:
#    lWords.append({v for (k,v) in dNatoAlphabet2.items() if k==letter})
#print(f"\nMethod 2: {lWords}")
#t2 = datetime.datetime.now()
#delta = t2 - t1
#print (f"Methos 2 Time: {delta.microseconds} seconds")



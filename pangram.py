"""

#This function helps check if a word is a pangram
print("Hello, I would love to tell you if a word or a sentence " + 
	" is a pangram")
print("If you are going to be entering a sentence, please do" + 
	" not space the words")
word = input("Please enter the word or sentence:\n")
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
separate_words = list(word)
uniques = set(separate_words)
new_list = []
for unique in uniques:
    new_list.append(unique)
new_list.sort()
if new_list == alphabets:
    print("This word is a pangram!!!")
else:
    print("This word is not a pangram!!!")
    
"""
    
    
    
            
        
	
   
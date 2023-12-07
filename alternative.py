
#For this task I am required to create a program that reads each alternate character an upper case character and each other alternate character a lowercase character.

phrase = "Rugby is my favourite sport."
final = ""
for b in range(len(phrase)):
    if b % 2 == 1:
      final += phrase[b].upper()
   
    else: 
      final += phrase[b].lower()

print(final)

#For this task I am required to create a program that reads each alternative word as an lowercase word and uppercase word.
sentence = "Mcdonalds is nice to eat"
split_sentence = sentence.split()
word = ""

for a in range(len(split_sentence)):
   
   if a % 2 == 1:
      word += split_sentence[a].lower()

   else: 
      word += split_sentence[a].upper()

print(word)
      


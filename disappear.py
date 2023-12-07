
#For this task I am required to ask user to input a string and then i will ask user which characters they would like to make disappear.
#E,g THe quick brown fox jumps
#after stripping a,e,i,o,u
#Th qck brwn fx jmps.

sentence = str(input("Enter a sentence: "))

print (sentence)

striped_sen = sentence.translate({ord(i): None for i in(input("Enter the letters that you want removed (Use commas to seperate letters): "))})

print(striped_sen)
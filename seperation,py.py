
#For this task I am required to ask a user to input a sentence and then display each word of the sentence on a seperate line.


sentence= str(input("Enter a sentence: "))
split_sentence = sentence.split()

for word in split_sentence:
    print(word)

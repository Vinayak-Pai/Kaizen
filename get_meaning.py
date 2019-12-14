from PyDictionary import PyDictionary

__author__ = 'vinayak'

input_word = input("Enter the word:")

meaning = PyDictionary().meaning(input_word)

if meaning and meaning['Noun']:
    print("Meaning of the word \"{}\":".format(input_word))
    for i in meaning['Noun']:
        print ("* {}".format(i))
else:
    print(" Sorry, word not found in our database")

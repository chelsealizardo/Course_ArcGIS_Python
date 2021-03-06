
#####
# Step 0 - Practice tasks before we start.
#####

# Task a: Express the following sequences as lists:

##### Create an integer list 1, 2, 3, 4, 5, 6, 7, call it "intList"

intList = [1, 2, 3, 4, 5, 6, 7]

##### Create a string list using the sentence: "daYS lAtEr EvEryoNe waS buSy SO I WenT To THE MOVie aLOne" and call it "strList"

strList = ["dAYS", "lAtEr", "EvEryoNe", "waS", "buSy", "SO", "I", "WenT", "To", "THE", "MOVie", "aLOne"]

# Task b: Using a for loop, do the following:

##### Sum the values of intList and print result (28), yes you can use: print sum(intList), call it strValue.

strValue = 0
for value in intList:
    strValue = strValue + value
print strValue

##### Go through each word of strList, and create a sentence (called strSentence) where each word is in lower case ( i.e.*.lower() )

strSentence = ""
for word in strList:
    strSentence = strSentence + " " + word.lower()
print strSentence

##### Concatenate (join) the result of strValue and strSentence:

print str(strValue) + strSentence

# Task c: Use if to check status:

##### Use if/else to ask what type of data your intList is, do the sum if int and print the result Ensure you
##### have an else that will catch a failure (i.e. if type does not equal int print "Input data not integer").
##### Hint, to test to see if all items in your list are integers, you need to use this: all(isinstance(item, int) for item in intList)
if all(isinstance(item, int) for item in intList):
    print sum(intList)
else:
    print "Input data not integer"

##### Using the same code, run your strList, this should exit appropriately.
if all(isinstance(item, int) for item in strList):
    print sum(intList)
else:
    print "Input data not integer"
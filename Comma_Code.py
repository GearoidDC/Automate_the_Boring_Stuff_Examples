#List of items

spam = ['apples', 'bananas', 'tofu', 'cats', 4]

def Comma(items):
    #Set sentence equal to first item
    sentence = items[0]
    #Get length of list
    check = len(items)
    #For items in list between first and last add them to sentence
    for item in items[1:(check-1)]:
        sentence += ", " + str(item)
    #Add final item and return the sentence
    sentence += " and " + str(items[check-1])
    return(sentence)

print(Comma(spam))

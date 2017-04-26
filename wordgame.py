# incase of anything, the app will finally pick a random letter.


import random
def input_(allwords,letter):
    global player
    try:
        if letter == '':
            var = raw_input("Hi ,Please enter your first letter:  ")
        else:
            if len(letter) % 2 == 0:
                var = raw_input('Enter the next letter for %s ' % (letter))
                varl = len(var)
                if varl >= 2:
                    print "You entered more that one letter. Game Over!"
            else:
                # Call comp_var function that choses a letter as computer player
                var = comp_var(allwords,letter)
        print var
        letter = letter + var
        select = [word for word in allwords if word.startswith(letter)]
        exists(letter,select)

        return 'Game over!'
    except Exception as e:
        print e


def exists(letter,select):
    try:
        if len(select) == 0:
            print ('No such word %s in this list' % (letter))
            if len(letter) % 2 == 0:
                print 'Computer lost'
            else:
                print 'You Lost'
        else:
            print letter
            print select
            if letter in select:
                print "%s Found!" % (letter)
                if len(letter) % 2 == 0:
                    print 'Computer lost'
                else:
                    print 'You Lost'

            else:
                input_(select,letter)
    except Exception as e:
        print e


def comp_var(select,letter):
    try:
        if len(select) !=0:
            if len(select) == 1:
                word = select[0]
                length = len(letter)
                nextletter = word[length]
            else:
                if len(select) == 2:
                    for word in select:
                        if (len(word)) != (len(letter) + 1) :
                            word = word
                        else:
                            word = random.choice(select)
                elif len(select) > 2:
                    for word in select:
                        #Remove all words from list which if chosen will lead to ending game
                        if (len(word)) <= (len(letter) + 1):
                            if len(select) > 1:
                                # This if will ensure that we don't remain with an empty list and hence no word to work with
                                select.remove(word)
                        # If at this point we are remaining with only one word in our list, then thats the word comp'll choose
                    if len(select) == 1:
                        word = select[0]
                        # If we have more words in the list to choose from, we continue eliminating
                    else:
                        select_2 = []
                        for word in select:
                            # Lets choose a list of words that will render the computer player not the last to pick a letter
                            # in the next steps because by so, the computer will loose
                            if len(word) % 2 != 0 :
                                select_2.append(word)
                            else:
                                pass
                        word = max(select_2, key=len)
                        del select_2[:]
                else:
                    #With no option, we can randomly select a word from the list
                    word = random.choice(select)
                length = len(letter)
                nextletter = word[length]
            var = nextletter
            print "The computer chose %s" %(var)
            return var
        else:
            print "Out of range"
    except Exception as e:
        print e


#Define Letter / Word formed as global
letter = ''
class my_game:
    global letter
    try:
        #Empty list of our available words
        allwords = []
        # Populate list with words from words.text file
        with open("words.txt") as f:
            allwords = [word for line in f for word in line.split()]

        print input_(allwords,letter)

    except Exception as e :
        print e
    pass





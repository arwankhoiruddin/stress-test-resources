from random_words import RandomWords
import random
import sys
import os


def createFile(fname, rval):
    '''
    this function is used to generate
    fname = file name
    rval = number of words generated in the file
    '''
    f = open(fname, 'w')
    # this is just to give feedback so it does not feel that the program hang
    # or do nothing
    if rval < 10:
        mod = rval
    elif rval < 1000:
        mod = rval / 10
    elif rval < 100000:
        mod = rval / 100
    else:
        mod = rval / 1000
    # generate the words
    for i in range(rval):
        r = random.randint(1, 4)
        if i % mod == 0:
            print('word number for file : ' + fname + ': ' + str(i))
        w = random.choice(word)
        if r==1:
            w = w + '\n'
        elif r==2:
            w = w + ' '
        elif r==3:
            w = w + ', '
        else:
            w = w + '. '
        f.write(w)
    f.close()


if __name__ == "__main__":
    rw = RandomWords()
    word = rw.random_words(count=5400)

    lotbig = 'tesroot/lotbig/'
    lotsmall = 'tesroot/lotsmall/'

    if not os.path.exists(lotbig):
        os.makedirs(lotbig)
    if not os.path.exists(lotsmall):
        os.makedirs(lotsmall)

    for i in range(10):
        # small files, between 10 to 10,000 words
        createFile(lotsmall + str(i) + '.txt', random.randint(10, 10000))

        # big files, between 1 to 3 million words
        createFile(lotbig + str(i) + '.txt', random.randint(1000000, 3000000))

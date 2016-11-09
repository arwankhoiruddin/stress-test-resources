import os
import random
import shutil

from random_words import RandomWords
import random
import sys
import os

"""
This code is used to generate some levels of directories
with different size of files

The goal of this is to be used as stress test for ScramBox and ScramExplorer

To do the stress test for each products, just change the following variables:
- directory level (nlevel),
- number of files generated (nfiles)
- maximum size of files (maxSize)
"""

def createFile(fname, rval):
    '''
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
        # if i % mod == 0:
        #     print('word number for file : ' + fname + ': ' + str(i))
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


def createFolder(fname):
    '''
    create folder, if the folder exists, remove it first then create
    '''
    if not os.path.exists(fname):
        os.makedirs(fname)
    else:
        shutil.rmtree(fname)
        os.makedirs(fname)

def createLevels(nlevel, folderName):
    '''
    create multiple levels of directories
    '''
    if nlevel == 0:
        return 0
    else:
        for i in range(nfiles):
            tmpfolder = folderName + '/' + str(i)
            createFolder(tmpfolder)
            print 'Folder ' + tmpfolder + ' has been created'

            for j in range(nfiles):
                # create some files here
                tmpfile = tmpfolder + '/' + str(chr(97+j)) + '.txt'
                createFile(tmpfile, random.randint(10, maxSize))
                print 'File ' + tmpfile + ' has been created'

            # recursively create files and folders
            createLevels(nlevel-1, tmpfolder) # + '/' + str(nlevel))


if __name__ == "__main__":
    rw = RandomWords()
    word = rw.random_words(count=5400)

    # number of files generated on each folders
    nfiles = 3
    nlevel = 2

    # maximum size of files (in kilobytes)
    maxSize = 3000

    # create test set directory
    testdir = 'testSet'
    # createFolder(testdir)

    print 'Recursively generating files and folders. Please wait'
    createLevels(nlevel, testdir)

#! /usr/bin/env python3
# coding: utf-8

from random import *
import time
import datetime

def generateRandomGrammaticalLabelList(size):
    # generate a random list of 3 grammatical labels : NN, AD and PR of 'size' elements
    list = []
    for i in range(size):
        if ((randint(0, 100) % 3) == 0):
            list.append("NN")
        elif ((randint(0, 100) % 3) == 1):
            list.append("AD")
        else:
            list.append("PR")
    return list

def filterNouns(grammaticalLabel):
    # Return True if the label is a noun
    if(grammaticalLabel == "NN"):
        return True
    else:
        return False

def main():
    # get a list of grammatical label
    start_time = datetime.datetime.now()
    grammaticalLabelList = generateRandomGrammaticalLabelList(10000000)
    elapsed_time = datetime.datetime.now() - start_time
    print("grammaticalLabelList length =", len(grammaticalLabelList), "elapsed time =", str(elapsed_time)) 

    # filter only the noun with filter()
    start_time = datetime.datetime.now()
    nounListByFilter = list(filter(filterNouns, grammaticalLabelList))
    elapsed_time = datetime.datetime.now() - start_time
    print("nounListByFilter length =", len(nounListByFilter), "elapsed time =", str(elapsed_time)) 

    # filter the noun with a loop
    start_time = datetime.datetime.now()
    nounListByLoop = []
    for label in grammaticalLabelList:
        if(filterNouns(label)):
            nounListByLoop.append(label)
    elapsed_time = datetime.datetime.now() - start_time
    print("nounListByLoop length =", len(nounListByLoop), "elapsed time =", str(elapsed_time)) 


if __name__ == "__main__":
    main()

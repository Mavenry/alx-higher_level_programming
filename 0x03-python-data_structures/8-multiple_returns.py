#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)

    if (len_s == 0):
        tuple = (len_s, None)
    else:
        tuple = (len_s, sentence[0])

    return (tuple)

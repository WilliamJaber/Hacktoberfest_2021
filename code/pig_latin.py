#!/usr/bin/env python3
"""project: Pig Latin Script
created:2021-10-15, @author:seraph★776, email:seraph776@gmail.com, github: https://github.com/seraph776"""


def pig_latin(sentence):
    punctuation = ''
    if sentence[-1] in '?!.':
        punctuation = sentence[-1]
        sentence = sentence.replace(punctuation, '')
    sentence = sentence.lower().split(' ')
 
    for i, word in enumerate(sentence):
        if word[0] not in 'aeiou':
            sentence[i] = f'{word[1:]}{word[0]}ay'            
        else:
            sentence[i] = f'{word}ay'
    
    return ' '.join(sentence).capitalize() + punctuation


def main():
    print(pig_latin('Hello World!'))
    print(pig_latin('What is your name?')) 


if __name__ == '__main__':
    main()

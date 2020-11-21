#!/usr/bin/env python 

import time
import os, sys 
import random
import wikipedia

def wiki():
    global page
    
    random_article = wikipedia.random()
    page = wikipedia.page(random_article)

    contents = page.summary
    sentences = contents.split(". ")
    os.system("clear")
    return sentences 

def random_sentence():
    sentences = wiki()
    sentence = random.choice(sentences)
    return sentence

def touchtyper(sentence_to_type):
    global page
    print(f"[WIKI] {page.title}")
    print("[INPUT] Type the following sentence and confirm by pressing enter!")
    print("[EXIT] You want to exit? Type: exit" )
    print("[SENTENCE] ", sentence_to_type)

    solution = input("Type here:  ") 
    stop = time.time()
    timeelapsed = stop - start
       
    if solution == sentence_to_type:
        print(f"Well done. No mistakes and you finished in \033[1m{round(timeelapsed, 3)}\033[0m seconds.")
    elif solution == "exit":
        return
    else:
        print(f"You made a few mistakes. Try again!")
    
    time.sleep(5)
    program()
    
def program(): 
    global start
    os.system("clear")
    sentence = random_sentence()
    start = time.time()
    touchtyper(sentence)

if __name__ == "__main__":
    program()

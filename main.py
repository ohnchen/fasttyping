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
    print("[LOADING]...")
    try:
        sentences = wiki()
        sentence = random.choice(sentences)
        return sentence
    except:
        print("[ERROR] Something went wrong. Lets try again")
        time.sleep(2)
        program()

def touchtyper(sentence_to_type):
    global page
    print(f"[WIKI] {page.title}")
    print("[INPUT] Type the following sentence and confirm by pressing enter!")
    print("[EXIT] You want to exit? Type: exit" )
    print("[SENTENCE] ", sentence_to_type)

    start = time.time() 
    solution = input("\nType here:  ") 
    stop = time.time()
    timeelapsed = stop - start
       
    wordlist = sentence_to_type.split()
    characters = 0

    string = "".join(wordlist)
    typed_string = "".join(solution.split())

    chars = len(string)
    for index, char in enumerate(string):
        for ind, ch in enumerate(typed_string):
            if ind == index and ch == char:
                characters += 1
    if solution == sentence_to_type:
        print(f"Accuracy: \033[1m{round((characters/chars)*100)}%\033[0m", end=" ")
        print(f"Time: \033[1m{round(timeelapsed, 3)}s\033[0m", end=" ")
        print(f"Speed: \033[1m{len(solution.split())/(int(timeelapsed)/60)} WPM\033[0m.")
        print(f"Well done. No mistakes.")
        input("")
    elif solution == "exit":
        return
    else:
        print(f"Accuracy: \033[1m{round((characters/chars)*100)}%\033[0m", end=" ")
        print(f"Time: \033[1m{round(timeelapsed, 3)}s\033[0m", end=" ")
        print(f"Speed: \033[1m{len(solution.split())/(int(timeelapsed)/60)} WPM\033[0m.")
        print(f"You made a few mistakes. Try again!")
        input("")

    time.sleep(5)
    program()
    
def program(): 
    global start
    os.system("clear")
    sentence = random_sentence()
    touchtyper(sentence)

if __name__ == "__main__":
    program()

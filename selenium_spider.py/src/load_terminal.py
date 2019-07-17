#!/usr/bin/python -tt
# coding: utf-8

import time
import sys

class Load_script:

    def __init__(self):
        
        print()#Pula linha no terminal
        print ("Iniciando script . . .")
        
        animation = ("|/-\\")

        for i in range(20):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print()#Pula linha no terminal
        print("Script iniciado . . .")
    
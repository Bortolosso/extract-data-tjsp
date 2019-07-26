#!/usr/bin/python -tt
# coding: utf-8

from color_terminal import printer

import os

p = printer()

class Remove_Pdf:
        
    def __init__(self):
    
        try: #Checa se tem algum PDF da rodagem passada deixado na pasta.
            file_path = ('/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio.pdf')
            bool = os.path.exists(file_path)
            if bool == True:   
                p.print(msg="\nExcluindo PDF !", color="YELLOW")  
                os.remove(file_path)
                p.print(msg="\nPDF excluido !", color="GREEN")
            else:        
                p.print(msg="\nNão há PDF para ser exluido !\n", color="GREEN")
        except:
            pass
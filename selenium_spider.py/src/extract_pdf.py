#!/usr/bin/python -tt
# coding: utf-8

import pdftotext
import os

class Extract_pdf:
    
    def __init__(self):
        
        pdf_file= ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio.pdf")
            
        with open(pdf_file, "rb") as f:
            pdf = pdftotext.PDF(f)

        for line in pdf:
            page_split = line.split('\n')
            
            line_tree = (page_split[3].strip()) #Credor Principal
            line_four = (page_split[4].strip()) #Número e Ano do EP
            line_six = (page_split[6].strip()) #Número do Processo Originário
            line_seven = (page_split[7].strip()) #Ordem Cronológica/Ano
            print()#Pula linha no terminal
            print(line_tree)
            print(line_four)
            print(line_six)
            print(line_seven)
            print()#Pula linha no terminal
                                    
        os.remove(pdf_file)
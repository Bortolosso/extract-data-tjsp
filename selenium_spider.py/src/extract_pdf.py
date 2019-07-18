#!/usr/bin/python -tt
# coding: utf-8

import pdftotext
import os

class Extract_pdf:
    
    def __init__(self):
        
        pdf_file= ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio.pdf")
            
        with open(pdf_file, "rb") as f:
            pdf = pdftotext.PDF(f)

        for name in pdf:
            page = name.split('\n')
            
            line_tree = page[3].split(':')#Credor Principal
            str_tree = line_tree[1].strip()
            
            line_four = (page[4].split(':'))#Número e Ano do EP
            str_four = line_four[1].strip()
            
            line_six = page[6].split(':')#Número do Processo Originário
            str_six = line_six[1].strip()
            
            line_seven = (page[7].split(':')) #Ordem Cronológica/Ano
            str_seven = line_seven[1].strip()
            
            print()#Pula linha no terminal
            print(str_tree)
            print(str_four)
            print(str_six)
            print(str_seven)
            print()#Pula linha no terminal

        directoryPath = ('/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/format_pdf/' + str_six)
        os.mkdir(directoryPath)
        
        newPath = (directoryPath + '/precatorio.pdf')
        os.rename(pdf_file, newPath)
    
        os.remove(pdf_file)
        
        


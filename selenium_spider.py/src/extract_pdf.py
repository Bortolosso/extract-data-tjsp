#!/usr/bin/python -tt
# coding: utf-8

import pdftotext
import os

class Extract_Pdf:
    
    def __init__(self):
        
        temp_pdf = ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio.pdf")
            
        with open(temp_pdf, "rb") as f:
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
            
            concat_str = (str_tree + '\n' + str_four + '\n' + str_six + '\n' + str_seven)
            
        print('\n', concat_str, '\n')

        try:
            directoryPath = ('/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/format_pdf/' + str_six)
            newPath = (directoryPath + '/precatorio.pdf')
        except:
            pass
        try:
            os.mkdir(directoryPath)
            os.rename(temp_pdf, newPath)
            os.remove(temp_pdf)
        except:
            os.remove(temp_pdf)
    
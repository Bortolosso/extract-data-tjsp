#!/usr/bin/python -tt
# coding: utf-8

import pdftotext
import os
import re

from constants import Constants

CONS = Constants()

class Extract_Pdf:
    
    def __init__(self):
        
        temp_pdf = CONS.VALUE.TEMP_PDF
            
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
        
        if "/" in str_six:
            try:
                new_format = re.sub("/", ".", str_six)
                
                directoryPath_one = (CONS.VALUE.DIRECTORY_PATH + new_format)
                os.mkdir(directoryPath_one)
                
                concat_str_format = (str_tree + '\n' + str_four + '\n' + new_format + '\n' + str_seven)
                        
                print('\n', concat_str_format, '\n')
                
                newPath = (directoryPath_one + '/precatorio.pdf')
                os.rename(temp_pdf, newPath)
                os.remove(temp_pdf)
            except:
                pass
        
        if not "/" in str_six:
            try:
                directoryPath_two = (CONS.VALUE.DIRECTORY_PATH + str_six)
                os.mkdir(directoryPath_two)
                
                concat_str = (str_tree + '\n' + str_four + '\n' + str_six + '\n' + str_seven)
                        
                print('\n', concat_str, '\n')
                
                newPath = (directoryPath_two + '/precatorio.pdf')
                os.rename(temp_pdf, newPath)
                os.remove(temp_pdf)
            except:
                os.remove(temp_pdf)

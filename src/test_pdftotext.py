#!/usr/bin/python -tt
# coding: utf-8

import pdftotext
import time

try:
    pdf_file= ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio (1).pdf")
    
    line_credor = 3 #Credor Principal
    line_num_ep = 4 #Número e Ano do EP
    line_process_origin = 6 #Número do Processo Originário
    line_ordem_crono = 7 #Ordem Cronológica/Ano
    
    for pdfs in range(2, len(pdf_file) + 1):
        # time.sleep(0.1)
        try:
            all_pdfs = ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio (%s).pdf" % (int(pdfs)))

            with open(all_pdfs, "rb") as f:
                pdf = pdftotext.PDF(f)

            for page in pdf:
                string_line_tree = page.split('\n')[line_credor]
                string_line_four = page.split('\n')[line_num_ep]
                string_line_six = page.split('\n')[line_process_origin]
                string_line_seven = page.split('\n')[line_ordem_crono]
                print(string_line_tree)
                print(string_line_four)
                print(string_line_six)
                print(string_line_seven)
                print('________________________________________________________________________________________________________________________________________________________')
                
        except Exception as error:
            print(error)
    
except Exception as error:
    print(error)
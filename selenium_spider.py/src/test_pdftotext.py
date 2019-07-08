#!/usr/bin/python -tt
# coding: utf-8

import pdftotext
import time
import os

class Extract:
    
    def __init__(self):
        
        self.extract_pdf()

    def extract_pdf(self):
        
            pdf_file= ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio (1).pdf")
                
            for pdfs in range(1, len(pdf_file) + 1):
                if pdfs < 5:
                    all_pdfs = ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio (%s).pdf" % (int(pdfs)))
                    
                    try:
                        with open(all_pdfs, "rb") as f:
                            pdf = pdftotext.PDF(f)

                        for page in pdf:
                            string_line_tree = page.split('\n')[3] #Credor Principal
                            string_line_four = page.split('\n')[4] #Número e Ano do EP
                            string_line_six = page.split('\n')[6] #Número do Processo Originário
                            string_line_seven = page.split('\n')[7] #Ordem Cronológica/Ano
                            print(string_line_tree)
                            print(string_line_four)
                            print(string_line_six)
                            print(string_line_seven)
                            print()                            
                    except Exception as error:
                        print(error)
                
                for delete_pdfs in range(1, len(pdf_file) + 1):
                    time.sleep(1)
                    all_pdfs = ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio (%s).pdf" % (int(delete_pdfs)))
                    os.remove(all_pdfs)
try:#FUNC_14
    Extract()
except Exception as error:
    print(error, "FUNC_14")

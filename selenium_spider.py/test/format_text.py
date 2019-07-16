import pdftotext
import os
import re

class extract():

    def __init__(self):
        
        self.extract_pdf()
    
    def extract_pdf(self):
            
            pdf_file= ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio.pdf")
                
            try:
                with open(pdf_file, "rb") as f:
                    pdf = pdftotext.PDF(f)

                for page in pdf:
                    page_split = page.split('\n')
                    string_line_tree = (page_split[3].strip()) #Credor Principal
                    string_line_four = (page_split[4].strip()) #Número e Ano do EP
                    string_line_six = (page_split[6].strip()) #Número do Processo Originário
                    string_line_seven = (page_split[7].strip()) #Ordem Cronológica/Ano
                    print()#Pula linha no terminal
                    print(string_line_tree)
                    print(string_line_four)
                    print(string_line_six)
                    print(string_line_seven)
                    print()#Pula linha no terminal
                    print()#Pula linha no terminal                            
            except Exception as error:
                print(error)
                    
            # os.remove(pdf_file)

try:
    extract()
except:
    pass
#!/usr/bin/python -tt
# coding: utf-8

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import time

try:
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    
    pdf_file= ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio (0).pdf")

    for i in range(2, len(pdf_file) + 1):   
        # time.sleep(0.5)     
        try: 
            text = ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio (%s).pdf" % (str(i)))

            with open(text, 'rb') as pdf_file:
                interpreter = PDFPageInterpreter(manager, device)

                for page in PDFPage.get_pages(pdf_file, check_extractable=True):
                    interpreter.process_page(page)#Se o PDF houver mais de uma página

                text = retstr.getvalue()
                format_str = text

                print(format_str)
                
                pdf_file.close
                
        except Exception as e:
            print(e)
    
except Exception as e:
    print(e)
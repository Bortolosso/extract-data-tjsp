# coding: utf-8

import os

class Remove_pdf(object):
    def remove(self):
        try: #Checa se tem algum PDF da rodagem passada deixado na pasta.
            file_path = ('/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio.pdf')
            bool = os.path.exists(file_path)
            if bool == True:   
                print()#Pula linha no terminal    
                print('Excluindo PDF !')
                os.remove(file_path)
                print('PDF excluido !')
                print()#Pula linha no terminal
            else:        
                print()#Pula linha no terminal
                print("Não há PDF para ser exluido !")
                print()#Pula linha no terminal
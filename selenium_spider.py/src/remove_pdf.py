#!/usr/bin/python -tt
# coding: utf-8

from color_terminal import printer
from constants import Constants

import os

CONS = Constants()
p = printer()

class Remove_Pdf:
        
    def __init__(self):
    
        try: #Checa se tem algum PDF da rodagem passada deixado na pasta.
            file_path = CONS.VALUE.TEMP_PDF
            bool = os.path.exists(file_path)
            if bool == True:   
                p.print(msg="\nExcluindo PDF . . .", color="YELLOW")  
                os.remove(file_path)
                p.print(msg="PDF excluido !", color="GREEN")
            else:        
                p.print(msg="\nNão há PDF para ser exluido !", color="GREEN")
        except:
            pass
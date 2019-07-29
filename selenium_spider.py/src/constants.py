#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from dotted_dict import DottedDict

class Constants:

    def __init__(self):
        
        #LOCAL_PATH
        self.WORKING_DIR = "/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py"
        
        self.VALUE = DottedDict({
            "PATH_PDF": self.WORKING_DIR + "/temp/pdf",
            "PATH_DRIVER": self.WORKING_DIR + "/driver/chromedriver75",
            "PATH_TEMP_CAPTCHA": self.WORKING_DIR + "/img_captcha.jpg",
            "TEMP_PDF": self.WORKING_DIR + "/temp/pdf/arelpesquisainternetprecatorio.pdf",
            "DIRECTORY_PATH": self.WORKING_DIR + "/format_pdf/"
        })

        #WEB
        self.CAC_SCP = DottedDict({
            "SP": {
                "URL": "https://www.tjsp.jus.br/cac/scp/webmenupesquisa.aspx"
            }
        })

        self.WORKING_XPATH = "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]"
        
        self.LOCAL_WEB = DottedDict({
            "XPATH": {
                "BUTTOM_PRECA": self.WORKING_XPATH + "/tr[3]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/span[1]/a[1]",
                "SEND_INPUT": self.WORKING_XPATH + "/tr[2]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/table[1]/tbody[1]/tr[1]/td[3]/input[1]",
                "URL_CAP": self.WORKING_XPATH + "/tr[5]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/img[1]",
                "ERRO_CAPTCHA": self.WORKING_XPATH + "/tr[7]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]",
                "NEW_CAPTCHA": self.WORKING_XPATH + "/tr[5]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/a[1]",
                "ERRO": "//span[contains(text(),'Código digitado incorretamente!')]",
                "ROWS_TABLE": "//table[@id='Grid1ContainerTbl']/tbody[1]/tr[*]",
                "NEXT_TABLE": "//span[@class='PagingButtonsNext']"
            }
        })
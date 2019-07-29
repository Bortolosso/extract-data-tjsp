#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from selenium import webdriver

from constants import Constants

import time

CONS = Constants()

class Driver:
    
    def __init__(self):
        
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_experimental_option('prefs', {
        "download.default_directory": CONS.VALUE.PATH_PDF, #Alterar diretório padrão para downloads
        "download.prompt_for_download": False, #Para baixar automaticamente o arquivo
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True, #Não mostrará PDF diretamente no chrome
        })
        
        self.__driver = webdriver.Chrome(options=options, executable_path = CONS.VALUE.PATH_DRIVER)

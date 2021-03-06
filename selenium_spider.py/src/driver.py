#!/usr/bin/python -tt
# coding: utf-8

from selenium import webdriver

class Driver:
    
    def __init__(self):
        
        local_dir_pdf = "/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf"
        local_dir_driver = "/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/driver/chromedriver75"
        url_tjsp = "https://www.tjsp.jus.br/cac/scp/webmenupesquisa.aspx"
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
        "download.default_directory": local_dir_pdf, #Alterar diretório padrão para downloads
        "download.prompt_for_download": False, #Para baixar automaticamente o arquivo
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True, #Não mostrará PDF diretamente no chrome
        })
        
        self.__driver = webdriver.Chrome( options=options, executable_path = local_dir_driver)
        self.__driver.get(url_tjsp)
         
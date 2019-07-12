#!/usr/bin/python -tt
# coding: utf-8

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

from PIL import Image, ImageOps, ImageEnhance
from time import sleep

import selenium.webdriver.support.ui as ui
import selenium.webdriver as webdriver

import pytesseract as ocr
import numpy as np
import pdftotext
import argparse
import requests
import time 
import sys
import cv2
import re
import os

class Main:
        
    def __init__(self):
                
        print()#Pula linha no terminal
        print ("Iniciando script . . .")
        animation = ("|/-\\")

        for i in range(20):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print()#Pula linha no terminal
        print("Script iniciado . . .")
        
        self.driver()
        
    def driver(self):
        
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
        
        self.remove_pdf()
        
    def remove_pdf(self):

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
        except:
            pass    
            
        self.join_tjsp()
        
    def join_tjsp(self):#Função responsavel para entrar no site do TJSP
        
        exit_click_link = True
        while exit_click_link:
            try:#FUNC_1 // #Clicar botão linkado 'Precatórios'
                buttom_join = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.ID, "TXTITEM1"))
                )
                exit_click_link = False
            except Exception as error:
                print(error, "FUNC_1")
        buttom_join.click()
        
        send_year = input('Digite o ano desejado para coletar os dados: ')
        time.sleep(0.2)
        exit_send_input = True
        while exit_send_input:
            try:#FUNC_2 // #Coloca valor '2015' na box
                xpath_iput = "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/table[1]/tbody[1]/tr[1]/td[3]/input[1]"
                send_input = xpath_iput
                year_id = WebDriverWait(self.__driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, send_input))
                )
                exit_send_input = False
            except Exception as error:
                print(error, "FUNC_2")
        time.sleep(0.5)        
        year_id.send_keys(send_year)
        print()#Pula linha no terminal
                        
        self.down_img()
  
    def down_img(self): #Função responsavel para o download da imagem do captcha
        
        try:#FUNC_3 // #Trás URL do  captcha gerado 
            url_cap = "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[5]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/img[1]"
            div_captcha = self.__driver.find_element_by_xpath(url_cap)
            img_url = div_captcha.get_attribute('src')
            
            print('Iniciando download (CAPTCHA) !')
            r = requests.get(img_url)
            self.__img = '/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/img_captcha/img_captcha.jpg'
            with open(self.__img, 'wb') as out_file:
                out_file.write(r.content)
            print('Download completo (CAPTCHA) !')
        except Exception as error:
            print(error, "FUNC_3")
        
        self.ocr_img()

    def ocr_img(self): #Função responsavel de processamento OCR(retirar string de imagem)
        
        path = (self.__img).strip()
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        filename = '/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/img_captcha.jpg'.format('temp')
        cv2.imwrite(filename, gray)
        self.__text = ocr.image_to_string(gray, lang = 'eng')
        os.remove(filename)        
        
        self.join_table()
    
    def join_table(self):  
        
        exit_send_key = True
        while exit_send_key:#Coloca a string processada pelo OCR no input de captcha
            try:#FUNC_4
                elem = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'cfield'))
            )
                exit_send_key = False
            except Exception as error:
                print(error, "FUNC_4")
            elem.send_keys(self.__text)
            
        exit_click_buttom = True
        while exit_click_buttom:#Clica no botão "pesquisar"
            try:#FUNC_5
                click_buttom = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'BUTTON3'))
                )
                exit_click_buttom = False
            except Exception as error:
                print(error, "FUNC_5")
            click_buttom.click(), time.sleep(0.3)
            
        try:#FUNC_6 // #Mensagem de erro no OCR 
            span_one = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Código digitado incorretamente!')]"))
        )
            span_one_txt = span_one.get_attribute('align')
            print()#Pula linha no terminal
            print("ERRO: INVALID OCR")
            print()#Pula linha no terminal
            
            #Caso der erro no OCR, executa esta função até passar
            while not (span_one_txt == False):
                try:#FUNC_7 // #Limpa Span
                    clear_span = "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[7]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]"
                    click_buttom_clear = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, clear_span))
                    )
                except Exception as error:
                    print(error, "FUNC_7")
                click_buttom_clear.click()
                            
                try:#FUNC_8 // #Clica no botão nova imagem
                    buttom_new = "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[5]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/a[1]"
                    click_buttom_new_img = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, buttom_new))
                    )
                except Exception as error:
                    print(error, "FUNC_8")
                click_buttom_new_img.click()
                
                self.down_img(), time.sleep(0.3)
                self.ocr_img(), time.sleep(0.3)
        except:
            pass 
        
        self.web_scraping()
        
    def web_scraping(self):
        
        url = self.__driver.current_url
        response = requests.get(url)
        
        if response != 200:
            print()#Pula linha no terminal
            print("Inicinado download dos PDF's !")
            time.sleep(0.2)
            try:#FUNC_9
                rows = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//table[@id='Grid1ContainerTbl']/tbody[1]/tr[*]"))
                )
                for i in range(2, len(rows) + 1):
                    time.sleep(0.5)
                    try:#FUNC_10
                        row_xpath = "//table[@id='Grid1ContainerTbl']/tbody[1]/tr[%s]/td[*]/span[1]" % (int(i))
                        table_xpath = "//table[@id='Grid1ContainerTbl']/tbody[1]/tr[%s]/td[*]/input[1]" % (int(i))

                        cols = self.__driver.find_elements_by_xpath(row_xpath)
                        cols_table = self.__driver.find_element_by_xpath(table_xpath)
                        
                        for x in range(len(cols)):
                            time.sleep(0.4)
                            if x == 0:
                                continue 
                            try:#FUNC_11 // #Função responsavel abrir PDF Viewer e fecha-lo, reduzindo o consumo de memoria volatil
                                str_scrap = cols[x].text.encode('utf-8') #Armazena todos os dados varrido na table no site do TJSP          
                                # print(str_scrap)
                                window_before = self.__driver.window_handles[0]
                                cols_table.click()
                                window_after = self.__driver.window_handles[1]
                                self.__driver.switch_to_window(window_after)
                                self.__driver.close()
                                self.__driver.switch_to_window(window_before)
                                self.extract_pdf()
                            except:
                                pass
        
                    except Exception as error:
                        print(error)
                        
                time.sleep(0.5)
                buttom = self.__driver.find_element_by_class_name('PagingButtonsNext')
                buttom.click()    
            except Exception as error:
                print(error, "FUNC_9")
        else:
            self.__driver.quit()
            return Main()
        
        print()#Pula linha no terminal
        print("Fim da extração de dados dos PDF's !")
    def extract_pdf(self):
        
        pdf_file= ("/home/bortolossohurst/Documents/ambv_boot/selenium_spider.py/temp/pdf/arelpesquisainternetprecatorio.pdf")
            
        try:
            with open(pdf_file, "rb") as f:
                pdf = pdftotext.PDF(f)

            for page in pdf:
                page_split = page.split('\n')
                string_line_one = page_split[1]#Entidade Devedora
                string_line_two = page_split[2]#Noda da/o Entidade Devedora
                string_line_tree = page_split[3] #Credor Principal
                string_line_four = page_split[4] #Número e Ano do EP
                string_line_six = page_split[6] #Número do Processo Originário
                string_line_seven = page_split[7] #Ordem Cronológica/Ano
                print()#Pula linha no terminal
                print(string_line_one)
                print(string_line_two)
                print(string_line_tree)
                print(string_line_four)
                print(string_line_six)
                print(string_line_seven)
                print()#Pula linha no terminal
                print()#Pula linha no terminal                            
        except Exception as error:
            print(error)
                
        os.remove(pdf_file)
                    
try:#FUNC_14
    Main()
except Exception as error:
    print(error, "FUNC_14")
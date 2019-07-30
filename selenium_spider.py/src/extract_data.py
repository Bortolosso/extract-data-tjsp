#!/usr/bin/python -tt
# coding: utf-8

from PIL import Image, ImageOps, ImageEnhance

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytesseract as ocr
import cv2
import time 
import requests
import os

from extract_pdf import Extract_Pdf
from remove_pdf import Remove_Pdf 
from color_terminal import printer
from constants import Constants

CONS = Constants()
p = printer()

class Extract_data_tjsp:
        
    def __init__(self):
        
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_experimental_option('prefs', {
        "download.default_directory": CONS.VALUE.PATH_PDF, #Alterar diretório padrão para downloads
        "download.prompt_for_download": False, #Para baixar automaticamente o arquivo
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True #Não mostrará PDF diretamente no chrome
        })
        
        self.__driver = webdriver.Chrome(options=options, executable_path = CONS.VALUE.PATH_DRIVER)
        self.__driver.get(CONS.CAC_SCP.SP.URL)
                
        self.remove_pdf()
        
    def remove_pdf(self): 

        R = Remove_Pdf()
            
        self.join_tjsp()
        
    def join_tjsp(self):#Função responsavel para entrar no site do TJSP
        
        exit_click_link = True
        while exit_click_link:
            try:#FUNC_1 // #Clicar botão linkado 'Precatórios'
                buttom_join = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CONS.LOCAL_WEB.XPATH.BUTTOM_PRECA))
                )
                exit_click_link = False
            except Exception as error:
                p.print(msg="FUNC_1", color="RED")
                print(error)
        buttom_join.click()
        
        # send_year = input('Digite o ano desejado para coleta de dados: ')
        time.sleep(0.2)
        exit_send_input = True
        while exit_send_input:
            try:#FUNC_2 // #Coloca valor '2015' na box
                year_id = WebDriverWait(self.__driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, CONS.LOCAL_WEB.XPATH.SEND_INPUT))
                )
                exit_send_input = False
            except Exception as error:
                p.print(msg="Error FUNC_2", color="RED")
                print(error)
        time.sleep(0.5)        
        year_id.send_keys('2004')
                        
        self.down_img()
  
    def down_img(self): #Função responsavel para o download da imagem do captcha
        
        try:#FUNC_3 // #Trás URL do  captcha gerado 
            div_captcha = self.__driver.find_element_by_xpath(CONS.LOCAL_WEB.XPATH.URL_CAP)
            img_url = div_captcha.get_attribute('src')
            
            p.print(msg="\nIniciando download (CAPTCHA) !", color="YELLOW")
            r = requests.get(img_url)
            with open(CONS.VALUE.PATH_TEMP_CAPTCHA, 'wb') as out_file:
                out_file.write(r.content)
            p.print(msg="Download completo (CAPTCHA) !", color="GREEN")
        except Exception as error:
            p.print(msg="Error FUNC_3", color="RED")
            print(error)
        
        self.ocr_img()

    def ocr_img(self): #Função responsavel de processamento OCR(retirar string de imagem)
        
        path = CONS.VALUE.PATH_TEMP_CAPTCHA.strip()
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        filename = CONS.VALUE.PATH_TEMP_CAPTCHA.format('temp')
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
                p.print(msg="Error FUNC_4", color="RED")
                print(error)
            elem.send_keys(self.__text)
            
        exit_click_buttom = True
        while exit_click_buttom:#Clica no botão "pesquisar"
            try:#FUNC_5
                click_buttom = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'BUTTON3'))
                )
                exit_click_buttom = False
            except Exception as error:
                p.print(msg="Error FUNC_5", color="RED")
                print(error)
            click_buttom.click(), time.sleep(0.3)
            
        try:#FUNC_6 // #Mensagem de erro no OCR 
            span_one = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CONS.LOCAL_WEB.XPATH.ERRO))
        )
            span_one_txt = span_one.get_attribute('align')
            p.print(msg="ERRO: INVALID OCR", color="RED")
                        
            #Caso der erro no OCR, executa esta função até passar
            while not (span_one_txt == False):
                try:#FUNC_7 // #Limpa Span
                    click_buttom_clear = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CONS.LOCAL_WEB.XPATH.ERRO_CAPTCHA))
                    )
                except Exception as error:
                    p.print(msg="FUNC_7", color="RED")
                    print(error)
                    
                click_buttom_clear.click()
                            
                try:#FUNC_8 // #Clica no botão nova imagem
                    click_buttom_new_img = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CONS.LOCAL_WEB.XPATH.NEW_CAPTCHA))
                    )
                except Exception as error:
                    p.print(msg="FUNC_8", color="RED")
                    print(error)
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
            p.print(msg="\nIniciando download dos PDF's !", color="YELLOW")
            try:#FUNC_9
                rows = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, CONS.LOCAL_WEB.XPATH.ROWS_TABLE))
                )
                for i in range(2, len(rows) + 1):
                    time.sleep(0.6)
                    if i < 22:
                        try:#FUNC_10
                            row_xpath = "//table[@id='Grid1ContainerTbl']/tbody[1]/tr[%s]/td[*]/span[1]" % (int(i))
                            table_xpath = "//table[@id='Grid1ContainerTbl']/tbody[1]/tr[%s]/td[*]/input[1]" % (int(i))

                            cols = self.__driver.find_elements_by_xpath(row_xpath)
                            cols_table = self.__driver.find_element_by_xpath(table_xpath)
                            
                            for x in range(len(cols)):
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
                                    E = Extract_Pdf()
                                    time.sleep(0.8)
                                except:
                                    pass
                        except Exception as error:
                            print(error)
                    else:
                        buttom = self.__driver.find_element_by_xpath(CONS.LOCAL_WEB.XPATH.NEXT_TABLE)
                        buttom.click() 
                        self.web_scraping()
            except:
                pass
        else:
            self.__driver.quit()
            return Extract_data_tjsp()
        
Extract_data_tjsp()
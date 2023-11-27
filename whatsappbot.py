from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')

time.sleep(30)
#Definir contatos e grupos e mensagem a ser enviada

contatos = ['']
mensagem = 'mensagem'

#Buscar contatos/grupos

def buscar_contato(contato):
    campo_pesquisa = navegador.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys()

def enviar_mensagem(mensagem):
    campo_mensagem = navegador.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)





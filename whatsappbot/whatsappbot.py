from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time

#navegate to the whatsapp.web
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get('https://web.whatsapp.com/')
time.sleep(20)


#define contacts and groups and messages to be send
contacts = ['DK Administracao']

#search contacts
def search_contact(contact):
    search_field = driver.find_element(
        By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    search_field.click()
    pyautogui.write(contact)
    search_field.send_keys(Keys.ENTER)
    time.sleep(2)

# Function to jump lines
def lines(lines):
    for line in range(lines):
        pyautogui.hotkey('shift','enter')

# Send your message   
def send_message():
    message_field = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message_field.click()
    pyautogui.write('DK ORIENTAL')
    lines(3)
    pyautogui.write('QUARTAS')
    lines(2)
    pyautogui.write('Ayrton 2️ vs 0️ Guigas                     Q1')
    lines(1)
    pyautogui.write('Faraó 1️ vs 2️ Kyaru                       Q2')
    lines(1)
    pyautogui.write('Faraó 1️ vs 2️ Kyaru                       Q2')
    lines(1)
    pyautogui.write('Diego 0 vs 2 Gabriel                     Q3')
    lines(1)
    pyautogui.write('Tunny 2️ vs 0️ Linduarte                   Q4')
    lines(4)
    pyautogui.write('SEMI FINAIS')
    lines(2)
    pyautogui.write('Ayrton 1 vs 2 Galobiel')
    lines(1)
    pyautogui.write('Kyaru 0 vs 2️ Tunny')
    lines(4)
    pyautogui.write('FINAL')
    lines(2)
    pyautogui.write('Galobiel 1️ vs 2️ Tunny')
    lines(3)
    pyautogui.write('TERCEIRO LUGAR')
    lines(2)
    pyautogui.write('Ayrtonaldo 2 vs 1 Kyaru')
    
    message_field.send_keys(Keys.ENTER)
    time.sleep(2)


# Execute commands
for contact in contacts:
    search_contact(contact)
    send_message()
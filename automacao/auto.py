import pyautogui as pa
import time

pa.press('win')
time.sleep(5)
pa.write('chrome')
time.sleep(5)
pa.press('enter')
time.sleep(5)

posicao = pa.locateOnScreen('usuario.png', confidence=0.8)
if posicao:
    pa.click(pa.center(posicao))
    print("Clique realizado!")

time.sleep(3)

posicao = pa.locateOnScreen('add_pagina.png', confidence=0.8)
if posicao:
    pa.click(pa.center(posicao))
    print("Clique realizado!")

time.sleep(5)

posicao = pa.locateOnScreen('img-github.png', confidence=0.8)
if posicao:
    pa.click(pa.center(posicao))
    print("Clique realizado!")

time.sleep(3)

import pyautogui

screenshot = pyautogui.screenshot()

screenshot.save("minha_screenshot.png")






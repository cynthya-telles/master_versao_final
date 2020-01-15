#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import keyboard
from pygame import mixer
import time

# Dependencias são das libs keyboard e da pygame


# In[ ]:


mixer.init()

print('================================'
      '\n TECLE P PARA INICIAR O ÁUDIO'
      '\n TECLE S PARA SAIR'
    '\n ================================')


# In[ ]:


while True:  # Um loop que vai rodar até que se pressione a tecla "q"

    if keyboard.is_pressed('s'):  # Se pressionar a tecla q o programa fecha
        print('SAINDO')
        break  # finishing the loop

    if keyboard.is_pressed('p'):  # Se pressionar a tecla a
        print("TECLA P PRESSIONADA") # Printa algo pra identificar
        mixer.music.load("C:\\Users\\pc\\Desktop\\modelo\\sequencial\\simples.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5) # Isso aqui é só pra debouncing, evitar que cada tecla seja pressionada varias vezes enquanto não soltar a tecla


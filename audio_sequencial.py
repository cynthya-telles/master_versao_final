#!/usr/bin/env python
# coding: utf-8

# In[4]:


from gtts import gTTS
import os


# In[6]:


with open ("C:\\Users\\pc\\Desktop\\modelo\\sequencial\\simples.txt") as arquivo:
    temp = arquivo.read()
tts = gTTS (text = temp, lang = 'pt-br')
tts.save('C:\\Users\\pc\\Desktop\\modelo\\sequencial\\simples.mp3')


# In[ ]:


with open ("C:\\Users\\pc\\Desktop\\modelo\\sequencial\\agrupadas.txt") as arquivo:
    temp = arquivo.read()
tts = gTTS (text = temp, lang = 'pt-br')
tts.save('C:\\Users\\pc\\Desktop\\modelo\\sequencial\\agrupadas.mp3')


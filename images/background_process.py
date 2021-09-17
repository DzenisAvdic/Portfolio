#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from windrose import WindroseAxes
from windrose import plot_windrose
import matplotlib.cm as cm
from PIL import Image
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


starttime = time.time()

def hmz_data_collecting(url):

    html = urlopen(url)

    soup = BeautifulSoup(html, "lxml")

    data = []
    allrows = soup.find_all("tr")
    for row in allrows:
        row_list = row.find_all("td")
        dataRow = []
        for cell in row_list:
            dataRow.append(cell.text)
        data.append(dataRow)
    #titles_1 = data[23]
    #data_1 = data[24:29]
    titles_2 = data[30]
    data_2 = data[31:46]
    #titles_3 = data[45]
    #data_3 = data[46:]

    #df_1 = pd.DataFrame(data_1)
    df_2 = pd.DataFrame(data_2)
    #df_3 = pd.DataFrame(data_3)

    #df_1.columns = titles_1
    df_2.columns = titles_2
    #df_3.columns = titles_3

    #dan = df_3['datum'][1]
    dan = df_2['dan'][1]

    df_2 = df_2.drop(['dan'], axis=1)
    #df_3 = df_3.drop(['datum'], axis=1)

    #df_1.columns = df_2.columns

    #meteo_data = (df_1.append(df_2, ignore_index=True)).append(df_3,ignore_index=True)
    meteo_data = (df_2)
    
    meteo_data.insert(0, 'datum', dan)
    
    sarajevo_meteo_data = meteo_data[meteo_data['stanica'] == 'Sarajevo']

    return sarajevo_meteo_data

while True:

    url = "http://www.fhmzbih.gov.ba/latinica/AKTUELNO/Automatske.php" #open url

    meteo_data = hmz_data_collecting(url)
    meteo_data.to_csv('hmz_sarajevo.csv', mode='a', header=not os.path.exists('hmz_sarajevo.csv'))

    df = pd.read_csv('hmz_sarajevo.csv')
    df.drop_duplicates(keep="first", inplace=True)
    df = df[df['stanica'] == "Sarajevo"]
    wd = np.array(df['smjer vjetra'].copy())
    for i in range(len(wd)):
        if wd[i] == "E":
            wd[i] = float(90)
        elif wd[i] == "ESE":
            wd[i] = float(112.5)
        elif wd[i] == "SE":
            wd[i] = float(135)
        elif wd[i] == "SSE":
            wd[i] = float(157.5)
        elif wd[i] == "S":
            wd[i] = float(180.0)
        elif wd[i] == "SSW":
            wd[i] = float(202.5)
        elif wd[i] == "SW":
            wd[i] = float(225)
        elif wd[i] == "WSW":
            wd[i] = float(247.5)
        elif wd[i] == "W":
            wd[i] = float(270)
        elif wd[i] == "WNW":
            wd[i] = float(292.5)
        elif  wd[i] == "NW":
            wd[i] = float(315)
        elif wd[i] == "NNW":
            wd[i] = float(337.5)
        elif wd[i] == "N":
            wd[i] = float(0)
        elif wd[i] == "NNE":
            wd[i] = float(22.5)
        elif wd[i] == "NE":
            wd[i] = float(45)
        elif wd[i] == "ENE":
            wd[i] = float(67.5)
        else: wd[i] = float(-1)
    ws = np.array(df['brzina vjetra (m/s)'].copy())
    for i in range(len(ws)):
        try:
            ws[i] = float(ws[i])
        except ValueError:
            ws[i] = 0
    d = {'direction': wd, 'speed': ws}
    tabela_vjetar = pd.DataFrame(data=d, dtype=float)

    selection = tabela_vjetar.groupby('direction', as_index=False)['speed'].mean()
    for i in range(tabela_vjetar.shape[0]):
        for j in range(selection.shape[0]):
            if tabela_vjetar['direction'][i] == selection['direction'][j]:
                tabela_vjetar['speed'][i] = selection['speed'][j]

    ws = tabela_vjetar['speed']
    wd = tabela_vjetar['direction']
    ax = WindroseAxes.from_ax()
    ax.bar(wd, ws, cmap=cm.summer, lw=2, nsector=16, blowto=False, normed=True, opening=1, edgecolor='white')
    xlabels = ('E','NE','N','NW','W','SW','S','SE')
    plt.gca().set_xticklabels(xlabels)
    ax.set_legend(loc="best")
    plt.savefig('sarajevo_windrose.png')

    #image = Image.open('sarajevo_windrose.png')
    #image.show()

    time.sleep(900.0 - ((time.time() - starttime) % 900.0))


# In[ ]:

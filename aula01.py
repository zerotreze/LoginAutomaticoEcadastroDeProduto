import pyautogui
print(pyautogui.__version__)
import time

pyautogui.PAUSE = 0.5


pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=830, y=464)
pyautogui.hotkey("ctrl", "a")

pyautogui.write("vitorska10@outlook.com")

pyautogui.press("tab")
pyautogui.write("minha senha")

pyautogui.click(x=673, y=607)

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:

        pyautogui.click(x=464, y=331)

        codigo = str(tabela.loc[linha, "codigo"])
        pyautogui.write(codigo)

        marca = str(tabela.loc[linha, "marca"])
        pyautogui.press("tab")
        pyautogui.write(marca)

        tipo = str(tabela.loc[linha, "tipo"])
        pyautogui.press("tab")
        pyautogui.write(tipo)

        categoria = str(tabela.loc[linha, "categoria"])
        pyautogui.press("tab")
        pyautogui.write(categoria)
        
        preco = str(tabela.loc[linha, "preco_unitario"])
        pyautogui.press("tab")
        pyautogui.write(preco)

        custo = str(tabela.loc[linha, "custo"])
        pyautogui.press("tab")
        pyautogui.write(custo)

        
        pyautogui.press("tab")
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
            pyautogui.write(obs)
        


        pyautogui.press("tab")
        pyautogui.press("enter")

        pyautogui.scroll(5000)

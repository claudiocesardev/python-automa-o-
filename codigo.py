# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
   # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui # para intalar: pip intall pyautogui
import time
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho ( combinação de teclas)

pyautogui.PAUSE = 0.5

# abrir o chrome
pyautogui.press("win")
pyautogui.press("edge")
pyautogui.press("enter")

# entar no link
pyautogui.press("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")  


# esperar o site carregar
time.sleep(4)

# Passo 2: Fazer loginata@gmail.com mar
pyautogui.click(x=666, y=446)
pyautogui.write("claudiocesartata@gmail.com")


pyautogui.press("tab") # passar para o campo de senha
pyautogui.write("maria190598")


pyautogui.press("tab") # pasei pro botão de login
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de dados de produtos
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:

   # passo 4 cadastrar 1 produto
   pyautogui.click(x=665, y=303)

   # prencher os campos
   pyautogui.write(str(tabela.loc[linha, "codigo"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "marca"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "tipo"]))
   pyautogui.press("tab")
   pyautogui.write(str( tabela.loc[linha, "categoria"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "custo"]))
   pyautogui.press("tab")

   obs = tabela.loc[linha, "obs"]
   if not pandas.isna(obs):
      pyautogui.write(str(obs))
   
   # apertar para enviarMO
   pyautogui.press("tab")
   pyautogui.press("entre")

   pyautogui.scroll(50000)

# Passo 5: Repetir o cadastro para todos os produtos

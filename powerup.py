# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer o login no sistema
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar o novo produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos


import pyautogui
import time

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
# Abrir o sistema da empresa
pyautogui.write(link)
pyautogui.press("enter")
# Fazer uma pausa maior para o site carregar
time.sleep(3)

# Fazer o login no sistema
pyautogui.click(x=436, y=425)
pyautogui.write("pythonimpressionador@gmail.com") #Credenciais fictícias utilizadas no ambiente de treinamento do curso
# Colocar a senha
pyautogui.press("tab")
pyautogui.write("python123") #Credenciais fictícias utilizadas no ambiente de treinamento do curso
# Apertar para logar
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")
# fazer uma pausa maior para o site carregar
time.sleep(3)

# Abrir a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    # Cadastrar um produto
    pyautogui.click(x=395, y=312) # clicar no botão de cadastrar produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # Tipo do produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # Preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # Passar para o enviar

    pyautogui.press("enter") # Enviar o produto
    pyautogui.scroll(500) # Scroll para cima para clicar no botão de cadastrar produto novamente

# Repetir o passo 4 até acabar a lista de produtos


# pyautogui.click - clicar 
# pyautogui.write - escrever
# pyautogui.press - pressionar tecla
# pyautogui.hotkey - pressionar combinação de teclas

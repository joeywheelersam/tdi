import subprocess
import os
import sys
import requests
os.system('cls' if os.name == 'nt' else 'clear')

# Menu
print ("0 - Voltar ao Main")
print ("1 - Verificar se um Site está Online ou Offline")
print ("2 - Verificar se um ou mais Sites estão Online ou Offline")
resultado=input("Quer executar qual módulo? ")

# Voltar para o Main
if resultado=="0":
    if __name__ == '__main__':
        cmd = r"python main.py"
        subprocess.call(cmd, shell=True)
# Verifica se um site está Online ou Offline
elif resultado=="1":
    url = input ("Informe a url sem o https: ")
    url_check = "https://www." + url + "/"
    try:
        r = requests.get (url_check)
        print (url_check + " está Online")
    except:
        print (url_check + " está Offline")
    if __name__ == '__main__':
        input ("Deseja continuar?")
        cmd = r"python exercicio3.py"
        subprocess.call(cmd, shell=True)
# Verificar se um ou mais Sites estão Online ou Offline
elif resultado=="2":
    alvo = []
    result = True
    while result == True:
        url = input ("Informe a url sem o https: ")
        alvo.append("https://www." + url + "/")
        print("0 - Para sair")
        print("1 - Digitar outra url")
        teste = input ("O que deseja? ")
        if teste == "0":
            break
        else:
            print ("Repetindo a solicitação")
    for i in alvo:
        try:
            r = requests.get (i)
            print (i + " está Online")
        except:
            print (i + " está Offline")
    if __name__ == '__main__':
        input ("Deseja continuar?")
        cmd = r"python exercicio3.py"
        subprocess.call(cmd, shell=True)
# Valor inválido, retorna para este programa.
else:
    input("Valor inválido!")
    if __name__ == '__main__':
        cmd = r"python exercicio3.py"
        subprocess.call(cmd, shell=True)
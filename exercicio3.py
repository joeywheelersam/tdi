import subprocess
import os
import requests
  # URL da Requests Get = r = requests.get ('https://pypi.org/project/requests/')
  # Captura o código fonte = print (r.text) 
  # Captura o Status Code = print (r.status_code)
os.system('cls' if os.name == 'nt' else 'clear')

url = "uol.com.br/"
lista = ["admin", "login", "css", "sports", "imagem", "mail", "painel"]

# Menu
print ("0 - Voltar ao Main")
print ("1 - Pesquisar Diretório")
print ("2 - Pesquisar Subdomínios")
resultado=input("Quer executar qual pesquisa? ")
# Voltar para o Main
if resultado=="0":
  if __name__ == '__main__':
    cmd = r"python main.py"
    subprocess.call(cmd, shell=True)
# Diretório
elif resultado=="1":
  for i in lista:
    url_check = "https://" + url + i
    r = requests.get (url_check)
    if r.status_code == 200:
      print (url_check, "-", r.status_code)
      print ("")
    else:
      continue
# Subdomínios
elif resultado=="2":
  for i in lista:
    sub_check = f"https://{i}.{url}"
    try:
      r = requests.get (sub_check)
      print (sub_check, "-", r.status_code)
      print ("")
    except:
      print ("Except em"+i)
      continue
# Retorna para o Exercício 3
else:
  print ("Retorna")
  if __name__ == '__main__':
    cmd = r"python exercicio3.py"
    subprocess.call(cmd, shell=True)
if __name__ == '__main__':
  cmd = r"python exercicio3.py"
  subprocess.call(cmd, shell=True)
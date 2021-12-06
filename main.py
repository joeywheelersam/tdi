import subprocess
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')

# Menu
print ("0 - Fechar")
print ("1 - Exercício")
print ("2 - Exercício")
print ("3 - Exercício")
resultado=input("Quer executar qual exercício? ")

# Fecha o programa
if resultado=="0":
  print ("Fechando programa!")
  sys.exit()
# Abre o Exercício 1
elif resultado=="1":
  if __name__ == '__main__':
    cmd = r"python exercicio1.py"
    subprocess.call(cmd, shell=True)
# Abre o Exercício 2
elif resultado=="2":
  if __name__ == '__main__':
    cmd = r"python exercicio2.py"
    subprocess.call(cmd, shell=True)
# Abre o Exercício 3
elif resultado=="3":
  if __name__ == '__main__':
    cmd = r"python exercicio3.py"
    subprocess.call(cmd, shell=True)
# Retorna ao Main
else:
    print ("Retorna")
    if __name__ == '__main__':
      cmd = r"python main.py"
      subprocess.call(cmd, shell=True)
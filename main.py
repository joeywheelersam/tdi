import subprocess
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')

# Menu
print ("0 - Fechar")
print ("1 - Exercício 01")
print ("2 - Exercício 02")
print ("3 - Exercício 03")
print ("4 - Exercício 04")
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
# Abre o Exercício 4
elif resultado=="4":
  if __name__ == '__main__':
    cmd = r"python exercicio4.py"
    subprocess.call(cmd, shell=True)
# Retorna ao Main
else:
    print ("Retorna")
    if __name__ == '__main__':
      cmd = r"python main.py"
      subprocess.call(cmd, shell=True)
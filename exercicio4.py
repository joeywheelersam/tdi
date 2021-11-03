import subprocess
import os
os.system('cls' if os.name == 'nt' else 'clear')

print ("Exercicio 04")

if __name__ == '__main__':
  cmd = r"python main.py"
  subprocess.call(cmd, shell=True)
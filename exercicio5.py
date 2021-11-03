import subprocess
import os
os.system('cls' if os.name == 'nt' else 'clear')

print ("Exercicio 05")

if __name__ == '__main__':
  cmd = r"python main.py"
  subprocess.call(cmd, shell=True)
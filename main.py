import subprocess

resultado=input("Quer executar qual exercicio? ")
if resultado=="1":
  if __name__ == '__main__':
    cmd = r"python exercicio1.py"
    subprocess.call(cmd, shell=True)
elif resultado=="2":
  if __name__ == '__main__':
    cmd = r"python exercicio2.py"
    subprocess.call(cmd, shell=True)
elif resultado=="3":
  if __name__ == '__main__':
    cmd = r"python exercicio3.py"
    subprocess.call(cmd, shell=True)
elif resultado=="4":
  if __name__ == '__main__':
    cmd = r"python exercicio4.py"
    subprocess.call(cmd, shell=True)
elif resultado=="5":
  if __name__ == '__main__':
    cmd = r"python exercicio5.py"
    subprocess.call(cmd, shell=True)
elif resultado=="6":
  if __name__ == '__main__':
    cmd = r"python exercicio6.py"
    subprocess.call(cmd, shell=True)
else:
    print ("Fechar")
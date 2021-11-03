import subprocess
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Declare abaixo uma variável chamada ip e atribua a ela o ip 8.8.8.8 (tipo string).
ip = "8.8.8.8"
print(ip, "\n")

# Declare abaixo uma variável chamada porta e atribua a ela o valor 80 (tipo int)
porta = 80
print(porta, "\n")

# Declare abaixo uma variável chamada alvo_ativo e armazene o valor True (tipo boolean).
alvo_ativo = True
print(alvo_ativo, "\n")

# Atribua à variável portas_principais uma lista com os as portas 21, 22, 23, 80, 443, 3306, , 8080 (todos tipo int).
portas_principais = [21, 22, 23, 80, 443, 3306, 8080]
print(portas_principais, "\n")

# Atribua à variável size_number o tamanho da lista numbers criada no exercício anterior. Dica - use uma função para descobrir o tamanho (len())
quantas_portas = (len(portas_principais))
print(quantas_portas, "\n")

# Use o print para imprimir a soma das variáveis n1 e n2 (não mexa na declaração das variáveis, apenas no print).
n1 = 10
n2 = "40"
print(n1 + int(n2), "\n")

# Na variavel alvo, insira no dicionário as seguintes keys e values:
## ip = 8.8.8.8
## porta = 80
## os = linux
## ativo = true
alvo = {
  'ip': '8.8.8.8',
  'porta': '80',
  'os': 'Windows',
  'ativo': True,
}
print(alvo, "\n")

# Com base na dict alvo (criada acima), imprima o valor da key "ip".
print(alvo["ip"], "\n")

# Com base na dict alvo (criada acima), imprima o valor da key "os".
print(alvo["os"], "\n")

# Com base na dict alvo (criada acima), adicione uma nova key chamada os_version com o value string de "1.0" (usando apenas 1 linha)..
alvo["os_version"] = "1.0"
print(alvo, "\n")

# Com base na dict alvo (criada acima), imprima o valor da key "os_version".
print(alvo["os_version"], "\n")

# Abaixo está criada uma lista com alguns alvos e vamos agora trabalhar um pouco com ela.
alvos = [
    "8.8.8.8", "1.1.1.1", "208.84.244.116", "200.147.3.15", "186.192.90.12",
    "66.254.114.41"
]
print(alvos, "\n")

# Adicione na na última posição da lista o alvo "66.96.146.129". OBS - Não altere a declaração da lista! Adicione o alvo na lista alvos com uma linha de código nova, utilizando uma função.
alvos.append("66.96.146.129")
print(alvos, "\n")

# Ops! O alvo "66.254.114.41" não é mais nosso alvo. Remova ele da lista com com uma função.
alvos.remove("66.254.114.41")
print(alvos, "\n")

# Quantos alvos estão na lista? Consulte a quantidade usando a função "len" dentro do print
print(len(alvos), "\n")

# No print faça uma operação para verificar se a "8.8.8.8" está na lista alvos.
print("8.8.8.8" in alvos, "\n")

# No print imprima a lista alvos em ordem reversa (reverse).
alvos.reverse()
print(alvos)

if __name__ == '__main__':
  cmd = r"python main.py"
  subprocess.call(cmd, shell=True)
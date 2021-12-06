import subprocess
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Declare abaixo uma variável chamada ip e atribua a ela o ip 8.8.8.8 (tipo string).
ip = "8.8.8.8"
print(ip)
print("########")

# Declare abaixo uma variável chamada porta e atribua a ela o valor 80 (tipo int)
porta = 80
print(porta)
print("########")

# Declare abaixo uma variável chamada alvo_ativo e armazene o valor True (tipo boolean).
alvo_ativo = True
print(alvo_ativo)
print("########")

# Atribua à variável portas_principais uma lista com os as portas
# 21, 22, 23, 80, 443, 3306, 8080 (todos tipo int).
portas_principais = [21, 22, 23, 80, 443, 3306, 8080]
print(portas_principais)
print("########")

# Atribua à variável size_number o tamanho da lista numbers criada no exercício anterior.
# Dica - use uma função para descobrir o tamanho (len())
quantas_portas = (len(portas_principais))
print(quantas_portas)
print("########")

# Use o print para imprimir a soma das variáveis n1 e n2.
# Obs.: não mexa na declaração das variáveis, apenas no print.
n1 = 10
n2 = "40"
print(n1 + int(n2))
print("########")

# Na variavel alvo, insira no dicionário as seguintes chaves (key) e valores (value):
# ip = 8.8.8.8 | porta = 80 | os = linux | ativo = true
alvo = {
  'ip': '8.8.8.8',
  'porta': '80',
  'os': 'Windows',
  'ativo': True,
}
print(alvo)
print("########")

# Com base na dict alvo (criada acima), imprima o valor da key "ip".
print(alvo["ip"])
print("########")

# Com base na dict alvo (criada acima), imprima o valor da key "os".
print(alvo["os"])
print("########")

# Com base na dict alvo (criada acima), adicione uma nova key chamada os_version
# com o valor da string de "1.0" (usando apenas 1 linha).
alvo["os_version"] = "1.0"
print(alvo)
print("########")

# Com base na dict alvo (criada acima), imprima o valor da key "os_version".
print(alvo["os_version"])
print("########")

# Abaixo está criada uma lista com alguns alvos e vamos agora trabalhar um pouco com ela.
alvos = ["8.8.8.8", "1.1.1.1", "208.84.244.116", "200.147.3.15", "186.192.90.12", "66.254.114.41"]
print(alvos)
print("########")

# Adicione na última posição da lista o alvo "66.96.146.129".
# Adicione o alvo na lista alvos com uma linha de código nova, utilizando uma função.
# OBS - Não altere a declaração da lista! 
alvos.append("66.96.146.129")
print(alvos)
print("########")

# Ops! O alvo "66.254.114.41" não é mais nosso alvo. Remova ele da lista com com uma função.
alvos.remove("66.254.114.41")
print(alvos)
print("########")

# Quantos alvos estão na lista? Consulte a quantidade usando a função "len" dentro do print
print(len(alvos))
print("########")

# No print faça uma operação para verificar se a "8.8.8.8" está na lista alvos.
print("8.8.8.8" in alvos)
print("########")

# No print imprima a lista alvos em ordem reversa (reverse).
alvos.reverse()
print(alvos)
print("########")

input ("Tecle enter para retornar ao main!")
if __name__ == '__main__':
  cmd = r"python main.py"
  subprocess.call(cmd, shell=True)
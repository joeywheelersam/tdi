import subprocess
import os
os.system('cls' if os.name == 'nt' else 'clear')

def verifica_na_lista(o_ip, a_lista):
    return o_ip in a_lista

def adiciona_alvo(o_ip, a_lista):
  a_lista.append(o_ip)

def remove_alvo(o_ip, a_lista):
  a_lista.remove(o_ip)

def pega_alvo(posicao, a_lista):
  return a_lista[posicao]

def soma_listas(lista_1, lista_2):
  return len(lista_1) + len(lista_2)

def junta_listas(lista_1, lista_2):
  return lista_1 + lista_2

def contar_na_lista(o_valor, a_lista):
  return a_lista.count(o_valor)

#Criando a lista
alvos = ["30.100.218.28", "42.8.149.16","7.55.10.234",  "12.140.8.113","74.237.168.216","191.189.175.243","215.176.131.191","169.38.77.209","161.24.110.149","224.130.150.168","11.25.41.252","247.143.215.238","39.2.161.168"]
print ("Alvos: ", alvos)
print("########")

#Verificar se um alvo está na lista (o return deve ser True or False)
print("Existe o alvo 161.24.110.149?", verifica_na_lista("161.24.110.149", alvos))
print("Existe o alvo 8.8.8.8?", verifica_na_lista("8.8.8.8", alvos))
print("Existe o alvo 42.8.149.16?", verifica_na_lista("42.8.149.16", alvos))
print("########")

#Adicionar um alvo de rastreio na lista
adiciona_alvo("46.72.74.0", alvos)
adiciona_alvo("6.25.174.32", alvos)
adiciona_alvo("58.232.21.212", alvos)

#Remover um código de rastreio da lista
remove_alvo("161.24.110.149", alvos)
remove_alvo("74.237.168.216", alvos)

#Verificar se realmente foi removido da lista
print("Existe o alvo 74.237.168.216?", verifica_na_lista("74.237.168.216", alvos))
print("Existe o alvo 161.24.110.149?", verifica_na_lista("161.24.110.149", alvos))
print("########")

#Consultar/Ler o alvo de uma posição (indice) X na lista
print("O alvo na segunda posição: ", pega_alvo(1, alvos))
print("O alvo na quinta posição:", pega_alvo(4, alvos))
print("########")

#Novos alvos:
novos_alvos = ["63.188.140.165","204.183.148.57","161.236.183.172", "7.55.10.234", "113.143.50.159","67.45.223.250","36.147.26.40", "7.55.10.234"]
print ("Novos Alvos: ", novos_alvos)
print("########")

#Primeiro vou usar a funcão soma_listas e passar as duas listas para ver o tamanho total delas juntas
print("O tamanho das 2 listas de alvos juntas é: ", soma_listas (alvos, novos_alvos))
print("########")

#Agora usando a função junta_listas vou salvar na variavel todos_alvos a concacetanação/junção das listas.
todos_alvos = junta_listas(alvos, novos_alvos)
print ("Todos os Alvos: ", todos_alvos)
print("########")

# Saber quantas vezes o alvo apareceu na lista.
print("O alvo 7.55.10.234 aparece: ", contar_na_lista("7.55.10.234", todos_alvos) , " vezes na lista.")
print("########")

if __name__ == '__main__':
  cmd = r"python main.py"
  subprocess.call(cmd, shell=True)
# Implementar uma primeira estrutura de dados denominada pilha (stack). Utilizá-la para fazer a
#inversão de uma frase (string)

# Global Variables
n = 0

# Input
frase = 'Mariana'
fraseSeparada = list(frase)
novaFrase = list()

# Tests
# print(len(frase))
# print(fraseSeparada)

# Main Program
while n != len(frase):
  n = n + 1
  revm = fraseSeparada.remove(frase[n - 1])
  add = novaFrase.insert(1 - n, frase[n - 1])

# Resultado = ['a', 'n', 'a', 'i', 'r', 'a', 'M']
print(novaFrase)
# Resultado = anairaM
print("".join(novaFrase))
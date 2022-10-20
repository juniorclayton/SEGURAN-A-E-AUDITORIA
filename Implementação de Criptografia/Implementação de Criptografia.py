''' 
Como o algoritmo de criptografia escolhido funciona?

R: O algoritmo abaixo utiliza a função str_xor para realizar uma criptografia simétrica.
A função faz algumas chamadas de função e uma operação de "xor", usando o operador ^ - e concatena o resultado numa string que ele chama de "xored".
A chave do processo é o "xor", feito com o operador "^": isso é uma operação feita bit a bit entre os dois valores: se um dos dois valores for "1" 
e o outro "0" o resultado é "1". Se os dois valores forem iguais, o resultado é "0". Essa operação tem uma propriedade interessante que ela é reversível: 
se eu faço um "xor" de um número X que eu tenho, com um número Y, o resultado é um número diferente "Z". Se eu faço xor de volta de Z com Y, o resultado 
é "X" - por isso que esse algoritmo consegue recuperar a mensagem original - na descriptografia, cada caractere cifrado vai sofre um xor com a mesma letra 
da chave com que foi "xorada" na operação de criptografar.

Justificar porquê da escolha de determinado algoritmo.

R:  Fácil implementação.

Quais serão as vantagens de utilizar o algoritmo no sistema?

R: Aumenta a segurança pois torna as mensagens em forma cifrada ou codificada para que apenas seu emissor e seu receptor sejam capazes de ter acesso ao conteúdo do material criptografado. 

Quais serão as desvantagens que o uso do algoritmo poderá trazer para o sistema?

R: No caso abaixo por se tratar de uma criptografia simétrica sua principal desvantagem é o uso da mesma chave tanto para criptografar como para descriptografar os dados.


'''
import string
import random

chave = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 1024))

print(chave)

texto = 'O programa deverá ler uma mensagem em texto puro, criptografar a mensagem, mostrar a mensagem criptografada, descriptografar a mensagem e por fim, mostrar a mensagem descriptografada.'

print("Texto: " + texto + '\n')

def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1,s2)])

texto_criptografado = str_xor(texto, chave)

print("texto criptografado :"+texto_criptografado + "\n")

texto_descriptografado = str_xor(texto_criptografado, chave)
print("texto descriptografado: " + "\n" + texto_descriptografado + "\n")
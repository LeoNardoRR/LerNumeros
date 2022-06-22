#Faça um programa USANDO MODULARIZAÇÃO para ler diversos números DIFERENTES a serem armazenados em uma lista. 
#Regras para leitura dos números: O programa deverá parar de inserir elementos na lista quando for digitado
#o valor ZERO. Os dados deverão ser armazenados na lista na ordem que forem sendo lidos.
#Caso o usuário digite um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar 
#outro número, não armazenando valores repetidos na lista. Note que cada valor digitado pelo usuário deve ser 
#pesquisado na lista, verificando se ele existe entre os números que já foram fornecidos. Depois de ler os 
#diversos números e armazená-los em uma lista, exiba na tela a lista final de números que foi digitada pelo 
#usuário. Além disso, você deverá calcular qual seria a quantidade total de dígitos que teria esta lista se 
#todos os números da lista fossem impressos um do lado do outro (obs: em caso de números negativos, não 
#considere o sinal como dígito).

#Ler lista
def verificaNaLista(lista, valor): #Verificar os elementos na lista
    if valor in lista: #Se valor estiver na lista
        return True #Retorna verdade
    else: #Senão
        return False #Retorna mentira

#ContaDigitos
def contaDigitos(lista): #Conta os digitos da lista
    qtdDigitos = 0 #Quantidade de dígitos inicias é igual a 0
    
    for elem in lista: #for é uma das estruturas de repetições, na comando atual esta adicionando o elemento na lista N vezes

#Verifica se negativo
        if elem<0: #Se elemento menor que 0
            elem *= -1 #convertendo para deixar negativo 

        qtdDigitos = qtdDigitos + len(str(elem)) #Len é usado para contar a quantidade de dígitos da lista
    
    return qtdDigitos #Retorna a quantidade de dígitos

#Entrada de dados
lista = [] #Lista de armazenamento dos dados 
while(True): #Comando de repetição
    num = int(input('Digite um numero inteiro:')) #Solicitação para digitar um número
    if num == 0: #Se numero igual a 0
        break #para
        
    if verificaNaLista(lista, num): #Verificar valor digitado na lista
        print('Este valor já consta na lista. Tentar novamente.') #Se valor estiver na lista, mostrar "Tentar novamente"
    
    else: #Senão
        lista.append(num)#Armazenar valor na lista

#Concatenando números
qtdDigitos = contaDigitos (lista) #Contando a quantidade de dígitos
print('Lista --> ', lista,' --> Qtd Digitos: ', qtdDigitos) # Mostra a lista e a quantidade de dígitos

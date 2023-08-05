import random
import time

# Textos Introdutórios

intro_math = "Hoje vamos aprender algo muito legal. A MATEMÁTICA!\n" +\
    "Matemática é como um jogo de quebra-cabeça onde usamos números e símbolos para resolver problemas e descobrir coisas novas.\n"+\
    "É como uma linguagem especial que nos ajuda a entender o mundo e resolver desafios divertidos! \n\n" +\
    "Podemos dividir a matemática em quatro operações fundamentais: \n\n" +\
    "1. Adição: É como juntar amigos para contar todos juntos.\n" +\
    "2. Subtração: É quando você tira um pouco de alguma coisa para saber quanto sobra.\n" +\
    "3. Multiplicação: É como fazer uma fila com os mesmos brinquedos e contar quantos temos no total.\n" +\
    "4. Divisão: É quando dividimos uma caixa de bombons igualmente, para ver quantos cada um recebe.\n\n" +\
    "O quê você quer aprender primeiro? \n"

menu = "1 - Adição\n" +\
        "2 - Subtração\n" +\
        "3 - Multiplicação\n" +\
        "4 - Divisão"

intro_adicao = "A adição é uma operação matemática em que você combina números para obter um total.\n" +\
                "Vamos ver alguns exemplos para tornar isso mais claro:\n\n" +\
                "1 - Exemplo com bombons:\n" +\
                "Imagine que você tem 3 bombons de chocolate e 2 bombons de morango. Se você somar esses números, ficará assim:\n" +\
                "3 + 2 = 5\n" +\
                "Então, você tem um total de 5 doces.\n\n" +\
                "Exemplo com frutas:\n" +\
                "Suponha que você tenha 4 maçãs e 3 laranjas. Ao somar esses números, obteremos:\n" +\
                "4 + 3 = 7\n" +\
                "Portanto, você tem um total de 7 frutas.\n\n" +\
                "Exemplo com contagem:\n" +\
                "Digamos que você tenha 6 lápis e seu amigo tenha 5 lápis. Se você adicionar esses números, teremos:\n" +\
                "6 + 5 = 11\n" +\
                "Agora, juntos, vocês têm um total de 11 lápis.\n\n"

intro_subtracao = "A subtração é uma operação matemática em que você retira um número de outro para encontrar a diferença entre eles.\n" +\
                "Vamos ver alguns exemplos para entender melhor:\n\n" +\
                "1 - Exemplo com dinheiro:\n" +\
                "Se você tem R$ 10 e gasta R$ 3, podemos subtrair esses números da seguinte forma:\n" +\
                "10 - 3 = 7.\n" +\
                "Agora você tem R$ 7 reais.\n\n" +\
                "2 - Exemplo com temperatura:\n" +\
                "Suponha que a temperatura atual seja de 25°C e ela diminui em 8°C. Ao subtrair esses números, temos:\n" +\
                "25 - 8 = 17\n" +\
                "Agora a temperatura é de 17°C.\n\n" +\
                "3 - Exemplo com balões:\n" +\
                "Digamos que você tenha 15 balões e 6 deles estouram. Ao subtrair esses números, obtemos:\n" +\
                "15 - 6 = 9\n" +\
                "Agora você tem 9 balões restantes.\n\n"

intro_multiplicacao = "A multiplicação é uma operação matemática em que você combina grupos iguais de números para encontrar o total.\n" +\
                      "Vamos explorar alguns exemplos para entender melhor:\n\n" +\
                      "1 - Exemplo com maçãs:\n" +\
                      "Suponha que você tenha 4 cestas de maçãs, e cada cesta contém 6 maçãs. Para encontrar o total de maçãs, vamos multiplicar esses números:\n" +\
                      "4 x 6 = 24\n" +\
                      "Portanto, você tem um total de 24 maçãs.\n\n" +\
                      "2 - Exemplo com animais:\n" +\
                      "Digamos que em uma fazenda existam 5 galinhas, e cada galinha põe 3 ovos por dia. Ao multiplicar esses números, obtemos:\n" +\
                      "5 x 3 = 15\n" +\
                      "Portanto, as galinhas na fazenda põem um total de 15 ovos por dia.\n\n" +\
                      "3 - Exemplo com dinheiro:\n" +\
                      "Se você tem 8 notas de R$ 10, podemos calcular o valor total multiplicando a quantidade de notas pelo valor de cada nota:\n" +\
                      "8 x 10 = 80\n" +\
                      "Então, você tem um total de R$ 80.\n\n"

intro_divisao = "A divisão é uma operação matemática em que você divide um número em partes iguais ou determina quantas vezes um número cabe em outro.\n" +\
               "Vamos explorar alguns exemplos para entender melhor:\n\n" +\
               "1 - Exemplo com bolos:\n" +\
               "Suponha que você tenha 12 fatias de bolo e deseje dividi-las igualmente entre 4 amigos.\nPara encontrar o número de fatias que cada amigo receberá, vamos realizar a divisão:\n" +\
               "12 ÷ 4 = 3\n" +\
               "Portanto, cada amigo receberá 3 fatias de bolo.\n\n" +\
               "2 - Exemplo com dinheiro:\n" +\
               "Se você tem R$ 100 e deseja dividir igualmente entre 5 pessoas, podemos calcular quanto cada pessoa receberá:\n" +\
               "100 ÷ 5 = 20\n" +\
               "Assim, cada pessoa receberá R$ 20.\n\n" +\
               "3 - Exemplo com contagem:\n" +\
               "Digamos que você tenha 30 lápis e deseje colocá-los em estojos, com 6 lápis em cada estojo.\nPodemos descobrir quantos estojos serão necessários fazendo a divisão:\n" +\
               "30 ÷ 6 = 5\n" +\
               "Serão necessários 5 estojos para acomodar os 30 lápis.\n\n"

respostas_corretas = ["Resposta correta! Parabéns!\n",
                     "Uhuu, você arrasou!\n",
                     "Temos um novo gênio surgindo!\n",
                     "Excelente trabalho!\n",
                     "Incrível, você acertou!\n",
                     "Muito bem, continue assim!\n",
                     "Você é um matemático em formação!\n",
                     "Isso aí, você é demais!\n",
                     "Maravilhoso, acertou em cheio!\n",
                     "Você é um campeão da matemática!\n"]

respostas_incorretas = ["Resposta incorreta. Tente novamente.\n",
                       "Ops, parece que houve um pequeno erro.\n",
                       "Quase lá, mas não é essa a resposta.\n",
                       "Hmm, não é a resposta correta.\n",
                       "Vamos tentar de novo, você consegue!\n",
                       "Não desista, tente mais uma vez!\n",
                       "Não foi dessa vez, mas continue tentando.\n",
                       "Não se preocupe, a próxima pergunta será mais fácil.\n",
                       "Quase, mas não é essa a resposta certa.\n",
                       "Hmm, não é exatamente isso. Vamos continuar tentando!\n"]

#Função para delay
def print_delay(texto):
    delay = 0.07
    for letra in texto:
        print(letra, end='', flush=True)

        if letra == ',' or letra == '.' or letra == ':':
            time.sleep(delay * 4)  # Delay maior para vírgulas e pontos
        else:
            time.sleep(delay)  # Delay padrão para outros caracteres

# Introdução
def iniciar_aplicativo():
    print_delay("Olá, hoje nós vamos conhecer o mundo mágico da Matemática!\n\n")
    print_delay("Como você se chama? \n")
    nome = input()
    print()

    print_delay(f"{nome}, é a primeira vez que você está acessando esse aplicativo?\nDigite 1 para SIM ou 2 para NÃO:\n")
    conhece = int(input())

    print_delay(f"\nOlá, {nome}! Você está pronto para aprender matemática?\n" +\
                "Sim!!! \nEntão vamos começar.\n\n")

    nivel = 1

# Na versão 2.0, vamos comerçar no nivel 1 e subir a cada rodada

    return nome, conhece, nivel

nome_retornado, conhece_retornado, nivel_retornado = iniciar_aplicativo()

# Função menu
if conhece_retornado == 1:
    print_delay(intro_math)
else:
    print_delay("Então você já sabe como funciona.\nO que você quer aprender?\n")

print()
print_delay(menu)
print()

while True:
    print_delay("Escolha um numero de 1 a 4\n")
    opcao = int(input())
    frase_simples = "ótima escolha!\n"
    if opcao == 1:
        operacao = "Adição"
        print_delay(f"\n{operacao}, {frase_simples}")
        print()
        break
    elif opcao == 2:
        operacao = "Subtração"
        print_delay(f"\n{operacao}, {frase_simples}")
        print()
        break
    elif opcao == 3:
        operacao = "Multiplicação"
        print_delay(f"\n{operacao}, {frase_simples}")
        print()
        break
    elif opcao == 4:
        operacao = "Divisão"
        print_delay(f"\n{operacao}, {frase_simples}")
        print()
        break
    else:
        print_delay("Não entendi.\n")
        print()


# Funções de testes / ajustes

qtd_questoes = int(3 * nivel_retornado)
menor_num = int(1)
maior_num = int(10 * nivel_retornado)

# Função de adição

def questoes_adicao():
    print_delay("Vamos aprender Adição!\n")
    print()
    pontos = 0

    for _ in range(qtd_questoes):
        num1 = random.randint(menor_num, maior_num)
        num2 = random.randint(menor_num, maior_num)

        resposta = int(input(f"\nQuanto é {num1} + {num2}? "))

        if resposta == num1 + num2:
            mensagem = random.choice(respostas_corretas)
            print()
            print_delay(f"{num1} + {num2} = {num1 + num2}")
            print()
            print_delay(mensagem)
            print()
            pontos += 1
        else:
            mensagem = random.choice(respostas_incorretas)
            print()
            print_delay(f"{num1} + {num2} = {num1 + num2}")
            print()
            print_delay(mensagem)
            print()
    print()
    pontos = int(pontos/(3 * nivel_retornado)*10)
    print_delay(f"Você fez {pontos} pontos!\n")

# Função de Subtração

def questoes_subtracao():
    print_delay("Vamos aprender Subtração!\n")
    pontos = 0

    for _ in range(qtd_questoes):
        num2 = random.randint(menor_num, maior_num)
        num1 = num2 * random.randint(menor_num, maior_num) # Garante que o resultado será positivo

        resposta = int(input(f"Quanto é {num1} - {num2}? "))

        if resposta == num1 - num2:
            mensagem = random.choice(respostas_corretas)
            print()
            print_delay(f"{num1} - {num2} = {num1 - num2}")
            print()
            print_delay(mensagem)
            print()
            pontos += 1
        else:
            mensagem = random.choice(respostas_incorretas)
            print()
            print_delay(f"{num1} - {num2} = {num1 - num2}")
            print()
            print_delay(mensagem)
            print()
    print()
    pontos = int(pontos/(3 * nivel_retornado)*10)
    print_delay(f"Você fez {pontos} pontos!\n")

# Função de Multimplicação

def questoes_multiplicacao():
    print_delay("Vamos aprender Multiplicação!\n")
    pontos = 0

    for _ in range(qtd_questoes):
        num1 = random.randint(menor_num, maior_num)
        num2 = random.randint(menor_num, maior_num)

        resposta = int(input(f"Quanto é {num1} * {num2}? "))

        if resposta == num1 * num2:
            mensagem = random.choice(respostas_corretas)
            print()
            print_delay(f"{num1} x {num2} = {num1 * num2}")
            print()
            print_delay(mensagem)
            print()
            pontos += 1
        else:
            mensagem = random.choice(respostas_incorretas)
            print()
            print_delay(f"{num1} x {num2} = {num1 * num2}")
            print()
            print_delay(mensagem)
            print()
    print()
    pontos = int(pontos/(3 * nivel_retornado)*10)
    print_delay(f"Você fez {pontos} pontos!\n")

# Função de Divisão

def questoes_divisao():
    print_delay("Vamos aprender Divisão!\n")
    pontos = 0

    for _ in range(qtd_questoes):
        num2 = random.randint(1, 10 * nivel_retornado)
        num1 = num2 * random.randint(1, 5 * nivel_retornado)  # Garante que num1 é múltiplo de num2

        resposta = float(input(f"Quanto é {num1} / {num2}? "))

        if resposta == num1 / num2:
            mensagem = random.choice(respostas_corretas)
            print()
            print_delay(f"{num1} ÷ {num2} = {num1 / num2}")
            print()
            print_delay(mensagem)
            print()
            pontos += 1
        else:
            mensagem = random.choice(respostas_incorretas)
            print()
            print_delay(f"{num1} ÷ {num2} = {num1 / num2}")
            print()
            print_delay(mensagem)
            print()
    print()
    pontos = int(pontos/(3*nivel_retornado)*10)
    print_delay(f"Parabéns, você fez {pontos} pontos!\n")
    print()

# Retornar Introdução se ainda nao utilizou o programa
def retorna_intro(opcao):
    if opcao == 1:
        print_delay(intro_adicao)
    elif opcao == 2:
        print_delay (intro_subtracao)
    elif opcao == 3:
        print_delay (intro_multiplicacao)
    else:
        print_delay (intro_divisao)

# Retornar as questões
def retorna_questao(opcao):
    if opcao == 1:
        return questoes_adicao()
    elif opcao == 2:
        return questoes_subtracao()
    elif opcao == 3:
        return questoes_multiplicacao()
    else:
        return questoes_divisao()

if conhece_retornado == 1:
    retorna_intro(opcao)
    retorna_questao(opcao)
else:
    print_delay("Vamos lá:\n")
    retorna_questao(opcao)


# Menu final
print()
print_delay("\nO que você que aprender agora?\n")
print()
print_delay(menu)
print()
print_delay("5 - Já aprendi o suficiente por hoje")
print()
nivel += 1

opcao = 0
while True:
    print_delay("Escolha um numero de 1 a 5\n")
    opcao = int(input())
    if opcao < 5:
        print()
        funcao_retornada = retorna_questao(opcao)
        funcao_retornada()
        print()
        break
    elif opcao == 5:
        print()
        print_delay(f"Tudo bem, agora descanse bem, pois amanhã tem mais. \n Até a próxima.")
        print()
        break
    else:
        print_delay("\nDesculpe, não entendi.\n")
        print()
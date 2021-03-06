"""Oficina_1_2_EvelynSantos.ipynb



**Oficina Aula 1.2**

Geralmente, os logs são configurados para registrar as mensagens de maior gravidade. Em contrapartida, o modo debug é utilizado somente quando o programa apresenta falhas e é necessário fazer uma auditoria para encontrar o problema.
Evelyn
A seguir, considere o caso descrito para resolver a questão.

Imagine que você é o cientista de dados de uma grande empresa e, como um bom colaborador, decidiu analisar os dados de log de um programa essencial da empresa, com o intuito de avaliar como o programa se comportou durante um ano de funcionamento.

Ao receber o arquivo de log, você percebeu que há dados de pelo menos um ano inteiro e que o arquivo possui 4 Gigabytes de tamanho. Então, você decidiu utilizar expressão regular para avaliar aquele comportamento.

Para isso, você precisou construir um código que:

1) informasse a quantidade de erros ocorridos e 

2) quais os horários em que mais ocorrem erro.

Estas informações serão uteis para lhe ajudar a investigar a causa do problema.

Sabendo que o log possui uma formatação clara (Dia-Mês-Ano Hora:Minuto:Segundo:Milesimos_de_segundos | Nivel_de_gravidade -> Mensagem), utilize a string a seguir como exemplo para fazer o seu código.

2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado
2020-05-11 00:09:52,532 | ERROR -> Erro não esperado
2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema
2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema
2020-05-11 20:46:35,271 | ERROR -> Erro não esperado
2020-05-12 08:14:59,895 | ERROR -> Erro não esperado
2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema
2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema
2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida
2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema
2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema
2020-05-15 08:40:33,776 | ERROR -> Erro não esperado
2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida
"""

log=("""
2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado
2020-05-11 00:09:52,532 | ERROR -> Erro não esperado
2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema
2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema
2020-05-11 20:46:35,271 | ERROR -> Erro não esperado
2020-05-12 08:14:59,895 | ERROR -> Erro não esperado
2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema
2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema
2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida
2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema
2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema
2020-05-15 08:40:33,776 | ERROR -> Erro não esperado
2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida
""")

##import logging
import re

levelError = re.findall(r'\s\d{2}\W\d{2}\W\d{2}\W\d{3}\s\W\s[ERROR]+', log)

eventList = []

findAsctime = [re.findall(r'\d{2}', x)[0] for x in levelError]

for ascTime in findAsctime:
    if ascTime not in [listy[0] for listy in eventList]:
        x = 0
        for i in range(len(findAsctime)):
            if ascTime == findAsctime[i]:
                x += 1
        eventList.append([ascTime, x])
    else: continue

print ("Quantidade de erros ocorridos: ", len(levelError))
print()
print("Análise de ocorrências:\n \n| Horas | Erro |")
for ascTime in eventList:
    print("|",ascTime[0],"h  | ",ascTime[1],"  |")

Algoritimo para representar um número não inteiro como fração.

Meu pseudo código:  


    1. Multiplique o número por 2 e arredonde-o para baixo (numerador)
    2. Agora a fração é numerador(resultado acima)/denominador(2)
    3. while |x-numerador/denominador| > erro:
    4.   if numerador/denominador> número:
    5.       denominador +=1
    6.   else:
    7.       numerador+=1
    8.   retornar numerador e denominador

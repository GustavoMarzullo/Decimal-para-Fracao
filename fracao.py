import matplotlib.pyplot as plt
def fracao(x,erro=1e-4,plotar=False,printar=False):
    '''Retorna o numerador e o demonimador respectivamente.'''
    num_iter=0
    numerador= int(x*2)
    denominador=2
    lista_erro,iteracao=[],[]
    while abs(x-numerador/denominador)>erro:
        num_iter+=1
        lista_erro.append(abs(x-numerador/denominador))
        iteracao.append(num_iter)
        if printar==True:
            print(str(num_iter), str(numerador), str(denominador), str(round(abs(x-numerador/denominador),5)))
        if numerador/denominador > x:
            denominador+=1
        else:
            numerador+=1
    print('Número de iterações = '+str(num_iter))
    if plotar==True:
        plt.plot(iteracao,lista_erro,color='black',linewidth=1)
        plt.xlabel('Iteração')
        plt.ylabel('Erro absoluto')
    return numerador,denominador

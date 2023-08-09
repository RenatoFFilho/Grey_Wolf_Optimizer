# Exemplo de uso do Grey_Wolf_Optimizer
import pandas as pd
import matplotlib.pyplot as plt
from gwo import Grey_Wolf_Optimizer
import fobs

parametros = {
    #'funcao': fobs.sphere_function,
    #'lim': fobs.limit_sphere, 
    'funcao': fobs.simionescu_function,
    'lim': fobs.limit_simionescu, 
    'n_dim': 2,              
    'alpha': 0.01,    
    'beta':0.5,
    'delta': 0.1,                
    'max_iter': 250,
    'pop_size':10 
}

gwo = Grey_Wolf_Optimizer(parametros)

# Chame o método inicializar_populacao()
populacao_inicial = gwo.inicializar_populacao()

melhor_solucao, melhor_fitness = gwo.run()
print("Melhor solução encontrada:", melhor_solucao)
print("Valor de fitness da melhor solução:", melhor_fitness)


plt.figure()
plt.plot(range(1, len(gwo.resultados_fitness) + 1), gwo.resultados_fitness, marker='o')
plt.xlabel('Número de Iterações')
plt.ylabel('Fitness do Melhor Indivíduo')
plt.title('Evolução do Fitness do Melhor Indivíduo')
plt.grid(True)
plt.show()


dados =  pd.DataFrame(gwo.resultados_wolves, columns=['X', 'Y'])
dados['fitness'] = gwo.resultados_fitness
print(dados)               
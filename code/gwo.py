import inspect
import numpy as np
import random

class Grey_Wolf_Optimizer:
    """
    Classe que implementa o Algoritmo de Otimização do Lobo Cinzento (Grey Wolf Optimizer - GWO) para otimização.

    Parâmetros:
        funcao (callable): Função de otimização a ser minimizada.
        n_dim (int): Número de dimensões da função de otimização.
        lim_inf (float): Limite inferior do espaço de busca para cada dimensão.
        lim_sup (float): Limite superior do espaço de busca para cada dimensão.
        max_iter (int): Número máximo de iterações do algoritmo GWO.
        alpha (float): Parâmetro alpha do algoritmo GWO (default: 2.0).
        beta (float): Parâmetro beta do algoritmo GWO (default: 3.0).
        delta (float): Parâmetro delta do algoritmo GWO (default: 0.5).

    Atributos:
        funcao (callable): Função de otimização a ser minimizada.
        n_dim (int): Número de dimensões da função de otimização.
        lim_inf (float): Limite inferior do espaço de busca para cada dimensão.
        lim_sup (float): Limite superior do espaço de busca para cada dimensão.
        max_iter (int): Número máximo de iterações do algoritmo GWO.
        alpha (float): Parâmetro alpha do algoritmo GWO.
        beta (float): Parâmetro beta do algoritmo GWO.
        delta (float): Parâmetro delta do algoritmo GWO.
        wolves (numpy array): Matriz contendo as coordenadas dos lobos na população atual.
        fitness (numpy array): Vetor contendo os valores de fitness dos lobos na população atual.

    Métodos:
        inicializar_populacao():
            Inicializa a população de lobos com coordenadas aleatórias dentro dos limites do espaço de busca.

        calcular_fitness():
            Calcula o valor de fitness para cada lobo na população atual.

        calcular_alpha_beta_delta(iteracao):
            Calcula os valores de alpha, beta e delta para a iteração atual do algoritmo GWO.

        atualizar_posicao(alfa, beta, delta):
            Atualiza a posição de cada lobo na população com base nos valores de alpha, beta e delta.

        otimizar():
            Executa o algoritmo de otimização do Lobo Cinzento (GWO) por várias iterações.

        run():
            Executa o algoritmo completo de otimização e retorna a melhor solução encontrada.

    """

    def __init__(self, parametros):
        self.parametros = parametros
        self.funcao = self.parametros['funcao']
        self.n_dim = self.parametros['n_dim']
        self.lim = self.parametros['lim']
        self.max_iter = self.parametros['max_iter']
        self.wolves = None
        self.fitness = None
        self.num_dim = self.num_entradas(parametros['funcao'])
        self.resultados_wolves = []
        self.resultados_fitness = []

    def num_entradas(self, funcao):
        assinatura = inspect.signature(funcao)
        return len(assinatura.parameters)

    def inicializar_populacao(self):
        """
        Inicializa a população de lobos com coordenadas aleatórias dentro dos limites do espaço de busca.

        Retorna:
            numpy array: Matriz contendo as coordenadas dos lobos na população inicial.
        """
        if self.num_dim == 1:
            wolves = np.random.uniform(self.lim[:, 0], self.lim[:, 1], size=(self.max_iter, self.n_dim))
            return wolves
        
        elif self.num_dim == 2:
            wolves_X = np.random.uniform(self.lim[:, 0], self.lim[:, 1], size=(self.max_iter, self.n_dim))
            wolves_Y = np.random.uniform(self.lim[:, 0], self.lim[:, 1], size=(self.max_iter, self.n_dim))            
            return wolves_X, wolves_Y
            
    def calcular_fitness(self):
        """
        Calcula o valor de fitness para cada lobo na população atual.

        Retorna:
            numpy array: Vetor contendo os valores de fitness dos lobos na população atual.
        """
        if self.num_dim == 1:
            fitness = np.array([self.funcao(wolf) for wolf in self.wolves])
            
            if self.fitness is not None:
                self.resultados_wolves.append(self.wolves[np.argmin(self.fitness)])
                self.resultados_fitness.append(fitness[np.argmin(self.fitness)])
            return fitness

        elif self.num_dim == 2:
            fitness = np.array([self.funcao(wolf[:,0],wolf[:,1]) for wolf in self.wolves])
          
            if self.fitness is not None:
                best_idx_X = np.argmin(self.fitness[0])
                best_idx_Y = np.argmin(self.fitness[1])    
                best_solution = self.wolves[0][best_idx_X] if self.fitness[0][best_idx_X] < self.fitness[1][best_idx_Y] else self.wolves[1][best_idx_Y]
                best_fitness = self.fitness[0][best_idx_X] if self.fitness[0][best_idx_X] < self.fitness[1][best_idx_Y] else self.fitness[1][best_idx_Y]
                self.resultados_wolves.append(best_solution)
                self.resultados_fitness.append(best_fitness)
            
            self.fitness = fitness  # Atribuir o array fitness à variável self.fitness
            return fitness

        else:
            pass  

    def calcular_alpha_beta_delta(self, iteracao):
        """
        Calcula os valores de alpha, beta e delta para a iteração atual do algoritmo GWO.

        Parâmetros:
            iteracao (int): Número da iteração atual.

        Retorna:
            float: Valor de alpha para a iteração atual.
            float: Valor de beta para a iteração atual.
            float: Valor de delta para a iteração atual.
        """
        if self.num_dim ==1:
            fitness_ordenado = np.argsort(self.fitness)
            alfa = fitness_ordenado[0] 
            beta = fitness_ordenado[1] 
            delta = fitness_ordenado[2]
        
        elif self.num_dim == 2:
            fitness_ordenado_X = np.argsort(self.fitness[0])
            fitness_ordenado_Y = np.argsort(self.fitness[1])
            
            alfa = [fitness_ordenado_X[0],fitness_ordenado_Y[0]]
            beta = [fitness_ordenado_X[1],fitness_ordenado_Y[1]]
            delta = [fitness_ordenado_X[2],fitness_ordenado_Y[2]]
        
        
        return alfa, beta, delta

    def atualizar_posicao(self, alfa, beta, delta):
        """
        Atualiza a posição de cada lobo na população com base nos valores de alpha, beta e delta.

        Parâmetros:
            alfa (float): Valor de alpha para a iteração atual.
            beta (float): Valor de beta para a iteração atual.
            delta (float): Valor de delta para a iteração atual.
        """

        if self.num_dim == 1:
            for i in range(self.max_iter):
                for j in range(self.n_dim):
                    alfa_idx = alfa
                    beta_idx = beta
                    delta_idx = delta

                    r1 = random.random()
                    r2 = random.random()

                    a1 = 2.0 - i * ((2.0) / self.max_iter)
                    A1 = 2 * a1 * r1 - a1
                    C1 = 2 * r2

                    D_alpha = abs(C1 * self.wolves[alfa_idx, j] - self.wolves[i, j])

                    X1 = self.wolves[i, j] - A1 * D_alpha

                    r1 = random.random()
                    r2 = random.random()

                    a2 = 2.0
                    A2 = 2 * a2 * r1 - a2
                    C2 = 2 * r2

                    D_beta = abs(C2 * self.wolves[beta_idx, j] - self.wolves[i, j])

                    X2 = self.wolves[i, j] - A2 * D_beta

                    r1 = random.random()
                    r2 = random.random()

                    a3 = random.uniform(0, 1)
                    A3 = 2 * a3 * r1 - a3
                    C3 = 2 * r2

                    D_delta = abs(C3 * self.wolves[delta_idx, j] - self.wolves[i, j])

                    X3 = self.wolves[i, j] - A3 * D_delta

                    self.wolves[i, j] = (X1 + X2 + X3) / 3.0
        
        
        elif self.num_dim == 2:
            for i in range(self.max_iter):
                for j in range(self.n_dim):
                    for k in range(self.num_dim):
                        
                        alfa_idx = alfa
                        beta_idx = beta
                        delta_idx = delta
                        
                        r1 = random.random()
                        r2 = random.random()

                        a1 = 2.0 - i * ((2.0) / self.max_iter)
                        A1 = 2 * a1 * r1 - a1
                        C1 = 2 * r2

                        D_alpha = abs(C1 * self.wolves[k][alfa_idx[k],j] - self.wolves[k][i,j])

                        X1 = self.wolves[k][i,j] - A1 * D_alpha

                        r1 = random.random()
                        r2 = random.random()

                        a2 = 2.0
                        A2 = 2 * a2 * r1 - a2
                        C2 = 2 * r2

                        D_beta = abs(C2 * self.wolves[k][beta_idx[k],j] - self.wolves[k][i,j])

                        X2 = self.wolves[k][i,j] - A2 * D_beta

                        r1 = random.random()
                        r2 = random.random()

                        a3 = random.uniform(0, 1)
                        A3 = 2 * a3 * r1 - a3
                        C3 = 2 * r2

                        D_delta = abs(C3 * self.wolves[k][delta_idx[k],j] - self.wolves[k][i,j])

                        X3 = self.wolves[k][i,j] - A3 * D_delta

                        self.wolves[k][i,j] = (X1 + X2 + X3) / 3.0
        else:pass            
    
        

    def otimizar(self):
        """
        Executa o algoritmo de otimização do Lobo Cinzento (GWO) por várias iterações.
        """
        self.wolves = self.inicializar_populacao()
        self.fitness = self.calcular_fitness()

        for i in range(self.max_iter):
            alfa, beta, delta = self.calcular_alpha_beta_delta(i)
            self.atualizar_posicao(alfa, beta, delta)
            self.fitness = self.calcular_fitness()
        

    def run(self):
        """
        Executa o algoritmo completo de otimização e retorna a melhor solução encontrada.

        Retorna:
            numpy array: Vetor contendo as coordenadas da melhor solução encontrada.
            float: Valor de fitness da melhor solução encontrada.
        """
        self.otimizar()
        if self.num_dim == 1:
            best_idx = np.argmin(self.fitness)
            best_solution = self.wolves[best_idx]
            best_fitness = self.fitness[best_idx]
            

        elif self.num_dim == 2:
            best_idx_X = np.argmin(self.fitness[0])
            best_idx_Y = np.argmin(self.fitness[1])

            best_solution_X = self.wolves[0][best_idx_X]
            best_solution_Y = self.wolves[1][best_idx_Y]
            
            best_solution = best_solution_X if self.fitness[0][best_idx_X] < self.fitness[1][best_idx_Y] else best_solution_Y
            best_fitness = self.fitness[0][best_idx_X] if self.fitness[0][best_idx_X] < self.fitness[1][best_idx_Y] else self.fitness[1][best_idx_Y]
        

        return best_solution, best_fitness

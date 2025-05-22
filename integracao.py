import math
cache_f = {}

def obter_valor_f(funcao, x):
    if x not in cache_f:
        cache_f[x] = funcao(x)
    return cache_f[x]

f1 = lambda x: math.log(1 + x) * math.sin(0.1 * x) / (x * (1 + x)) * math.exp(x)
f2 = lambda x: math.sin(x) * math.exp(x / 10) * math.cos(1 / x)
f3 = lambda x: x**2 + 2
f4 = lambda x: math.log(1 + x) * math.sin(0.1 * x) / (x * (1 + x)) * math.exp(x)
f5 = lambda x: math.exp(2**x) - x**10

a = 3
b = 12

def T_dinamico(funcao, c, d):

    if c > d or c < a or d > b:
        print("Erro: Limites de integração inválidos!")
        return None
    return ((d - c) * (obter_valor_f(funcao, c) + obter_valor_f(funcao, d)) / 2)

# Regra de Simpson Simples
def S_dinamico(funcao, c, d):
    m = (c + d) / 2
    return ((d - c) / 6 * (obter_valor_f(funcao, c) + 4 * obter_valor_f(funcao, m) + obter_valor_f(funcao, d)))

def I_dinamico_simpson(funcao, c, d, nivel_recursao):

    if nivel_recursao == 0:
        return S_dinamico(funcao, c, d)
    else:
        m = (c + d) / 2
        return (I_dinamico_simpson(funcao, c, m, nivel_recursao - 1) +
                I_dinamico_simpson(funcao, m, d, nivel_recursao - 1))

_contador_chamadas_f = 0

def envolver_funcao_para_contagem(funcao_original, x):

    global _contador_chamadas_f
    _contador_chamadas_f += 1
    return funcao_original(x)


if __name__ == "__main__":
    intervalo_c = 3.0
    intervalo_d = 12.0
    niveis_recursao = 3

    print(f"Exercício 9: Abordagem Dinâmica para Integração")
    print(f"Função em uso: f3 = lambda x: x**2+2")
    print(f"Intervalo de integração: [{intervalo_c}, {intervalo_d}]")
    print(f"Níveis de recursão para subdivisão: {niveis_recursao}\n")

    print("A calcular o integral com a abordagem DINÂMICA (com memoização):")
    cache_f.clear()
    _contador_chamadas_f = 0

    f_envolvida_para_contagem = lambda x: envolver_funcao_para_contagem(f3, x)

    resultado_dinamico = I_dinamico_simpson(f_envolvida_para_contagem, intervalo_c, intervalo_d, niveis_recursao)

    print(f"Resultado do Integral (Dinâmico, Simpson): {resultado_dinamico}")
    print(f"Número de chamadas EFETIVAS à função f3 (com memoização): {_contador_chamadas_f}\n")

    print("A calcular o integral SEM a abordagem DINÂMICA (sem memoização):")

    def S_sem_memo(funcao, c, d):
        m = (c + d) / 2
        return ((d - c) / 6 * (funcao(c) + 4 * funcao(m) + funcao(d)))

    def I_sem_memo_simpson(funcao, c, d, nivel_recursao):
        if nivel_recursao == 0:
            return S_sem_memo(funcao, c, d)
        else:
            m = (c + d) / 2
            return (I_sem_memo_simpson(funcao, c, m, nivel_recursao - 1) +
                    I_sem_memo_simpson(funcao, m, d, nivel_recursao - 1))

    _contador_chamadas_f = 0

    resultado_sem_memo = I_sem_memo_simpson(f_envolvida_para_contagem, intervalo_c, intervalo_d, niveis_recursao)

    print(f"Resultado do Integral (Sem Memoização, Simpson): {resultado_sem_memo}")
    print(f"Número de chamadas EFETIVAS à função f3 (SEM memoização): {_contador_chamadas_f}\n")

    print("Análise da Redução de Avaliações")
    print("Para a Regra de Simpson recursiva com 'N' níveis de recursão:")
    print(f"Com memoização, o número de avaliações de f é 2^(N+1) + 1.")
    print(f"Para N={niveis_recursao}, espera-se 2^({niveis_recursao}+1) + 1 = {2**(niveis_recursao+1) + 1} chamadas.")
    print(f"Sem memoização, cada chamada recursiva para S(f,c,d) avalia f(c), f(m) e f(d) *novamente*.")
    print(f"O número de chamadas cresce muito mais rapidamente.")
    print("\nObserve a diferença no 'Número de chamadas EFETIVAS' para ver o benefício da abordagem dinâmica.")
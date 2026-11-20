# Yield: aloca um espaço na memória para a execução de determinada tarefa. Cria o "gerador". Executa passo a passo. O Yield só existe dentro de função. Muito útil em leitura de planilhas.
def counter_function():
    yield 1
    yield 2
    yield 3
contador = counter_function()
# Exibe o 1 do "yield 1"
print(next(contador))
# Exibe o 1 do "yield 2"
print(next(contador))
# Exibe o local da memória do contador
print(contador)

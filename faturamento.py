import json

def calcular_faturamento(dados):
    # Carregar os dados do arquivo JSON
    with open(dados, 'r') as f:
        faturamento = json.load(f)

    # Filtra os dias que tiveram faturamento maior que 0
    faturamento_valido = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

    if not faturamento_valido:
        return "Não houve faturamento no mês."

    # Calcular o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    # Calcular a média de faturamento considerando apenas os dias com valor maior que 0
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    # Contar os dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

    # Retornar os resultados
    return {
        "Menor Faturamento": menor_faturamento,
        "Maior Faturamento": maior_faturamento,
        "Dias Acima da Média": dias_acima_media
    }

# Nome do arquivo JSON com os dados de faturamento
dados = 'dados.json'

# Calcular e exibir os resultados
resultados = calcular_faturamento(dados)
for chave, valor in resultados.items():
    print(f"{chave}: {valor}")
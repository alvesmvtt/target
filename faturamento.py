import json

def calcular_faturamento(dados):

    with open(dados, 'r') as f:
        faturamento = json.load(f)

    faturamento_valido = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

    if not faturamento_valido:
        return "Não houve faturamento no mês."

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

   
    return {
        "O Menor valor de faturamento no mês": menor_faturamento,
        "o Maior valor de  faturamento no mês": maior_faturamento,
        "Dias acima da média no mês": dias_acima_media
    }

dados = 'dados.json'

resultados = calcular_faturamento(dados)
for chave, valor in resultados.items():
    print(f"{chave}: {valor}")
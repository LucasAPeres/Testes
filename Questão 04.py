faturamento = {
    'São Paulo': 67836.43,
    'Rio de Janeiro': 36678.66,
    'Mina Gerais': 29229.88,
    'Espírito Santo': 27165.48,
    'Outros': 19849.53
}

faturamento_empresa = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / faturamento_empresa) * 100
    print("O percentual do estado de "f'{estado}: {percentual:.2f}%')
import pandas as pd
import matplotlib.pyplot as plt
import re

def parse_serial_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            match = re.search(r'AccelX: ([-+]?\d+\.\d+), AccelY: ([-+]?\d+\.\d+), AccelZ: ([-+]?\d+\.\d+) m/s\^2', line)
            if match:
                accel_x = float(match.group(1))
                accel_y = float(match.group(2))
                accel_z = float(match.group(3))
                data.append({'AccelX': accel_x, 'AccelY': accel_y, 'AccelZ': accel_z})
    return pd.DataFrame(data)

# Copie os dados do output no Monitor Serial e cole em um arquivo chamado 'dados_simulados.txt' ou 'dados_simulados.csv'

# Tentar ler como CSV primeiro
try:
    df = pd.read_csv('dados/dados_simulados.csv')
except FileNotFoundError:
    # Se não encontrar CSV, tentar ler como texto do Monitor Serial
    try:
        df = parse_serial_data('dados/dados_simulados.txt')
    except FileNotFoundError:
        print("Erro: Nenhum arquivo de dados simulados encontrado. Certifique-se de ter 'dados_simulados.csv' ou 'dados_simulados.txt' na pasta 'dados/'.")
        exit()

if not df.empty:
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['AccelX'], label='Aceleração X (m/s^2)', color='red')
    plt.plot(df.index, df['AccelY'], label='Aceleração Y (m/s^2)', color='green')
    plt.plot(df.index, df['AccelZ'], label='Aceleração Z (m/s^2)', color='blue')
    plt.xlabel('Amostra')
    plt.ylabel('Aceleração (m/s^2)')
    plt.title('Variação da Aceleração ao Longo do Tempo (Dados Simulados)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('analise/grafico_aceleracao.png')
    plt.show()

    print("Gráfico de aceleração gerado e salvo como 'analise/grafico_aceleracao.png'")
else:
    print("Nenhum dado válido encontrado para gerar o gráfico.")



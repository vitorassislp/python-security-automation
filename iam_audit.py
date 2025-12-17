import pandas as pd
import sys

# Função principal que roda a auditoria
def verificar_acessos():
    print("Iniciando auditoria de usuários...")

    try:
        # Carregando as planilhas (CSVs)
        # O ideal é exportar isso do sistema antes de rodar
        rh_df = pd.read_csv('rh_base.csv')
        sistema_df = pd.read_csv('sist_acessos.csv')
    except FileNotFoundError:
        print("Erro: Não encontrei os arquivos 'rh_base.csv' ou 'sist_acessos.csv'.")
        print("Coloque eles na mesma pasta do script.")
        return

    # Cruzando os dados (Procv / Left Join)
    # Estou usando a coluna 'id_funcionario' para ligar as duas tabelas
    tabela_unificada = pd.merge(sistema_df, rh_df, left_on='id_funcionario', right_on='id', how='left')

    # REGRA DE NEGÓCIO:
    # Se o status no RH for 'Desligado', a pessoa NÃO pode estar nessa lista de acessos.
    acessos_indevidos = tabela_unificada[tabela_unificada['status'] == 'Desligado']

    if not acessos_indevidos.empty:
        print(f"\n[ALERTA] Encontrei {len(acessos_indevidos)} usuários desligados com acesso ativo!")
        
        # Mostra na tela
        print(acessos_indevidos[['id', 'nome', 'login', 'status']])
        
        # Salva em Excel para mandar pro gestor bloquear
        nome_arquivo = 'relatorio_bloqueio.xlsx'
        acessos_indevidos.to_excel(nome_arquivo, index=False)
        print(f"\nRelatório salvo como: {nome_arquivo}")
    else:
        print("\n[OK] Nenhuma irregularidade encontrada. Tudo limpo.")

if __name__ == "__main__":
    verificar_acessos()
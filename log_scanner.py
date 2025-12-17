from collections import Counter

def analisar_logs(arquivo_log):
    print(f"Lendo o arquivo: {arquivo_log} ...")
    
    ips_suspeitos = []
    LIMITE_ERROS = 3  # Se errar a senha mais que 3 vezes, é suspeito

    try:
        with open(arquivo_log, 'r') as arquivo:
            for linha in arquivo:
                # Só me interessa se tiver ERROR e falha de login
                if "ERROR" in linha and "Login failed" in linha:
                    
                    # Quebra a linha em pedaços para achar o IP
                    # Exemplo de linha: "ERROR Login failed user=admin ip=192.168.0.1"
                    pedacos = linha.split()
                    
                    for item in pedacos:
                        if item.startswith("ip="):
                            # Remove o "ip=" e guarda só o número
                            ip_limpo = item.replace("ip=", "")
                            ips_suspeitos.append(ip_limpo)
        
        # Conta quantas vezes cada IP apareceu na lista de erros
        contagem = Counter(ips_suspeitos)
        
        ameaca_detectada = False
        print("\n--- Resultado da Análise ---")
        
        for ip, qtd_erros in contagem.items():
            if qtd_erros > LIMITE_ERROS:
                print(f"[CRÍTICO] Possível ataque (Brute Force): O IP {ip} falhou {qtd_erros} vezes.")
                ameaca_detectada = True
        
        if not ameaca_detectada:
            print("Nenhuma atividade suspeita encontrada.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_log}' não existe.")

if __name__ == "__main__":
    # Testando com um arquivo padrão
    analisar_logs('server.log')
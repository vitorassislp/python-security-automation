import os
import shutil

# Configurações
PASTA_ALVO = "Downloads_Test" # Mude isso para a pasta real que quiser organizar
EXTENSOES = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.csv'],
    'Executaveis': ['.exe', '.msi', '.zip', '.rar']
}

def organizar_pasta():
    # Verifica se a pasta existe antes de começar
    if not os.path.exists(PASTA_ALVO):
        print(f"A pasta '{PASTA_ALVO}' não existe. Crie ela para testar o script.")
        return

    print(f"Organizando arquivos em: {PASTA_ALVO}...")
    
    arquivos = os.listdir(PASTA_ALVO)
    
    for arquivo in arquivos:
        caminho_completo = os.path.join(PASTA_ALVO, arquivo)
        
        # Se for uma pasta, ignora (não mexe em pastas, só arquivos)
        if os.path.isdir(caminho_completo):
            continue

        # Pega a extensão (ex: .pdf)
        _, ext = os.path.splitext(arquivo)
        ext = ext.lower() # Deixa tudo minúsculo pra não dar erro

        movido = False
        
        # Verifica em qual categoria se encaixa
        for nome_pasta, lista_extensoes in EXTENSOES.items():
            if ext in lista_extensoes:
                
                # Cria a pasta de destino se ela não existir (ex: Documentos)
                pasta_destino = os.path.join(PASTA_ALVO, nome_pasta)
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)
                
                # Tenta mover
                try:
                    shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))
                    print(f"Movido: {arquivo} -> {nome_pasta}/")
                    movido = True
                except Exception as e:
                    print(f"Erro ao mover {arquivo}: {e}")
                break
        
    print("Organização concluída!")

if __name__ == "__main__":
    organizar_pasta()
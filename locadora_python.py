import sqlite3
import os

def carregar_sql(arquivo_sql):
    """Carrega e retorna o conteúdo de um arquivo SQL com verificação"""
    # Verifica se o arquivo existe
    if not os.path.exists(arquivo_sql):
        print(f"❌ ERRO: Arquivo '{arquivo_sql}' não encontrado!")
        print("📁 Arquivos na pasta atual:")
        for file in os.listdir('.'):
            if file.endswith('.sql'):
                print(f"   - {file}")
        return None
    
    try:
        with open(arquivo_sql, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"✅ Arquivo '{arquivo_sql}' carregado com sucesso!")
            print(f"📏 Tamanho do script: {len(content)} caracteres")
            return content
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        return None

def criar_banco_dados():
    # Remove arquivo existente
    arquivo_path = 'bd/locadora.db'
    if os.path.exists(arquivo_path):
        os.remove(arquivo_path)
        print("🗑️ Arquivo anterior do banco removido")
    
    # Cria diretório se não existir
    os.makedirs('bd', exist_ok=True)
    
    # Conecta ao banco
    conn = sqlite3.connect(arquivo_path)
    cursor = conn.cursor()
    
    try:
        # Tenta carregar o arquivo SQL - CORRIJA O NOME AQUI!
        script_sql = carregar_sql('locadora_python.sql')  # ← Altere para o nome correto
        
        if script_sql is None:
            print("💡 Dica: Verifique se o arquivo SQL está na mesma pasta")
            return
        
        # Executa o script
        print("🚀 Executando script SQL...")
        cursor.executescript(script_sql)
        conn.commit()
        print("✅ Script SQL executado com sucesso!")
        
        # Testa as consultas
        print("\n🎬 SISTEMA DE LOCADORA CRIADO COM SUCESSO!")
        print("=" * 50)
        
        # Mostra tabelas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cursor.fetchall()
        print("📊 TABELAS CRIADAS:")
        for tabela in tabelas:
            print(f"  - {tabela[0]}")
        
        # Mostra filmes
        print("\n🎭 FILMES CADASTRADOS:")
        cursor.execute("SELECT id_filme, titulo, diretor, quantidade_total FROM Filme;")
        for filme in cursor.fetchall():
            print(f"  {filme[0]}. {filme[1]} - {filme[2]} ({filme[3]} cópias)")
        
        # Mostra atores
        print("\n🌟 ATORES CADASTRADOS:")
        cursor.execute("SELECT id_ator, nome, nacionalidade FROM Ator;")
        for ator in cursor.fetchall():
            print(f"  {ator[0]}. {ator[1]} - {ator[2]}")
        
        conn.close()
        print(f"\n💾 Banco de dados salvo como: {arquivo_path}")
        
    except sqlite3.Error as e:
        print(f"❌ Erro SQLite: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    criar_banco_dados()
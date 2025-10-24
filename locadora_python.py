import sqlite3
import os
#https://sqliteonline.com/
#https://sqliteviewer.app

def criar_banco_dados():
    # Remove arquivo existente
    arquivo_path = 'bd\locadora.db'
    if os.path.exists(r'bd\locadora.db'):
        os.remove(r"bd\locadora.db")
    
    # Conecta ao banco
    conn = sqlite3.connect(r'bd/locadora.db')
    cursor = conn.cursor()
    
    # Script SQL
    script_sql = """
    -- Tabela Ator
    CREATE TABLE Ator (
        id_ator INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento TEXT,
        nacionalidade TEXT
    );

    -- Tabela Filme
    CREATE TABLE Filme (
        id_filme INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        diretor TEXT,
        ano_lancamento INTEGER,
        duracao INTEGER,
        quantidade_total INTEGER DEFAULT 0,
        genero TEXT
    );

    -- Tabela Atuacao
    CREATE TABLE Atuacao (
        id_filme_ator INTEGER PRIMARY KEY AUTOINCREMENT,
        id_filme INTEGER NOT NULL,
        id_ator INTEGER NOT NULL,
        personagem TEXT,
        FOREIGN KEY (id_filme) REFERENCES Filme(id_filme),
        FOREIGN KEY (id_ator) REFERENCES Ator(id_ator)
    );

    -- Inserir dados de exemplo
    INSERT INTO Ator (nome, data_nascimento, nacionalidade) VALUES 
    ('Tom Hanks', '1956-07-09', 'Americano'),
    ('Meryl Streep', '1949-06-22', 'Americana'),
    ('Leonardo DiCaprio', '1974-11-11', 'Americano'),
    ('Robert De Niro', '1943-08-17', 'Americano');

    INSERT INTO Filme (titulo, diretor, ano_lancamento, duracao, quantidade_total, genero) VALUES 
    ('Forrest Gump', 'Robert Zemeckis', 1994, 142, 5, 'Drama'),
    ('O Poderoso Chefão', 'Francis Ford Coppola', 1972, 175, 3, 'Drama'),
    ('Titanic', 'James Cameron', 1997, 195, 4, 'Romance'),
    ('O Irlandês', 'Martin Scorsese', 2019, 209, 2, 'Drama');

    INSERT INTO Atuacao (id_filme, id_ator, personagem) VALUES 
    (1, 1, 'Forrest Gump'),
    (2, 4, 'Vito Corleone'),
    (3, 3, 'Jack Dawson'),
    (4, 1, 'Frank Sheeran'),
    (4, 4, 'Jimmy Hoffa');

    -- Views
    CREATE VIEW vw_filmes_atores AS
    SELECT 
        f.titulo AS filme,
        f.diretor,
        f.ano_lancamento,
        f.genero,
        a.nome AS ator,
        atu.personagem,
        f.quantidade_total
    FROM Filme f
    JOIN Atuacao atu ON f.id_filme = atu.id_filme
    JOIN Ator a ON atu.id_ator = a.id_ator;

    CREATE VIEW vw_filmes_disponiveis AS
    SELECT 
        id_filme,
        titulo,
        diretor,
        ano_lancamento,
        genero,
        quantidade_total
    FROM Filme
    WHERE quantidade_total > 0;
    """
    
    # Executa o script
    cursor.executescript(script_sql)
    conn.commit()
    
    # Testa as consultas
    print("🎬 SISTEMA DE LOCADORA CRIADO COM SUCESSO!")
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
    
    # Mostra elenco
    print("\n🎬 ELENCO DE FILMES:")
    cursor.execute("""
        SELECT f.titulo, a.nome, atu.personagem 
        FROM vw_filmes_atores atu
        JOIN Filme f ON atu.filme = f.titulo
        JOIN Ator a ON atu.ator = a.nome
        LIMIT 5;
    """)
    for elenco in cursor.fetchall():
        print(f"  🎞 {elenco[0]}: {elenco[1]} como '{elenco[2]}'")
    
    conn.close()
    print(f"\n💾 Banco de dados salvo como: locadora.db")
    print("✅ Pronto! Use 'sqlite3 locadora.db' para acessar o banco.")

if __name__ == "__main__":
    criar_banco_dados()
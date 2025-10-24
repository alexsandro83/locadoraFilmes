
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
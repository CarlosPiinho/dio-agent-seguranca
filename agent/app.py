import sqlite3

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    # CORRETO: usa parâmetros (placeholders) em vez de interpolação de strings.
    # Isso impede que entradas adversárias sejam interpretadas como comandos SQL.
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"

    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()    
    conexao.close()

    if resultado:
        return "Acesso Permitido!"
    else:
        return "Acesso Negado."
'''from http.server import SimpleHTTPRequestHandler, HTTPServer

#definindo a porta
port = 8000

#definindo o gerenciador/manipulador de requisições
handler = SimpleHTTPRequestHandler

#criando a instancia do servidor
server = HTTPServer(("localhost", port), handler)

#imprimindo mensagem de ok
print(f"Server runing in http://localhost:{port}")

server.serve_forever()'''

import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json

class MyHandle (SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            f = open(os.path.join(path, 'index.html'), encoding='utf-8')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass
        return super().list_directory(path)
    
    def accont_user(self, login, password):
        loga = "thainara@gmail.com"
        senha = "123456"

        if login == loga and senha == password:
            return "Usuário logado"
        else:
            return "Usuário inexistente"

    def do_GET(self):
        if self.path == "/login":
            try:
                with open(os.path.join(os.getcwd(), "login.html"), encoding='utf-8') as login:
                    content = login.read()

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif self.path == "/cadastro":
            try:
                with open(os.path.join(os.getcwd(), "cadastro.html"), encoding='utf-8') as cadastro:
                    content = cadastro.read()

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif self.path == "/listar_filmes":
            try:
                with open(os.path.join(os.getcwd(), "listar_filmes.html"), encoding='utf-8') as listar_filmes:
                    html = listar_filmes.read()

                linhas = ""
                for filme in filmes:
                    linhas += f"""
                    <tr>
                        <td>{filme['nome']}</td>
                        <td>{filme['atores']}</td>
                        <td>{filme['diretor']}</td>
                        <td>{filme['ano']}</td>
                        <td>{filme['genero']}</td>
                        <td>{filme['produtora']}</td>
                        <td>{filme['sinopse']}</td>
                    </tr>
                    """

                html = html.replace("<!-- LISTA_DE_FILMES -->", linhas)

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode('utf-8'))

            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path == '/sendlogin':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            login = form_data.get('email', [""])[0]
            password = form_data.get('password', [""])[0]

            logou = self.accont_user(login, password)

            print("Data Form: ")
            print("Email: ", form_data.get('email', [""])[0])
            print("Password: ", form_data.get('password', [""])[0])

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(logou. encode('utf-8'))

        elif self.path == '/sendfilme':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            

            nome = form_data.get('nome', [""])[0]
            atores = form_data.get('atores', [""])[0]
            diretor = form_data.get('diretor', [""])[0]
            ano = form_data.get('ano', [""])[0]
            genero = form_data.get('genero', [""])[0]
            produtora = form_data.get('produtora', [""])[0]
            sinopse = form_data.get('sinopse', [""])[0]

            filme = {
                'nome': nome,
                'atores': atores,
                'diretor': diretor,
                'ano': ano,
                'genero': genero,
                'produtora': produtora,
                'sinopse': sinopse
            }

            filmes.append(filme)


            print("\n--- Dados do Filme Recebido ---")
            print("Nome: ", nome)
            print("Atores: ", atores)
            print("Diretor: ", diretor)
            print("Ano: ", ano)
            print("Gênero: ", genero)
            print("Produtora: ", produtora)
            print("Sinopse: ", sinopse)
            print("-------------------------------\n")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("filme adicionado".encode('utf-8'))

        else:
            super(MyHandle, self).do_POST()


filmes = []

def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server running in http://localhost:8000")
    httpd.serve_forever()

main()



#jeito da mary
#aq é a minha lista flmes, no dela o nome é jsum
'''arquivo = "dados.json"

if os.path.exists(arquivo):
    with open(arquivo, encoding="utf-8") as listinha:
        try:
            filmes = json.load(listinha)
        except json.JSONDecoderError:
            filmes = []
    filmes.append(jsum)
else:
    filmes = [jsum]

with open(arquivo, 'w', encoding='utf-8') as lista:
    json.dump(filmes, lista, indent=4, ensure_ascii=False)

self.send_response(200)
self.send_header("Content-type", "application/json")
self.end_headers()
self.wfile.write(str(jsum).encode('utf-8'))'''

"""elif self.path == "/get_listinha":
    arquivo = "dados.json"

    if os.path.exists(arquivo):
        with open (arquivo, encoding='utf-8') as listagem:
            try:
                filmes = json.load(listagem)
            except json.JSONEncoderError:
                filmes = []
    else:
        filmes = []
    
    self.send_response(200)
    self.send_header("content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps{filmes}.encode{"utf-8"})"""
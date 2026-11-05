# IMPORTAÇÕES
from flask import Flask, render_template, request, session, redirect 

app = Flask(__name__)
app.secret_key = "senai"

# DADOS DE ACESSO DO ADMIN
ADM_EMAIL = "gustavo.saturnino@gmail.com"
ADM_SENHA = "seil@#123"

@app.route("/") # "/" PÁGINA INICIAL DO SITE - HOMEPAGE 
def home():
    if "login" not in session: # NAO PODE ABRIR A PAGINA INICIAL SEM FAZER LOGIN
        return redirect("/login") # RETORNA PARA FAZER LOGIN 

    # USUARIO LOGADO
    return render_template("index.html")

# ROTA DE LOGIN 
@app.route("/login", methods=["GET","POST"])
def login():
    if "login" in session: # VÁ DIRETO PARA A PAGINA INICIAL (EX: VÁ PARA O CINEMA)
        return redirect("/")

    if request.method == "GET":
        return render_template("login.html")
    # POST - n precisa do else

    email = request.form.get("email") # PEGANDO O EMAIL QUE ESTAVA NO FORM HTML
    senha = request.form.get("senha") # ESSA INFORMAÇÃO ESTA NO ATRIBUTO NAME 

    if email == ADM_EMAIL and senha == ADM_SENHA:
        session["login"] = True # CRIA A SESSAO LOGIN
        return redirect("/") # REDIRECIONA PARA A ROTA INICIAL
    else:
        return render_template("login.html", msgerro = "E-mail ou senha incorretas"
        "")
    
# ROTA DE LOGOUT
@app.route("/logout")
def logout():
    session.clear() # APAGA A LISTA SESSÃO
    return redirect("/login")

# TRATAMENTO DE ERRO - 404
@app.errorhandler(404)
def not_found(erro):
    return render_template("erro404.html")












if __name__ == "__main__":
    app.run(debug=True, port=5000) # DEBUG NOS AJUDA A ENCONTRAR ERROS, CASO ESTEJA DESLIGADO, ELE MASCARA OS ERROS MAS NÃO SIGNIFICA QUE O SISTEMA FUNCIONE PERFEITAMENTE
    # host='0.0.0.0' habilita IP público 
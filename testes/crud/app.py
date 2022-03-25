from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mysql.connector
import json

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///youtube.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }


def resposta(status, nome, conteudo, mensagem=""):
    corpo = {}
    corpo[nome] = conteudo

    if mensagem:
        corpo["mensagem"] = mensagem

    return Response(json.dumps(corpo), status=status, mimetype="api/json")


# SELECIONAR TODOS (ALL)
@app.route("/usuarios", methods=["GET"])
def todos_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    return resposta(200, 'Usuarios', usuarios_json, "Todos os usuários")


# SELECIONAR UM (FILTER BY)
@app.route("/usuario/<user_id>", methods=["GET"])
def ver_usuario(user_id):
    usuario_objeto = Usuario.query.filter_by(id=user_id).first()
    usuario_json = usuario_objeto.to_json()

    return resposta(200, "Usuario", usuario_json, f'Mostrando usuario {user_id}')


# CADASTRAR USUARIO
@app.route("/usuario", methods=["POST"])
def criar_usuario():
    body = request.get_json()
    try:
        usuario = Usuario(nome=body["nome"], email=body["email"])
        db.session.add(usuario)
        db.session.commit()
        return resposta(201, "Usuario", usuario.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return resposta(400, "usuario", {}, "Erro ao cadastrar")


# ATUALIZAR USUARIO
@app.route("/usuario/<user_id>", methods=["PUT"])
def att_usuario(user_id):
    usuario_objeto = Usuario.query.filter_by(id=user_id).first()
    body = request.get_json()
    try:
        if "nome" in body:
            usuario_objeto.nome = body["nome"]
        if "email" in body:
            usuario_objeto.email = body["email"]
        db.session.add(usuario_objeto)
        db.session.commit()
        return resposta(200, "Usuario", usuario_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return resposta(400, "usuario", {}, "Erro ao atualizar")


# DELETAR USUARIO
@app.route("/usuario/<user_id>", methods=["DELETE"])
def deletar_usuario(user_id):
    usuario = Usuario.query.filter_by(id=user_id).first()
    usuario_json = usuario.to_json()
    try:
        db.session.delete(usuario)
        db.session.commit()
        return resposta(200, 'Usuario', usuario_json, 'Usuario deletado com sucesso')
    except Exception as e:
        print('Erro', e)
        return resposta(400, "usuario", {}, "Erro ao deletar")


if __name__ == "__main__":
    app.run()

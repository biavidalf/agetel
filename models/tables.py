from app import db
from flask_user import UserMixin


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')


class Contato(db.Model):
    __tablename__ = "contatos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    profissao = db.Column(db.String(50))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    image = db.Column(db.String(100))

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario = db.relationship('Usuario', foreign_keys=usuario_id)

    grupo_id = db.Column(db.Integer, db.ForeignKey('grupos.id'))
    grupo = db.relationship('Grupo', foreign_keys=grupo_id)

    def __init__(self, nome, profissao, email, telefone, cidade, image, usuario_id, grupo_id):
        self.nome = nome
        self.profissao = profissao
        self.email = email
        self.telefone = telefone
        self.cidade = cidade
        self.image = image
        self.usuario_id = usuario_id
        self.grupo_id = grupo_id

    def __repr__(self):
        return f'<Contato {self.id}>'


class Grupo(db.Model):
    __tablename__ = "grupos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario = db.relationship('Usuario', foreign_keys=usuario_id)

    def __init__(self, nome, usuario_id):
        self.nome = nome
        self.usuario_id = usuario_id

    def __repr__(self):
        return f'<Grupo {self.id}>'

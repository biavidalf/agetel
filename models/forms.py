from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from app import IMAGES

from wtforms.fields.html5 import SearchField

# from ..widgets import html5 as widgets
# from . import core


class ContatoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    profissao = StringField('profissao', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    telefone = StringField('telefone', validators=[DataRequired()])
    cidade = StringField('cidade', validators=[DataRequired()])
    image = FileField('image', validators=[FileAllowed(IMAGES, 'Apenas imagens')])
    # usuario_id = IntegerField('usuario_id', validators=[DataRequired()])
    grupo = SelectField("Grupo")
# , choices=[('1', 'Familia'), ('2', 'Amigos'), ('3', 'Trabalho')]


class GrupoForm(FlaskForm):
    grupo = SelectField("Grupo")


class BuscarForm(FlaskForm):
    busca = SearchField('busca', validators=[DataRequired()])


class NewGrupo(FlaskForm):
    grupo = StringField('grupo', validators=[DataRequired()])

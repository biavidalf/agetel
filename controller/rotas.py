from app import app, db, photos, IMAGES
from models.tables import Contato, Usuario, Grupo
from models.forms import ContatoForm, GrupoForm, BuscarForm, NewGrupo
from flask import render_template, url_for, flash, redirect
from templates import *
from flask_user import UserManager, UserMixin, login_required, current_user


"""
=================== ROTAS DE HOME, MOSTRAR CONTATOS E FITLROS ====================
"""


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@login_required
def index():
    contatos = Contato.query.filter_by(usuario_id=current_user.id).order_by(Contato.nome)

    form = BuscarForm()
    form_gp = GrupoForm()

    # Pegando a quantidade de grupos do usuario, e se ele nao tiver nenhum, ser igual a um (para ter um Todos no filtro)
    todos = Grupo.query.filter_by(usuario_id=current_user.id).all()
    if todos:
        todos = len(todos) + 100
    else:
        todos = 1

    # Criando uma lista onde a primeira tupla seja 1, Todos. Depois, adicionar os grupos que o usuario tem
    lista = []
    grps = Grupo.query.filter_by(usuario_id=current_user.id).all()
    for row in grps:
        if len(lista) == 0:
            lista.append((todos, 'Todos'))
            lista.append((row.id, row.nome))
        else:
            lista.append((row.id, row.nome))

    # Passando os grupos que o usuario tem para o form
    form_gp.grupo.choices = lista

    # Checando formulario de busca
    if form.validate_on_submit():
        resultado = f"%{form.busca.data}%"
        contatos = Contato.query.filter(Contato.nome.like(resultado), Contato.usuario_id == current_user.id).all()

        # Checando se a busca encontrou algum contato
        if len(contatos) == 0:
            flash('Contato não encontrado', 'error')
        return render_template('index.html', contatos=contatos, form=form, form_gp=form_gp)

    # Checando formulario de filtro
    if form_gp.validate_on_submit():
        grupo_id = form_gp.grupo.data

        # Checando se o filtro selecionado foi 'Todos'
        if str(grupo_id) == str(todos):

            contatos = Contato.query.filter_by(usuario_id=current_user.id).order_by(Contato.nome)
            return render_template('index.html', contatos=contatos, form=form, form_gp=form_gp)

        contatos = Contato.query.filter_by(usuario_id=current_user.id, grupo_id=grupo_id).all()
        return render_template('index.html', contatos=contatos, form=form, form_gp=form_gp)

    return render_template('index.html', contatos=contatos, form=form, form_gp=form_gp)


"""
=================== ROTAS DE GRUPO ===================
"""


@app.route('/grupos', methods=['GET', 'POST'])
@login_required
def grupos():
    grupos = Grupo.query.filter_by(usuario_id=current_user.id)
    form = NewGrupo()

    if form.validate_on_submit():
        nome = form.grupo.data
        new_grupo = Grupo(nome, current_user.id)
        try:
            db.session.add(new_grupo)
            db.session.commit()
        except:
            flash('Grupo já cadastrado')
        return redirect(url_for('grupos'))
    return render_template('grupos.html', grupos=grupos, form=form)


@app.route('/att_grupo/<idg>', methods=['GET', 'POST'])
@login_required
def att_grupo(idg):
    form = NewGrupo()
    grupo_atual = Grupo.query.filter_by(id=idg).first()

    if form.validate_on_submit():
        grupo_atual.nome = form.grupo.data
        db.session.commit()
        return redirect(url_for('grupos'))
    return render_template('att_grupo.html', form=form, grupo=grupo_atual)


@app.route('/deletar_grupo/<idg>')
@login_required
def deletar_grupo(idg):
    grupo = Grupo.query.filter_by(id=idg).first()
    db.session.delete(grupo)
    db.session.commit()
    return redirect(url_for('grupos'))


"""
=================== ROTAS DE CONTATO ===================
"""


@app.route('/ver-contato/<idc>')
@login_required
def ver_contato(idc):
    contato = Contato.query.filter_by(id=idc).first()
    return render_template('individual_contact.html', contato=contato)


@app.route('/deletar_contato/<idc>')
@login_required
def deletar_contato(idc):
    contato = Contato.query.filter_by(id=idc).first()
    db.session.delete(contato)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/novo-contato', methods=['GET', 'POST'])
@login_required
def add_contato():
    form = ContatoForm()
    form.grupo.choices = [(row.id, row.nome) for row in Grupo.query.filter_by(usuario_id=current_user.id)]

    if form.validate_on_submit():
        nome = form.nome.data
        profissao = form.profissao.data
        email = form.email.data
        telefone = form.telefone.data
        cidade = form.cidade.data
        usuario_id = current_user.id
        grupo_id = form.grupo.data

        image = photos.url(photos.save(form.image.data))

        contato = Contato(nome, profissao, email, telefone, cidade, image, usuario_id, grupo_id)

        try:
            db.session.add(contato)
            db.session.commit()
        except:
            flash('Contato ja cadastrado', 'error')
        return redirect(url_for('index'))

    return render_template('addcontato.html', form=form)


@app.route('/att-contato/<idc>', methods=['GET', 'POST'])
@login_required
def att_contato(idc):
    form = ContatoForm()
    contato_atual = Contato.query.filter_by(id=idc).first()
    grp_atual_id = contato_atual.grupo_id
    grupo_atual = Grupo.query.filter_by(id=grp_atual_id).first()
    form.grupo.choices = [(row.id, row.nome) for row in Grupo.query.filter_by(usuario_id=current_user.id)]

    if form.validate_on_submit():
        print('chegou')
        contato_atual.nome = form.nome.data
        contato_atual.profissao = form.profissao.data
        contato_atual.email = form.email.data
        contato_atual.telefone = form.telefone.data
        contato_atual.cidade = form.cidade.data
        contato_atual.usuario_id = current_user.id
        contato_atual.grupo_id = form.grupo.data

        contato_atual.image = photos.url(photos.save(form.image.data))

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editar_contato.html', form=form, contato_atual=contato_atual, grupo_atual=grupo_atual.nome)

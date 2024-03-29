# Projeto Final de Engenharia de Software
###  Agenda de Contatos
####  Equipe: Beatriz Vidal Freire, Evellyn Gisely de Castro, Nilton Luan Guedes Barros e Paulo Victor se Souza Rodrigues

*Table of Contents*

[TOCM]

[TOC]

##### 1) Documentação
######  Projeto
> Nome: Agenda Telefonica Virtual
Versão: 1.57
[Link do Código](https://github.com/biavidalf/biavidalf.github.io)

###### Editores UML usados
> LucidChart e GenMyModel

###### Linguagem
> Python, HTML, CSS e JS

###### Framework
> Flask

###### Database
> SQLite e SQLAlquemy

###### Referencias
>[Flask documentation (Flask-user)](https://flask-user.readthedocs.io/en/latest/quickstart.html)
[Github Flask User](https://github.com/lingthio/Flask-User)
[W3schools](https://www.w3schools.com/css/default.asp)
[Youtube Flask User App Tea Time](https://www.youtube.com/watch?v=baxLKI4-QKE&t=501s)
[SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/)
[Jinja documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/)
[Flask WTForms documentation](https://flask-wtf.readthedocs.io/)
[Stack OverFlow](https://stackoverflow.com/)
[Video sobre diagrama de implementação](https://www.youtube.com/watch?v=P0wXFFsdMzI)
[Video sobre diagrama de componentes](https://www.youtube.com/watch?v=2VUPhYY_YLE&t=605s)
[Video uml diagrams sequence](https://www.youtube.com/watch?v=pCK6prSq8aw)
[Video sobre diagrama de sequencia](https://www.youtube.com/watch?v=UVkj3ed0ZuM&t=374s)
[Video sobre arquitetura mvc](https://www.youtube.com/watch?v=ZW2JLtX4Dag)
[Video padrão mvc](https://www.youtube.com/watch?v=mMDt9g7bMjk)
[Video sobre diagrama de atividade](https://www.youtube.com/watch?v=vReuK7_tYWc&list=PLvSnBLKgRyHWINbSrLEEE6cen3ghoM_LG&index=8)
[Video sobre diagrama de caso de uso](https://www.youtube.com/watch?v=xrcgbMQdM8Y&list=PLvSnBLKgRyHWINbSrLEEE6cen3ghoM_LG&index=7)
[Tutoral diagrama de pacotes](https://www.lucidchart.com/pages/pt/diagrama-de-pacotes-uml/#section_2)
[Tutorial diagrama de estados](https://www.lucidchart.com/pages/uml-state-machine-diagram)

#####  2) Telas do Sistema

###### Tela Login

[![Tela Login](https://www.bing.com/images/blob?bcid=TroU6Dt2V.sCidLRRGHWI66YnLnQ.....74 "Tela Login")](http://https://www.bing.com/images/blob?bcid=TroU6Dt2V.sCidLRRGHWI66YnLnQ.....74 "Tela Login")

######  Tela Registro

[![Tela Registro](https://www.bing.com/images/blob?bcid=TjlztEZq2fsCidLRRGHWI66YnLnQ.....1s "Tela Registro")](http://https://www.bing.com/images/blob?bcid=TjlztEZq2fsCidLRRGHWI66YnLnQ.....1s "Tela Registro")

###### Tela Inicial (contatos)

[![Tela Inicial](https://www.bing.com/images/blob?bcid=ToSizWSgJvsCidLRRGHWI66YnLnQ.....6c "Tela Inicial")](http://https://www.bing.com/images/blob?bcid=ToSizWSgJvsCidLRRGHWI66YnLnQ.....6c "Tela Inicial")

###### Tela Edição de Contato

[![Tela Edição de Contato](https://www.bing.com/images/blob?bcid=Tu.nWrjaQvsCqxcxoNWLuD9SqbotqVTdP0g "Tela Edição de Contato")](http://https://www.bing.com/images/blob?bcid=Tu.nWrjaQvsCqxcxoNWLuD9SqbotqVTdP0g "Tela Edição de Contato")

###### Tela Individual do Contato

[![Tela Individual de um Contato](https://www.bing.com/images/blob?bcid=TkYnAseAz.sCidLRRGHWI66YnLnQ.....yU "Tela Individual de um Contato")](http://https://www.bing.com/images/blob?bcid=TkYnAseAz.sCidLRRGHWI66YnLnQ.....yU "Tela Individual de um Contato")

###### Tela Adição de Contato

[![Tela Adicionar um Contato](https://www.bing.com/images/blob?bcid=Tp7fRf9c0.sCqxcxoNWLuD9SqbotqVTdP6Q "Tela Adicionar um Contato")](http://https://www.bing.com/images/blob?bcid=Tp7fRf9c0.sCqxcxoNWLuD9SqbotqVTdP6Q "Tela Adicionar um Contato")

##### 3) UML:
###### a. Desenvolver os casos de uso do sistema.

[![Casos de Uso do Sistema](https://www.bing.com/images/blob?bcid=TmmJgSzNjPsCidLRRGHWI66YnLnQ.....xs "Casos de Uso do Sistema")](https://www.bing.com/images/blob?bcid=TmmJgSzNjPsCidLRRGHWI66YnLnQ.....xs "Casos de Uso do Sistema")

**_Caso de Uso - Agenda de Telefone_**

###### Caso de Uso: Criar perfil
>Ator: Usuário
1. O usuário acessa o site
2. Cadastro seus dados
3. Se os dados cumprirem os requisitos, cadastro concluído
4. Se os dados não cumprirem os requisitos, cadastro cancelado/não concluído.

######  Caso de Uso: Adicionar contato
>Ator: Usuário
1. O usuário acessa o site
2. Realiza o login
3. Se os dados ok, segue. Se não, permanece até os dados corretos serem adicionados.
4. Insere contato - Se os dados cumprirem os requisitos, cadastro concluído. Se os dados não cumprirem os requisitos, cadastro cancelado/não concluído.

###### Caso de Uso: Remover contato
>Ator: Usuário
1. O usuário acessa o site
2. Realiza o login
3. Se os dados ok, segue. Se não, permanece até os dados corretos serem adicionados.
4. Apagar contato

###### Caso de Uso: Buscar contato
>Ator: Usuário
1. O usuário acessa o site
2. Realiza o login
3. Se os dados ok, segue. Se não, permanece até os dados corretos serem adicionados.
4. Clica em buscar contatos
5. Se o contato existir, exibir dados do contato.
6. Se o contato não existir, encaminhar para opção de Inserir Contato.


###### b. Elaborar diagramas de sequência para os casos de uso mais importantes.

- [x] Busca e Delete de um contato
- [x] Adição de um novo contato
- [x] Registro de Usuário

###### Diagrama de Sequência -  Busca e Delete de um Contato
[![Diagrama de Sequencia - Busca e Delete e um Contato](https://www.bing.com/images/blob?bcid=TlTnfZXSLvsCidLRRGHWI66YnLnQ.....-0 "Diagrama de Sequencia - Busca e Delete e um Contato")](http://https://www.bing.com/images/blob?bcid=TlTnfZXSLvsCidLRRGHWI66YnLnQ.....-0 "Diagrama de Sequencia - Busca e Delete e um Contato")

###### Diagrama de Sequência - Adicionar Novo Contato
[![Diagrama de Sequencia - Adicionar Contato](https://www.bing.com/images/blob?bcid=TjH9iVXG-PsCidLRRGHWI66YnLnQ.....wQ "Diagrama de Sequencia - Adicionar Contato")](http://https://www.bing.com/images/blob?bcid=TjH9iVXG-PsCidLRRGHWI66YnLnQ.....wQ "Diagrama de Sequencia - Adicionar Contato")

###### Diagrama de Sequência - Registro de Usuário
[![Diagrama de Sequencia - Registro de Usuario](https://www.bing.com/images/blob?bcid=TjqUoRfqhfsCidLRRGHWI66YnLnQ.....3w "Diagrama de Sequencia - Registro de Usuario")](http://https://www.bing.com/images/blob?bcid=TjqUoRfqhfsCidLRRGHWI66YnLnQ.....3w "Diagrama de Sequencia - Registro de Usuario")

###### c. Elaborar diagramas de atividade. Elabore, no mínimo, os seguintes diagramas de atividades:
- [x] Listagem de um dado contato
- [x] Mapa de navegação de telas

[![Diagrama de Atividade - Listagem de Contato](https://www.bing.com/images/blob?bcid=Tr5mi5zR.PsCidLRRGHWI66YnLnQ.....yE "Diagrama de Atividade - Listagem de Contato")](http://https://www.bing.com/images/blob?bcid=Tr5mi5zR.PsCidLRRGHWI66YnLnQ.....yE "Diagrama de Atividade - Listagem de Contato")

###### Diagrama de Atividade - Mapa de Navegação de Telas
[![Diagrama de Atividade - Mapa de Navegação de Telas](https://www.bing.com/images/blob?bcid=Tkspth98avsCidLRRGHWI66YnLnQ......s "Diagrama de Atividade - Mapa de Navegação de Telas")](http://https://www.bing.com/images/blob?bcid=Tkspth98avsCidLRRGHWI66YnLnQ......s "Diagrama de Atividade - Mapa de Navegação de Telas")

###### d. Elaborar os diagramas de classe do sistema.

> A seguir se encontra o digrama se classes do nosso sistema, foi a partir dele, e dos outros diagramas, que desenvolvemos o nosso projeto. A classe Usuário e a classe Contato se associam mutualmente, já as classes Grupo e Contato têm uma associação unilateral, pois somente a classe Grupo se associa a classe Contato.

[![Diagrama de Classes Sistema Agenda](https://www.bing.com/images/blob?bcid=ToFDe1x9z.sCidLRRGHWI66YnLnQ.....50 "Diagrama de Classes Sistema Agenda")](http://https://www.bing.com/images/blob?bcid=ToFDe1x9z.sCidLRRGHWI66YnLnQ.....50 "Diagrama de Classes Sistema Agenda")

###### e. Elaborar os diagramas de estado de um objeto Conta (Account)
[![Diagrama de Estado - Objeto Conta](https://www.bing.com/images/blob?bcid=Tr8bDJ0JT.sCqxcxoNWLuD9SqbotqVTdP6Q "Diagrama de Estado - Objeto Conta")](http://https://www.bing.com/images/blob?bcid=Tr8bDJ0JT.sCqxcxoNWLuD9SqbotqVTdP6Q "Diagrama de Estado - Objeto Conta")

###### f. Explicitar a arquitetura escolhida. Use, para tal, diagramas de componentes e/ou de pacotes.

>A arquitetura escolhida foi a MVC, que é muito vista em aplicações para Web, onde a View é geralmente a página HTML, e o código que gera os dados dinâmicos para dentro do HTML é o Controller. E, por fim, o Model é representado pelo conteúdo de fato, geralmente armazenado em bancos de dados ou arquivos XML.
Ainda que existam diferentes formas de MVC, o controle de fluxo geralmente funciona como segue:
1. O usuário interage com a interface de alguma forma (por exemplo, o usuário aperta um botão)
2. O Controller manipula o evento da interface do usuário através de uma rotina pré-escrita.
3. O Controller acessa o Model, possivelmente atualizando-o de uma maneira apropriada, baseado na interação do usuário (por exemplo, atualizando os dados de cadastro do usuário).
4. Algumas implementações de View utilizam o Model para gerar uma interface apropriada (por exemplo, mostrando na tela os dados que foram alterados juntamente com uma confirmação). O View obtém seus próprios dados do Model. O Model não toma conhecimento direto da View.
5. A interface do usuário espera por próximas interações, que iniciarão o ciclo novamente.

[![Diagrama de Pacotes - Arquitetura MVC](https://www.bing.com/images/blob?bcid=TqV4nquOmfsCqxcxoNWLuD9SqbotqVTdP2I "Diagrama de Pacotes - Arquitetura MVC")](http://https://www.bing.com/images/blob?bcid=TqV4nquOmfsCqxcxoNWLuD9SqbotqVTdP2I "Diagrama de Pacotes - Arquitetura MVC")

###### g. Elaborar os diagramas de implantação.

[![Diagrama de Implementação](https://www.bing.com/images/blob?bcid=ToWmVe2YtvsCidLRRGHWI66YnLnQ......w "Diagrama de Implementação")](http://https://www.bing.com/images/blob?bcid=ToWmVe2YtvsCidLRRGHWI66YnLnQ......w "Diagrama de Implementação")
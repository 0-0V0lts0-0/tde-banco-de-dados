from models import session, Autor, Categoria, Cd, Usuario, Emprestimo

def criar_autor(nome):
    novo_autor = Autor(nome=nome)
    session.add(novo_autor)
    session.commit()
    print(f"Autor {nome} adicionado!")

def criar_categoria(nome):
    nova_categoria = Categoria(nome=nome)
    session.add(nova_categoria)
    session.commit()
    print(f"Categoria {nome} adicionada!")

def criar_cd(titulo, genero, autor_id, categoria_id):
    novo_cd = Cd(titulo=titulo, genero=genero, autor_id=autor_id, categoria_id=categoria_id)
    session.add(novo_cd)
    session.commit()
    print(f"CD {titulo} adicionado!")

def criar_usuario(nome, idade):
    novo_usuario = Usuario(nome=nome, idade=idade)
    session.add(novo_usuario)
    session.commit()
    print(f"Usuário {nome} adicionado!")

def criar_emprestimo(cd_id, usuario_id):
    novo_emprestimo = Emprestimo(cd_id=cd_id, usuario_id=usuario_id)
    session.add(novo_emprestimo)
    session.commit()
    print(f"Empréstimo do CD ID {cd_id} para o usuário ID {usuario_id} adicionado!")

def ler_autores():
    autores = session.query(Autor).all()
    for autor in autores:
        print(f"ID: {autor.id}, Nome: {autor.nome}")

def ler_categorias():
    categorias = session.query(Categoria).all()
    for categoria in categorias:
        print(f"ID: {categoria.id}, Nome: {categoria.nome}")

def ler_cds():
    cds = session.query(Cd).all()
    for cd in cds:
        print(f"ID: {cd.id}, Título: {cd.titulo}, Gênero: {cd.genero}, Autor ID: {cd.autor_id}, Categoria ID: {cd.categoria_id}")

def ler_usuarios():
    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Idade: {usuario.idade}")

def ler_emprestimos():
    emprestimos = session.query(Emprestimo).all()
    for emprestimo in emprestimos:
        print(f"ID: {emprestimo.id}, CD ID: {emprestimo.cd_id}, Usuário ID: {emprestimo.usuario_id}")

def atualizar_autor(autor_id, novo_nome=None):
    autor = session.query(Autor).filter_by(id=autor_id).first()
    if autor:
        if novo_nome:
            autor.nome = novo_nome
        session.commit()
        print(f"Autor ID {autor_id} atualizado!")
    else:
        print(f"Autor ID {autor_id} não encontrado!")

def atualizar_categoria(categoria_id, novo_nome=None):
    categoria = session.query(Categoria).filter_by(id=categoria_id).first()
    if categoria:
        if novo_nome:
            categoria.nome = novo_nome
        session.commit()
        print(f"Categoria ID {categoria_id} atualizada!")
    else:
        print(f"Categoria ID {categoria_id} não encontrada!")

def atualizar_cd(cd_id, novo_titulo=None, novo_genero=None, novo_autor_id=None, nova_categoria_id=None):
    cd = session.query(Cd).filter_by(id=cd_id).first()
    if cd:
        if novo_titulo:
            cd.titulo = novo_titulo
        if novo_genero:
            cd.genero = novo_genero
        if novo_autor_id:
            cd.autor_id = novo_autor_id
        if nova_categoria_id:
            cd.categoria_id = nova_categoria_id
        session.commit()
        print(f"CD ID {cd_id} atualizado!")
    else:
        print(f"CD ID {cd_id} não encontrado!")

def atualizar_usuario(usuario_id, novo_nome=None, nova_idade=None):
    usuario = session.query(Usuario).filter_by(id=usuario_id).first()
    if usuario:
        if novo_nome:
            usuario.nome = novo_nome
        if nova_idade is not None:
            usuario.idade = nova_idade
        session.commit()
        print(f"Usuário ID {usuario_id} atualizado!")
    else:
        print(f"Usuário ID {usuario_id} não encontrado!")

def atualizar_emprestimo(emprestimo_id, novo_cd_id=None, novo_usuario_id=None):
    emprestimo = session.query(Emprestimo).filter_by(id=emprestimo_id).first()
    if emprestimo:
        if novo_cd_id:
            emprestimo.cd_id = novo_cd_id
        if novo_usuario_id:
            emprestimo.usuario_id = novo_usuario_id
        session.commit()
        print(f"Empréstimo ID {emprestimo_id} atualizado!")
    else:
        print(f"Empréstimo ID {emprestimo_id} não encontrado!")

def deletar_autor(autor_id):
    autor = session.query(Autor).filter_by(id=autor_id).first()
    if autor:
        session.delete(autor)
        session.commit()
        print(f"Autor ID {autor_id} deletado!")
    else:
        print(f"Autor ID {autor_id} não encontrado!")

def deletar_categoria(categoria_id):
    categoria = session.query(Categoria).filter_by(id=categoria_id).first()
    if categoria:
        session.delete(categoria)
        session.commit()
        print(f"Categoria ID {categoria_id} deletada!")
    else:
        print(f"Categoria ID {categoria_id} não encontrada!")

def deletar_cd(cd_id):
    cd = session.query(Cd).filter_by(id=cd_id).first()
    if cd:
        session.delete(cd)
        session.commit()
        print(f"CD ID {cd_id} deletado!")
    else:
        print(f"CD ID {cd_id} não encontrado!")

def deletar_usuario(usuario_id):
    usuario = session.query(Usuario).filter_by(id=usuario_id).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f"Usuário ID {usuario_id} deletado!")
    else:
        print(f"Usuário ID {usuario_id} não encontrado!")

def deletar_emprestimo(emprestimo_id):
    emprestimo = session.query(Emprestimo).filter_by(id=emprestimo_id).first()
    if emprestimo:
        session.delete(emprestimo)
        session.commit()
        print(f"Empréstimo ID {emprestimo_id} deletado!")
    else:
        print(f"Empréstimo ID {emprestimo_id} não encontrado!")

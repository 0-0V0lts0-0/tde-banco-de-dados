from crud import (
    criar_autor, criar_categoria, criar_livro, criar_usuario, criar_emprestimo,
    ler_autores, ler_categorias, ler_livros, ler_usuarios, ler_emprestimos,
    atualizar_autor, atualizar_categoria, atualizar_livro, atualizar_usuario, atualizar_emprestimo,
    deletar_autor, deletar_categoria, deletar_livro, deletar_usuario, deletar_emprestimo
)

def menu():
    print("\nEscolha uma ação:")
    print("1. Criar Autor")
    print("2. Criar Categoria")
    print("3. Criar Livro")
    print("4. Criar Usuário")
    print("5. Criar Empréstimo")
    print("6. Ler Autores")
    print("7. Ler Categorias")
    print("8. Ler Livros")
    print("9. Ler Usuários")
    print("10. Ler Empréstimos")
    print("11. Atualizar Autor")
    print("12. Atualizar Categoria")
    print("13. Atualizar Livro")
    print("14. Atualizar Usuário")
    print("15. Atualizar Empréstimo")
    print("16. Deletar Autor")
    print("17. Deletar Categoria")
    print("18. Deletar Livro")
    print("19. Deletar Usuário")
    print("20. Deletar Empréstimo")
    print("0. Sair")

def main():
    while True:
        menu()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '0':
            break

        elif escolha == '1':
            nome = input("Digite o nome do autor: ")
            criar_autor(nome)

        elif escolha == '2':
            nome = input("Digite o nome da categoria: ")
            criar_categoria(nome)

        elif escolha == '3':
            titulo = input("Digite o título do livro: ")
            genero = input("Digite o gênero do livro: ")
            autor_id = int(input("Digite o ID do autor: "))
            categoria_id = int(input("Digite o ID da categoria: "))
            criar_livro(titulo, genero, autor_id, categoria_id)

        elif escolha == '4':
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))
            criar_usuario(nome, idade)

        elif escolha == '5':
            livro_id = int(input("Digite o ID do livro: "))
            usuario_id = int(input("Digite o ID do usuário: "))
            criar_emprestimo(livro_id, usuario_id)

        elif escolha == '6':
            ler_autores()

        elif escolha == '7':
            ler_categorias()

        elif escolha == '8':
            ler_livros()

        elif escolha == '9':
            ler_usuarios()

        elif escolha == '10':
            ler_emprestimos()

        elif escolha == '11':
            autor_id = int(input("Digite o ID do autor a ser atualizado: "))
            novo_nome = input("Digite o novo nome do autor: ")
            atualizar_autor(autor_id, novo_nome)

        elif escolha == '12':
            categoria_id = int(input("Digite o ID da categoria a ser atualizada: "))
            novo_nome = input("Digite o novo nome da categoria: ")
            atualizar_categoria(categoria_id, novo_nome)

        elif escolha == '13':
            livro_id = int(input("Digite o ID do livro a ser atualizado: "))
            novo_titulo = input("Digite o novo título do livro: ")
            novo_genero = input("Digite o novo gênero do livro: ")
            novo_autor_id = int(input("Digite o novo ID do autor (ou deixe em branco): ") or 0)
            nova_categoria_id = int(input("Digite o novo ID da categoria (ou deixe em branco): ") or 0)
            atualizar_livro(livro_id, novo_titulo, novo_genero, novo_autor_id or None, nova_categoria_id or None)

        elif escolha == '14':
            usuario_id = int(input("Digite o ID do usuário a ser atualizado: "))
            novo_nome = input("Digite o novo nome do usuário: ")
            nova_idade = int(input("Digite a nova idade do usuário: "))
            atualizar_usuario(usuario_id, novo_nome, nova_idade)

        elif escolha == '15':
            emprestimo_id = int(input("Digite o ID do empréstimo a ser atualizado: "))
            novo_livro_id = int(input("Digite o novo ID do livro (ou deixe em branco): ") or 0)
            novo_usuario_id = int(input("Digite o novo ID do usuário (ou deixe em branco): ") or 0)
            atualizar_emprestimo(
                emprestimo_id,
                novo_livro_id or None,
                novo_usuario_id or None
            )

        elif escolha == '16':
            autor_id = int(input("Digite o ID do autor a ser deletado: "))
            deletar_autor(autor_id)

        elif escolha == '17':
            categoria_id = int(input("Digite o ID da categoria a ser deletada: "))
            deletar_categoria(categoria_id)

        elif escolha == '18':
            livro_id = int(input("Digite o ID do livro a ser deletado: "))
            deletar_livro(livro_id)

        elif escolha == '19':
            usuario_id = int(input("Digite o ID do usuário a ser deletado: "))
            deletar_usuario(usuario_id)

        elif escolha == '20':
            emprestimo_id = int(input("Digite o ID do empréstimo a ser deletado: "))
            deletar_emprestimo(emprestimo_id)

        else:
            print("Opção inválida, tente novamente.")

main()

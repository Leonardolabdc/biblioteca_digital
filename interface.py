import argparse
import arquivos  # Importa o módulo criado com a lógica

def main():
    parser = argparse.ArgumentParser(
        description="📚 Sistema de Gerenciamento de Biblioteca Digital"
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # Comando: listar
    listar = subparsers.add_parser(
        "listar", help="📂 Listar documentos por tipo e ano"
    )
    listar.add_argument("diretorio", help="Diretório principal da biblioteca digital")

    # Comando: adicionar
    adicionar = subparsers.add_parser(
        "adicionar", aliases=["add"], help="➕ Adicionar um novo documento"
    )
    adicionar.add_argument("origem", help="Caminho do arquivo original")
    adicionar.add_argument("destino", help="Local de destino na biblioteca")

    # Comando: renomear
    renomear = subparsers.add_parser(
        "renomear", aliases=["ren"], help="✏️ Renomear um documento"
    )
    renomear.add_argument("caminho", help="Caminho atual do documento")
    renomear.add_argument("novo_nome", help="Novo nome do documento")

    # Comando: remover
    remover = subparsers.add_parser(
        "remover", aliases=["del", "excluir"], help="🗑️ Remover um documento"
    )
    remover.add_argument("caminho", help="Caminho do documento a ser removido")

    # Comando: buscar
    buscar = subparsers.add_parser(
        "buscar", help="🔍 Buscar documentos por nome"
    )
    buscar.add_argument("diretorio", help="Diretório base")
    buscar.add_argument("nome", help="Parte do nome do documento a buscar")

    # Comando: marcar
    marcar = subparsers.add_parser(
        "marcar", help="🏷️ Marcar documento com uma tag"
    )
    marcar.add_argument("caminho", help="Caminho do documento a ser marcado")
    marcar.add_argument("tag", help="Nome da tag")

    # 🔧 Parse dos argumentos depois de definir todos os comandos
    args = parser.parse_args()

    # Execução dos comandos
    match args.comando:
        case "listar":
            docs = arquivos.listar_documentos_por_tipo_e_ano(args.diretorio)
            for tipo, anos in docs.items():
                print(f"\nTipo: {tipo}")
                for ano, arquivos_lista in anos.items():
                    print(f"  Ano {ano}:")
                    for doc in arquivos_lista:
                        print(f"    - {doc}")
        case "adicionar" | "add":
            arquivos.adicionar_documento(args.origem, args.destino)
            print("✅ Documento adicionado com sucesso!")
        case "renomear" | "ren":
            arquivos.renomear_documento(args.caminho, args.novo_nome)
            print("✏️ Documento renomeado com sucesso!")
        case "remover" | "del" | "excluir":
            arquivos.remover_documento(args.caminho)
            print("🗑️ Documento removido com sucesso!")
        case "buscar":
            resultados = arquivos.buscar_documento_por_nome(args.diretorio, args.nome)
            if resultados:
                print("🔎 Documentos encontrados:")
                for r in resultados:
                    print(f"  - {r}")
            else:
                print("⚠️ Nenhum documento encontrado com esse nome.")
        case "marcar":
            arquivos.marcar_documento_com_tag(args.caminho, args.tag)
            print(f"🏷️ Documento marcado com a tag '{args.tag}' com sucesso.")

if __name__ == "__main__":
    main()

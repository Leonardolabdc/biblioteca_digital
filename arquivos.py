import os
from pathlib import Path
from typing import Dict, List

##Lista documentos por tipo e ano
def listar_documentos_por_tipo_e_ano(diretorio: str) -> Dict[str, Dict[str, List[str]]]:
    documentos = {}
    path = Path(diretorio)

    for file_path in path.rglob("*.*"):
        if file_path.is_file():
            tipo = file_path.suffix[1:].lower()
            ano = file_path.parent.name

            if tipo not in documentos:
                documentos[tipo] = {}
            if ano not in documentos[tipo]:
                documentos[tipo][ano] = []

            documentos[tipo][ano].append(str(file_path.name))

    return documentos

# Adiciona (move) um arquivo para o destino
def adicionar_documento(origem: str, destino: str):
    Path(destino).parent.mkdir(parents=True, exist_ok=True)
    os.rename(origem, destino)

# Renomeia um arquivo
def renomear_documento(caminho_atual: str, novo_nome: str):
    novo_caminho = Path(caminho_atual).with_name(novo_nome)
    os.rename(caminho_atual, novo_caminho)

# Remove um arquivo
def remover_documento(caminho: str):
    os.remove(caminho)
# Busca um arquivo
def buscar_documento_por_nome(diretorio_base, termo_busca):
    """
    Busca recursivamente por arquivos que contenham o termo no nome.
    Retorna uma lista com os caminhos dos arquivos encontrados.
    """
    encontrados = []

    for raiz, _, arquivos in os.walk(diretorio_base):
        for arquivo in arquivos:
            if termo_busca.lower() in arquivo.lower():
                caminho_completo = os.path.join(raiz, arquivo)
                encontrados.append(caminho_completo)

    return encontrados
def marcar_documento_com_tag(caminho: str, tag: str):
    """
    Cria um arquivo marcador com a extensão da tag, por exemplo:
    arquivo.pdf → arquivo.importante.tagged
    """
    arquivo_original = Path(caminho)
    tag_path = arquivo_original.with_suffix(f".{tag}.tagged")
    tag_path.touch()  # Cria o arquivo vazio como marcador
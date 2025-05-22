# 📚 Sistema de Gerenciamento de Biblioteca Digital

Sistema simples de linha de comando (CLI) em Python para bibliotecários organizarem documentos digitais por tipo (extensão) e ano (nome da pasta). Permite listar, adicionar, renomear e remover arquivos de forma prática.

---

## ✅ Funcionalidades

- 📂 Listar documentos organizados por tipo e ano
- ➕ Adicionar novos documentos à biblioteca
- ✏️ Renomear arquivos
- 🗑️ Remover documentos

---

## 🏗️ Estrutura do Projeto

```bash
projeto_biblioteca/
├── arquivos.py      # Funções para manipular os arquivos
├── interface.py     # Interface de linha de comando (CLI)
└── README.md        # Este arquivo
```

---

## ⚙️ Requisitos

- Python 3.7 ou superior

---

## 🚀 Como usar

### 1. Clonar o projeto

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

### 2. Executar a interface de linha de comando

```bash
python interface.py <comando> [argumentos]
```

---

## 📌 Comandos e Exemplos de Uso

### 📂 1. Listar documentos

Lista os documentos do diretório base, organizados por **tipo** e **ano** (baseado no nome da pasta).

```bash
python interface.py listar biblioteca/
```

**Exemplo de saída:**

```
Tipo: pdf
  Ano 2023:
    - artigo1.pdf
    - resumo.pdf
  Ano 2024:
    - relatorio-final.pdf

Tipo: jpg
  Ano 2024:
    - capa.jpg
```

---

### ➕ 2. Adicionar documento

Adiciona (move) um novo documento para a estrutura da biblioteca.

```bash
python interface.py adicionar caminho/original.pdf biblioteca/2025/original.pdf
```

Também pode ser usado com alias `add`:

```bash
python interface.py add caminho/original.pdf biblioteca/2025/original.pdf
```

---

### ✏️ 3. Renomear documento

Renomeia um documento dentro do mesmo diretório.

```bash
python interface.py renomear biblioteca/2025/original.pdf novo-nome.pdf
```

Alias disponível: `ren`

```bash
python interface.py ren biblioteca/2025/original.pdf novo-nome.pdf
```

---

### 🗑️ 4. Remover documento

Remove um arquivo específico da biblioteca.

```bash
python interface.py remover biblioteca/2025/novo-nome.pdf
```

Também pode ser usado com:

- `del`
- `excluir`

```bash
python interface.py del biblioteca/2025/novo-nome.pdf
python interface.py excluir biblioteca/2025/novo-nome.pdf
```

---

## 🧼 Organização dos Arquivos

Os arquivos devem estar organizados assim:

```
biblioteca/
├── 2023/
│   └── artigo1.pdf
├── 2024/
│   ├── relatorio.pdf
│   └── capa.jpg
└── 2025/
    └── novo-arquivo.pdf
```

---

## 🧾 Licença

Este projeto é de uso livre para fins educacionais e institucionais.

---

## 🙋 Suporte

Dúvidas ou sugestões? Abra uma [issue](https://github.com/seu_usuario/seu_repositorio/issues) ou envie um pull request!

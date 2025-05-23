# 📚 Sistema de Gerenciamento de Biblioteca Digital

Sistema de linha de comando (CLI) em Python para bibliotecários organizarem documentos digitais por tipo (extensão) e ano (nome da pasta). Permite listar, buscar, adicionar, renomear, remover e marcar documentos com tags.

---

## ✅ Funcionalidades

- 📂 **Listar** documentos organizados por tipo e ano (com nome e tamanho)
- 🔍 **Buscar** documentos por nome
- 🏷️ **Marcar** documentos com tags
- ➕ **Adicionar** novos documentos à biblioteca
- ✏️ **Renomear** arquivos
- 🗑️ **Remover** documentos

---

## 🏗️ Estrutura do Projeto

```

biblioteca\_digital/
├── biblioteca/
│   ├── 2023/
│   ├── 2024/
│   ├── 2025/
│   └── 2026/
│
├── arquivos.py
├── interface.py
├── CONTRIBUTING.md
├── FEEDBACK.md
└── README.md

````

---

## ⚙️ Requisitos

- Python **3.7** ou superior

---

## 🚀 Como Usar

### 1. Clonar o Projeto

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
````

### 2. Executar a Interface de Linha de Comando

```bash
python interface.py <comando> [argumentos]
```

---

## 📌 Comandos e Exemplos de Uso

### 📁 Verifique se os arquivos estão no lugar certo

* Os arquivos `arquivos.py` e `interface.py` devem estar na mesma pasta.
* Rode os comandos a partir dessa pasta.

### 🧪 Crie pastas e arquivos para testes

```bash
mkdir -p biblioteca/2027
mkdir -p biblioteca/2028
mkdir -p biblioteca/2029

echo "Documento de teste PDF" > biblioteca/2027/exemplo1.pdf
echo "Documento de teste TXT" > biblioteca/2028/anotacoes.txt
echo "Outro documento DOC" > biblioteca/2029/relatorio.doc
```

---

### 📂 1. Listar documentos

```bash
python interface.py listar biblioteca/
```

**Exemplo de saída:**

```
Tipo: pdf
  Ano 2023:
    - artigo1.pdf (12.45 KB)
  Ano 2024:
    - relatorio-final.pdf (78.23 KB)

Tipo: jpg
  Ano 2024:
    - capa.jpg (50.12 KB)
```

---

### 🔍 2. Buscar documentos

```bash
python interface.py buscar biblioteca exemplo
```

---

### 🏷️ 3. Marcar documentos com tags

```bash
python interface.py marcar biblioteca/2023/exemplo1.pdf importante
```

---

### ➕ 4. Adicionar novos documentos

```bash
echo "Novo documento para adicionar" > novo_arquivo.txt
python interface.py adicionar novo_arquivo.txt biblioteca/2023/novo_arquivo.txt
python interface.py listar biblioteca
```

---

### ✏️ 5. Renomear arquivos

```bash
python interface.py renomear biblioteca/2023/novo_arquivo.txt arquivo_renomeado.txt
```

---

### 🗑️ 6. Remover documentos

```bash
python interface.py remover biblioteca/2023/arquivo_renomeado.txt
```

---

## 🧼 Organização Esperada dos Arquivos

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

Este projeto é de **uso livre** para fins educacionais e institucionais.

```

Se quiser, posso salvar esse conteúdo direto no arquivo `README.md` ou gerar uma versão com cores (ex: Markdown com HTML estilizado para GitHub Pages). Deseja isso?
```

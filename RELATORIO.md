
---

# 📄 Relatório de Testes e Feedback

## 🧪 Testes Realizados

### ✅ Funcionalidades testadas:

| Funcionalidade            | Testado? | Resultado | Observações                                |
| ------------------------- | -------- | --------- | ------------------------------------------ |
| Listar documentos         | ✔️       | OK        | Mostra por tipo e ano corretamente         |
| Adicionar novo documento  | ✔️       | OK        | Documento é copiado para o destino correto |
| Renomear documento        | ✔️       | OK        | Renomeia corretamente na pasta             |
| Remover documento         | ✔️       | OK        | Remove sem erros                           |
| Buscar por nome           | ✔️       | OK        | Busca parcial funcionando                  |
| Marcar documento com tag  | ✔️       | OK        | Gera arquivo `.tagged` correspondente      |
| Exibir tamanho do arquivo | ✔️       | OK        | Mostra em KB ao lado do nome               |

---

## 💬 Feedback Recebido

Durante os testes e interações com colaboradores (reais ou simulados), recebemos os seguintes feedbacks:

| Origem        | Feedback                                                               | Status               |
| ------------- | ---------------------------------------------------------------------- | -------------------- |
| Colaborador 1 | Incluir funcionalidade de **buscar por nome**                          | ✅ Implementado       |
| Colaborador 2 | Adicionar **tags** nos documentos                                      | ✅ Implementado       |
| Interno       | Exibir **tamanho dos arquivos** ao listá-los                           | ✅ Implementado       |
| Interno       | Melhorar a **documentação do projeto (README.md)**                     | ✅ Reescrito          |
| Interno       | Incluir um arquivo de **contribuição (CONTRIBUTING.md)**               | ✅ Criado             |
| Interno       | Permitir **remover arquivos com alias `del` ou `excluir`**             | ✅ Implementado       |
| Interno       | Organizar o projeto com subpastas por ano dentro da pasta `biblioteca` | ✅ Estrutura aplicada |

---

## 🔁 Ações Tomadas com base no feedback

1. ✅ **`buscar`**: Comando incluído na `interface.py` e implementado no módulo `arquivos.py`
2. ✅ **Tags**: Criado sistema `.tagged` para armazenar tags associadas aos arquivos
3. ✅ **Tamanho**: A função de listagem foi adaptada para exibir o tamanho do arquivo em KB
4. ✅ **Documentação**:

   * `README.md`: reestruturado com emojis, exemplos e comandos passo a passo
   * `CONTRIBUTING.md`: criado para orientar pull requests
5. ✅ **Interface CLI**: Adicionadas aliases como `add`, `ren`, `del`, `excluir` para facilitar comandos
6. ✅ **Estrutura de diretórios**: Pastas para os anos de 2023 a 2026 criadas dentro da pasta `biblioteca/`

---

## 📌 Conclusão

O projeto foi testado com sucesso em diferentes funcionalidades, incluindo as novas adicionadas após feedback. O fluxo de pull requests foi simulado e funcionou conforme o esperado. O feedback recebido foi incorporado de forma incremental, melhorando a usabilidade e organização do projeto.

---


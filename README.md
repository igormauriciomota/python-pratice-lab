# 🐍 Python Learning Lab

Bem-vindo ao meu **Python Learning Lab**!

Este repositório foi criado para documentar minha jornada de aprendizado, prática e aperfeiçoamento em **Python**.

Aqui concentro exercícios, testes, pequenos programas, desafios e experimentos desenvolvidos durante meus estudos. O objetivo é praticar os conceitos da linguagem de forma constante, acompanhar minha evolução e construir uma base sólida para o desenvolvimento de projetos cada vez mais completos.

---

## 🎯 Objetivo do repositório

O `python-learning-lab` funciona como meu laboratório pessoal de desenvolvimento em Python.

Neste espaço, procuro transformar teoria em prática por meio de exercícios progressivos, repetição de conceitos, testes e pequenos sistemas.

Os principais objetivos são:

* Praticar os fundamentos da linguagem Python;
* Desenvolver lógica de programação;
* Melhorar a organização e legibilidade do código;
* Aprender a dividir programas em funções;
* Trabalhar com módulos e pacotes;
* Evoluir para Programação Orientada a Objetos;
* Praticar manipulação e persistência de dados;
* Desenvolver pequenos CRUDs;
* Experimentar diferentes formas de resolver um mesmo problema;
* Aprender boas práticas de desenvolvimento;
* Preparar uma base sólida para projetos reais.

---

# 📚 Conteúdos estudados

O repositório será atualizado continuamente conforme avanço nos estudos.

## Fundamentos

Prática dos principais fundamentos da linguagem:

* Variáveis;
* Tipos de dados;
* Operadores;
* `input()`;
* `print()`;
* Conversão de tipos;
* Strings;
* Listas;
* Tuplas;
* Dicionários;
* Conjuntos.

## Estruturas condicionais

Exercícios utilizando:

```python
if
elif
else
```

Aplicados em situações como:

* Validação de dados;
* Verificação de condições;
* Classificação de valores;
* Menus;
* Regras de negócio.

---

## Estruturas de repetição

Prática com:

```python
for
while
```

Incluindo:

* Percorrer listas;
* Percorrer dicionários;
* Contadores;
* Acumuladores;
* Menus interativos;
* Repetição de cadastros;
* Validação de entradas.

---

# ⚙️ Funções

Estudo da divisão do programa em responsabilidades menores.

Exemplos:

```python
def cadastrar():
    pass


def buscar():
    pass


def alterar():
    pass


def excluir():
    pass


def listar():
    pass
```

Também são estudados:

* Funções sem parâmetros;
* Funções com parâmetros;
* `return`;
* Escopo de variáveis;
* Reutilização de código;
* Separação entre entrada de dados e lógica;
* Responsabilidade das funções;
* Organização do programa através de `main()`.

---

# 📦 Módulos e Pacotes

Uma das etapas importantes deste laboratório é aprender a organizar programas Python em diferentes arquivos.

Exemplo:

```text
sistema/
│
├── main.py
├── cadastro.py
├── validacoes.py
├── relatorios.py
└── banco.py
```

E posteriormente utilizando pacotes:

```text
sistema/
│
├── main.py
│
├── clientes/
│   ├── __init__.py
│   ├── cadastrar.py
│   ├── buscar.py
│   ├── alterar.py
│   └── excluir.py
│
├── financeiro/
│   ├── __init__.py
│   ├── receitas.py
│   ├── despesas.py
│   └── relatorios.py
│
└── validacoes/
    ├── __init__.py
    └── dados.py
```

O objetivo é compreender progressivamente:

* `import`;
* `from ... import`;
* Criação de módulos;
* Comunicação entre módulos;
* Criação de pacotes;
* `__init__.py`;
* Separação de responsabilidades;
* Reutilização de funções;
* Organização de projetos maiores.

---

# 🧱 Programação Orientada a Objetos

Conforme a evolução dos estudos, este laboratório também incluirá exercícios envolvendo:

* Classes;
* Objetos;
* Atributos;
* Métodos;
* Construtores;
* `__init__`;
* Encapsulamento;
* Herança;
* Polimorfismo;
* Composição.

Exemplo:

```python
class Cliente:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
```

---

# 🗃️ Banco de Dados e CRUD

Outra etapa será integrar Python com banco de dados.

Os exercícios poderão envolver:

* SQLite;
* SQL;
* Criação de tabelas;
* INSERT;
* SELECT;
* UPDATE;
* DELETE;
* Conexões com banco de dados;
* Persistência das informações.

Aplicando esses conhecimentos na construção de operações de:

```text
CREATE
READ
UPDATE
DELETE
```

ou simplesmente:

```text
CRUD
```

---

# 🧪 Exercícios e experimentos

Nem todo código presente neste repositório representa uma aplicação finalizada.

Este é propositalmente um **ambiente de aprendizagem**.

Por isso, poderão existir:

* Exercícios simples;
* Diferentes soluções para o mesmo problema;
* Códigos em processo de melhoria;
* Testes;
* Refatorações;
* Pequenos experimentos;
* Exercícios repetitivos para fixação;
* Mini projetos.

A intenção é justamente registrar o processo de evolução.

---

# 📈 Evolução esperada

A progressão dos estudos segue aproximadamente:

```text
Fundamentos
    ↓
Estruturas de Dados
    ↓
Condicionais
    ↓
Loops
    ↓
Funções
    ↓
Módulos
    ↓
Pacotes
    ↓
Programação Orientada a Objetos
    ↓
Arquivos e Banco de Dados
    ↓
CRUD
    ↓
SQL / SQLite
    ↓
Projetos Modulares
    ↓
Desenvolvimento Web
    ↓
Projetos Reais
```

---

# 🚀 Próxima etapa: Portfólio

O `python-learning-lab` representa principalmente o meu **processo de aprendizado e evolução**.

Projetos maiores e aplicações desenvolvidas especificamente para portfólio serão organizados separadamente em seus próprios repositórios.

A proposta é manter uma divisão clara entre:

```text
python-learning-lab
        │
        └── Estudos + Exercícios + Testes + Experimentação

                    ↓ evolução

Projetos de Portfólio
        │
        └── Aplicações completas + Projetos reais
```

Dessa forma, este repositório registra **o caminho de aprendizado**, enquanto os repositórios de portfólio demonstrarão a aplicação prática dos conhecimentos adquiridos.

---

# 🛠️ Tecnologias

Tecnologias e ferramentas que poderão aparecer ao longo dos estudos:

* Python;
* SQLite;
* SQL;
* Git;
* GitHub;
* VS Code;
* Flask;
* Django;
* APIs;
* HTML;
* CSS;
* Bootstrap;
* Pandas;
* NumPy.

Novas tecnologias poderão ser adicionadas conforme a evolução dos projetos.

---

# 📂 Organização

A estrutura poderá evoluir junto com os estudos:

```text
python-learning-lab/
│
├── 01-fundamentos/
│
├── 02-listas/
│
├── 03-dicionarios/
│
├── 04-condicionais/
│
├── 05-loops/
│
├── 06-funcoes/
│
├── 07-modulos/
│
├── 08-pacotes/
│
├── 09-poo/
│
├── 10-arquivos/
│
├── 11-sqlite/
│
├── 12-crud/
│
├── 13-desafios/
│
├── 14-mini-projetos/
│
└── README.md
```

Essa organização não é definitiva. Ela poderá ser modificada conforme novos conceitos forem estudados.

---

# 💡 Filosofia de aprendizado

A proposta deste laboratório pode ser resumida em:

> **Aprender → Praticar → Errar → Corrigir → Refatorar → Repetir → Construir**

Mais importante do que apenas finalizar exercícios é compreender a lógica utilizada, saber explicar o código e conseguir reconstruí-lo posteriormente.

Cada exercício representa uma pequena etapa dessa evolução.

---

## 📌 Status

🚧 **Em desenvolvimento contínuo**

Este repositório será atualizado conforme novos conceitos, exercícios e experiências forem adicionados durante minha jornada de desenvolvimento com Python.

---

**Python Learning Lab 🐍**

*Do fundamento aos projetos reais, um exercício de cada vez.*

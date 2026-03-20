# Conjuntos de Exercícios Python

Este repositório contém exercícios de programação em Python organizados em conjuntos de exercícios separados

Cada pasta inclui scripts independentes cobrindo tópicos essenciais como lógica básica, entrada e saída, condicionais, loops, arrays e manipulação de strings

## Estrutura do Repositório

- `lista02/`: exercícios introdutórios sobre cálculos e condicionais
- `lista04/`: exercícios envolvendo loops, operações numéricas e simulações simples
- `lista06/`: exercícios sobre sequências, estruturas de repetição e validações
- `lista07/`: exercícios com arrays, matrizes e manipulação de caracteres
- `lista08/`: exercícios focados em strings, validações e problemas um pouco mais avançados

## Como Executar

Certifique-se de que o Python3.x está instalado e execute qualquer script individualmente pelo terminal  
Exemplo:

```bash
python3 lista08/jogo_forca.py
```

## Observações

- Os scripts leem entrada do terminal usando `input()`
- Cada arquivo resolve um exercício específico
- Os scripts atuais não requerem dependências externas

## Sobre

Este repositório é uma coleção de exercícios de estudo criados para praticar Python através de pequenos problemas focados

---

## 📚 Resumo do Aprendizado

Esta seção resume os conceitos já praticados neste repositório e aponta os tópicos que ainda faltam para completar uma base sólida de Introdução à Programação.

---

### ✅ O que já foi estudado

#### Entrada e Saída
- Leitura de dados do usuário com `input()` — `lista02/`
- Impressão de resultados com `print()`, strings formatadas (f-strings) e múltiplos valores — `lista02/`, `lista06/`

#### Tipos de Dados Primitivos
- Inteiros (`int`) e ponto flutuante (`float`) — `lista02/salario.py`, `lista02/area_circulo.py`
- Texto (`str`) — `lista02/saudacoes_turno.py`
- Conversão de tipos: `int()`, `float()`, `str()` — utilizado em quase todos os exercícios

#### Operadores
- Aritméticos: `+`, `-`, `*`, `/`, `//` (divisão inteira), `%` (módulo), `**` (exponenciação) — `lista04/divisao_int_resto.py`, `lista02/area_circulo.py`
- Relacionais: `==`, `!=`, `>`, `<`, `>=`, `<=` — `lista02/triangulo.py`
- Lógicos: `and`, `or`, `not` — `lista02/triangulo.py`, `lista06/primo.py`

#### Estruturas de Decisão (Condicionais)
- `if`, `elif`, `else` simples e aninhados — `lista02/media_aluno.py`, `lista02/loja_biju_cartao.py`
- Comparações com strings (`.upper()`, `.lower()`) — `lista02/loja_biju.py`, `lista02/saudacoes_turno.py`

#### Estruturas de Repetição (Loops)
- **`while`**: com sentinela, com condição de parada, com acumuladores — `lista04/divida.py`, `lista04/min_max_soma.py`
- **`for` com `range()`**: contagem crescente e decrescente — `lista06/tabuada.py`, `lista06/rendimento.py`
- Controle de fluxo dentro de loops: `break`, `continue` — `lista04/sistema_vendas.py`, `lista06/primo.py`

#### Funções
- Definição com `def`, parâmetros e valor de retorno simples — `lista08/soma_de_tres.py`, `lista08/positivo_negativo.py`
- Retorno de múltiplos valores (tuplas) — `lista08/tamanho_conteudo.py`
- Retorno de dicionário — `lista08/ocorrencia_caractere2.py`
- Padrão `main()` com `if __name__ == "__main__"` — `lista08/soma_de_tres.py`

#### Strings
- Fatiamento (`string[inicio:fim]`) e indexação (`string[i]`) — `lista08/escada_str.py`
- Iteração caractere a caractere com `for char in string` — `lista08/numero_digitos.py`
- Métodos: `.upper()`, `.lower()`, `.split()` — `lista02/`, `lista08/`
- Concatenação com `+` e repetição com `*` — `lista08/triangulo_n.py`

#### Listas (Arrays)
- Criação, indexação, iteração e `len()` — `lista07/altura_sexo.py`
- Listas paralelas — `lista07/altura_sexo.py`
- Interleaving (intercalação) de listas — `lista07/vetor_intercalado.py`

#### Matrizes (Listas de Listas)
- Criação e acesso a elementos com índices duplos `[i][j]` — `lista07/troca_linha_coluna.py`
- Laços aninhados sobre matrizes — `lista07/dist_pontos.py`

#### Tuplas
- Uso de tuplas para armazenar coordenadas — `lista07/dist_pontos.py`
- Desempacotamento de tuplas — `lista08/tamanho_conteudo.py`

#### Dicionários
- Criação e acesso a pares chave-valor — `lista07/ocorrencia_caractere.py`
- Contagem de frequências com dicionários — `lista07/ocorrencia_caractere.py`, `lista08/ocorrencia_caractere2.py`

#### Módulos da Biblioteca Padrão
- `import random` / `from random import choice` — `lista07/lancamento_dado.py`, `lista08/jogo_forca.py`
- `random.randint()`, `random.choice()` — `lista07/lancamento_dado.py`, `lista08/jogo_forca.py`

#### Algoritmos e Problemas Clássicos
- Sequência de Fibonacci — `lista06/fibonacci.py`
- Verificação de número primo — `lista06/primo.py`
- Raiz quadrada pelo Método de Newton — `lista04/raiz_quadrada.py`
- Crescimento populacional composto — `lista04/taxa_cresc_pop.py`
- Validação de CPF (dígitos verificadores) — `lista08/validar_cpf.py`
- Jogo da Forca — `lista08/jogo_forca.py`
- Distância Euclidiana entre pontos — `lista07/dist_pontos.py`

---

### ❌ O que ainda falta estudar

Os tópicos abaixo são comumente cobertos em disciplinas de Introdução à Programação e ainda **não aparecem** nos exercícios deste repositório:

#### Tratamento de Erros e Exceções
- `try`, `except`, `finally`, `raise`
- Evitar que o programa quebre com entradas inválidas do usuário

#### Leitura e Escrita de Arquivos
- Abrir, ler, escrever e fechar arquivos com `open()`, `.read()`, `.write()`, `.readlines()`
- Uso do gerenciador de contexto `with open(...) as f:`
- Trabalho com arquivos `.txt` e `.csv`

#### Recursão
- Funções que chamam a si mesmas
- Casos base e casos recursivos
- Exemplos clássicos: fatorial, Fibonacci recursivo, busca binária recursiva

#### Orientação a Objetos (POO) — conceitos básicos
- Definição de classes com `class`
- Atributos de instância e métodos
- Construtor `__init__`
- Encapsulamento e uso de objetos
- Herança simples

#### Compreensão de Listas (*List Comprehensions*)
- Sintaxe `[expressão for item in lista if condição]`
- Forma mais idiomática e eficiente de construir listas em Python

#### Funções de Ordem Superior e Funções Anônimas
- `lambda` — funções anônimas de uma linha
- `map()`, `filter()` — aplicar funções sobre sequências
- `sorted()` com chave personalizada

#### Algoritmos de Ordenação e Busca
- Ordenação por seleção, inserção ou bolha (Selection Sort, Insertion Sort, Bubble Sort)
- Busca linear e busca binária
- Uso de `sorted()` e `list.sort()` nativos do Python

#### Conjuntos (`set`)
- Criação e operações: união, interseção, diferença
- Verificação de pertencimento sem duplicatas

#### Módulos Adicionais da Biblioteca Padrão
- `math` — funções matemáticas avançadas (`sqrt`, `ceil`, `floor`, `log`, etc.)
- `os` / `sys` — interação com o sistema operacional
- `datetime` — datas e horas
- `collections` — estruturas como `Counter`, `defaultdict`

#### Testes Unitários
- Verificar o comportamento de funções com `assert` ou com o módulo `unittest`
- Conceito de caso de teste, resultado esperado vs. resultado obtido

#### Boas Práticas e Organização de Código
- Docstrings em funções e módulos
- Separação do código em múltiplos arquivos/módulos com `import`
- Uso de constantes nomeadas ao invés de números mágicos
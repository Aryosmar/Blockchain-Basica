# Blockchain Básica

Este projeto é uma implementação de uma blockchain básica, desenvolvida para atender aos requisitos de uma atividade que simula o funcionamento de uma rede blockchain distribuída. O objetivo é explorar conceitos fundamentais como propagação de blocos e transações, resolução de conflitos, controle de saldos e aplicação de taxas e recompensas para mineradores.

## Objetivos do Projeto

- Simular uma rede onde diferentes "nós" trocam informações sobre blocos e transações.
- Resolver conflitos (forks) e garantir que todos os nós concordem com a mesma cadeia.
- Implementar um sistema que controla os saldos dos endereços e processa apenas transações válidas.
- Adicionar taxas de transação e recompensas para os mineradores.

## Estrutura do Projeto

O projeto está organizado em diferentes módulos para facilitar a manutenção e o entendimento:

### `transacao.py`

Define as transações entre endereços.

**Principais Funções:**

- `__init__`: Inicializa uma transação, validando remetente, destinatário e valores.
- `adicionar_ao_historico`: Registra a transação no histórico de endereços.
- `mostrar_historico`: Exibe o histórico de transações de um endereço.

### `bloco.py`

Representa os blocos da blockchain.

**Principais Funções:**

- `__init__`: Inicializa um bloco com transações, hash anterior e dificuldade.
- `gerar_hash`: Calcula o hash do bloco combinando suas informações.
- `proof_of_work`: Resolve o desafio computacional para validar o bloco.

**Destaques:**

- Inclui a árvore de Merkle para validação de transações.

### `cadeia_de_blocos.py`

Gerencia a cadeia de blocos.

**Principais Funções:**

- `criar_bloco_genesis`: Cria o bloco inicial com uma transação gênese.
- `adicionar_bloco`: Adiciona novos blocos à cadeia após validações.
- `mostrar_saldos`: Exibe os saldos dos endereços na rede.
- `mostrar_cadeia`: Lista todos os blocos e suas informações.

### `arvore_merkle.py`

Implementa a árvore de Merkle para validação eficiente de transações.

**Vantagens:**

- Permite verificar a presença de uma transação sem processar todas as transações do bloco.

### `carteira.py`

Gera e valida endereços de carteiras.

**Principais Funções:**

- `gerar_endereco`: Cria endereços únicos com prefixo "2x".
- `endereco_valido`: Verifica se o endereço segue o formato padrão.

### `main.py`

Ponto de entrada principal da aplicação.

- Inclui exemplos de criação de blocos, transações e sincronização de nós.

## Executando o Projeto

### No Terminal

1. Navegue até o diretório do projeto.
2. Certifique-se de que o Python 3 está instalado.
3. Verifique a versão do Python com o comando:

   ```bash
   python3 --version
   ```

4. Execute o arquivo `main.py` com o comando:

   ```bash
   python3 main.py
   ```

### No Visual Studio Code

1. Abra o Visual Studio Code e carregue o diretório do projeto.
2. Configure o Interpretador Python:

   - Na barra de status inferior, clique na versão do Python exibida (ou no aviso de seleção do interpretador).
   - Selecione Python 3 na lista de interpretadores disponíveis.

3. Abra o terminal integrado:

   - Vá em **Terminal > New Terminal**.

4. Execute o arquivo `main.py`:

   - No terminal integrado, digite:

     ```bash
     python3 main.py
     ```

   - Ou clique com o botão direito em `main.py` no Explorer e selecione **Run Python File in Terminal**.

5. Certifique-se de que o VS Code está usando o Python 3 como interpretador.

## Funcionalidades

### Propagação de Blocos e Transações

- Simulação de comunicação entre nós para manter a blockchain sincronizada.

### Resolução de Conflitos

- Implementação da regra "a cadeia mais longa vence".

### Controle de Saldos

- Cada endereço possui um saldo, e as transações só são processadas se houver fundos suficientes.

### Taxas de Transação e Recompensas

- Taxas incentivam os mineradores, somando-se à recompensa base de cada bloco.

### Histórico de Transações

- Registro detalhado de todas as transações por endereço.

### Validação de Endereços

- Garantia de que apenas endereços válidos participam das transações.

## Exemplo de Uso

### Criação de um Bloco Gênese e Adição de Transações

```python
from cadeia_de_blocos import CadeiaDeBlocos
from transacao import Transacao
from carteira import Carteira

# Criação de Nós
no1 = CadeiaDeBlocos(dificuldade=2, recompensa=50)
no2 = CadeiaDeBlocos(dificuldade=2, recompensa=50)
nos = [no1, no2]

# Gerar endereços
minerador = Carteira.gerar_endereco()
remetente = Carteira.gerar_endereco()
destinatario = Carteira.gerar_endereco()

# Configurar saldo inicial
no1.saldos[remetente] = 100

# Criar e propagar transação
transacao = Transacao(remetente, destinatario, 30, taxa=2)
no1.adicionar_bloco([transacao], minerador)
```

## Desenvolvido por

Aryosmar Felipe Almeida.

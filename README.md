# Blockchain Básica

Este projeto é uma implementação de uma blockchain básica, desenvolvida para atender aos requisitos de uma atividade que simula o funcionamento de uma rede blockchain distribuída. O objetivo é explorar conceitos fundamentais como propagação de blocos e transações, resolução de conflitos, controle de saldos e aplicação de taxas e recompensas para mineradores.

## Objetivos do Projeto

- Simular uma rede onde diferentes "nós" trocam informações sobre blocos e transações.
- Resolver conflitos (forks) e garantir que todos os nós concordem com a mesma cadeia.
- Implementar um sistema que controla os saldos dos endereços e processa apenas transações válidas.
- Adicionar taxas de transação e recompensas para os mineradores.

## Pré-requisitos

Para executar este projeto, certifique-se de ter o seguinte ambiente configurado:

- **Python 3.6** ou superior instalado.
- Dependências padrão do Python: `hashlib` e `time`.

## Clonando o Repositório

Clone o repositório para o seu ambiente local utilizando o comando:

```bash
git clone https://github.com/Aryosmar/Blockchain-Basica.git 
```
## Acesse o Diretório do Projeto

```bash
cd Blockchain-Basica
```
## Estrutura do Projeto

O projeto está organizado em diferentes módulos para facilitar a manutenção e o entendimento:

- **transacao.py**: Define as transações entre endereços.
- **bloco.py**: Representa os blocos da blockchain, incluindo a lógica de prova de trabalho.
- **cadeia_de_blocos.py**: Gerencia a cadeia de blocos, validando e adicionando novos blocos.
- **arvore_merkle.py**: Implementa a árvore de Merkle para validação de transações.
- **carteira.py**: Gera e valida endereços de carteiras.
- **main.py**: Ponto de entrada principal da aplicação.

## Executando o Projeto

### No Terminal

1. Navegue até o diretório do projeto.
2. Certifique-se de que o **Python 3** está instalado.
3. Verifique a versão do Python com o comando:

```bash
python3 --version
```
4. Execute o arquivo `main.py` com o comando:

```bash
python3 main.py
```
### No Visual Studio Code

1. Abra o **Visual Studio Code** e carregue o diretório do projeto.

2. **Configure o Interpretador Python**:
   - Na barra de status inferior, clique na versão do Python exibida (ou no aviso de seleção do interpretador).
   - Selecione **Python 3** na lista de interpretadores disponíveis.

3. **Abra o terminal integrado**:
   - Vá em **Terminal > New Terminal**.

4. **Execute o arquivo `main.py`**:
   - No terminal integrado, digite:

   ```bash
   python3 main.py
    ```
5. Ou clique com o botão direito em `main.py` no Explorer e selecione **Run Python File in Terminal**.

6. Certifique-se de que o **VS Code** está usando o **Python 3** como interpretador.

## Funcionalidades

- **Propagação de Blocos e Transações**: Simulação de comunicação entre nós para manter a blockchain sincronizada.
- **Resolução de Conflitos**: Implementação da regra "a cadeia mais longa vence".
- **Controle de Saldos**: Cada endereço possui um saldo, e as transações só são processadas se houver fundos suficientes.
- **Taxas de Transação e Recompensas**: Taxas incentivam os mineradores, somando-se à recompensa base de cada bloco.
- **Histórico de Transações**: Registro detalhado de todas as transações por endereço.
- **Validação de Endereços**: Garantia de que apenas endereços válidos participam das transações.

## Desenvolvido por

Aryosmar Felipe Almeida.






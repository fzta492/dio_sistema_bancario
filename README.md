# Simulação de Operações Bancárias Simples em Python

Este é um projeto simples em Python que simula operações bancárias básicas, como saques, depósitos e visualização de extrato. Ele utiliza a biblioteca `pandas` para armazenar e exibir o histórico de transações.

[Código](https://github.com/fzta492/dio_sistema_bancario/blob/main/banco.py)

## Funcionalidades

* **Sacar:** Permite realizar saques com as seguintes restrições:
    * Limite de 3 saques diários.
    * Valor máximo de R$ 500,00 por saque.
    * Verificação de saldo insuficiente.
* **Depositar:** Permite realizar depósitos de valores positivos.
* **Visualizar Extrato:** Exibe o histórico de todas as transações (saques e depósitos) e o saldo atual da conta.

## Como Usar

1.  **Pré-requisitos** <br>
   Certifique-se de ter o Python instalado em seu sistema. Além disso, a biblioteca `pandas` precisa estar instalada. Caso não esteja, você pode instalá-la usando o pip:
    ```bash
    pip install pandas
    ```

3.  **Execução** <br>
    * Salve o código Python em um arquivo (por exemplo, `banco.py`).
    * Abra o terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute o script com o comando:
        ```bash
        python banco.py
        ```
    * O programa iniciará automaticamente.

4.  **Interação** <br>
   O programa exibirá um menu com as opções disponíveis:
    ```
    ====== Operação ======

    1 - Sacar
    2 - Depositar
    3 - Visualizar Extrato
    4 - Sair

    ======================
    ```
    Digite o número da opção desejada e siga as instruções na tela.

## Estrutura do Código

* `banco.py`: Contém todo o código da simulação bancária.
* `saldo`: Variável global que armazena o saldo atual da conta.
* `contagem_saques`: Variável global que controla o número de saques realizados no dia.
* `historico`: DataFrame do pandas utilizado para armazenar o histórico de transações, com as colunas "Tipo" (Saque ou Depósito) e "Valor".
* `menu()`: Função que exibe o menu de opções e recebe a entrada do usuário.
* `sacar()`: Função que implementa a lógica de saque, incluindo as validações de limite, valor máximo e saldo.
* `depositar()`: Função que implementa a lógica de depósito.
* `visualizar_extrato()`: Função que exibe o saldo atual e o histórico de transações utilizando o DataFrame `historico`.
* `executar()`: Função principal (anteriormente `main()`) que contém o loop para interação com o usuário e é chamada diretamente no final do script para iniciar a execução.

## Observações e Melhorias Futuras

* **Persistência de Dados:** Atualmente, os dados (saldo e histórico) são perdidos ao encerrar o programa. Em futuras versões, poderia ser implementada a persistência de dados utilizando arquivos (como CSV, JSON) ou um banco de dados simples.
* **Autenticação:** Adicionar um sistema de autenticação para proteger a conta.
* **Mais Operações:** Implementar outras operações bancárias, como transferências, pagamentos, etc.
* **Tratamento de Erros:** Refinar o tratamento de erros para entradas inválidas.
* **Interface:** Considerar a criação de uma interface gráfica (GUI) para uma melhor experiência do usuário.

## Autor

Fellipe Bandeira

## Licença
MIT License

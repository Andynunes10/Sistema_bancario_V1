Sistema Bancário em Python

📋 Descrição

Uma aplicação de terminal simples que simula as operações básicas de um sistema bancário. Este projeto foi desenvolvido como parte do meu aprendizado em Python, implementando conceitos fundamentais de programação como variáveis, condicionais, loops e manipulação de strings.

✨ Funcionalidades

💰 Depósito

- Permite realizar depósitos de valores positivos
- Atualiza o saldo automaticamente
- Registra cada operação no extrato

💸 Saque

- Limite de 3 saques diários
- Valor máximo por saque: R$ 500,00
- Validação de saldo suficiente
- Contagem de saques restantes
- Registra cada operação no extrato

📃 Extrato

- Exibe todas as operações realizadas (depósitos e saques)
- Mostra o saldo atual da conta
- Exibe mensagem específica quando não há movimentações

🚪 Sair

- Encerra a aplicação com uma mensagem de despedida

🚀 Como usar

1. Clone este repositório
2. Execute o arquivo Python:

python sistema_bancario.py

3. Siga as instruções no menu interativo

🔧 Tecnologias utilizadas

- Python 3.x
- Conceitos fundamentais:
  - Variáveis e constantes
  - Estruturas condicionais (if, elif, else)
  - Loops (while)
  - Formatação de strings
  - Manipulação de tipos de dados

📌 Limitações atuais

- Sistema com apenas um usuário
- Os dados não são persistentes (são perdidos ao encerrar o programa)
- Interface limitada ao terminal

🔜 Possíveis melhorias futuras

- Implementar múltiplos usuários e contas
- Adicionar autenticação por senha
- Persistência de dados em arquivo ou banco de dados
- Interface gráfica
- Novas funcionalidades (transferências, pagamentos, etc.)
# Mob Programming Conta Azul

Mob programming realizado para alunos da Trybe

## Desafio de leitura de faturas

O objetivo do desafio é:

1. Ler os arquivos de registros de faturas na pasta /faturas/*.ftr

2. Realizar as validações dos campos seguindo o modelo:

### Layout

Campo              | Descrição            | Posição | Tipo
---                | ---                  | ---     | --- 
Pagamento          | Meio de pagamento    | 01-01   | MDP
Pagador            | Nome do Pagador      | 02-22   | Alphanumérico
Recebedor          | Nome do recebedor    | 23-33   | Alphanumérico
Emissão            | Data da emissão      | 34-42   | Datetime
Pagamento          | Data do pagamento    | 43-51   | Datetime


### Tipos de dados

Tipo|Descrição
---|---
Alphanumérico|A-Za-z0-9
Datetime|2020-01-01
Pagamento|1-3

### Valores
MDP| Descrição  
--- | --- 
1 | Boleto
2 | Cartão
3 | PIX

Status| Descrição
--- | --- 
Pago | Data de pagamento preenchida, com valor maior ou igual a data de emissão
Em aberto | Data de pagamento não preenchida
Agendado    | Data de pagamento após a data de hoje

<br>

3. Realizar a impressão da fatura com o seu devido status. Resultado esperado:

```composer log
- Boleto do Ivan Sandrini com vencimento no dia 03/01/2020 Pago para Maria no dia 03/01/2020.
- Cartão do João Agendado para o dia 15/05/2021.
- PIX enviado Pelo Murilo no dia 03/01/2020 para o Ivan.
```







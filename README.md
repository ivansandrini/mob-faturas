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
Recebedor          | Nome do recebedor    | 23-43   | Alphanumérico
Emissão            | Data da emissão      | 44-51   | Datetime
Pagamento          | Data do pagamento    | 52-59   | Datetime
Valor              | Valor da Fatura    | 60-80   | Decimal


### Tipos de dados

Tipo|Descrição
---|---
Alphanumérico|A-Za-z0-9
Datetime|2020-01-01
Pagamento|1-3
Decimal|999.999.999,99

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
- Pagamento de Boleto do Ivan Sandrini no valor de "99,99", com vencimento no dia 03/01/2020, Pago para Maria no dia 03/01/2020.
- Compra no Cartão de crédito do João Agendado para o dia 15/05/2021.
- Transferência PIX no valor de "99,99" enviado de Murilo para Ivan no dia 03/01/2020.
- Boleto em Aberto de Ivan sandrini para Marcos Brito no valor de "99,99". Vencimento no dia 01/01/2022. 
```







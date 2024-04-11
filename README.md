<h1 align="center"> Predição de vendas das lojas Rossmann</h1> 

<img align="center"  height="450" width="1000" src="https://github.com/aroldobrancalhao/data_science_producao/blob/main/img/rossmann.jpg" >


## 1.0 Contexto

<p> Rossmann possui mais de 3.000 farmácias em 7 países da Europa. Atualmente, os gerentes das farmácias Rossmann receberam a tarefa de precificar as vendas de cada loja para as próximas seis semanas. As vendas são influenciadas por vários fatores como promoções, competição, feriados, sazonalidade e localização. Como centenas de gerentes realizam suas previsões de maneiras distintas, o resultado ficaria muito variado e dificilmente poderia ser comparado de maneira justa.</p>

## 2.0 Desafio do Negócio

<p> Durante uma reunião mensal com os gerentes, o CFO da Rossmann solicitou que estes enviassem uma previsão de vendas de cada loja das próximas 6 semanas. Desta forma foi necessária a atuação do cientista de dados para criar um modelo de previsão de vendas das próximas 6 semanas separados por loja. </p>

## 3.0 Resumo

<p> Após ser contactado por diversos gerentes para realizar a previsão de cada uma das lojas, entendemos que a demanda partiu do CFO, e para verificar se realmente esta precificação seria a melhor entrega conversamos com o CFO para entender sua demanda. Após esta conversa nos foi informado que a precificação das vendas é parte da estratégia de definição de investimento nas lojas, e para isso ele precisaria que a precificação fosse melhor que a média de vendas das lojas que atualmente é utilizado.</p>
<p> Desta forma entendemos que realmente o modelo de precificação supre a necessidade do CFO, e ele será entregue via bot no Telegram, que permitirá que de qualquer local o CFO possa realizar tal consulta de seu celular e definir sua estratégia de investimentos nas lojas.</p>

- [Fonte de dados](https://www.kaggle.com/c/rossmann-store-sales)

## 4.0 Descrição dos Dados

- <b>Id</b> - Id único que representa (Loja, Data)
- <b>Store</b> - ID das lojas
- <b>Sales</b> - Vendas do dia
- <b>Customers</b> - Número de clientes no dia
- <b>Open</b> - Indicador se a loja está aberta: 0 = Fechada, 1 = Aberta
- <b>StateHoliday</b> - Feriados. Normalmente as lojas ficam fechadas nos feriados estaduais, exceto algumas. Todas as escolas ficam fechadas nos feriados públicos e fins de semana. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
- <b>SchoolHoliday</b> - indica se a loja foi afetada pelo fechament das escolas públicas
- <b>StoreType</b> - 4 tipos de moedlos de loja: a, b, c, d
- <b>Assortment</b> - descreve o sortimento de cada loja: a = basic, b = extra, c = extended
- <b>CompetitionDistance</b> - distancia em metros para o competidor mais próximo
- <b>CompetitionOpenSince[Month/Year]</b> - ano e mês aproximado em que a competição mais próxima foi aberta
- <b>Promo</b> - indica se a loja está realizando promoção no dia
- <b>Promo2</b> - Promo2 é uma promoção contínua e consecutiva para algumas lojas: 0 = Loja não participante, 1 = Loja participante
- <b>Promo2Since[Year/Week]</b> - Ano e semena em que a loja começou a participar da Promo2
- <b>PromoInterval</b> - descreve os intervalos consecutivos em que a Promo2 éiniciada, nomeando os meses em que cada rodada de promoção começa para qualquer ano para esta loja

## 5.0 Solução 

<p> Para a solução foi aplicado o método CRISP-DS, onde começamos com o entendimento do negócio, passamos para coleta dos dados, limpeza dos dados, EDA (Análise Exploratória dos dados), modelagem, Avaliação do modelo e por fim a publicação do modelo em produção.</p>

<p> Para o deploy do modelo utilizamos o render, onde o modelo treinado recebe os dados através de uma requisição por um arquivo JSON e devolve com a coluna de previsão.</p>

## 6.0 Bot do Telegram

<p> Com o intuito de melhorar a solução para o usuário, criamos um bot no Telegram onde o usuário pode informar o número da loja e receber a previsão das próximas 6 semanas diretamente em seu celular ou computador.</p>

## 7.0 Próximos passos:

- Melhorar as métricas do modelo;
- Utilizar métodos complementares ao Bot do Telegram para que o usuário possa realizar tal consulta;

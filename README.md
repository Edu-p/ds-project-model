

# :mag: O Proposito 
## **Este é um Repositorio de estudo, com a finalidade de estruturar um projeto completo em ciencia de dados, desde o questionamento de qual o real problema de negocio ate o deploy do modelo final.**



# 💎 Objeto de estudo

Você recebe dados históricos de vendas de 1.115 lojas da Rossmann( a segunda maior rede de farmácias da Alemanha ). A tarefa é prever a coluna "Vendas" nas proximas seis semanas para o conjunto de teste. Esse problema de negocio foi tirado do [kaggle](https://www.kaggle.com), de uma competiçao realizada em meados de 2015 => [link da competiçao](https://www.kaggle.com/c/rossmann-store-sales/overview)

![entrada-rossmann](https://user-images.githubusercontent.com/72039442/128021834-c36f75d8-b021-4d0d-8806-fc4d1e165f02.jpg)


---

# 📔O Conteúdo

- Todo o estudo foi acompannhado pelo Meigarom Lopes em suas video-aulas, acompanhadas pela "Comunidade DS".
    - Seu canal do [Youtube](https://www.youtube.com/channel/UCar5Cr-pVz08GY_6I3RX9bA).
    - Seu linkedin [Linkedin](https://www.linkedin.com/in/meigarom/?originalSubdomain=br).
    - Seu instagram [Instagram](https://www.instagram.com/meigarom/).
- Esse visa ajudar os proximos estudantes que passarem pelo curso "DS em produçao", com os codigos feitos em cada uma das aulas, com pequenas alteraçoes feitas por mim.
- O obejtivo desse projeto não é de servir como um copy and paste, mas de um gabarito de alguem que ja passou por algum dos possiveis problemas enfrentados durante o curso do [Meigarom](https://www.instagram.com/meigarom/).

- Como esta estruturado o repositorio:
    - De forma semelhante à estrutura do repositorio do curso disponibilizado por [Meigarom](https://www.instagram.com/meigarom/), o repositorio tem 10 notebooks principais que foram feitos em cada modulo do programa. Eles sao acumulativos, por isso, um notebook de um modulo superior tem as mesmas etapas ja feitas do inferior.
    - A pasta 'api' é destinada ao primeiro deploy do modelo final, no heroku, com a url => https://prediction-rossmann-v2.herokuapp.com/
    - A pasta 'img' contem uma imagem de um mapa mental das hipoteses levantadas na etapa da análise exploratoria de dados do projeto 
    - A pasta 'parameters' tem o modelo final e os scaler's necessarios para colocar o modelo em produçao
    - A pasta 'datasets' contem os conjunto de dados disponibilizados no desafio no Kaggle
    - A pasta 'rossmann-api-telegram' contem todo o codigo que fiz para colocar o modelo acessivel por um bot no telegram
    

---

# 🖱️Considerações e utilização

- Foi utilizando o [Pycharm](https://www.jetbrains.com/pt-br/pycharm/) como IDE e o [Python 3.8](https://www.python.org/downloads/release/python-380/) como interpretador
- Link para acessar os resultados pelo=> [conversar com bot no telegram](t.me/rossmann_pred_edu_bot)
    - ![telegram-bot](https://user-images.githubusercontent.com/72039442/128722507-d8a02fcf-d363-430f-9e39-984a79aab36e.gif)
    - Para conseguir as previsoes das lojas, voce deve abrir a conversa com o "RossmannPrediction", pelo telegram, e digitar /numero_da_loja_desejada, que ele mandara o numero de identificaçao da loja para o algoritmo para fazer previsao em tempo real e devolver o resultado, depois das devidas manipulaçoes necessarias.



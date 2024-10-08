# Monitoramento de Investimentos: Investai

Este projeto é uma aplicação web desenvolvida com Flask que permite monitorar ações e criptomoedas em tempo real, utilizando a API gratuita da Alpha Vantage. A aplicação exibe os dados de fechamento dos ativos em gráficos interativos utilizando Plotly.
[imagem-do-projeto](imagem.png)

## Funcionalidades

- Escolha entre ações ou criptomoedas para monitorar.
- Insira o símbolo do ativo (ex: AAPL para Apple, BTCUSD para Bitcoin).
- Visualize gráficos interativos de preços.

## Tecnologias Utilizadas

- **Python** (Flask) - Backend da aplicação.
- **Plotly** - Criação de gráficos interativos.
- **Alpha Vantage** - API gratuita para dados financeiros.
- **Bootstrap** - Estilização da interface.

## Como Rodar a Aplicação

### 1. Clone o repositório:

```bash
git clone https://github.com/NatHanNSilva12/investai-python-invest.git
cd investai-python-invest
``` 
2. Crie um ambiente virtual e ative-o:
```bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```

3. Instale as dependências:
```bash
Copiar código
pip install -r requirements.txt
```

4. Defina sua chave da API Alpha Vantage:
No arquivo app.py, substitua 'YOUR_API_KEY' pela sua chave de API obtida no site da Alpha Vantage.

5. Rode a aplicação:
```bash
Copiar código
python app.py
```
Acesse a aplicação no navegador pelo endereço http://127.0.0.1:5000.

Paleta de Cores
```
Fundo: Cinza claro (#f4f5f7)
Texto Principal: Cinza escuro (#2c3e50)
Botão: Azul (#007bff)
```

#Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

yaml
Copiar código

---

### 7. **Notas Finais**

- **Chave da API**: Certifique-se de obter uma chave de API da Alpha Vantage [neste link](https://www.alphavantage.co/support/#api-key) e substituí-la no código onde aparece `'YOUR_API_KEY'`.
  
- **Hospedagem**: Você pode hospedar a aplicação no **Heroku** ou **PythonAnywhere** seguindo as instruções específicas de cada plataforma.

Com esses códigos, você tem uma aplicação completa de monitoramento de investimentos, com gráficos e futuramente pretendo adicionar uma IA para monitorar os investimentos e dizer qual é o melhor a ser feito no momento.

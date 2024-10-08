from flask import Flask, render_template, request
import plotly.graph_objs as go
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies

app = Flask(__name__)

# Função para pegar dados de ações
def get_stock_data(symbol):
    ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
    data, _ = ts.get_intraday(symbol=symbol, interval='1min', outputsize='compact')
    return data

# Função para pegar dados de criptomoedas
def get_crypto_data(symbol):
    cc = CryptoCurrencies(key='YOUR_API_KEY', output_format='pandas')
    data, _ = cc.get_digital_currency_intraday(symbol=symbol, market='USD')
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    graph = None
    error = None

    if request.method == 'POST':
        investment_type = request.form['investment_type']
        symbol = request.form['symbol']

        try:
            if investment_type == 'stock':
                df = get_stock_data(symbol)
                title = f'Preço da Ação ({symbol.upper()})'
            elif investment_type == 'crypto':
                df = get_crypto_data(symbol)
                title = f'Preço da Criptomoeda ({symbol.upper()})'
            else:
                df = None

            if df is None or df.empty:
                error = f"O símbolo {symbol.upper()} não foi encontrado."
            else:
                # Criar gráfico com Plotly
                fig = go.Figure(data=[go.Scatter(x=df.index, y=df['4. close'], mode='lines', name='Fechamento')])
                fig.update_layout(title=title)
                graph = fig.to_html(full_html=False)

        except Exception as e:
            error = f"Erro ao buscar os dados: {e}"

    return render_template('index.html', graph=graph, error=error)

if __name__ == '__main__':
    app.run(debug=True)

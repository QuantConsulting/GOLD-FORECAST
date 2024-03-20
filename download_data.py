import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Configurar el período de tiempo
end_date = datetime(2023, 3, 1)
start_date = datetime(2003, 3, 6)

# Lista de símbolo
symbols = {
    "Gold": "GC=F",
    "SP500": "^GSPC",
    "DJI": "^DJI",
    "EGO": "EGO",
    "EURUSD": "EURUSD=X",
    "BrentOil": "BZ=F",
    "WTICrude": "CL=F",
}


# Descargar datos de Yahoo Finance
# Función para descargar los datos
def download_and_prepare_data(symbols, start_date, end_date):
    all_data = []
    for name, symbol in symbols.items():
        data = yf.download(symbol, start=start_date, end=end_date, interval="1d")
        data["Symbol"] = name
        data.reset_index(inplace=True)
        data["Date"] = data["Date"].dt.date
        all_data.append(data)
    return pd.concat(all_data)


# Descargar y preparar los datos
data = download_and_prepare_data(symbols, start_date, end_date)

# Pivotar el DataFrame
pivot_data = pd.pivot_table(
    data,
    values=["Open", "High", "Low", "Close", "Adj Close", "Volume"],
    index="Date",
    columns="Symbol",
)

# Para aplanar las columnas
pivot_data.columns = ["_".join(col).strip() for col in pivot_data.columns.values]

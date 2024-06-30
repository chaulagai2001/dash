from dash import Dash, html, dcc
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data.loader import load_transaction_data

DATA_PATH = r"D:\my_projects\dash\day2\data\transactions.csv"

def main() -> None: 
    data = load_transaction_data(path= DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial Dashboard"
    app.layout= create_layout(app, data)
    app.run(debug=True)

if __name__ == "__main__": 
    main()
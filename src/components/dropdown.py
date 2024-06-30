from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from src.components import ids

def render(app: Dash)-> html.Div:
    all_nations = ["South Korea", "China", "India"]
    @app.callback(
        Output(ids.NATION_DROPDOWN, "value"), 
        Input(ids.SELECT_ALL_NATIONS_BUTTON, "n_clicks")
    )
    # def select_all_nations(n_clicks: int)-> list[str]: 
    #     if n_clicks: 
    #         return all_nations
    #     return []
    def select_all_nations(_: int)-> list[str]: 
        return all_nations

    return html.Div(
        children = [
            html.H6("Nation"), 
            dcc.Dropdown(
                id= ids.NATION_DROPDOWN,
                options = [{"label": nation, "value": nation} for nation in all_nations],
                value= all_nations,
                multi = True
            ),
            html.Button(
                className = "Button",
                children = ["Select All"], 
                id = ids.SELECT_ALL_NATIONS_BUTTON, 
                n_clicks = 0
            )
        ]
    )
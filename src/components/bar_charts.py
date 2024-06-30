from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids

MEDAL_DATA = px.data.medals_long()
# print(MEDAL_DATA)

def render(app: Dash) -> html.Div: 
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.NATION_DROPDOWN, "value")
    )
    def update_bar_chart(nations: list[str]) -> html.Div:
        filtered_data = MEDAL_DATA.query("nation in @nations")
        # print(filtered_data)

        # print(".....................")
        # print(MEDAL_DATA)
        # for nation in nations:
        #     print(nation)
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BAR_CHART)

        fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
    
    return html.Div(id=ids.BAR_CHART)
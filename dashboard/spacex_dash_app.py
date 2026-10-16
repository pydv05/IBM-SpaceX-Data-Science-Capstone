import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
df = pd.read_csv(DATA_URL)

app = Dash(__name__)
app.title = "SpaceX Launch Records Dashboard"

sites = ["ALL"] + sorted(df["Launch Site"].dropna().unique().tolist())
min_payload = float(df["Payload Mass (kg)"].min())
max_payload = float(df["Payload Mass (kg)"].max())

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard",
            style={"textAlign": "center"}),

    html.Label("Select Launch Site"),
    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label": s, "value": s} for s in sites],
        value="ALL",
        clearable=False
    ),

    html.Br(),
    dcc.Graph(id="success-pie-chart"),

    html.Label("Payload range (kg)"),
    dcc.RangeSlider(
        id="payload-slider",
        min=min_payload,
        max=max_payload,
        value=[min_payload, max_payload],
        step=100,
        marks=None,
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    dcc.Graph(id="success-payload-scatter")
])


@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value")
)
def update_pie(site):
    filtered = df if site == "ALL" else df[df["Launch Site"] == site]
    counts = filtered["class"].value_counts().reindex([0, 1], fill_value=0)
    fig = px.pie(
        values=counts.values,
        names=["Unsuccessful", "Successful"],
        title=f"Landing Outcomes — {site}"
    )
    return fig


@app.callback(
    Output("success-payload-scatter", "figure"),
    [Input("site-dropdown", "value"),
     Input("payload-slider", "value")]
)
def update_scatter(site, payload_range):
    filtered = df[df["Payload Mass (kg)"].between(payload_range[0], payload_range[1])]
    if site != "ALL":
        filtered = filtered[filtered["Launch Site"] == site]

    fig = px.scatter(
        filtered,
        x="Flight Number",
        y="Payload Mass (kg)",
        color="Booster Version Category",
        hover_data=["Launch Site", "class"],
        title="Flight Number vs Payload Mass"
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)

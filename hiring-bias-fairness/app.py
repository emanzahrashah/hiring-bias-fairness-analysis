import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Use your computed summary (hardcoded for simplicity)
df = pd.DataFrame({
    "gender": ["Female", "Male"],
    "shortlisted_rate": [0.753695, 0.248731],
    "recall": [0.764706, 0.281690],
    "false_negative_rate": [0.098522, 0.258883]
})

app = dash.Dash(__name__)

app.layout = html.Div(
    style={"padding": "40px", "fontFamily": "Arial"},
    children=[
        html.H1("Hiring Model Fairness Dashboard"),

        html.H3("Predicted Shortlisting Rate by Gender"),
        dcc.Graph(figure=px.bar(df, x="gender", y="shortlisted_rate")),

        html.H3("Recall by Gender (Qualified Candidates Found)"),
        dcc.Graph(figure=px.bar(df, x="gender", y="recall")),

        html.H3("False Negative Rate by Gender (Missed Qualified Candidates)"),
        dcc.Graph(figure=px.bar(df, x="gender", y="false_negative_rate")),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

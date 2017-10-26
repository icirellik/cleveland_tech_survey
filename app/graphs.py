import json
import numpy as np
import pandas as pd
import plotly

rng = pd.date_range('1/1/2011', periods=7500, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)

graphs = [
    dict(
        data=[
            dict(
                x=[1, 2, 3],
                y=[10, 20, 30],
                type='scatter'
            ),
        ],
        layout=dict(
            title='first graph'
        )
    ),

    dict(
        data=[
            dict(
                x=[1, 3, 5],
                y=[10, 50, 30],
                type='bar'
            ),
        ],
        layout=dict(
            title='second graph'
        )
    ),

    dict(
        data=[
            dict(
                x=ts.index,  # Can use the pandas data structures directly
                y=ts
            )
        ]
    )
]

# Add "ids" to each of the graphs to pass up to the client
# for templating
ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

# Convert the figures to JSON
# PlotlyJSONEncoder appropriately converts pandas, datetime, etc
# objects to their JSON equivalents
graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from apps.view import CanvasMeta
from tools.frame import Shape


def plot_frame(data):
    fig = make_subplots(rows=3, cols=2)
    # mode = 'lines+markers'
    mode = 'lines'
    fig.add_trace(go.Scatter(x=data.frame_id, y=data.x, mode=mode, name='$x$'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=data.frame_id, y=data.y, mode=mode, name='$y$'),
                  row=1, col=2)
    fig.add_trace(go.Scatter(x=data.frame_id, y=data.v_x, mode=mode, name='$v_x$'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(x=data.frame_id, y=data.v_y, mode=mode, name='$v_x$'),
                  row=2, col=2)
    fig.add_trace(go.Scatter(x=data.frame_id, y=data.a_x, mode=mode, name='$a_x$'),
                  row=3, col=1)
    fig.add_trace(go.Scatter(x=data.frame_id, y=data.a_y, mode=mode, name='$a_x$'),
                  row=3, col=2)
    fig.update_layout(
        height=750,
        margin={'l': 10,
                'r': 50,
                't': 10,
                'b': 10},
    )
    return fig


class Canvas(CanvasMeta):
    def __init__(self):
        super().__init__()


def simulate_shape(frame_id, track_id, choice_class):
    from random import choice
    choice_origin = choice(['visual', 'fusion', 'radar'])
    choice_y = choice(range(0, 100, 1))
    choice_x = choice(range(-35, 35, 5))/10
    choice_vx = choice(range(0, 30, 5))/100
    choice_vy = choice(range(0, 100, 1))/10
    choice_ax = choice(range(0, 30, 5))/100
    choice_ay = choice(range(0, 100, 1))/10
    return Shape(frame_id, track_id, choice_origin, choice_class,
                 choice_x, choice_y,
                 choice_vx, choice_vy,
                 choice_ax, choice_ay)


def frame2pandas(frame):
    df = pd.DataFrame.from_dict(frame)
    # df.index = df['id']
    # df = df.iloc[:, 1:]
    return df

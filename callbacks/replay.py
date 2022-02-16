import datetime
import pandas as pd
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from utils.client import plot_frame, Canvas
from tools.frame import Shape

from app import app
from layouts.replay import stream

frames = []
frame_id = -1

@app.callback(
              Output('replay-frame-end', 'value'),
              Input('replay-interval-frame', 'n_intervals'),
              Input('replay-frame-start', 'value'))
def replay_frame_end(n_intervals, frame_start):
    global frame_id
    if frame_start is None or frame_start>stream.max_id or frame_start < stream.min_id or len(stream)==0 or frame_start+frame_id>stream.max_id:
        frame_id = 0
        raise PreventUpdate
    else:
        frame_id += 1
        return frame_start+frame_id


@app.callback(Output('replay-memory-frame', 'data'),
              Output('replay-memory-frames', 'data'),
              Input('replay-frame-end', 'value'))
def replay_frame(frame_end):
    if frame_end > stream.max_id or stream.max_id==0 or len(stream)==0:
        frame_end=0
        raise PreventUpdate
    else:
        global frames, frame_id
        frame = stream[frame_end]
        if isinstance(frame, str):
            raise PreventUpdate
        frame_dict = frame.to_dict('records')
        frames.extend(frame_dict)
        if len(frames) > 500:
            frames = frames[-500:]
        return frame_dict, frames[1:]

@app.callback(Output('replay-view-graph', 'figure'),
              Input('replay-memory-frame', 'data'))
def replay_view_graph_frame(frame):
    '''更新鸟瞰图'''
    if len(stream)==0:
        raise PreventUpdate
    canvas = Canvas()
    shapes = [Shape(**shape) for shape in frame]
    shapes = [canvas.to_shape(*shape.view) for shape in shapes]
    canvas.view.update_layout(shapes=shapes)
    canvas.update_base()
    return canvas.view


@app.callback(Output('replay-memory-output', 'data'),
              Input('replay-memory-frames', 'data'),
              Input('replay-memory-class', 'value'))
def replay_store_frame(frames, class_selected):
    if len(stream)==0:
        raise PreventUpdate
    df = pd.DataFrame.from_records(frames)
    if frames is None:
        raise PreventUpdate
    filtered = df[df['class_name'] == class_selected]
    return filtered.to_dict('records')


@app.callback(Output('replay-feature-graph', 'figure'),
              Input('replay-memory-output', 'data'))
def replay_on_data_set_graph(data):
    if data is None:
        raise PreventUpdate
    filtered = pd.DataFrame.from_records(data)
    return plot_frame(filtered)

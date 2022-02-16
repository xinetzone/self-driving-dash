import pandas as pd
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import callback_context

from utils.client import plot_frame, Canvas
from tools.frame import Shape

from app import app
from layouts.watch import stream


@app.callback(
    Output('frame-slider', 'value'),
    Output('frame-start', 'value'),
    Output('frame-end', 'value'),
    Input('frame-slider', 'value'),
    Input('frame-start', 'value'),
    Input('frame-end', 'value'))
def callback(slider_value, frame_start, frame_end):
    ctx = callback_context
    trigger = ctx.triggered[0]
    if value := trigger['value']:
        trigger_id = trigger["prop_id"].split(".")[0]
        if trigger_id == 'frame-slider':
            slider_value = value
        elif trigger_id == 'frame-start':
            slider_value[0] = value
        elif trigger_id == 'frame-end':
            slider_value[1] = value
        frame_start = min(slider_value)
        frame_end = max(slider_value)
        slider_value = frame_start, frame_end
    else:
        raise PreventUpdate
    return slider_value, frame_start, frame_end


@app.callback(Output('watch-view-graph', 'figure'),
              Input('frame-end', 'value'))
def replay_view_graph_frame(frame_end):
    '''更新鸟瞰图'''
    if len(stream)==0:
        raise PreventUpdate
    frame = stream[frame_end]
    canvas = Canvas()
    shapes = [Shape(**shape) for shape in frame.to_dict('records')]
    shapes = [canvas.to_shape(*shape.view) for shape in shapes]
    canvas.view.update_layout(shapes=shapes)
    canvas.update_base()
    return canvas.view


@app.callback(Output('watch-memory-output', 'data'),
              Input('frame-start', 'value'),
              Input('frame-end', 'value'),
              Input('watch-memory-class', 'value'))
def store_frame(frame_start, frame_end, class_selected):
    if frame_start == frame_end or len(stream)==0:
        raise PreventUpdate
    df = stream[frame_start:frame_end+1]
    filtered = df[df['class_name'] == class_selected]
    return filtered.to_dict('records')

@app.callback(Output('watch-feature-graph', 'figure'),
              Input('watch-memory-output', 'data'))
def on_data_set_graph(data):
    if data is None or len(stream)==0:
        raise PreventUpdate
    filtered = pd.DataFrame.from_records(data)
    return plot_frame(filtered)

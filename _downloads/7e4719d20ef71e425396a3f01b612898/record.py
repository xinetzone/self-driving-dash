import datetime
import pandas as pd
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from utils.client import plot_frame, Canvas
from tools.frame import Shape

from utils.client import frame2pandas, simulate_shape
from app import app
from layouts.record import layout_options

frames = []

@app.callback(Output('live-update-text', 'value'),
              Input('interval-frame', 'n_intervals'))
def update_metrics(frame_id):
    '''⏲计时，更新时间和帧数'''
    now = datetime.datetime.now()
    now = now.strftime('%H:%M:%S')
    return f'{now} @ {frame_id}'


@app.callback(Output('memory-frame', 'data'),
              Output('memory-frames', 'data'),
              Input('interval-frame', 'n_intervals'))
def update_frame(frame_id):
    choice_class = layout_options.class_names + ['other']
    # shapes = [simulate_shape(frame_id, k, class_name)
    #           for k, class_name in enumerate(choice_class)]
    shapes = []
    k = 0
    for _ in range(10):
        for class_name in choice_class:
            shape = simulate_shape(frame_id, k, class_name)
            shapes.append(shape)
            # print(shape)
            k += 1
    
    frame = [shape.asdict() for shape in shapes]
    frame = frame2pandas(frame)
    frame.to_hdf(layout_options.save_path, key=f'frame_{frame_id}', mode='a')
    frame_dict = frame.to_dict('records')
    global frames
    frames.extend(frame_dict)
    if len(frames) > 500:
        frames = frames[-500:]
    return frame_dict, frames[1:]


@app.callback(Output('view-graph', 'figure'),
              Input('memory-frame', 'data'))
def update_view_graph_frame(frame):
    '''更新鸟瞰图'''
    canvas = Canvas()
    shapes = [Shape(**shape) for shape in frame]
    shapes = [canvas.to_shape(*shape.view) for shape in shapes]
    canvas.view.update_layout(shapes=shapes)
    canvas.update_base()
    return canvas.view


@app.callback(Output('memory-output', 'data'),
              Input('memory-frames', 'data'),
              Input('memory-class', 'value'))
def store_frame(frames, class_selected):
    df = pd.DataFrame.from_records(frames)
    if frames == None:
        raise PreventUpdate
    filtered = df[df['class_name'] == class_selected]
    return filtered.to_dict('records')


@app.callback(Output('memory-table', 'data'),
              Input('memory-output', 'data'))
def on_data_set_table(data):
    if data is None:
        raise PreventUpdate
    return data


@app.callback(Output('feature-graph', 'figure'),
              Input('memory-output', 'data'))
def on_data_set_graph(data):
    if data is None:
        raise PreventUpdate
    filtered = pd.DataFrame.from_records(data)
    fig = plot_frame(filtered)
    return fig

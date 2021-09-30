from dash import dcc, html


def update_frame_layout(frame_slider, frame_start, frame_end, frame_run, frame_stop, stream):
    frame_section = html.Div([
        html.Div([
            dcc.RangeSlider(
                id=frame_slider,
                min=stream.min_id,
                max=stream.max_id,
                step=None,
                marks=stream.marks,
                value=[0, 0], className='w3-col m8 w3-padding'),
            html.Button('运行', id=frame_run, className='w3-button w3-aqua'),
            html.Button('终止', id=frame_stop, className='w3-button w3-aqua'), ],
            className='w3-row w3-gray'
        ),
        html.Div([html.Label('frame: ', htmlFor=frame_slider, className='w3-col m1'),
                  dcc.Input(id=frame_start, value=0,
                            min=stream.min_id,
                            max=stream.max_id,
                            type="number", className='w3-col m1'),
                  dcc.Input(id=frame_end, value=0,
                            min=stream.min_id,
                            max=stream.max_id,
                            readOnly='readonly',
                            type="number", className='w3-col m1')],
                 className='w3-row w3-pale-red')
    ])
    return frame_section

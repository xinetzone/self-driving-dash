from dash import dcc, html

from utils.nav import page_header
from utils.toml import load_option
from utils.stream import Stream
from utils.graph import create_graph
# from utils.update import update_frame_layout
# 数据
layout_options = load_option('options/replay.toml')

stream = Stream(layout_options.save_path)

frame_section = html.Div([
        html.Div([
                  dcc.Input(id='replay-frame-start', value=0,
                            min=stream.min_id,
                            max=stream.max_id,
                            type="number", className='w3-col m1'),
                  dcc.Input(id='replay-frame-end', value=0,
                            min=stream.min_id,
                            max=stream.max_id,
                            readOnly='readonly',
                            type="number", className='w3-col m1')],
                 className='w3-row w3-pale-red')
    ])

# 布局
header = page_header(title=layout_options.title)

graph = create_graph('replay-view-graph', 'replay-feature-graph',
                     'replay-memory-class', layout_options)

main = html.Main([dcc.Store(id='replay-memory-frame'),  # 存储每帧数据
                  dcc.Store(id='replay-memory-output'),  # 输出数据流
                  dcc.Store(id='replay-memory-frames'),  # 输出筛选后的数据留
                  dcc.Interval(id='replay-interval-frame',  # 用于数据更新
                 interval=200,
                 n_intervals=0),
                 graph,
                 frame_section
                  ])

layout = html.Article([header, main])

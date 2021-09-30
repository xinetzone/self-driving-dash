from dash import dcc, html

from utils.nav import page_header
from utils.toml import load_option
from utils.stream import Stream
from utils.graph import create_graph
from utils.update import update_frame_layout
# 数据
layout_options = load_option('options/watch.toml')

stream = Stream(layout_options.save_path)

frame_section = update_frame_layout('frame-slider', 'frame-start', 'frame-end', 'frame-run', 'frame-stop', stream)
# 布局
header = page_header(title=layout_options.title)

graph = create_graph('watch-view-graph', 'watch-feature-graph',
                     'watch-memory-class', layout_options)

main = html.Main([dcc.Store(id='watch-memory-frame'),  # 存储每帧数据
                  dcc.Store(id='watch-memory-output'),  # 输出数据流
                  dcc.Store(id='watch-memory-frames'),  # 输出筛选后的数据留
                  dcc.Interval(id='watch-interval-frame',  # 用于数据更新
                 interval=200,
                 n_intervals=0),
                 graph,
                 frame_section
                  ])

layout = html.Article([header, main])

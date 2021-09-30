from dash.dash_table import DataTable
from dash import dcc, html

from utils.toml import load_option
from utils.nav import page_header
from utils.graph import create_graph

layout_options = load_option('options/record.toml')


# 与硬件通信
device = html.Aside([
    html.Button('打开', id='open-devide',
                n_clicks=0,
                className='w3-pale-green w3-round-xlarge'),
    html.Button('关闭', id='close-devide',
                n_clicks=0,
                className='w3-pale-green w3-round-xlarge'), 
    dcc.Input(id='live-update-text', type='text',
              readOnly=True, className='w3-right')
], className='w3-cell-row w3-pale-blue')

graph = create_graph('view-graph', 'feature-graph',
                     'memory-class', layout_options)

header = page_header(title=layout_options.title)
main = html.Main([dcc.Store(id='memory-frame'),  # 存储每帧数据
                  dcc.Store(id='memory-output'),  # 输出数据流
                  dcc.Store(id='memory-frames'),  # 输出筛选后的数据留
                  dcc.Interval(id='interval-frame',  # 用于数据更新
                 interval=300,
                 n_intervals=0),
                  graph,
                  # 显示数据框
                  DataTable(
    id='memory-table',
    columns=[{'name': i, 'id': i} for i in layout_options.columns]
)])

layout = html.Article([header, device, main])

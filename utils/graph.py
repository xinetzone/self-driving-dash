from dash import dcc, html


def create_graph(view_graph, feature_graph, memory_class, layout_options):
    # 鸟瞰图
    left_graph = dcc.Graph(id=view_graph,
                           className='w3-container w3-cell w3-light-blue w3-col m3 l3 s3')
    # 分析图
    right_graph = html.Div([dcc.Dropdown(id=memory_class,
                                         options=[{'value': x, 'label': x}
                                                  for x in layout_options.class_names],
                                         value='ACC'),
                            dcc.Graph(id=feature_graph, className='w3-row')],
                           className='w3-col m9 l9 s9')
    return html.Article([left_graph, right_graph],
                         className='w3-row')

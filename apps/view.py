import plotly.graph_objects as go


class CanvasMeta:
    def __init__(self):
        self.x_range = [-7.5, 7.5]
        self.y_range = [-30, 210]
        self.y_scale = 270/15
        self._fig_height = 750
        self.view = go.Figure()
        self.view.update_layout(
            plot_bgcolor='lightgrey',
            paper_bgcolor='lightslategrey',
            font_color='goldenrod'
        )

    @property
    def base_shapes(self):
        center_vline = {'x': 0,
                        'line_width': 5,
                        'line_dash': 'dash',
                        'line_color': 'green',
                        'annotation_text': '中心线',
                        'annotation': {'font_size': 12, 'font_family': '宋体'},
                        'opacity': 0.25}
        vline1 = {'x': 3,
                 'line_width': 5,
                 'line_dash': 'dash',
                 'line_color': 'green',
                 'annotation_text': '3',
                 'annotation': {'font_size': 12, 'font_family': '宋体'},
                 'opacity': 0.2}
        vline2 = {'x': -3,
                 'line_width': 5,
                 'line_dash': 'dash',
                 'line_color': 'green',
                 'annotation_text': '-3',
                 'annotation': {'font_size': 12, 'font_family': '宋体'},
                 'opacity': 0.2}
        hline1 = {'y': 0,
                  'line_width': 5,
                  'line_dash': 'dash',
                  'line_color': 'red',
                  'annotation_text': '0',
                  'opacity': 0.3}
        hline2 = {'y': 60,
                  'line_width': 2,
                  'line_dash': 'dash',
                  'line_color': 'red',
                  'annotation_text': '60',
                  'opacity': 0.3}
        hline3 = {'y': 120,
                  'line_width': 2,
                  'line_dash': 'dash',
                  'line_color': 'yellow',
                  'annotation_text': '120',
                  'opacity': 0.3}
        hline4 = {'y': 180,
                  'line_width': 2,
                  'line_dash': 'dash',
                  'line_color': 'blue',
                  'annotation_text': '180',
                  'opacity': 0.3}
        # 本车
        car = {'type': 'rect',
               'xref': 'x',
               'yref': 'y',
               'x0': -0.25,
               'x1': 0.25,
               'y0': -3.5,
               'y1': 3.5,
               'fillcolor': 'blue',
               'opacity': 0.8,
               'line': {'color': 'Lightgreen', 'width': 1}}
        return {
            'center_vline': center_vline,
            'vline1': vline1,
            'vline2': vline2,
            'hline1': hline1,
            'hline2': hline2,
            'hline3': hline3,
            'hline4': hline4,
            'host_vehicle': car
        }

    def update_base(self):
        base_shapes = self.base_shapes
        self.view.add_vline(**base_shapes['center_vline'])
        self.view.add_vline(**base_shapes['vline1'])
        self.view.add_vline(**base_shapes['vline2'])
        self.view.add_hline(**base_shapes['hline1'])
        self.view.add_hline(**base_shapes['hline2'])
        self.view.add_hline(**base_shapes['hline3'])
        self.view.add_hline(**base_shapes['hline4'])
        self.view.add_shape(**base_shapes['host_vehicle'])
        self.view.update_xaxes(range=self.x_range,
                               showline=True,
                               linewidth=2,
                               linecolor='grey',
                               mirror=True
                               )

        self.view.update_yaxes(range=self.y_range,
                               showline=True,
                               linewidth=2,
                               linecolor='grey',
                               mirror=True
                               )
        self.view.update_layout(
            margin={'l': 20, 'r': 20, 't': 20, 'b': 10},
            height=self._fig_height,
        )

    def to_bbox(self, x, y, w, h):
        return {
            'x0': x-w,
            'x1': x+w,
            'y0': y-h,
            'y1': y+h
        }

    def to_obj(self, _type, x, y, w, h,
               fillcolor, opacity,
               line_color='LightSeaGreen'):
        '''视觉目标'''
        obj = ({
            'type': _type,
            'xref': "x", 'yref': "y",
            **self.to_bbox(x, y, w, h),
            'fillcolor': fillcolor,
            'opacity': opacity,
            'line': {
                'color': line_color,
                'width': 2,

            }
        })
        return obj

    def to_visual_obj(self, x, y):
        '''视觉目标'''
        return self.to_obj('circle', x, y, 0.27, 2.8, 'orange', 0.8, 'grey')

    def to_radar_obj(self, x, y):
        '''视觉目标'''
        return self.to_obj('rect', x, y, 0.3, 3, 'white', 0.4, 'black')

    def to_fusion_obj(self, x, y):
        '''融合目标'''
        obj = self.to_obj('rect', x, y, 0.36, 3.8, 'yellow', 0.4, 'red')
        return obj

    def to_shape(self, _type, x, y):
        if _type == 'visual':
            obj = self.to_visual_obj(x, y)
        elif _type == 'radar':
            obj = self.to_radar_obj(x, y)
        elif _type == 'fusion':
            obj = self.to_fusion_obj(x, y)
        else:
            obj = {}
        return obj

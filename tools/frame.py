from dataclasses import dataclass, asdict


@dataclass
class Shape:
    frame_id: int # 帧号
    track_id: int
    origin: str  # 目标物来源，取值 'visual', 'radar', 'fusion'
    class_name: str  # ACC主目标，AEB主目标，CIPV目标，MCP目标，other
    x: float  # 横向距离
    y: float  # 纵向距离
    v_x: float  # 横向速度
    v_y: float  # 纵向速度
    a_x: float  # 横向加速度
    a_y: float  # 纵向加速度

    def __repr__(self):
        return (
            f'{self.origin.capitalize()}'
            f'(track_id={self.track_id}, class_name={self.class_name}, x={self.x}, y={self.y},'
            f'v_x={self.v_x}, v_y={self.v_y}, '
            f'a_x={self.a_x}, a_y={self.a_y})'
        )

    @property
    def view(self):
        return self.origin, self.x, self.y

    @property
    def prop(self):
        return {'x': self.x,
             'y': self.y,
             'v_x': self.v_x,
             'v_y': self.v_y,
             'a_x': self.a_x,
             'a_y': self.a_y}

    def asdict(self):
        return asdict(self)


class Frame:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def bunch(self):
        _bunch = {}
        for shape in self.shapes:
            class_name = shape.class_name
            _bunch.setdefault(class_name, []).append(shape)
        return _bunch

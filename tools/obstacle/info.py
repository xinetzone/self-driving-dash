from enum import IntEnum, IntFlag, Enum, Flag


class Valid:
    def __bool__(self):
        return bool(self.value)

    def describe(self):
        # self is the member here
        return self.name, self.value


class ObstacleValid(Valid, Flag):
    '''障碍物有效性'''
    INVALID = 0  # 默认值
    NEW_VALID = 1
    OLDER_VALID = 2


class ObstacleMotionCategory(Valid, Enum):
    '''障碍物运动状态分类

    该信号基于对目标现在相对于车道的位置的估计，其变化率以及对目标在一秒内的位置的估计
    '''
    INVALID = 0
    UNDEFINED = 1  # 模糊不清，不能准确识别
    PASSING = 2  # 自车左右相邻车道车辆同向经过，相对位置基本保持不变
    PASSING_IN = 3  # 自车左右相邻车道车辆同向经过，自车被超车
    PASSING_OUT = 4  # 自车左右相邻车道车辆同向经过，自车超车
    CLOSE_CUT_IN = 5  # 自车左右相邻车道车辆将要切入车道或者靠近
    MOVING_IN = 6  # 从左右相邻车道进入自车道
    MOVING_OUT = 7  # 从自车道移出
    CROSSING = 8  # 横向穿越车道或者与本车呈一定角度（非ONCOMING和非PRECEEDING的角度）
    LTAP = 9  # 十字路口对向车道左拐（ONCOMING -> LTAP），对向调头（ONCOMING -> CROSSING）
    RTAP = 10  # Right Rurn Across Path 十字路口右侧车辆左拐
    MOVING = 11
    PRECEEDING = 12  # 同向直行的车辆
    ONCOMING = 13  # 迎面驶来的车辆


class ObstacleMotionStatus(Valid, Enum):
    '''障碍物运动状态(Range:[0, 7])

    目标正在移动或停止
    '''
    INVALID = 0
    UNKNOWN = 1  # 如遮挡后出现的，杠开始几帧的状态
    MOVING = 2  # 相对地面运动的车辆
    STATIONARY = 3  # 在视野范围内没有相对地面运动的
    STOPPED = 4  # 在视野范围内曾经运动，当前静止的状态
    MOVING_SLOWLY = 5  # 缓慢移动的状态，是 STOPPED 和 MOVING 之间的状态


class ObstacleMeasuringStatus(Valid, Enum):
    '''障碍物观测状态(Range:[0, 7])

    测量值是预测的，旧的还是无效的
    '''
    INVALID = 0
    MEASURED = 1  # 测量值
    PREDICTED = 2  # 预测值


class ObstacleClass(Valid, Enum):
    '''障碍物类型(Range:[0, 7])

    目标种类
    '''
    INVALID = 0
    VEHICLE = 1  # 车辆
    PEDESTRIAN = 2  # 行人
    CYCLIST = 3  # 自行车
    GENERAL_OBJECT = 4  # 一般目标物


class VehicleSubType(Valid, Enum):
    '''车辆子类型
    '''
    UNKNOWN = 0
    BUS = 1  # 公共汽车
    SMALL_MIDDLE_CAR = 2  # 中小型车
    TRUCKS = 3  # 卡车
    MOTORS = 4  # Tri-cycle，摩托车，三轮车
    SPECIAL_VEHICLE = 5  # 特种车
    TINY_CAR = 6  # 微型车
    LORRY = 7  # 货车


class PedSubType(Valid, Enum):
    '''行人子类型
    '''
    UNKNOWN = 0
    ADULT = 1  # 成人
    CHILD = 2  # 儿童


class PedPos(Valid, Enum):
    '''行人姿态
    '''
    UNKNOWN = 0
    BENDED = 1  # 弯腰
    CYCLIST_POS = 2  # 骑车
    LIER = 3  # 躺卧
    PEDESTRIAN_POS = 4  # 正常状态
    SITTER = 5  # 坐着


class CIPVFlag(Valid, Flag):
    '''最危险目标物标志'''
    NOT_CIPV = 0
    CIPV = 1


class MCPFlag(Valid, Flag):
    '''?标志'''
    NOT_MCP = 0
    MCP = 1


class ObstacleReplaced(Valid, Flag):
    '''障碍物更换(暂不存在该类)'''
    reserved = 1
    not_reserved = 0


class PedOrientation(Valid, Enum):
    '''行人相对本方向
    '''
    UNKNOWN = 0
    BACK = 1
    FRONT = 2
    LEFT = 3
    LEFT_ANTERIOR = 4  # 左前
    LEFT_BACK = 5  # 左后
    RIGHT = 6
    RIGHT_FRONT = 7  # 右前
    BACK_FRONT = 8


class ObstacleLaneAssignment(Valid, Enum):
    '''障碍物所属车道
    '''
    UNKNOWN = 0
    LEFT_LEFT = 1  # 左左车道
    LEFT = 2  # 左车道
    HOST = 3  # 当前车道
    RIGHT = 4
    RIGHT_RIGHT = 5


class ObstacleBlinkerInfo(Valid, Enum):
    '''车辆转向灯状态
    '''
    UNAVAILABLE = 0
    OFF = 1
    LEFT = 2
    RIGHT = 3
    BOTH = 4


class ObstacleBrakeLights(Flag):
    '''障碍物刹车灯
    '''
    OFF = 0
    ON = 1

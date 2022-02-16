from dataclasses import dataclass
from random import choice

from .info import *


def shuffle_choice(enum_class):
    _class = choice(list(enum_class))
    return _class.value # _class.name, _class.value


@dataclass
class ObstacleInfo:
    obstacle_ID: int = choice(range(256))  # 障碍物ID [0, 255]

    obstacle_length: float = choice(range(256))/10.  # 目标物长度，单位：m [0, 25.6]
    obstacle_width: float = choice(range(1024))/100.  # 宽度，单位：m [0, 10.24]
    obstacle_height: float = choice(range(1024))/100.  # 高度，单位：m [0, 10.24]
    obstacle_PosX: float = choice(
        range(-250, 250))/1.  # 目标物纵向距离，单位 m [-250, 250]
    obstacle_PosY: float = choice(
        range(-250, 250))/1.  # 目标物横向距离，单位 m [-250, 250]
    obstacle_VelX: float = choice(
        range(-10240, 10235))/100.  # 相对纵向速度，单位 m/s [-102.4, 102.35]
    obstacle_VelY: float = choice(
        range(-50, 50))/1.  # 相对横向速度，单位 m/s  [-50, 50]
    obstacle_AccX: float = choice(
        range(-1497, 1497))/100.  # 相对纵向加速度，单位 m/s^2 [-14.97, 14.97]
    obstacle_AccY: float = choice(
        range(-1497, 1497))/100.  # 横向相对加速度，单位 m/s^2 [-14.97, 14.97]
    obstacle_VelXAbs: float = choice(
        range(-10240, 10235))/100.  # 障碍物绝对纵向速度，单位 m/s^2 [-102.4, 102.35]
    obstacle_VelYAbs: float = choice(
        range(-50, 50))/1.  # 障碍物绝对横向速度，单位 m/s^2 [-50, 50]
    obstacle_angle: float = choice(
        range(-32768, 32767))/100.  # 障碍物航向角，单位弧度 [-327.68, 327.67]
    obstacle_center_angle: float = choice(
        range(-32768, 32767))/100.  # 障碍物中心角度，单位弧度 [-327.68, 327.67]
    obstacle__ttc: float = choice(range(10))/1.  # TTC 碰撞时间，单位 s [0, 10]

    obstacle_confidence: int = choice(range(100))  # 障碍物置信度[0, 100]
    obstacle_age: int = choice(range(65535))  # 障碍物生命帧数,[0,65535]

    obstacle_valid: int = shuffle_choice(
        ObstacleValid)  # 障碍物有效性，0为无效，1为新目标，2为老目标
    obstacle_replaced: int = shuffle_choice(
        ObstacleReplaced)  # 障碍物更换（Reserved）
    obstacle_motion_category: int = shuffle_choice(
        ObstacleMotionCategory)  # 障碍物运动状态分类，[0,13],具体定义见 motion_category_e
    obstacle_motion_status: int = shuffle_choice(
        ObstacleMotionStatus)   # 障碍物运动状态，[0,7]，具体定义见motion_status_e
    obstacle_measuring_status: int = shuffle_choice(
        ObstacleMeasuringStatus)  # 障碍物观测状态，1为测量，2为预测
    obstacle_class: int = shuffle_choice(
        ObstacleClass)  # 障碍物类型,具体定义见obstacle_class_t
    vehicle_subtype: int = shuffle_choice(
        VehicleSubType)  # 车辆类型，具体定义见vehicle_subtype_t
    ped_subtype: int = shuffle_choice(PedSubType)  # 行人类型，具体定义见ped_subtype_t
    ped_pos: int = shuffle_choice(PedPos)  # 行人姿态，具体定义见ped_pos_t
    # 行人相对本方向位置，具体定义见ped_orientation_t;
    ped_orientation: int = shuffle_choice(PedOrientation)
    obstacle_lane_assignment: int = shuffle_choice(
        ObstacleLaneAssignment)  # 障碍物所属车道，具体定义见obstacle_lane_assign_t
    # 最危险车辆目标物标志，closest in path vehicle
    CIPV_flag:  int = shuffle_choice(CIPVFlag)
    MCP_flag:  int = shuffle_choice(MCPFlag)  # 最危险行人标志, most closet pedestrian
    obstacle_blinker_info: int = shuffle_choice(ObstacleBlinkerInfo)  # 车辆转向灯信息
    obstacle_brake_lights: int = shuffle_choice(ObstacleBrakeLights)  # 车辆刹车灯信息

    # 这里的信息不重要
    # obstacle_PosXSTD: float = choice(range(0, 250))/1.  # 纵向距离的标准偏差 [0 ,250]
    # obstacle_PosYSTD: float = choice(range(0, 250))/1.  # 横向距离的标准偏差 [0 ,250]
    # obstacle_VelXSTD: float = choice(range(0, 10235))/100.  # 纵向速度的标准偏差 [0, 102.35]
    # obstacle_VelYSTD: float = choice(range(0, 50))/1.  # 横向速度的标准偏差 [0, 50]
    # obstacle_angle_std: float = choice(range(0, 32767))/100.  # 障碍物航向角标准差 [0, 327.67]


def obstacle_simulate():
    return {
        'obstacle_ID': choice(range(255)),  # 障碍物ID [0, 255]
        'obstacle_length': choice(range(256))/10.,  # 目标物长度，单位：m [0, 25.6]
        'obstacle_width': choice(range(1024))/100.,  # 宽度，单位：m [0, 10.24]
        'obstacle_height': choice(range(1024))/100.,  # 高度，单位：m [0, 10.24]
        'obstacle_PosX': choice(
            range(-250, 250))/1.,  # 目标物纵向距离，单位 m [-250, 250]
        'obstacle_PosY': choice(
            range(-250, 250))/1.,  # 目标物横向距离，单位 m [-250, 250]
        'obstacle_VelX': choice(
            range(-10240, 10235))/100.,  # 相对纵向速度，单位 m/s [-102.4, 102.35]
        'obstacle_VelY': choice(
            range(-50, 50))/1.,  # 相对横向速度，单位 m/s  [-50, 50]
        'obstacle_AccX': choice(
            range(-1497, 1497))/100.,  # 相对纵向加速度，单位 m/s^2 [-14.97, 14.97]
        'obstacle_AccY': choice(
            range(-1497, 1497))/100.,  # 横向相对加速度，单位 m/s^2 [-14.97, 14.97]
        'obstacle_VelXAbs': choice(
            range(-10240, 10235))/100.,  # 障碍物绝对纵向速度，单位 m/s^2 [-102.4, 102.35]
        'obstacle_VelYAbs': choice(
            range(-50, 50))/1.,  # 障碍物绝对横向速度，单位 m/s^2 [-50, 50]
        'obstacle_angle': choice(
            range(-32768, 32767))/100.,  # 障碍物航向角，单位弧度 [-327.68, 327.67]
        'obstacle_center_angle': choice(
            range(-32768, 32767))/100.,  # 障碍物中心角度，单位弧度 [-327.68, 327.67]
        'obstacle__ttc': choice(range(10))/1.,  # TTC 碰撞时间，单位 s [0, 10]
        'obstacle_confidence': choice(range(100)),  # 障碍物置信度[0, 100]
        'obstacle_age': choice(range(65535)),  # 障碍物生命帧数,[0,65535]
        'obstacle_valid': shuffle_choice(
            ObstacleValid),  # 障碍物有效性，0为无效，1为新目标，2为老目标
        'obstacle_replaced': shuffle_choice(
            ObstacleReplaced),  # 障碍物更换（Reserved）
        'obstacle_motion_category': shuffle_choice(
            ObstacleMotionCategory),  # 障碍物运动状态分类，[0,13],具体定义见 motion_category_e
        'obstacle_motion_status': shuffle_choice(
            ObstacleMotionStatus),   # 障碍物运动状态，[0,7]，具体定义见motion_status_e
        'obstacle_measuring_status': shuffle_choice(
            ObstacleMeasuringStatus),  # 障碍物观测状态，1为测量，2为预测
        'obstacle_class': shuffle_choice(
            ObstacleClass),  # 障碍物类型,具体定义见obstacle_class_t
        'vehicle_subtype': shuffle_choice(
            VehicleSubType),  # 车辆类型，具体定义见vehicle_subtype_t
        'ped_subtype': shuffle_choice(PedSubType),  # 行人类型，具体定义见ped_subtype_t
        'ped_pos': shuffle_choice(PedPos),  # 行人姿态，具体定义见ped_pos_t
        # 行人相对本方向位置，具体定义见ped_orientation_t;
        'ped_orientation': shuffle_choice(PedOrientation),
        'obstacle_lane_assignment': shuffle_choice(
            ObstacleLaneAssignment),  # 障碍物所属车道，具体定义见obstacle_lane_assign_t
        # 最危险车辆目标物标志，closest in path vehicle
        'CIPV_flag': shuffle_choice(CIPVFlag),
        'MCP_flag': shuffle_choice(MCPFlag),  # 最危险行人标志, most closet pedestrian
        # 车辆转向灯信息
        'obstacle_blinker_info': shuffle_choice(ObstacleBlinkerInfo),
        'obstacle_brake_lights': shuffle_choice(ObstacleBrakeLights)  # 车辆刹车灯信息
    }
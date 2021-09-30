#encoding: utf-8
from dataclasses import dataclass


@dataclass
class ObstacleInfo:
    obstacle_ID: int # 障碍物ID
    obstacle_valid: int  # 障碍物有效性，0为无效，1为新目标，2为老目标
    obstacle_replaced: int        # 障碍物更换（Reserved）
    obstacle_confidence: int     # 障碍物置信度[0, 100]
    obstacle_motion_category: int   # 障碍物运动状态分类，[0,13],具体定义见 motion_category_e
    obstacle_motion_status: int    # 障碍物运动状态，[0,7]，具体定义见motion_status_e
    obstacle_measuring_status: int  # 障碍物观测状态，1为测量，2为预测
    obstacle_class: int           # 障碍物类型,具体定义见obstacle_class_t
    vehicle_subtype: int           # 车辆类型，具体定义见vehicle_subtype_t
    ped_subtype:  int              # 行人类型，具体定义见ped_subtype_t
    ped_pos: int                   # 行人姿态，具体定义见ped_pos_t
    ped_orientation: int       # 行人相对本方向位置，具体定义见ped_orientation_t;
    obstacle_lane_assignment: int  # 障碍物所属车道，具体定义见obstacle_lane_assign_t
    obstacle_age: int              # 障碍物生命帧数,[0,65535]
    CIPV_flag:  int                # 最危险车辆目标物标志，closest in path vehicle
    MCP_flag:    int               # 最危险行人标志, most closet pedestrian
    obstacle_blinker_info: int     # 车辆转向灯信息
    obstacle_brake_lights: int     # 车辆刹车灯信息
    obstacle_center_angle:  float      # 障碍物中心角度
    obstacle_length:    float           # 目标物长度，单位：m
    obstacle_width:   float             # 宽度
    obstacle_height:  float             # 高度
    obstacle_PosX:    float             # 目标物纵向距离，单位m
    obstacle_PosY:    float             # 目标物横向距离，单位m
    obstacle_VelX:    float             # 相对纵向速度，单位m/s
    obstacle_VelY:    float             # 相对横向速度，单位m/s
    obstacle_AccX:   float              # 相对纵向加速度，单位m/s^2
    obstacle_PosXSTD:   float           # 纵向距离的标准偏差
    obstacle_PosYSTD:   float           # 横向距离的标准偏差
    obstacle_VelXSTD:   float           # 纵向速度的标准偏差
    obstacle_VelYSTD:   float           # 横向速度的标准偏差
    obstacle_AccY:    float             # 横向相对加速度
    obstacle_angle:   float             # 障碍物航向角
    obstacle_angle_std:  float           # 障碍物航向角标准差
    obstacle_VelXAbs:   float           # 障碍物绝对纵向速度
    obstacle_VelYAbs:  float            # 障碍物绝对横向速度
    obstacle__ttc:   float              # TTC碰撞时间
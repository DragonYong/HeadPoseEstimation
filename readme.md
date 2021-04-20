### 基于OPENCV对人脸检测的实现（Head pose estimation）

===========================
#### 00-项目信息
```
作者：TuringEmmy
时间:2021-04-21 14:19:25
详情：使用res10对人脸进行检测
```
#### 01-环境依赖
```
ubuntu:18.04
python:3.7
tensorflow:2.4
opencv:4.5.1
h5py:3.1
```
#### 02-部署步骤
在线与本地两种检测方案
```
sh scripts/local.sh  
sh scripts/line.sh
```

#### 03-目录结构描述
```
.
├── estimate_head_pose.py
├── mark_detector.py
├── optical_flow_tracker.py
├── os_detector.py
├── pose_estimator.py
├── __pycache__
│   ├── mark_detector.cpython-36.pyc
│   ├── mark_detector.cpython-37.pyc
│   ├── os_detector.cpython-36.pyc
│   ├── os_detector.cpython-37.pyc
│   ├── pose_estimator.cpython-36.pyc
│   ├── pose_estimator.cpython-37.pyc
│   ├── stabilizer.cpython-36.pyc
│   └── stabilizer.cpython-37.pyc
├── readme.md
├── requirements.txt
├── scripts
│   ├── local.sh
│   └── online.sh
└── stabilizer.py
```


#### 04-版本更新
##### V1.0.0 版本内容更新-2021-04-21 14:54:13
- 模型是训练好的

#### 05-TUDO
- 整理相关人头位置检测的模型
- 考虑如何服务器段部署

- 300-W: https://ibug.doc.ic.ac.uk/resources/300-W/
- 300-VW: https://ibug.doc.ic.ac.uk/resources/300-VW/
- LFPW: https://neerajkumar.org/databases/lfpw/
- HELEN: http://www.ifp.illinois.edu/~vuongle2/helen/
- AFW: https://www.ics.uci.edu/~xzhu/face/
- IBUG: https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/
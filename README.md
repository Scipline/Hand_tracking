## 项目介绍

对[htamd](https://pypi.org/project/htamd/)库的简单运用，主要就是对cv,matplotlib环境的搭建学习理解。项目暂时无任何应用场景。

### htamd official description：

HT (AMD Intel System) 

A package that allows to track the x, y, z locations of specific points from 0-20 in your hands. (AMD Intel System)

- Tracks your hand
- The hand connections or lines can be show or hidden
- Works for almost all computers
- Quick and not much lag
- Simple code that is easy to understand and customize if needed

### htamd官方描述:

HT (AMD英特尔系统)

一个包，允许跟踪x, y, z位置的特定点从0-20在你的手中。(AMD英特尔系统)

- 追踪你的手
- 手的连接或线可以显示或隐藏
- 适用于几乎所有计算机
- 速度快，没有太多延迟
- 简单的代码，易于理解和定制，如果需要

## 安装依赖

### 在线安装

`pip install -r requirements.txt`

```bash
htamd==0.2
opencv-python==4.7.0.68
opencv-contrib-python==4.7.0.68
opencv-python-headless==4.6.0.66
kiwisolver==1.4.4
```

### 离线包

在[release](https://github.com/Scipline/Hand_tracking/releases/tag/0.0.1)中的**Library.zip**，已打包好本项目所需要的运行环境，解压到本项目同一目录下即可。

## R＆M

1. pycharm找不到cv2中比如imshow,imread,VideooCapture等方法找不到标黄下划线

![Snipaste_2023-01-11_17-13-24](https://i2.100024.xyz/2023/01/11/scnhfw.webp)
![Snipaste_2023-01-11_17-13-45](https://i2.100024.xyz/2023/01/11/scnh17.webp)
![Snipaste_2023-01-11_17-13-58](https://i2.100024.xyz/2023/01/11/scnnf3.webp)

2. cv2启动摄像头缓慢卡顿

   `cap = cv2.VideoCapture(0)`添加一个启动参数`cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)`

   

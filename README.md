Using RTAB-Map package for 3D SLAM with robot Pepper. RTAB-Map can be installed via sudo apt:
```bash
sudo apt install ros-melodic-rtabmap-ros
```
or by hand [rtabmap_ros](http://wiki.ros.org/rtabmap_ros).

To use package on a real robot, [pepper_ros_stack](https://github.com/larics/pepper-ros-stack) needs to be built and for connecting to robot pepper_full_py.launch needs to be launched:
```bash
roslaunch pepper_bringup pepper_full_py.launch nao_ip:=<robot_ip> roscore_ip:=<roscore_ip>
```

For starting RTAB-Map real_robot_rtabmap.launch needs to be launched:
```bash
roslaunch pepper_robot_rtabmap real_robot_rtabmap.launch
```

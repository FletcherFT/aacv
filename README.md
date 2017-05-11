# rc_aacv ROS package
## Install Instructions

Built for [Ubuntu 14.04 Trusty Tahr LTS](http://releases.ubuntu.com/14.04/).
Install [ROS Indigo](http://wiki.ros.org/indigo/Installation/Ubuntu)

Make sure these ROS packages are installed:
```
sudo apt-get install ros-indigo-joystick-drivers
sudo apt-get install ros-indigo-sensor-msgs
sudo apt-get install ros-indigo-rosserial-arduino
sudo apt-get install ros-indigo-rosserial
```

Clone this repo into the package location for your ROS workspace and build the packages.
```
git clone https://github.com/FletcherFT/rc_aacv.git
cd ../..
catkin_make
```

Connect laptop up to wifi network, boot up aacv and check that you can ping the beaglebone black
```
ping aacv-bbb.local
```

Connect joystick to laptop, wait 30s then execute:
```
roscd rc_aacv/launch
. test.sh
```

All nodes should then launch, you should be able to remotely control Blue!

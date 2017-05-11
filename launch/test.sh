export ROS_HOSTNAME=$HOSTNAME.local
export ROS_MASTER_URI=http://$HOSTNAME.local:11311
export ROSLAUNCH_SSH_UNKNOWN=1
roslaunch rc_aacv remote_aacv.launch

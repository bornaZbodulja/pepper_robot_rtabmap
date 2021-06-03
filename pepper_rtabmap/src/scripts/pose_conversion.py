#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Header

class Odometry_Converter():
    
    def __init__(self):
        
        self.pub = rospy.Publisher('combined_odometry', Odometry, queue_size=1)
        self.odom_converted = Odometry()
        rospy.Subscriber('ekf_odom_combined', PoseWithCovarianceStamped, self.pose_covarience_callback)
        
    def pose_covarience_callback(self, data):
        
        self.odom_converted.header = data.header
	self.odom_converted.header.frame_id = "pepper_robot/odom_combined"
        self.odom_converted.pose = data.pose
        self.odom_converted.child_frame_id = "pepper_robot/base_link"
        
        if not rospy.is_shutdown(): 
            self.pub.publish(self.odom_converted)
        
if __name__ == "__main__":
    
    # odom_combined_topic = '/pose_ekf/robot_pose_ekf/odom_combined'
    # odom_combined_topic = '/robot_pose_ekf/odom_combined'
    # converted_odom_topic = '/combined_odometry'
    
    try:
	rospy.init_node('pose_conversion')
        odometry_Converter = Odometry_Converter()
        rospy.spin()
        
    except rospy.ROSInterruptException: pass

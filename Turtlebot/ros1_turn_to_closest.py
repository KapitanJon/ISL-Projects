import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import os

#closest_object_node
class find_closest_node():
    #init node with sub and publisher
    def __init__(self):
        self.sub = rospy.Subscriber('scan',LaserScan, self.callback)
        self.shortest_pub = rospy.Publisher('/shortest_distance', String, queue_size=10)
        self.movement_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    
    def callback(self, msg: LaserScan, move_cmd = Twist()):
        output = String()
        min = 3.5
        for val in msg.ranges:
            if val <= min and val != 0.0 and val != 'inf':
                min = val
        output.data = str(min)
        self.shortest_pub.publish(output)
        print(f'min distance {min}')
        print(f'current distance {msg.ranges[0] - 0.07}')
        if msg.ranges[0]-.04 > min or msg.ranges[0] == 0.0:
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.3
            print('move bot')
            self.movement_pub.publish(move_cmd)
        else:
            move_cmd = Twist()
            self.movement_pub.publish(move_cmd)
            print("object found")
            print('killing node')
            os.system('rosnode kill find_closest_object')
            #self.destroy_node()

def main():
    rospy.init_node('find_closest_object')
    find_closest_node()
    rospy.spin()


if __name__ == "__main__":
    main()
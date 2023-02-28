import rospy
from ros1_turn_to_closest import find_closest_node


def main():
    #run first node to turn towards nearest object
    print('Attempting to move towards nearest object')
    rospy.init_node('find_closest_object')
    find_closest_node()
    rospy.spin()
    #need to create node for taking photo with cv bridge



if __name__ == "__main__":
    main()
#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_srvs.srv import SetBool, SetBoolResponse

i = 0
j = 0


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(0.5) # 10hz
    global j
    while not rospy.is_shutdown():
        hello_str = "hello world %d" % j
        #rospy.loginfo(hello_str)
        j += 1
        pub.publish(hello_str)
        rate.sleep()


def srv_cb(req):
    print "Returning ", (req)
    global i
    i += 1
    return SetBoolResponse(success=True, message='This is the %d time I was called' % i)


def srv_server():
    s = rospy.Service('test_service', SetBool, srv_cb)
    print "Ready to add two ints."
    #rospy.spin()


if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    try:
        srv_server()
        talker()
    except rospy.ROSInterruptException:
        pass
import rospy
import time
from clever import srv
from std_srvs.srv import Trigger

rospy.init_node('foo')

navigate = rospy.ServiceProxy('navigate', srv.Navigate)
land = rospy.ServiceProxy('land', Trigger)

navigate(x=0, y=0, z=1.3, speed=0.3, yaw=float('nan'), frame_id='fcu_horiz', update_frame = False, auto_arm=True)
time.sleep(5)
navigate(x=8, y=3, z=1.5, speed=0.5, yaw=float('nan'), frame_id='aruco_map', update_frame = True, auto_arm=False)
time.sleep(10)
navigate(x=8, y=4, z=2.1, speed=0.5, yaw=float('nan'), frame_id='aruco_map', update_frame = True, auto_arm=False)
time.sleep(10)
land()

def robot_at(msg, params): 
    ret_value = []
    attributes = get_kb_attribute("robot_at")
    #print params, attributes
    curr_wp = ''
    # Find current robot_location
    for a in attributes:
        if not a.is_negative:
            curr_wp = a.values[1].value
            break
    print "Current location is:", curr_wp
    new_wp = int(msg.data.split(' ')[-1])%len(params[1])

    for robot in params[0]:
        distance = float('inf')
        closest_wp = ''
        ret_value.append((robot + ':' + curr_wp, False)) # Set current waypoint to false
        ret_value.append((robot + ':' + params[1][new_wp], True))  # Set new wp to true
        print 'Setting wp to ', params[1][new_wp]
    return ret_value

#from std_srvs.srv import SetBoolRequest
def req_docked():
    return SetBoolRequest(data=False)

def docked(res, params):  # params is a list with all the parameters - fully instantiated for services!
    print params
    return int(res.message.split(' ')[3])%2 == 0

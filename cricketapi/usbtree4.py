import sys

if sys.platform == "win32":
    import wmi

def scan_usbandusb4():
    
    c = wmi.WMI()
    wql = "Select * From Win32_USBControllerDevice"
    count = 0
    usbdlist = []
    parlist = []
    for item in c.query(wql):
        
        devid = item.Dependent.DeviceID
        # devclass = item.Dependent.Name.upper()

        dlist = devid.split('\\')
        if(dlist[0] == "USB" or dlist[0] == "USB4"):
            usbdlist.append("".join(devid.rstrip().lstrip()))
            for i in usbdlist:
                vid_index = i.find("VID_")
                pid_index = i.find("PID_")

                # Extract the values after "VID_" and "PID_"
                vid_value = i[vid_index + 4 : vid_index + 8]
                pid_value = i[pid_index + 4 : pid_index + 8]
                # print(vid_value, pid_value)

                vpid = "vid = " + str(vid_value) + "; pid = " + str(pid_value) 
                # print(vpid)
    return usbdlist
    
def get_tree_change(masterlist, presentlist):
    added = []
    removed = []
    if len(masterlist) == 0:
        added = presentlist
        removed = []
    else:
        tempmlist = []
        for item in masterlist:
            tempmlist.append(item)
        for dev in presentlist:
            if dev not in tempmlist:
                added.append(dev)
            else:
                tempmlist.remove(dev)
        tempplist = []
        for item in presentlist:
            tempplist.append(item)
        for dev in masterlist:
            if dev not in tempplist:
                removed.append(dev)
            else:
                tempplist.remove(dev)
    return added, removed
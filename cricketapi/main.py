from  searchswitch import get_switches
from switch3141 import Switch3141
from switch import Switch
import time
# import usbtreeview
import sys
import usbtree4
import copy
import re

print("main Started")
arglist = sys.argv
model = arglist[1]
vvid = int(arglist[2], 16)  # Parse hexadecimal VID value
vid = hex(vvid)[2:].zfill(4).upper()
print(vid)
ppid = int(arglist[3], 16)  # Parse hexadecimal PID value
pid = hex(ppid)[2:].zfill(4).upper()
print(pid)
delay = int(int(arglist[4], 16) / 1000)  # Parse hexadecimal delay value and divide by 1000
repeat = int(arglist[5])

cport = None

scount = 0
fcount = 0

gs = get_switches() # Getting the list of COM list


switches = gs["switches"]

for x in range(0, len(switches)):
    if switches[x]["model"] == model:
        cport = switches[x]["port"]

sw1 = Switch3141(cport)  # Selecting Switch 3142
sw1.connect()            # Switch open (Connect)

sw1.port_off()           # Switch 3141 port off
time.sleep(1)            # delay for 1 Second
mlist = usbtree4.scan_usbandusb4()

for iter in range(0, repeat):
   
    sw1.port_on(2)  # Here port 2 ON  
                   # sw1.port_on(1)  # Here port 1 ON
    time.sleep(delay)
    clist = usbtree4.scan_usbandusb4()
    added = usbtree4.get_tree_change(mlist, clist)[0]
    if added:
        pattern = r'USB\\VID_(\w+)&PID_(\w+)'
        dvid, dpid = re.findall(pattern, added[0])[0]
        deinfo = "(Count = " + str(iter+1) + "; vid = " + str(dvid) + "; pid = " + str(dpid) + ")"
        print(deinfo)
        print("Programme is Running....:")
        if dvid == vid and dpid == pid:
            scount += 1  # Success Couting
            vpid = "(Pass = " + str(scount) + "; Fail = " + str(fcount) + ")"
            print("Programe Sequence:",vpid)
            print("\n")
        else:
            print("VID and PID Not Match, Please enter Valid VID and PID:")
            break
    else:
        fcount += 1 # Failure Counting
        if fcount == 1:
            vpid = "(Pass = " + str(scount) + "; Fail = " + str(fcount) + ")"
            print("Programe Is Terminated VID and PID is Incorrect:",vpid)
            break

    mlist = copy.deepcopy(clist)

    sw1.port_off()    # Switch3141 port off
    time.sleep(1)
    clist = usbtree4.scan_usbandusb4()
    rmd = usbtree4.get_tree_change(mlist, clist)[1]
    mlist = copy.deepcopy(clist)
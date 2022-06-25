#!D:\Coding\Pyhton Programs\Simple Port Scanner (project2)
import pyfiglet, sys, socket, time, threading#, queue
from datetime import datetime
#Add Banner
print(pyfiglet.figlet_format("PORT SCANNER"))
print(" "*56,"By Abdul Ahad")
print("-"*70)
print("Syntax : python3 PortScanner.py <Target_ip> <Start_port> <End_port>")
#Adding the Target
if len(sys.argv) == 4:
    #Add the Target IP
    target=socket.gethostbyname(sys.argv[1])
else:
    print("Invalid arguments you passed!!")
    sys.exit()
print("Scanning Target: "+target)
print("Scanning Started at: "+ str(datetime.now()))
#q=queue()

#if len(sys.argv) < 2:
 #   sys.argv[2]=0
#else:
start_port=int(sys.argv[2])
#if len(sys.argv) < 3:
 #   sys.argv[3]=65534
#else:
end_port=int(sys.argv[3])

start_time=time.time()
def scan_port(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    conn_result=s.connect_ex((target,port))
    if not conn_result:
        print("Port {} is open.".format(port))
    s.close()
#q=queue.Queue()
try:
    for port in range(start_port,end_port+1):
        thread = threading.Thread(target=scan_port,args=(port,))
        thread.daemon=True
        #q.get(thread)
        thread.start()
except KeyboardInterrupt:
    print("\n Exiting Program")
    sys.exit()
except socket.gaierror:
    print("\n Hostname could not Resolved")
    sys.exit()
except socket.error:
    print("\n !!!!!! Server not responding !!!!!!")
    sys.exit()
#q.empty()
end_time=time.time()
print("Time elapsed: ",end_time-start_time)

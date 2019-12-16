import libvirt
import sys, time
import logging
import datetime
LOG_FILENAME = 'logging.out'
logging.basicConfig(filename=LOG_FILENAME,
                    format='%(asctime)s %(message)s',
                    filemode='w'
                    )
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug('This message should go to the log file')
f = open(LOG_FILENAME, 'rt')

conn = libvirt.open('qemu:///system')
memory=[]
cpuser=[]
ids=[]
Z=[]
user = raw_input("Enter either CPU or MEM for sorting: ")
T = int(raw_input("Enter the threshold cpusage IN nanosecs (eg= 10000000000000):"))
if user == 'MEM':
        i=5
else:
        i=4
indexes = [0,2,4]

for id in conn.listDomainsID():
        dom = conn.lookupByID(id)
        name= conn.lookupByID(id).name()
        mem = dom.maxMemory()
        dom1 = conn.lookupByName(name)
        cpus = dom.maxVcpus()
        stats = dom.getCPUStats(True)
        Memory  = dom.memoryStats()
        Memory1 = int(Memory.get('usable'))
        Memory2 = int(Memory.get('actual'))
        MemUsage = Memory2 - Memory1
        stats1 = stats[0]
        stats2=int(stats1.get('cpu_time'))
        ids.append(id)
        timestamp=datetime.datetime.now()
        memory.append(mem)
        cpuser.append(cpus)
        infos = dom.info()
        if (stats2>T):
                print("**ALERT** {3} CPU USAGE i.e {0} of VM :{1} is greater then Threshold: {2}".format(stats2,name,T,timestamp))
                logger.critical("**ALERT** {3} CPU USAGE i.e {0} of VM :{1} is greater then Threshold: {2}".format(stats2,name,T,timestamp))
        for index in sorted(indexes, reverse=True):
                del infos[index]
        print ("Total memory and NO. of cpu in VM of name:{3} and id:{0} with *CPU* Usage:{1} and *MEM* Usage :{4} is {2} ".format(id,stats2,infos,name,MemUsage))
        infos.append(id)
        infos.append(name)
        infos.append(stats2)
        infos.append(MemUsage)
        infos[0] = int(infos[0])
        Z.append(infos)


print("Sorted based on your input: {}".format(user))
def Sort(Z):
        Z.sort(key = lambda x: x[i])
        return Z
(Sort(Z))
for elem in Z:
        print elem
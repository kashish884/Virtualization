import libvirt
conn = libvirt.open('qemu:///system')

host = conn.getHostname()
mem = conn.getFreeMemory()
vcpus = conn.getMaxVcpus(None)
nodeinfo = conn.getInfo()
stats = conn.getCPUStats(0)

print('Hostname:'+host)

print('Maximum support virtual CPUs: '+str(vcpus))

print('Model: '+str(nodeinfo[0]))
print('Number of CPUs: '+str(nodeinfo[2]))
print('MHz of CPUs: '+str(nodeinfo[3]))
print('Number of NUMA nodes: '+str(nodeinfo[4]))
print('Number of CPU sockets: '+str(nodeinfo[5]))
print('Number of CPU cores per socket: '+str(nodeinfo[6]))
print("Free memory on the node (host) is " + str(mem) + " bytes.")
print("kernel: " + str(stats['kernel']))
print("idle:   " + str(stats['idle']))
print("user:   " + str(stats['user']))
print("iowait: " + str(stats['iowait']))
import libvirt
conn = libvirt.open('qemu:///system')
for id in conn.listDomainsID():
	dom = conn.lookupByID(id)
	infos = dom.info()
	print infos
    
user = raw_input("Enter the domName: ")

domName = str(user)
dom = conn.lookupByName(domName)
id = dom.ID()
if id == -1:
	print('The domain is not running so has no ID.')
else:
	print('The ID of the domain is ' + str(id))
dom = conn.lookupByName(domName)
type = dom.OSType()
print('The OS type of the domain is "' + type + '"')
cpus = dom.maxVcpus()
if cpus != -1:
	print('The max Vcpus for domain is ' + str(cpus))
else:
	print('There was an error.')
dom = conn.lookupByName(domName)

name = dom.name()
print('Thename of the domain is "' + name +'".')
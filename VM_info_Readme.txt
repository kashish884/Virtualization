##Libvirt commands to Obtain Guest Domain information:

## Description

-This code is used to collect the info of the all the VM's that are present on the host domain i.e. hypervisor

## Modules used
-libvirt
-sys


## Steps to run:

Step 1 : to run the code
Run the code on the hypervisor after saving it in the working directory as q5_P2 then using following command: python q5_P2.py

The output will fetch for you the detailed info of VM's on the host in below order:

[note: In the following script o/p at first instance, we print the information (State (1 for running) , Max Memory (in bytes), Number of vCPUs, CPU Time (in ns) ) about all running VMs]

[1, 2097152L, 2097152L, 4, 520230000000L]
[1, 2097152L, 2097152L, 4, 515520000000L]
The ID of the domain is 13
The OS type of the domain is "hvm"
The max Vcpus for domain is 4
Thename of the domain is "ksingh9lab2VM2".
Thename of the domain is "ksingh9_VM1".




# Version
 - 1.0

#Authors
----
Kashish Singh, Sathwik Kalvakuntla

# License

  - All rights reserved by the owner and NC State University.
  - Usage of the code can be done post approval from the above.

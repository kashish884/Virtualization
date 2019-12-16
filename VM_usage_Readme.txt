##Performance monitoring to monitor VCPU and VMEM of all VMs.(alongwith it total memory, no. of cpu's, vm id)


## Description

-This code is used to collect the info of all the VM's that are active presently on the hypervisor and then sorts the list of these VM's details with respect to either memory or CPU usage as given by user.
(a) print all VMs in ascending order, based on CPU /memory usage.(input taken from the user)
(b) print and also log in file an alert message (Vm name, time stamp, CPU usage) if CPU usage crossed a threshold T (input taken from user)



##Concepts:
1.)CPU usage implementation
The overall CPU usage is simply the sum of the time spent in userspace and the time spent on kernel space. So naively one would have expected user_time + system_time to equal cpu_time. Over this cputime we will implement sorting when CPU is mentioned by the user.

2.)Memory usage implementation

dom.memoryStats() fetches the data in this format:
{'swap_out': 0L, 'available': 1881600L, 'usable': 1695932L, 'actual': 2097152L, 'major_fault': 196L, 'swap_in': 0L, 'last_update': 1570425181L, 'unused': 1748248L, 'minor_fault': 175274L, 'rss': 837860L}
If memoryStats output is not in proper order then below error may appear

**Traceback (most recent call last):
  File "q5_P3.py", line 37, in <module>
    Memory1 = int(Memory.get('usable'))
TypeError: int() argument must be a string or a number, not 'NoneType'**

So to calculate the available memory we did
MEM = int(actual - usable)

MEM usage = (actual - usable memory) 
CPU usage = CPUTIME

3.)Useful feature of the python logging API is the ability to produce different messages at different log levels. Here since we needed to log for the alert we made use of 
Logger.critical(msg[, *args[, **kwargs]])
Logs a message with level CRITICAL on this logger. The arguments are interpreted as for debug().


## Modules used
-libvirt
-sys
-time
-logging
-datetime


## Usage

Step 1 : to run the code

Run the code on the hypervisor after saving it in the working directory as q5_P3 then using following command: python q5_P3.py

Step 2 : Enter 2 inputs
1st : MEM or CPU (to sort the list on the basis of either CPU or Memory )
2nd : threshold value of the CPU usage in nano seconds to create an alert logging in logging.out folder instantly created in the same working directory.

The output fetched is in following manner:

sorted based on your input:MEM

[ACTUAL MEMORY, NO. OF VCPU'S, VM ID, VM NAME, CPU usage, 1Available memory]
[ACTUAL MEMORY, NO. OF VCPU'S, VM ID, VM NAME, CPU usage, 2Available memory]
[ACTUAL MEMORY, NO. OF VCPU'S, VM ID, VM NAME, CPU usage, 3Available memory]

If the cpu usage in nano seconds crosses the given threshold by the user then the output expected is as below in logging.out folder at cwd level:

ece792@t11_vm5:~$ cat logging.out
2019-10-06 19:36:40,899 This message should go to the log file
2019-10-06 19:36:50,923 **ALERT** 2019-10-06 19:36:50.922974 CPU USAGE i.e 179172398784 of VM :skalvak_vm is greater then Threshold: 12345
2019-10-06 19:36:50,928 **ALERT** 2019-10-06 19:36:50.927935 CPU USAGE i.e 172801105119 of VM :ksingh9_VM1 is greater then Threshold: 12345
2019-10-06 19:36:50,932 **ALERT** 2019-10-06 19:36:50.932071 CPU USAGE i.e 1231014368298 of VM :ksingh9lab2VM2 is greater then Threshold: 12345






# Version
 - 1.0

#Authors
----
Kashish Singh, Sathwik Kalvakuntla

# License

  - All rights reserved by the owner and NC State University.
  - Usage of the code can be done post approval from the above.

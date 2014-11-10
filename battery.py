#!/usr/bin/python
# coding=UTF-8
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
import commands
#a=commands.getstatusoutput("more /sys/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/device:01/PNP0C09:00/PNP0C0A:00/power_supply/BAT0/capacity")
a=commands.getstatusoutput("battery")
a=a[1]
a=a.split('%')
a=a[0]
a=float(a)-1;
temp=a;
a=int(a)
remaining=20
color=bcolors.FAIL
if(a>30):
	color=bcolors.WARNING
if(a>60):
	color=bcolors.OKBLUE
if(a>=80):
	color=bcolors.OKGREEN
times=a/5
t="▸"

for ch in range(times):
	t=t+"▸"
	remaining=remaining-1
for ch in range(remaining-1):
	t=t+"▹"
print color,t,a,bcolors.ENDC
#print a,bcolors.ENDC

import os
import sys
import subprocess
import string
from pprint import pprint
from threading import Thread
import paramiko
from multiprocessing import Pool

reach_file = open('reachablehosts.txt','a')
unreach_file = open('unreachablehosts.txt','a')
output=""
print "Enter file name with hosts\n"
flname = raw_input()
f=open(flname,'r')
for line in f:
        print line
        variable = os.popen('ping6 -c 2 '+line).read()
        print variable
        if 'received' not in variable:
            print "UnReachable\n"
            unreach_file.write(line)
        else:
            print "Reachable\n"
            reach_file.write(line)
unreach_file.close()
reach_file.close()
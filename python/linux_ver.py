#! /usr/bin/python3
'''
written by Hossein Yeganeh
This is a python script that print os and kernel version.
'''
import platform

lin_ver = platform.platform()
print(platform.platform())

ver5 = "Linux-5."
ver6 = "Linux-6."
ver7 = "Linux-7."


if ver5 in lin_ver:
    print("Linux Kernel Version is: l5")
elif ver6 in lin_ver:
    print("Linux Kernel Version is: l6")
elif ver7 in lin_ver:
    print("Linux Kernel Version is: l7")
else:
    print("unknown_version")

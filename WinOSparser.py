#!/usr/bin/env python
#
# Created by Linus Nissi, Computer Forensic Examiner, DFIR at Swedish Police
# linus@nissi.se
# Current version 0.3
# date 2018-02-09
# Version 0.3 - Added Release ID (appears on some old installations)
# Version 0.3 - Usage update and Windows executable added.
# Version 0.2 - Cleanup code, added Registered Owner and Organization
# Version 0.1 - Initial version - Currently installed OS, old installations, OS version, Prodcut ID, Current Build, Path, Name, Install date
#
# Todo
# Add csv output
#
# Credits 
# Willi Ballenthin (Windows Registry library)
# Glenn P. Edwards Jr (reused code)

from __future__ import print_function
from __future__ import unicode_literals

import os
import re
import sys
import time
import re
def usage():
    return "\n\t This script is written by Linus Nissi (while at Swedish Police Authority as Digital Forensic Examiner) and parses current operating system information, old installations or upgrades from Windows 7,8 and 10. \n\t Run the program through the Python code or the executable for Windows. \n\t This script is written in python 3. For more information and example files visit www.github.com/DFIRdoctor \nUSAGE:\n\t WinOSparser.py <SYSTEM registry file> <SOFTWARE registry file> \nEXAMPLE:\n\t WinOSparser.py SYSTEM SOFTWARE \nEXAMPLE Windows executable:\n\t WinOSparser.exe SYSTEM SOFTWARE"





def os_settings(soft_reg):
    """
    Installed Operating System information
    """
    results = []
    registry = Registry.Registry(soft_reg)
    os_dict = {}
    key = registry.open("Microsoft\\Windows NT\\CurrentVersion")
    for v in key.values():
        if v.name() == "ProductName":
            os_dict['ProductName'] = v.value()
        if v.name() == "ProductId":
            os_dict['ProductId'] = v.value()
        if v.name() == "CurrentBuild":
            os_dict['CurrentBuild'] = v.value()
        if v.name() == "PathName":
            os_dict['PathName'] = v.value()
        if v.name() == "RegisteredOwner":
            os_dict['RegisteredOwner'] = v.value()
        if v.name() == "RegisteredOrganization":
            os_dict['RegisteredOrganization'] = v.value()
        if v.name() == "ReleaseId":
            os_dict['ReleaseId'] = v.value()
        if v.name() == "InstallDate":
            os_dict['InstallDate'] = time.strftime('%Y-%m-%d %H:%M:%S (UTC)', time.gmtime(v.value()))


    print(("=" * 51) + "\n[+] Current Operating System Information\n" + ("=" * 51))
    print("[-] Registry file....: %s" % soft_reg)
    print("[-] Key path.........: %s" % key)
    print("[-] Product Name.....: %s" % os_dict['ProductName'])
    print("[-] Product ID.......: %s" % os_dict['ProductId'])
    print("[-] CurrentBuild.......: %s" % os_dict['CurrentBuild'])
    print("[-] Path Name........: %s" % os_dict['PathName'])
    print("[-] Install Date.....: %s" % os_dict['InstallDate'])
    #print (os_dict.keys())
    #print (os_dict.values())
    if 'RegisteredOwner' in os_dict.keys():
        print("[-] Owner.....: %s" % os_dict['RegisteredOwner'])
    if 'ReleaseId' in os_dict.keys():
            print("[-] Release ID...: %s" % os_dict['ReleaseId'])

def os_source(regkey):
    """
    Installed Operating System information
    """
    results = []
    registry = Registry.Registry(sys_reg)
    os_dict = {}
    key = registry.open("Setup\\" + regkey)
    for v in key.values():
        if v.name() == "ProductName":
            os_dict['ProductName'] = v.value()
        if v.name() == "ProductId":
            os_dict['ProductId'] = v.value()
        if v.name() == "CurrentBuild":
            os_dict['CurrentBuild'] = v.value()
        if v.name() == "RegisteredOwner":
            os_dict['RegisteredOwner'] = v.value()
        if v.name() == "RegisteredOrganization":
            os_dict['RegisteredOrganization'] = v.value()
        if v.name() == "ReleaseId":
            os_dict['ReleaseId'] = v.value()
        if v.name() == "PathName":
            os_dict['PathName'] = v.value()
        if v.name() == "InstallDate":
            os_dict['InstallDate'] = time.strftime('%Y-%m-%d %H:%M:%S (UTC)', time.gmtime(v.value()))


    print(("=" * 51) + "\n[+] Parsing old Operating System Information\n" + ("=" * 51))
    print("[-] Registry file....: %s" % sys_reg)
    print("[-] Key path.........: %s" % key)
    print("[-] Product Name.....: %s" % os_dict['ProductName'])
    print("[-] Product ID.......: %s" % os_dict['ProductId'])
    print("[-] Current Build....: %s" % os_dict['CurrentBuild'])
    print("[-] Path Name........: %s" % os_dict['PathName'])
    print("[-] Install Date.....: %s" % os_dict['InstallDate'])
    #print (os_dict.keys())
    #print (os_dict.values())
    if 'RegisteredOwner' in os_dict.keys():
        print("[-] Owner.....: %s" % os_dict['RegisteredOwner'])
    if 'RegisteredOrganization' in os_dict.keys():
        if os_dict['RegisteredOrganization'] is '':
            print("[-] Registered Organization.....: <empty>")
        else:
            print("[-] Registered Organization.....: %s" % os_dict['RegisteredOrganization'])
    if 'ReleaseId' in os_dict.keys():
            print("[-] Release ID...: %s" % os_dict['ReleaseId'])

"""
Parse old installation data from SYSTEM\Setup\Source OS...
"""
def parse_oldos(sys_reg): 
    """
    Parse old OS in SYSTEM\Setup
    """
    os_parser = {}
    os_dict = {}
    registry = Registry.Registry(sys_reg)
    key = registry.open("Setup")    
    for subkey in key.subkeys(): 
        os = "Source OS" # define Source OS
        if 'Source OS' in subkey.name(): #search for Source OS in Setup with dictionary Installation
            os_parser['SourceOS'] = subkey.name()
            for key,val in os_parser.items(): 
            	os_source(val) # calling function os_source

if __name__ == "__main__":
    """
    Print out all of the information
    """
    try:
        from Registry import Registry
    except ImportError:
        sys.exit("[ERROR] Python-Registry not found, try execute with python3")
    if len(sys.argv) != 4 and len(sys.argv) != 3:
        print(usage())
        sys.exit(-1)
    sys_reg = sys.argv[1]
    soft_reg = sys.argv[2]
    print("[+] SYSTEM hive:   %s" % sys_reg)
    print("[+] SOFTWARE hive: %s" % soft_reg)
    os_settings(soft_reg)
    parse_oldos(sys_reg)

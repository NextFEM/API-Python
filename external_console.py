# coding=utf8

# sample script with AutoREST - interact with main window

import clr; import time
import os; import sys
from winreg import *

def NFapiPath():
    addr = r"SOFTWARE\Classes\NextFEM Designer\shell\open\command"
    aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    aKey = OpenKey(aReg, addr); vkey = QueryValueEx(aKey,None)
    return os.path.split(vkey[0].replace('"','').replace("%1","").strip())[0]

clr.AddReference(NFapiPath() + '\\NextFEMapi.dll')
import NextFEMapi

# Create the nf object (instance of the application)
nf = NextFEMapi.API()
while nf.loading:
    print("Loading...")
    time.sleep(1)
print("NextFEM API successfully loaded")
# starts Designer and wait for idle
nf.startDesigner('-plugin "REST API server"',False, True)
# connect to running instance of NextFEM Designer
print("Connected to NextFEM Designer: " + str(nf.connect()))
# new model
nf.comm("op/new")
# add nodes
n1=nf.addNode(0,0,0)
n2=nf.addNode(3,0,0)
# add beam
b1=nf.addBeam(n1,n2,0,0)

# refresh view - NodesVisible=2, resizeView True
nf.refreshDesignerView(2,True)

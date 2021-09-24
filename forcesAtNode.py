# coding=utf8
# to launch file: exec(open('filename.py').read())
import clr
import os;
import ctypes; # for dialog boxes
from winreg import * # for reg. access
addr = r"SOFTWARE\Classes\NextFEM Designer\shell\open\command"
aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, addr); vkey = QueryValueEx(aKey,None)
dir=os.path.split(vkey[0].replace('"','').replace("%1","").strip())[0]

dirname=os.path.dirname
# support for cleaning screen: call clear()
clear = lambda: os.system('cls')
clr.AddReference(dir + "\\NextFEMapi.dll")
# support for message boxes in Windows
def msgbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

import NextFEMapi
nf=NextFEMapi.API()
# put you model name HERE
nf.openModel(dir + "\\testAPI.nxf")

# nodal forces
node = "21"; loadcase = "perm"
d={}; dt={}
connElem = nf.getConnectedElements(node); print("Connected elements: " + str(connElem))
if not connElem:
    quit()
# for coordinate tranformation use local axes of 1st element in list
lcs=nf.getLocalAxes(connElem[0])

for el in connElem:
    solls=nf.getBeamForcesAtNode(el,node,loadcase)
    s=[]
    for so in solls:
        s.append(so)
    d[el] = s
    # tranformation
    print("Elem" + str(el) +" ----------------------------------------")
    print(s)
    vF=NextFEMapi.vert3(s[0],s[1],s[2]); vM=NextFEMapi.vert3(s[3],s[4],s[5])
    res1=vF.v3Transform(lcs); res2=vM.v3Transform(lcs)
    sT=[res1.X,res1.Y,res1.Z,res2.X,res2.Y,res2.Z]; print(sT)
    dt[el] = sT
    print("-----------------------------------------------")

print(d); print(dt)
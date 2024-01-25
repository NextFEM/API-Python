# coding=windows-1252
import clr
import os
import ctypes; # for dialog boxes
from winreg import * # for registry access
addr = r"SOFTWARE\Classes\NextFEM Designer\shell\open\command"
aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, addr); vkey = QueryValueEx(aKey,None)
dir=os.path.split(vkey[0].replace('"','').replace("%1","").strip())[0]
# support for cleaning screen: call clear()
clear = lambda: os.system('cls')
def msgbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# instance of NextFEM API
clr.AddReference(dir + "\\NextFEMapi.dll")
import NextFEMapi

nf=NextFEMapi.API()
# path for saving models - be sure the folder already exists
savedir = r"C:\NextFEM models" + "\\"

def model45(len,hei,isTria):
    """ buckling analysis for a meshed wall
    """
    global nf
    nf.newModel()
    nf.modelName="model45_" + ("tria_" if isTria else "") + str(len) + "x" + str(hei)
    d1=int(len/0.125); d2=int(hei/0.125)
    nodes=nf.addMeshedWall(1,0.0,0.0,0.0,d1,d2,"XZ",len,hei)
    sides=nf.getNodesOnSides(nodes)
    mat=nf.addIsoMaterial("Mat",70000000,0.23,0)
    sec=nf.addPlanarSection(0.008)
    nf.addLoadCase("st"); nf.setBucklingAnalysis("st",5)
    load=20; # total load in kN

    for e in nf.elemsList:
        nf.assignMaterialToElement(e,mat); nf.assignSectionToElement(e,sec)
        if isTria: nf.quad2tria(e)
    nf.mergeOverlappedNodes()
    for ss in sides[0]:
        nf.setBC(ss, True, True, True, False, False, False)
    for ss in sides[1]:
        nf.setBC(ss, False, True, False, False, False, False)
    for ss in sides[2]:
        nf.setBC(ss, False, True, False, False, False, False)
        nf.addNodalLoad(ss, load/(sides[2].Length), 1, "st")
    for ss in sides[3]:
        nf.setBC(ss, False, True, False, False, False, False)
    nf.RunModel()
    print(nf.modelName + " - 1st mult. = " + str(nf.getModalPeriod(1,"st")))
    print("Exported: " + str(nf.exportMidas(savedir + nf.modelName + ".mgt")))
    nf.saveModel(savedir + nf.modelName + ".nxf")

for r in range(14,1,-1):
    model45(0.25*r,2.0,False)
input("Press key to close...")
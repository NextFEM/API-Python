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

from System.Collections.Generic import Dictionary
from System import String

nf=NextFEMapi.API()
# always use standard solver to check for labilites
nf.changeDefSolverType(0)
# path for saving models - be sure the folder already exists
savedir = r"C:\NextFEM models" + "\\"

def model42():
    """non-linear analysis with springs
    """
    global nf
    nf.newModel()
    nf.modelName = "model42"; print(nf.modelName + " ---------------------------------------")
    # set units
    nf.setUnits("m","kN")
    # nodes - spring in global Z
    n1=nf.addNode(0,0,0); n2=nf.addNode(0,0,1)
    # restraints
    nf.setBC(n1, True, True, True, True, True, True)
    nf.setBC(n2, True, True, False, True, True, True); # Z free
    # lumped mass
    nf.addNodalMass(n2,100,100,100,0,0,0)
    # add spring property - GLOBAL
    local=False
    # spring 1D properties - WARNING: extra zeroes are missing, not as in GUI
    nf.addSpringNLProperty("bilinear",[-1,-1,0,-1,-1,-1],[ [], [], [100,20.0,0.1,10.0,5.0], [], [], [] ],local)
    nf.addSpringNLProperty("trilinear",[-1,-1,1,-1,-1,-1],[ [], [], [100,20,5,25,-5,100,-20,5,-25,-5,40,-40], [], [], [] ],local)
    nf.addSpringNLProperty("pivot",[-1,-1,2,-1,-1,-1],[ [], [], [100,20,5,25,-5,100,-20,5,-25,-5,40,-40,5,0.5,  0, 5,0.5, 0,0,0,0,0,0,0], [], [], [] ],local)
    nf.addSpringNLProperty("tomazevic-lutman",[-1,-1,3,-1,-1,-1],[ [], [], [100,20,5,25,-5,0,0.4,0.06,25], [], [], [] ],local)
    nf.addSpringNLProperty("ring-shape",[-1,-1,4,-1,-1,-1],[ [], [], [100,20,5,25,1,0.2,0,0,25, 0, 0], [], [], [] ],local)
    nf.addSpringNLProperty("slip-type",[-1,-1,5,-1,-1,-1],[ [], [], [100,20,5,25,-5,4,0.5,0.9,40,  1,1,  0.005,0,1,1,1], [], [], [] ],local)
    nf.addSpringNLProperty("dashpot",[-1,-1,6,-1,-1,-1],[ [], [], [100,0.2,1,0.1,100,0], [], [], [] ],local)
    nf.addSpringNLProperty("unsymm-slip",[-1,-1,7,-1,-1,-1],[ [], [], [100,20,5,25,-5,4,0.5,0.9,40,  1,1,  -1000,10,0.15,  1,  0.1,0.005,0,1,1], [], [], [] ],local)
    nf.addSpringNLProperty("gap",[-1,-1,8,-1,-1,-1],[ [], [], [0.1,100,0.00000001], [], [], [] ],local)
    nf.addSpringNLProperty("hook",[-1,-1,9,-1,-1,-1],[ [], [], [0.1,100,0.00000001], [], [], [] ],local)
    nf.addSpringNLProperty("bilinUnsymm",[-1,-1,10,-1,-1,-1],[ [], [], [100,20,0.1,10,5,100,-20,0.1,10,-5], [], [], [] ],local)
    nf.addSpringNLProperty("AMD",[-1,-1,15,-1,-1,-1],[ [], [], [1000000,200,0.1,1,0,0,0,0], [], [], [] ],local)
    nf.addSpringNLProperty("VRM",[-1,-1,16,-1,-1,-1],[ [], [], [0.5,1,10,0,0,2,40,0,1,0.5,1,10,0,0,2,40,0,-1], [], [], [] ],local)

    listS=["bilinear","trilinear","pivot","tomazevic-lutman","ring-shape","slip-type","dashpot","unsymm-slip","gap","hook","bilinUnsymm","AMD","VRM"]

    # add a loadcase
    lc="st"
    nf.addLoadCase(lc)
    # load
    nf.addNodalDisp(n2,1.0,3,lc)
    # add growing sine TH
    thID=nf.addSineFunction(2.0,0,20,1.0,1.0,True)
	# add non-linear static analysis
    nf.setNLSanalysis(lc,0.01,100,0.001,30,thID)
    # save state variables
    nf.saveStateVariables=True
    nf.OS_saveStateVariables=True
    # change solver to OpenSees (optional)
    # if not nf.changeSolver(1): quit()
    currElem="0"
    for ss in listS:
        # linear properties
        print(ss + " linear properties: " + str(nf.changeSpringProperty(ss,100,100,100,100,100,100)))
        if int(currElem)>0:
            nf.removeElement(currElem)
        # add spring element
        currElem=nf.addSpring(n1,n2,ss)
        print("Solver messages: " + nf.RunModel())
        # extract data on the go
        d=nf.getResultHistory(lc,str(n2),1,3)
        f=nf.getResultHistory(lc,currElem,8,1,1)
        print("Plot: " + str(nf.getDataPlot(d,f,savedir + nf.modelName + ss + ".png",ss)))
        print("Done " + ss)
    # save model
    print("Model saved: " + str(nf.saveModel(savedir + nf.modelName + ".nxf")))

model42()
input("Press key to close...")
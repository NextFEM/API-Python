# coding=utf8
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
# always use standard solver to check for labilites
nf.changeDefSolverType(0)
# path for saving models - be sure the folder already exists
savedir = r"C:\NextFEM models" + "\\"

def model17():
    """ portal with end releases and rigid offsets in beams, distributed load on beam
    """
    global nf
    # new instance
    nf.newModel()
    nf.modelName = "model17"; print(nf.modelName + " ---------------------------------------")
    # add nodes in XZ plane
    n1=nf.addNode(0,0,0)
    n2=nf.addNode(0,0,3)
    n3=nf.addNode(3,0,3)
    n4=nf.addNode(3,0,0)
    # restrain nodes
    nf.setBC(n1, True, True, True, True, True, True)
    nf.setBC(n4, True, True, True, True, True, True)
    # section and material from library
    sectID = nf.addRectSection(0.3,0.5)
    matID = nf.addMatFromLib("C25/30")
    print("sect: " + str(sectID) + " mat: " + str(matID))
    # elements
    b1 = nf.addBeam(n1, n2, sectID, matID)
    b2 = nf.addBeam(n2, n3, sectID, matID)
    b3 = nf.addBeam(n3, n4, sectID, matID)
    
    # length of element b2
    b2len = nf.getElementProperty(b2,"lun")
    # loadcase and loads
    nf.addLoadCase("st")
    # nf.addNodalLoad(n2, 10.0, 1, "st")
    nf.addBeamLoad(b2,-10.,-10.,0,b2len,3,"st")

    # end releases for horizontal beam
    nf.setEndRelease(b2,n2,[1.,1.,1.,1.,0.5,0.1])
    nf.setEndRelease(b2,n3,[-1.,-1.,-1.,-1.,0.,0.],True)
    print("End release b2: " + " ".join(str(i) for i in nf.getEndRelease(b2)) )
    
    # rigid offset for columns
    nf.setRigidOffsets(b1,[0.1,0.1])
    nf.setRigidOffsets(b3,[0.1,0.1])
    print("End offset b1: " + " ".join(str(i) for i in nf.getRigidOffsets(b1)) )
    print("End offset b2: " + " ".join(str(i) for i in nf.getRigidOffsets(b2)) )
    print("End offset b3: " + " ".join(str(i) for i in nf.getRigidOffsets(b3)) )

    print("Solver messages: " + nf.RunModel())
    nf.saveModel(savedir + nf.modelName + ".nxf")
    nf.startDesigner('"' + savedir + nf.modelName + ".nxf" + '"')

model17()
input("Press key to close...")
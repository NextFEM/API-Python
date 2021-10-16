# coding=utf8
import clr
import os
import ctypes; # for dialog boxes
from winreg import * # for reg. access
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
# path for saving models
savedir = r"C:\NextFEM models" + "\\"

# modal analysis with OpenSees (not included in the program, see https://www.nextfem.it/it/opensees/)
def model3():
    """ vertical cantilever and modal analysis + Opensees
    """
    global nf
    nf.newModel()
    nf.modelName = "model3"; print(nf.modelName + " ---------------------------------------")
    nf.addNodeWithID(0,0,0,"1"); nf.addNodeWithID(0,0,1,"2")
    # section and material from library
    sectID = nf.addSectFromLib("IPE 140")
    matID = nf.addMatFromLib("C25/30")
    nf.addBeam("1", "2", sectID, matID)
    # restraint
    nf.setBC("1", True, True, True, True, True, True)
    # loadcase and loads
    nf.addLoadCase("lc")
    # set sw to this loadcase
    nf.setSelfWeight("lc")
    # set load to mass
    nf.setLoadsToMass("lc")
    # add mass
    nf.addNodalMass("2", 1, 1, 1,0,0,0)
    # modal analysis
    nf.addLoadCase("modal"); nf.setModalAnalysis("modal",3)
    # change solver to OpenSees - path must be set inside Designer options, best having it in the installation path
    nf.changeSolver(1)
    print("Solver messages: " + nf.RunModel())
    print("1st period T1=" + str(nf.getModalPeriod(1,"modal")))
    nf.saveModel(savedir + nf.modelName + ".nxf")
    #nf.startDesigner('"' + savedir + nf.modelName + ".nxf" + '"')

model3()

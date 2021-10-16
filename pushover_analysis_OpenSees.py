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

# fiber model with OpenSees (not included in the program, see https://www.nextfem.it/it/opensees/)
def model8(Nfloors):
    """generating spatial RC frame, non-linear static analysis + Opensees
    """
    global nf
    varFact=0.3 # factor for variable loading
    nf.newModel()
    nf.modelName = "model8_" + str(Nfloors) + "storey"; print(nf.modelName + " ---------------------------------------")
    # set units
    nf.setUnits("m","kN")
    # get sections and material
    sX=nf.addRectSection(0.30,0.50); sY=nf.addRectSection(0.5,0.24); sZ=nf.addRectSection(0.40,0.40)
    matID = nf.addMatFromLib("C25/30")
    # loadcases
    nf.addLoadCase("pp"); nf.addLoadCase("perm"); nf.addLoadCase("var")
    # self-weight
    nf.setSelfWeight("pp")
    # use frame generator
    nf.generateFrame(2,4,Nfloors,5.0,6.0,3.5,sX, sY, sZ, matID, matID, matID, "perm","var","",-2.0,-3.0,0,True,False)
    # combination
    nf.addLoadCase("ULS")
    nf.setCombination("ULS","pp",1.3); nf.setCombination("ULS","perm",1.5); nf.setCombination("ULS","var",1.5)
    # combination for vertical loading in pushover
    nf.addLoadCase("seismW")
    nf.setCombination("seismW","pp",1); nf.setCombination("seismW","perm",1); nf.setCombination("seismW","var",varFact)
    # set loads to masses
    nf.setLoadsToMass("pp"); nf.setLoadsToMass("perm"); nf.setLoadsToMass("var",varFact)
    # load case from combo for both vertical ULS and seismic vertical cases
    newLC1=nf.LoadCaseFromCombo("ULS"); newLC2=nf.LoadCaseFromCombo("seismW")
    print("Loadcases " + newLC1 + " and " + newLC2 + " created.")
    # rigid diaphragms at each Z level, using auto-determined master nodes
    nf.setRigidDiaphragms()
    # auto-rebar
    desMat=nf.addDesignMatFromLib("B450C")
    print("Design mat.: " + str(desMat))
    print("Solving..."); print(nf.RunLoadCase(newLC1))
    # dimensioning of rebar on the base of static results (vertical load only). 3 stations used.
    print("Auto-sizing rebar, please wait ...")
    print(nf.checkModel(newLC1,"1",1,"Static_Rebar_Design",True,True,[desMat]))
    # set OpenSees as default solver - path must be set inside Designer options, best having it in the installation path
    nf.changeSolver(1,dir + "\\opensees.exe")
    # set fiber section
    nf.setFiberSection(sX); nf.setFiberSection(sY); nf.setFiberSection(sZ)
    
    # add nonlinear analysis in sequence
    nf.setNLSanalysis(newLC2,0.1,10,0.001,30) # vertical loading
    pushLC="pushoverX"
    nf.addLoadCase(pushLC)
    # control node 158
    cnode=nf.getControlNode()
    nf.setNLSanalysis(pushLC,0.001,1000,0.1,30,-1,cnode,1) # pushover in displ. control for X dir.
    nf.setAnalysisSequence(pushLC,newLC2) # pushX after LC_seismW
    # add functions for pushover analysis
    sID=nf.addEC8spectrum(0.35,1.5,"LLS") # spectrum as per EC8 with ag=0.35, q=1.5 and for Life-Safety limit state
    nf.applyEC8lateralForces(sID,pushLC,"",False,0,0.075)
    print("Solving..."); print(nf.RunLoadCase(pushLC))
    print("Model saved: " + str(nf.saveModel(savedir + nf.ModelName + ".nxf")))
    #if msgbox("NextFEM API","Open model with results?",4): nf.startDesigner('"' + savedir + nf.ModelName + ".nxf" + '"' + " -res")
    # export pushover curve
    print("Executing data extraction: " + nf.ModelName + ".nxf" + " -d " + pushLC + " pushX")
    nf.startDesigner('"' + savedir + nf.ModelName + ".nxf" + '"' + " -d " + pushLC + " pushX")

# launch with 3 floors
model8(3)
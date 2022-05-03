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

# non-linear hinge model
def model9(Nfloors):
    """generating spatial RC frame, non-linear static analysis with hinges
    """
    global nf
    varFact=0.3 # factor for variable loading
    nf.newModel()
    nf.modelName = "model9_" + str(Nfloors) + "storey"; print(nf.modelName + " ---------------------------------------")
    # set units
    nf.setUnits("m","kN")
    # get sections and material
    sX=nf.addRectSection(0.30,0.50); sY=nf.addRectSection(0.5,0.24); sZ=nf.addRectSection(0.40,0.50)
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
    if not nf.changeSolver(1): quit()
    # add hinges as per Italian code
    print("Adding hinges, please wait ...")
    considerShearHinges=False
    nf.addNVMhinge("h0","NTC_CA_hinge",0,considerShearHinges); nf.addNVMhinge("h1","NTC_CA_hinge",100,considerShearHinges)
    #nf.addNormalhinge("h0","NTC_CA_hinge",0,considerShearHinges); nf.addNormalhinge("h1","NTC_CA_hinge",100,considerShearHinges)
    for ee in nf.elemsList:
        nf.assignHinge(ee,"h0"); nf.assignHinge(ee,"h1")
    # add nonlinear analysis in sequence
    nf.setNLSanalysis(newLC2,0.1,10,0.001,10) # vertical loading
    pushLC="pushoverX"; nf.addLoadCase(pushLC)
    # pushover in Y
    pushLCy="pushoverY"; nf.addLoadCase(pushLCy)
    # control node
    cnode=nf.getControlNode()
    step=0.001
    # calculate number of steps from step length, considering 2% of ultimate lateral displacement
    nsteps=int(float(nf.getNodeProperty(cnode,"Z"))*0.02/step)
    tol=1
    nf.setNLSanalysis(pushLC,step,nsteps,tol,10,-1,cnode,1) # pushover in displ. control for X dir.
    nf.setNLSanalysis(pushLCy,step,nsteps,tol,10,-1,cnode,2) # pushover in displ. control for Y dir.
    nf.setAnalysisSequence(pushLC,newLC2) # pushX after LC_seismW
    nf.setAnalysisSequence(pushLCy,newLC2) # pushY after LC_seismW
    # add functions for pushover analysis
    sID=nf.addEC8spectrum(0.35,1.5,"LLS") # spectrum as per EC8 with ag=0.35, q=1.5 and for Life-Safety limit state
    nf.applyEC8lateralForces(sID,pushLC,pushLCy,False,0,0.075)
    print("Model saved: " + str(nf.saveModel(savedir + nf.modelName + ".nxf")))

    print("Solving..."); print(nf.RunLoadCase(pushLC)); print(nf.RunLoadCase(pushLCy))

    print("Model saved: " + str(nf.saveModel(savedir + nf.modelName + ".nxf")))
    #if msgbox("NextFEM API","Open model with results?",4): nf.startDesigner('"' + savedir + nf.modelName + ".nxf" + '"' + " -res")
    # export pushover curve X
    print("Executing data extraction: " + nf.modelName + ".nxf" + " -d " + pushLC + " pushX")
    nf.startDesigner('"' + savedir + nf.modelName + ".nxf" + '"' + " -d " + pushLC + " pushX")
    # export pushover curve Y
    print("Executing data extraction: " + nf.modelName + ".nxf" + " -d " + pushLCy + " pushY")
    nf.startDesigner('"' + savedir + nf.modelName + ".nxf" + '"' + " -d " + pushLCy + " pushY")

# launch with 3 floors
model9(3)
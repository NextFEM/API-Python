import sys
import clr
clr.AddReference("C:\\Program Files\\NextFEM\\NextFEM Designer 64bit\\NextFEMapi.dll")
import NextFEMapi

nf=NextFEMapi.API()

# set units
nf.setUnits("m","kN")
# get sections and material
sX=nf.addRectSection(0.30,0.50); sY=nf.addRectSection(0.5,0.24); sZ=nf.addRectSection(0.40,0.40)
matID = nf.addMatFromLib("C25/30")
# add loadcases
nf.addLoadCase("pp"); nf.addLoadCase("perm"); nf.addLoadCase("var")
# set self-weight
nf.setSelfWeight("pp")
# use frame generator
nf.generateFrame(2,4,10,5.0,6.0,3.5,sX, sY, sZ, matID, matID, matID, "perm","var","",-2.0,-3.0,0,True,False)
# add a combination
nf.addLoadCase("ULS")
nf.setCombination("ULS","pp",1.3); nf.setCombination("ULS","perm",1.5); nf.setCombination("ULS","var",1.5)
# load case from combo
nf.LoadCaseFromCombo("ULS")
# set rigid diaphragms for all floors
nf.setRigidDiaphragms()
# auto-rebar
print("Design mat.: " + str(nf.addDesignMatFromLib("B450C")))
# set modelname and run linear analysis
nf.ModelName = "testAPI"; print("Solver messages: " + nf.RunLoadCase("LC_ULS"))

# dimensioning of rebar on the base of static results. 3 stations used.
print(nf.checkModel("LC_ULS","1",1,"Static_Rebar_Design"))

# set OpenSees as default solver - path must be input (OpenSees not included)
nf.changeSolver(1,r"C:\opensees.exe")
# set fiber section
nf.setFiberSection(sX); nf.setFiberSection(sY); nf.setFiberSection(sZ)

# set non-linear analysis - to be run later
nf.setNLSanalysis("LC_ULS",0.1,10,0.001,30)
# save and open model
nf.saveModel(nf.ModelName + ".nxf")
nf.startDesigner(nf.ModelName + ".nxf")
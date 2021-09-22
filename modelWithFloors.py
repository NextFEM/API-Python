import sys
import clr
clr.AddReference("C:\\Program Files\\NextFEM\\NextFEM Designer 64bit\\NextFEMapi.dll")

import NextFEMapi
nf=NextFEMapi.API()

nf.newModel
Lu=nf.getLenUnit()
Fu=nf.getForceUnit()
print("Model units: " + Lu + ", " + Fu)
n1=nf.addNode(0,0,0,1,0,-1,0,1,0)
n2=nf.addNode(2,0,0)
n3=nf.addNode(2,4,0)
n4=nf.addNode(0,4,0,1,0,-1,0,1,0)
nf.setBC(n1, True, True, True, True, True, True)
nf.setBC(n4, True, True, True, True, True, True)
sectID=nf.addSectFromLib("IPE 140")
matID=nf.addMatFromLib("S275")
beamID1=nf.addBeam(n1, n2, sectID, matID)
beamID2=nf.addBeam(n2, n3, sectID, matID)
beamID3=nf.addBeam(n3, n4, sectID, matID)
beamID4=nf.addBeam(n4, n1, sectID, matID)
nf.addLoadCase("G")
nf.setFloorLoad("load", "G", 1.8, 0, 0, -1)
nf.addFloorLoadPlane("load", 2, n1, n2, n3, n4)
s=nf.RunModel(); print(s)
nf.saveModel("proj_roof.nxf")
nf.startDesigner("proj_roof.nxf")
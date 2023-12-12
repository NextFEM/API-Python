# coding=windows-1252
import clr; import os; import time; import math
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
# wait for licenses to load
while nf.loading:
    print("Loading...")
    time.sleep(1)
# path for saving models - be sure the folder already exists
savedir = r"C:\NextFEM models" + "\\"

def model43():
    """moment-curvature of RC section
    """
    global nf
    from operator import length_hint
    nf.newModel()
    nf.modelName="model43"
    # set units
    nf.setUnits("m","kN")
    # get sections and material
    se=nf.addRectSection(0.3,0.5)
    matID = nf.addMatFromLib("C25/30")
    nf.setSectionMaterial(se,matID); nf.renameSection(se,"RCsect","EN")
    # add rebar (longitudinal)
    desMat=nf.addDesignMatFromLib("B450C")
    diam = 14; areaB=nf.convertValue(math.pi*pow(diam,2) / 4,"mm^2","m^2")
    cover=0.04; rebN=6
    # pattern: Top=0, Bottom=1, Equal spacing=2, Wall=3, Lateral=4, Left=5, Right=6
    nf.addRebarPatternInSection(2,se,rebN,cover,desMat,areaB)
    # image
    nf.saveSectionImage(se,savedir + "RCsect")
    # set axial force N and a sign of moment in section for strength calculation (+ tension, - compression)
    N=-90; Mzz=1; Myy=0
    # from here on, Concrete module license is required ------------------------------------------------------------
    # to save image of neutral axis, use: https://www.nextfem.it/api/html/M_NextFEMapi_API_getSectionResMoments3.htm
    # 0 plastic, 1 elastic, 2 thermal-plastic, 3 thermal-elastic, 4 elastic limit, 5 thermal-elastic limit
    res=nf.getSectionResMoments3(se,0,N,Mzz,Myy,savedir + "RCsect_ultimate",0)
    print("Calculate strength in ultimate conditions --------------------------------------")
    for i in range(0,length_hint(res.checkNames)):
        print(res.checkNames[i] + " = " + str(res.values[i]))
    # Optional. Domain type for image: 0 for Myy_Mzz, 1 for N_Myy, 2 for N_Mzz
    res1=nf.getSectionResMoments3(se,4,N,Mzz,Myy,savedir + "RCsect_yielding",0)
    print("Calculate strength in yielding conditions --------------------------------------")
    for i in range(0,length_hint(res1.checkNames)):
        print(res1.checkNames[i] + " = " + str(res1.values[i]))
    nf.saveModel(savedir + nf.modelName + ".nxs"); # save in NextFEM Section Analyzer format

model43()
input("Press key to close...")
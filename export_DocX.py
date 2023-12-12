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

def model39():
    """export docx
    """
    global nf
    nf.createDocX(savedir + r"testReport.docx",["Test report"])
    nf.appendDocXtext(["##MRd##"]); nf.appendDocXtext(["##cm2##"])
    # dictionary from System.Collections
    dict1 = Dictionary[String, String]()
    dict1["MRd"]="M¬Rd¬=12kN"; dict1["cm2"]="cm¶2¶"
    nf.compileDocX(dict1)
    nf.saveDocX(); os.startfile(savedir + r"testReport.docx")
    print("Done.")

model39()
input("Press key to close...")
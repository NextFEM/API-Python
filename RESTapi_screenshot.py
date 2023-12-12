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

def model38():
    """test REST api
    """
    import json
    global nf
    # this is successful only if the plugin "REST API server" is running
    cnt=nf.connect()
    print("Connection status: " + str(cnt))
    if not cnt: return

    # get screen
    stim=nf.comm("/op/command/7", "", 1)
    from PIL import Image; import io; import base64
    bts=base64.b64decode(stim)
    img=Image.open(io.BytesIO(bts))
    img.save(savedir + r"\image.png")

model38()
input("Press key to close...")
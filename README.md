# API-Python
Python scripts using NextFEM API - free environment to model and analyze structures!
## Requirements
[Python.NET](https://github.com/pythonnet/pythonnet) is required to use NextFEM API in Python environment. See also [API usage](https://www.nextfem.it/it/free-api/).
## Instructions
Please read instructions [here](https://www.nextfem.it/it/build-models-in-python-with-nextfem-apis/).

[Python Console plugin](https://www.nextfem.it/it/python-console/) also helps learning NextFEM API. It's available for free in NextFEM Designer.

![pythonConsole](https://github.com/user-attachments/assets/1140bed6-1a5b-4153-ae3a-d2ce4db801b2)

# Python REST API wrapper
A wrapper for using NextFEM REST API is available in the file 'NextFEMapiREST.py'. See also [NextFEM API documentation](https://api.nextfem.it/).

Code sample:

```python
import os,json
import NextFEMapiREST
# connects to local copy of NextFEM Designer
nf=NextFEMapiREST.NextFEMrest()
# current dir
dir = os.path.dirname(os.path.realpath(__file__))

# new model
print(nf.newModel())
# load json model
with open(dir + r"\sample.json") as f:
    contents = json.load(f)
nf.modeldata=contents
# get json model and print first node number
print("First node = " + json.loads(nf.modeldata)['nodes'][0]['num'])
# print first node number in the model
print(str(nf.nodesList[0]))
# consider masses in Z direction: property reading and writing sample
nf.autoMassInZ=False; print(str(nf.autoMassInZ))
nf.autoMassInZ=True; print(str(nf.autoMassInZ))
# set combination coefficients
print(str(nf.setCombinationFactors(1.5,1.5,[0.7,0.5,0.3],[0.6,0.2,0.0],[0.5,0.2,0.0],1.3)))
```

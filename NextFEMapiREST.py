import requests,json

class NextFEMrest:
    def __init__(self,_baseUrl=None,_user="",_msg=True):
        if _baseUrl is None:
            self.baseUrl="http://localhost:5151"
        else:
            self.baseUrl=str(_baseUrl)
        self.user=_user
        self.msg=_msg

    def nfrest(self, method, command, body=None, heads=None):
        url = self.baseUrl + command
        headers = {}
        if self.user != "": headers["user"]=self.user
        if not(heads is None):
            for dd in heads:
                headers[dd]=heads[dd]
        if method == "POST":
            response = requests.post(url=url, headers=headers, json=body)
        elif method == "PUT":
            response = requests.put(url=url, headers=headers, json=body)
        elif method == "GET":
            response = requests.get(url=url, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url=url, headers=headers)
        # print request and return response
        if self.msg: print("*** " + self.user + " :: " + method, command, response.status_code)
        return response.text

    def nfrestB(self, method, command, body=None, heads=None):
        # return bytes
        url = self.baseUrl + command
        headers = {}
        if self.user != "": headers["user"]=self.user
        if not(heads is None):
            for dd in heads:
                headers[dd]=heads[dd]
        if method == "POST":
            response = requests.post(url=url, headers=headers, json=body)
        elif method == "PUT":
            response = requests.put(url=url, headers=headers, json=body)
        elif method == "GET":
            response = requests.get(url=url, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url=url, headers=headers)
        return response.content

    # methods and properties
    def activeBarsDiameters(self): return json.loads(self.nfrest('GET', '/element/rebar/barsdiam', None, None))
    def activeHoopsDiameters(self): return json.loads(self.nfrest('GET', '/element/rebar/hoopsdiam', None, None))
    def addBeam(self, n1, n2, sect, mat, sect2): return self.nfrest('GET', '/element/add/beam/'+n1+'/'+n2+'/'+str(sect)+'/'+str(mat)+'/'+str(sect2)+'', None, None)
    def addBeamLoad(self, elem, value1, value2, position1, position2, direction, loadcase, local): return bool(self.nfrest('GET', '/load/element/beamadd/'+elem+'/'+str(value1)+'/'+str(value2)+'/'+str(position1)+'/'+str(position2)+'/'+str(direction)+'/'+loadcase+'/'+str(local)+'', None, None))
    def addBeamLoad(self, elem, values, positions, direction, loadcase, local): return bool(self.nfrest('GET', '/load/element/beamaddA/'+elem+'/'+str(direction)+'/'+loadcase+'/'+str(local)+'', None, dict([("values",json.dumps(values)),("positions",json.dumps(positions))])))
    def addBeamLoadU(self, elem, value, direction, loadcase, local): return bool(self.nfrest('GET', '/load/element/beamaddU/'+elem+'/'+str(value)+'/'+str(direction)+'/'+loadcase+'/'+str(local)+'', None, None))
    def addBoxSection(self, Lz, Ly, tw, tf1, tf2): return int(self.nfrest('GET', '/section/add/box/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(tf2)+'', None, None))
    def addCircleInSection(self, sectionID, diameter, centerX, centerY, isEmpty, material, doNotCenter): return bool(self.nfrest('GET', '/section/add/addcirc/'+str(sectionID)+'/'+str(diameter)+'/'+str(centerX)+'/'+str(centerY)+'/'+str(isEmpty)+'/'+str(material)+'/'+str(doNotCenter)+'', None, None))
    def addCircSection(self, D): return int(self.nfrest('GET', '/section/add/circ/'+str(D)+'', None, None))
    def addCSection(self, Lz, Ly, tw, tf1, tf2, Lz2): return int(self.nfrest('GET', '/section/add/cshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(tf2)+'/'+str(Lz2)+'', None, None))
    def addDCSection(self, Lz, Ly, tw, tf1, tf2, gap, Lz2): return int(self.nfrest('GET', '/section/add/doublecshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(tf2)+'/'+str(gap)+'/'+str(Lz2)+'', None, None))
    def addDesignMatFromLib(self, name): return int(self.nfrest('GET', '/designmaterial/add/fromlib/'+name+'', None, None))
    def addDesMaterial(self, name, E, fk, ni, type): return int(self.nfrest('GET', '/material/add/des/'+name+'/'+str(E)+'/'+str(fk)+'/'+str(ni)+'/'+str(type)+'', None, None))
    def addDLSection(self, Lz, Ly, tw, tf1, gap): return int(self.nfrest('GET', '/section/add/doublelshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(gap)+'', None, None))
    def addDTSection(self, Lz, Ly, tw, tf1, tf2, Lz2): return int(self.nfrest('GET', '/section/add/dtshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(tf2)+'/'+str(Lz2)+'', None, None))
    def addEC8spectrum(self, ag, q, LS, damping, soilType, type1): return int(self.nfrest('GET', '/function/ec8spectrum/'+str(ag)+'/'+str(q)+'/'+LS+'/'+str(damping)+'/'+soilType+'/'+str(type1)+'', None, None))
    def addEdgeLoad(self, elem, values, edge, direction, loadcase, local): return bool(self.nfrest('POST', '/load/element/edgeadd/'+elem+'/'+str(edge)+'/'+str(direction)+'/'+loadcase+'/'+str(local)+'', values, None))
    def addFillInSection(self, sectionID, x, y, material, doNotCenter): return bool(self.nfrest('GET', '/section/add/fill/'+str(sectionID)+'/'+str(material)+'/'+str(doNotCenter)+'', None, dict([("x",json.dumps(x)),("y",json.dumps(y))])))
    def addFloorPlane(self, name, type, n1, n2, n3, n4): return bool(self.nfrest('GET', '/load/floor/planeadd/'+name+'/'+str(type)+'/'+n1+'/'+n2+'/'+n3+'/'+n4+'', None, None))
    def addGroup(self, name): return bool(self.nfrest('GET', '/group/add/'+name+'', None, None))
    def addHoleInSection(self, sectionID, x, y, material, doNotCenter): return bool(self.nfrest('GET', '/section/add/hole/'+str(sectionID)+'/'+str(material)+'/'+str(doNotCenter)+'', None, dict([("x",json.dumps(x)),("y",json.dumps(y))])))
    def addIsoMaterial(self, name, E, ni, Wden, fk, conductivity, specificHeat, type): return int(self.nfrest('GET', '/material/add/iso/'+name+'/'+str(E)+'/'+str(ni)+'/'+str(Wden)+'/'+str(fk)+'/'+str(conductivity)+'/'+str(specificHeat)+'/'+str(type)+'', None, None))
    def addLayeredPlanarSection(self, layerThicknesses, layerMaterials): return int(self.nfrest('GET', '/section/add/layeredplanar', None, dict([("layerThicknesses",json.dumps(layerThicknesses)),("layerMaterials",json.dumps(layerMaterials))])))
    def addLoadCase(self, name): return bool(self.nfrest('GET', '/loadcase/add/'+name+'', None, None))
    def addLoadCaseToCombination(self, name, loadcase, factor): return bool(self.nfrest('GET', '/loadcase/combo/add/'+name+'/'+loadcase+'/'+str(factor)+'', None, None))
    def addLoadCaseToTimeHistoryAnalysis(self, name, loadcase, factor, THid): return bool(self.nfrest('GET', '/loadcase/combo/addth/'+name+'/'+loadcase+'/'+str(factor)+'/'+str(THid)+'', None, None))
    def addLongitRebar(self, elem, X, Y, area, matID, Linit, Lfin, rectBase, strandTens): return bool(self.nfrest('GET', '/element/rebar/long/'+elem+'/'+str(X)+'/'+str(Y)+'/'+str(area)+'/'+str(matID)+'/'+str(Linit)+'/'+str(Lfin)+'/'+str(rectBase)+'/'+str(strandTens)+'', None, None))
    def addLongitRebarInSection(self, sectionID, X, Y, area, matID, rectBase, strandTens): return bool(self.nfrest('GET', '/section/rebar/long/'+sectionID+'/'+str(X)+'/'+str(Y)+'/'+str(area)+'/'+str(matID)+'/'+str(rectBase)+'/'+str(strandTens)+'', None, None))
    def addLongitRebarInSection(self, sectionID, X, Y, area, matID, rectBase, strandTens): return bool(self.nfrest('GET', '/section/rebar/long/'+str(sectionID)+'/'+str(X)+'/'+str(Y)+'/'+str(area)+'/'+str(matID)+'/'+str(rectBase)+'/'+str(strandTens)+'', None, None))
    def addLSection(self, Lz, Ly, tw, tf1): return int(self.nfrest('GET', '/section/add/lshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'', None, None))
    def addMatFromLib(self, name): return int(self.nfrest('GET', '/material/add/fromlib/'+name+'', None, None))
    def addMember(self, elems): return bool(self.nfrest('GET', '/model/member/add', None, dict([("elems",json.dumps(elems))])))
    def addMeshedWall(self, ID, origX, origY, origZ, div1, div2, plan, leng, hei, angle, tilt, nodeOffset, isHorizontal): return json.loads(self.nfrest('GET', '/op/mesh/addmeshedwall/'+str(ID)+'/'+str(origX)+'/'+str(origY)+'/'+str(origZ)+'/'+str(div1)+'/'+str(div2)+'/'+plan+'/'+str(leng)+'/'+str(hei)+'/'+str(angle)+'/'+tilt+'/'+str(nodeOffset)+'/'+str(isHorizontal)+'', None, None))
    def addNodalDisp(self, node, disp, direction, loadcase): return bool(self.nfrest('GET', '/load/node/disp/'+node+'/'+str(disp)+'/'+str(direction)+'/'+loadcase+'', None, None))
    def addNodalLoad(self, node, value, direction, loadcase, local): return bool(self.nfrest('GET', '/load/node/add/'+node+'/'+str(value)+'/'+str(direction)+'/'+loadcase+'/'+str(local)+'', None, None))
    def addNodalMass(self, ID, tmx, tmy, tmz, rmx, rmy, rmz): return bool(self.nfrest('GET', '/mass/add/'+ID+'/'+str(tmx)+'/'+str(tmy)+'/'+str(tmz)+'/'+str(rmx)+'/'+str(rmy)+'/'+str(rmz)+'', None, None))
    def addNodalSpring(self, n1, propName): return self.nfrest('GET', '/element/add/nodalspring/'+n1+'/'+propName+'', None, None)
    def addNode(self, x, y, z, lcs1X, lcs1Y, lcs1Z, lcs2X, lcs2Y, lcs2Z): return self.nfrest('GET', '/node/add/'+str(x)+'/'+str(y)+'/'+str(z)+'/'+str(lcs1X)+'/'+str(lcs1Y)+'/'+str(lcs1Z)+'/'+str(lcs2X)+'/'+str(lcs2Y)+'/'+str(lcs2Z)+'', None, None)
    def addNodeWithID(self, x, y, z, ID): return bool(self.nfrest('GET', '/node/add/'+str(x)+'/'+str(y)+'/'+str(z)+'/'+ID+'', None, None))
    def addNormalhinge(self, name, checkType, position, includeShear, includeTorsion, cKpl, FresRatio): return bool(self.nfrest('GET', '/hinge/add/simple/'+name+'/'+checkType+'/'+str(position)+'/'+str(includeShear)+'/'+str(includeTorsion)+'/'+str(cKpl)+'/'+str(FresRatio)+'', None, None))
    def addNTCspectrum(self, lat, lon, LS, soil, Vr, St, hh, q0, isHregular, damping, customAg, VerticalComponent): return int(self.nfrest('GET', '/function/ntcspectrum/'+str(lat)+'/'+str(lon)+'/'+LS+'/'+soil+'/'+str(Vr)+'/'+str(St)+'/'+str(hh)+'/'+str(q0)+'/'+str(isHregular)+'/'+str(damping)+'/'+str(customAg)+'/'+str(VerticalComponent)+'', None, None))
    def addNVMhinge(self, name, checkType, position, includeShear, includeTorsion, cKpl, FresRatio, stopResidualBranch): return bool(self.nfrest('GET', '/hinge/add/nvm/'+name+'/'+checkType+'/'+str(position)+'/'+str(includeShear)+'/'+str(includeTorsion)+'/'+str(cKpl)+'/'+str(FresRatio)+'/'+str(stopResidualBranch)+'', None, None))
    def addObject(self, o, other): return bool(self.nfrest('POST', '/model/addobject/'+str(other)+'', o, None))
    def addOmegaSection(self, Lz, Ly, tw, d): return int(self.nfrest('GET', '/section/add/omega/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(d)+'', None, None))
    def addOrChangeDesMaterialProperty(self, ID, name, value, units): return bool(self.nfrest('POST', '/designmaterial/prop/'+str(ID)+'/'+name+'/'+str(value)+'/'+units+'', None, None))
    def addOrChangeMaterialProperty(self, ID, name, value, units): return bool(self.nfrest('POST', '/material/prop/'+str(ID)+'/'+name+'/'+value+'/'+units+'', None, None))
    def addOrModifyCustomData(self, key, value): return bool(self.nfrest('POST', '/model/customdata'+key+'', value, None))
    def addPipeSection(self, D, t): return int(self.nfrest('GET', '/section/add/pipe/'+str(D)+'/'+str(t)+'', None, None))
    def addPlanarSection(self, t): return int(self.nfrest('GET', '/section/add/planar/'+str(t)+'', None, None))
    def addQuad(self, n1, n2, n3, n4, sect, mat): return self.nfrest('GET', '/element/add/quad/'+n1+'/'+n2+'/'+n3+'/'+n4+'/'+str(sect)+'/'+str(mat)+'', None, None)
    def addRebarPattern(self, elem, pattern, Linit, Lfin, numBars, rebCover, matID, area, netSpacing): return bool(self.nfrest('GET', '/element/rebar/pattern/'+elem+'/'+str(pattern)+'/'+str(Linit)+'/'+str(Lfin)+'/'+str(numBars)+'/'+str(rebCover)+'/'+str(matID)+'/'+str(area)+'/'+str(netSpacing)+'', None, None))
    def addRebarPatternInSection(self, pattern, sectionID, numBars, rebCover, matID, area, netSpacing): return bool(self.nfrest('GET', '/section/rebar/pattern/'+str(pattern)+'/'+str(sectionID)+'/'+str(numBars)+'/'+str(rebCover)+'/'+str(matID)+'/'+str(area)+'/'+str(netSpacing)+'', None, None))
    def addRectangleInSection(self, sectionID, b, h, centerX, centerY, isEmpty, material, doNotCenter): return bool(self.nfrest('GET', '/section/add/addrect/'+str(sectionID)+'/'+str(b)+'/'+str(h)+'/'+str(centerX)+'/'+str(centerY)+'/'+str(isEmpty)+'/'+str(material)+'/'+str(doNotCenter)+'', None, None))
    def addRectSection(self, Lz, Ly): return int(self.nfrest('GET', '/section/add/rect/'+str(Lz)+'/'+str(Ly)+'', None, None))
    def addSectFromLib(self, name): return int(self.nfrest('GET', '/section/add/fromlib/'+name+'', None, None))
    def addSectFromLib(self, name, doNotCenter): return int(self.nfrest('GET', '/section/add/fromlib/'+name+'/'+str(doNotCenter)+'', None, None))
    def addSectionByPoints(self, x, y, CF_tw, CF_rc, material, doNotCenter): return int(self.nfrest('GET', '/section/add/bypoints/'+str(CF_tw)+'/'+str(CF_rc)+'/'+str(material)+'/'+str(doNotCenter)+'', None, dict([("x",json.dumps(x)),("y",json.dumps(y))])))
    def addSectionCover(self, sectionID, coverMat, coverThickness): return bool(self.nfrest('GET', '/section/add/cover/'+str(sectionID)+'/'+str(coverMat)+'/'+str(coverThickness)+'', None, None))
    def addSectionFromDXF(self, path, CF_tw, CF_rc, material): return int(self.nfrest('GET', '/section/add/fromdxf/'+str(CF_tw)+'/'+str(CF_rc)+'/'+str(material)+'', None, dict([("path",path)])))
    def addSeriesFunction(self, Xlist, Ylist, type, units): return int(self.nfrest('GET', '/function/add/'+str(type)+'', None, dict([("x",json.dumps(Xlist)),("y",json.dumps(Ylist)),("units",units)])))
    def addSineFunction(self, frequency, phase, stp, duration, maxAmplitude, isGrowing, type, units): return int(self.nfrest('GET', '/function/sine/'+str(frequency)+'/'+str(phase)+'/'+str(stp)+'/'+str(duration)+'/'+str(maxAmplitude)+'/'+str(isGrowing)+'/'+str(type)+'', None, dict([("units",units)])))
    def addSolid(self, nodes, mat): return self.nfrest('GET', '/element/add/solid/'+str(mat)+'', None, dict([("nodes",json.dumps(nodes))]))
    def addSpring(self, n1, n2, propName): return self.nfrest('GET', '/element/add/beam/'+n1+'/'+n2+'/'+propName+'', None, None)
    def addSpringNLProperty(self, name, NLdofs, NLprops, local): return bool(self.nfrest('POST', '/springproperty/nl/add/'+name+'/'+json.dumps(NLdofs)+'/'+str(local)+'', NLprops, None))
    def addSpringProperty(self, name, Kx, Ky, Kz, Krx, Kry, Krz, local): return bool(self.nfrest('GET', '/springproperty/simple/add/'+name+'/'+str(Kx)+'/'+str(Ky)+'/'+str(Kz)+'/'+str(Krx)+'/'+str(Kry)+'/'+str(Krz)+'/'+str(local)+'', None, None))
    def addSpringsOnOverlappedNodes(self, n, propName): return json.loads(self.nfrest('POST', '/element/add/springsonnodes/'+propName+'', n, None))
    def addStirrupBars(self, elem, LnumY, LnumZ, area, spacing, matID, Linit, Lfin): return bool(self.nfrest('GET', '/element/rebar/stirrup/'+elem+'/'+str(LnumY)+'/'+str(LnumZ)+'/'+str(area)+'/'+str(spacing)+'/'+str(matID)+'/'+str(Linit)+'/'+str(Lfin)+'', None, None))
    def addStirrupBarsInSection(self, sectionID, LnumY, LnumZ, area, spacing, matID): return bool(self.nfrest('GET', '/section/rebar/stirrup/'+str(sectionID)+'/'+str(LnumY)+'/'+str(LnumZ)+'/'+str(area)+'/'+str(spacing)+'/'+str(matID)+'', None, None))
    def addSubsoilNodalSpringsOnElements(self, n, propName): return bool(self.nfrest('POST', '/element/add/soilsprings/'+propName+'', n, None))
    def addSubsoilZProperty(self, width, Rmodulus): return self.nfrest('GET', '/springproperty/subsoil/add/'+str(width)+'/'+str(Rmodulus)+'', None, None)
    def addSurfaceLoad(self, elem, values, direction, loadcase, local): return bool(self.nfrest('POST', '/load/element/surfaceadd/'+elem+'/'+str(direction)+'/'+loadcase+'/'+str(local)+'', values, None))
    def addThermalDistLoad(self, elem, values, loadcase): return bool(self.nfrest('POST', '/load/element/tempdistadd/'+elem+'/'+loadcase+'', values, None))
    def addTria(self, n1, n2, n3, sect, mat): return self.nfrest('GET', '/element/add/tria/'+n1+'/'+n2+'/'+n3+'/'+str(sect)+'/'+str(mat)+'', None, None)
    def addTruss(self, n1, n2, sect, mat): return self.nfrest('GET', '/element/add/truss/'+n1+'/'+n2+'/'+str(sect)+'/'+str(mat)+'', None, None)
    def addTSection(self, Lz, Ly, tw, tf1): return int(self.nfrest('GET', '/section/add/tshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'', None, None))
    def addVolumeLoad(self, elem, value, direction, loadcase): return bool(self.nfrest('GET', '/load/element/volumeadd/'+elem+'/'+str(value)+'/'+str(direction)+'/'+loadcase+'', None, None))
    def alignShellXaxis(self, num, x, y, z): return bool(self.nfrest('GET', '/element/shellxaxis/'+num+'/'+str(x)+'/'+str(y)+'/'+str(z)+'', None, None))
    def AnalyzeFireElement(self, elem, endTime, beamExposure, columnExposure, checkCombo, selectForcesCrit, fireCurve, outOfProc, noWindow, customFireCurve): return json.loads(self.nfrest('GET', '/res/check/analyzefire/'+elem+'/'+str(endTime)+'/'+str(beamExposure)+'/'+str(columnExposure)+'/'+checkCombo+'/'+str(selectForcesCrit)+'/'+str(fireCurve)+'/'+str(outOfProc)+'/'+str(noWindow)+'/'+str(customFireCurve)+'', None, None))
    def appendDocXformula(self, TeXcode, alignment): return bool(self.nfrest('POST', '/op/docx/appendformula/'+str(alignment)+'', TeXcode, None))
    def appendDocXimage(self, imagePath, ratio, alignment): return bool(self.nfrest('GET', '/op/docx/appendimage/'+str(ratio)+'/'+str(alignment)+'', None, dict([("path",imagePath)])))
    def appendDocXtext(self, text, alignment, color, bold, italic, underline): return bool(self.nfrest('POST', '/op/docx/appendtext/'+str(alignment)+'/'+str(color)+'/'+str(bold)+'/'+str(italic)+'/'+str(underline)+'', text, None))
    def applyButterworthFilter(self, values, samplingF, cutF, order, lowPass): return json.loads(self.nfrest('POST', '/op/bwfilter/'+str(samplingF)+'/'+str(cutF)+'/'+str(order)+'/'+str(lowPass)+'', values, None))
    def applyEC8lateralForces(self, thID, loadCaseX, loadCaseY, propMasses, T1, ct, lam): return bool(self.nfrest('GET', '/load/lateralforces/'+str(thID)+'/'+loadCaseX+'/'+loadCaseY+'/'+str(propMasses)+'/'+str(T1)+'/'+str(ct)+'/'+str(lam)+'', None, None))
    def assignHinge(self, beamID, hingeName): return bool(self.nfrest('GET', '/hinge/assign/'+beamID+'/'+hingeName+'', None, None))
    def assignMaterialToElement(self, element, materialID): return bool(self.nfrest('GET', '/material/assign/'+element+'/'+str(materialID)+'', None, None))
    def assignSectionToElement(self, element, sectionID): return bool(self.nfrest('GET', '/section/assign/'+element+'/'+str(sectionID)+'', None, None))
    def assignSubsoilProperty(self, element, prop): return bool(self.nfrest('GET', '/springproperty/subsoil/assign/'+element+'/'+prop+'', None, None))
    def assignToGroup(self, name, nodes, elements, clear): return bool(self.nfrest('GET', '/group/assign/'+name+'/'+str(clear)+'', None, dict([("nodes",json.dumps(nodes)),("elements",json.dumps(elements))])))
    def changeDefSolverType(self, type): return bool(self.nfrest('GET', '/op/opt/changedefsolvertype/'+str(type)+'', None, None))
    def changeElementProperty(self, ID, prop, value): return bool(self.nfrest('POST', '/element/prop/'+ID+'/'+prop+'/'+value+'', None, None))
    def changeLoadValue(self, i, loadValue): return bool(self.nfrest('GET', '/load/change/'+str(i)+'/'+str(loadValue)+'', None, None))
    def changeOrAddSectionPoint(self, sectionID, seriesID, ptID, x, y): return bool(self.nfrest('GET', '/section/add/changeaddpt/'+str(sectionID)+'/'+str(seriesID)+'/'+str(ptID)+'/'+str(x)+'/'+str(y)+'', None, None))
    def changeSolver(self, type, path): return bool(self.nfrest('GET', '/op/opt/changesolver/'+str(type)+'', None, dict([("path",path)])))
    def changeSpringNLProperty(self, name, NLdofs, NLprops): return bool(self.nfrest('POST', '/springproperty/nl/change/'+name+'/'+json.dumps(NLdofs)+'', NLprops, None))
    def changeSpringNLPropertyDof(self, name, DoF, NLtype, NLprops): return bool(self.nfrest('POST', '/springproperty/nl/change/'+name+'/'+str(DoF)+'/'+str(NLtype)+'', NLprops, None))
    def changeSpringProperty(self, name, Kx, Ky, Kz, Krx, Kry, Krz): return bool(self.nfrest('GET', '/springproperty/simple/change/'+name+'/'+str(Kx)+'/'+str(Ky)+'/'+str(Kz)+'/'+str(Krx)+'/'+str(Kry)+'/'+str(Krz)+'', None, None))
    def checkElements(self, elems, lc, ts, stationType, verName, savelog, messages, defaultParams): return bool(self.nfrest('GET', '/res/check/elements/'+lc+'/'+ts+'/'+str(stationType)+'/'+verName+'/'+str(savelog)+'/'+str(messages)+'', None, dict([("defaultParams",json.dumps(defaultParams)),("elems",json.dumps(elems))])))
    def checkElementsRatio(self, elems, lc, ts, stationType, verName, savelog, messages, defaultParams): return float(self.nfrest('GET', '/res/check/elementsRatio/'+lc+'/'+ts+'/'+str(stationType)+'/'+verName+'/'+str(savelog)+'/'+str(messages)+'', None, dict([("defaultParams",json.dumps(defaultParams)),("elems",json.dumps(elems))])))
    def checkFreeNodes(self): return json.loads(self.nfrest('GET', '/op/mesh/findfreenodes', None, None))
    def checkLineElements(self): return int(self.nfrest('GET', '/op/mesh/lineelems', None, None))
    def checkModel(self, lc, ts, stationType, verName, savelog, messages, defaultParams): return bool(self.nfrest('GET', '/res/check/model/'+lc+'/'+ts+'/'+str(stationType)+'/'+verName+'/'+str(savelog)+'/'+str(messages)+'', None, dict([("defaultParams",json.dumps(defaultParams))])))
    def checkNodes(self, nodes, lc, ts, stationType, verName, savelog, messages, defaultParams): return bool(self.nfrest('GET', '/res/check/nodes/'+lc+'/'+ts+'/'+str(stationType)+'/'+verName+'/'+str(savelog)+'/'+str(messages)+'', None, dict([("defaultParams",json.dumps(defaultParams)),("nodes",json.dumps(nodes))])))
    def checkOverlappedElements(self): return json.loads(self.nfrest('GET', '/op/mesh/findoverlappedelements', None, None))
    def clearElementCustomProperties(self, elem): return bool(self.nfrest('DELETE', '/element/customprop/'+elem+'', None, None))
    def clearElementRebar(self, elem): return bool(self.nfrest('GET', '/element/rebar/clear/'+elem+'', None, None))
    def clearSectionRebar(self, ID): return bool(self.nfrest('GET', '/section/rebar/clear/'+ID+'', None, None))
    def clearSectionRebar(self, ID): return bool(self.nfrest('GET', '/section/rebar/clear/'+str(ID)+'', None, None))
    def clearSelection(self): return bool(self.nfrest('GET', '/op/clearselection', None, None))
    def clearStoredDomains(self): return bool(self.nfrest('GET', '/res/check/cleardomains', None, None))
    def colorizeModel(self, criterion, excl): return self.nfrest('GET', '/model/colors/colorize/'+str(criterion)+'', None, dict([("excl",json.dumps(excl))]))
    def convertToMeshedSection(self, sectionID): return int(self.nfrest('GET', '/op/mesh/meshedsection/'+str(sectionID)+'', None, None))
    def convertUnits(self, length, force): return self.nfrest('GET', '/units/convertunits/'+length+'/'+force+'', None, None)
    def convertValue(self, value, OldUnits, NewUnits): return float(self.nfrest('GET', '/units/convert/'+str(value)+'', None, dict([("OldUnits",OldUnits),("NewUnits",NewUnits)])))
    def createDocX(self, path, text, template): return bool(self.nfrest('GET', '/op/docx/create'+json.dumps(text)+'', None, dict([("path",path),("template",template)])))
    def CustomLicense(self, lic): return bool(self.nfrest('GET', '/op/lic', None, dict([("val",lic)])))
    def defaultColors(self): return self.nfrest('GET', '/model/colors/default', None, None)
    def deleteChecks(self): return bool(self.nfrest('GET', '/res/delchecks', None, None))
    def deleteGroup(self, name): return bool(self.nfrest('GET', '/group/delete/'+name+'', None, None))
    def deleteResults(self): return bool(self.nfrest('GET', '/res/delete', None, None))
    def divideHexa(self, hexaID, divX, divY, divZ): return json.loads(self.nfrest('GET', '/op/mesh/dividehexa/'+hexaID+'/'+str(divX)+'/'+str(divY)+'/'+str(divZ)+'', None, None))
    def divideLine(self, lines, fractions): return json.loads(self.nfrest('GET', '/op/mesh/divideline', None, dict([("lines",json.dumps(lines)),("fractions",json.dumps(fractions))])))
    def divideLineByNodes(self, line, nodes): return bool(self.nfrest('GET', '/op/mesh/dividelinebynodes/'+line+'', None, dict([("nodes",json.dumps(nodes))])))
    def divideQuad(self, quadID, divX, divY): return json.loads(self.nfrest('GET', '/op/mesh/dividequad/'+quadID+'/'+str(divX)+'/'+str(divY)+'', None, None))
    def divideWedge(self, wedgeID, div): return json.loads(self.nfrest('GET', '/op/mesh/dividewedge/'+wedgeID+'/'+str(div)+'', None, None))
    def duplicateSection(self, originalID): return int(self.nfrest('GET', '/section/duplicate/'+str(originalID)+'', None, None))
    def exportGLTF(self, path, saveIFC): return bool(self.nfrest('GET', '/op/export/gltf/'+str(saveIFC)+'', None, dict([("path",path)])))
    def exportIFC(self, path, saveAsXML): return bool(self.nfrest('GET', '/op/export/ifc/'+str(saveAsXML)+'', None, dict([("path",path)])))
    def exportIOM(self, filename): return bool(self.nfrest('GET', '/op/export/idea', None, dict([("path",filename)])))
    def exportMidas(self, path): return bool(self.nfrest('GET', '/op/export/midas', None, dict([("path",path)])))
    def exportOpenSees(self, path, loadcase): return bool(self.nfrest('GET', '/op/export/opensees/'+loadcase+'', None, dict([("path",path)])))
    def exportRCbeamsDXF(self, path, elements): return bool(self.nfrest('GET', '/element/exportdxf', None, dict([("path",path),("elements",json.dumps(elements))])))
    def exportRCmemberDXF(self, path, member): return bool(self.nfrest('GET', '/model/member/exportdxf/'+member+'', None, dict([("path",path)])))
    def exportSAP2000(self, path): return bool(self.nfrest('GET', '/op/export/sap2000', None, dict([("path",path)])))
    def exportSectionDXF(self, path, sID): return bool(self.nfrest('GET', '/section/exportdxf/'+str(sID)+'', None, dict([("path",path)])))
    def exportWexBIM(self, path, saveIFC, copyViewer): return bool(self.nfrest('GET', '/op/export/wexbim/'+str(saveIFC)+'/'+str(copyViewer)+'', None, dict([("path",path)])))
    def exportXMLresults(self, filename): return bool(self.nfrest('GET', '/op/export/xmlres', None, dict([("path",filename)])))
    def functionFromFile(self, filename, type, units): return int(self.nfrest('GET', '/function/fromfile/'+str(type)+'', None, dict([("units",units),("path",filename)])))
    def generateFrame(self, baysX, baysY, sn, ddx, ddy, ddz, sx, sy, sz, matx, maty, matz, lc1, lc2, lc3, Lval1, Lval2, Lval3, loadBeamX, rigidfloor): return bool(self.nfrest('GET', '/op/mesh/generateframe/'+str(baysX)+'/'+str(baysY)+'/'+str(sn)+'/'+str(ddx)+'/'+str(ddy)+'/'+str(ddz)+'/'+str(sx)+'/'+str(sy)+'/'+str(sz)+'/'+str(matx)+'/'+str(maty)+'/'+str(matz)+'/'+lc1+'/'+lc2+'/'+lc3+'/'+str(Lval1)+'/'+str(Lval2)+'/'+str(Lval3)+'/'+str(loadBeamX)+'/'+str(rigidfloor)+'', None, None))
    def generateLoadCombinations(self, type, comboPrefix): return bool(self.nfrest('GET', '/loadcase/generate/'+str(type)+'/'+comboPrefix+'', None, None))
    def getAlignedNodes(self, n1, n2, tol): return json.loads(self.nfrest('GET', '/op/mesh/alignednodes/'+str(tol)+'', None, dict([("n1",n1),("n2",n2)])))
    def getAnalysisTimeSteps(self, lc): return json.loads(self.nfrest('GET', '/res/steps/'+lc+'', None, None))
    def getAreaByNodes(self, nodes): return float(self.nfrest('POST', '/node/area', nodes, None))
    def getBC(self, node): return json.loads(self.nfrest('GET', '/bc/get/'+node+'', None, None))
    def getBeamDeflection(self, num, loadcase, time, type, station): return float(self.nfrest('GET', '/res/beamdeflection/'+num+'/'+loadcase+'/'+time+'/'+str(type)+'/'+str(station)+'', None, None))
    def getBeamDeflections(self, num, loadcase, type, offsetL, numStations, time): return self.nfrest('GET', '/res/beamdeflections/'+num+'/'+loadcase+'/'+str(type)+'/'+str(offsetL)+'/'+str(numStations)+'/'+time+'', None, None)
    def getBeamForce(self, num, loadcase, time, type, station): return float(self.nfrest('GET', '/res/beamforce/'+num+'/'+loadcase+'/'+time+'/'+str(type)+'/'+str(station)+'', None, None))
    def getBeamForce2(self, num, loadcase, time, type, absissa): return float(self.nfrest('GET', '/res/beamforce2/'+num+'/'+loadcase+'/'+time+'/'+str(type)+'/'+str(absissa)+'', None, None))
    def getBeamForces(self, num, loadcase, station, time): return json.loads(self.nfrest('GET', '/res/beamforces/'+num+'/'+loadcase+'/'+str(station)+'/'+time+'', None, None))
    def getBeamForcesAtNode(self, elem, node, loadcase, time): return json.loads(self.nfrest('GET', '/res/beamforcesatnode/'+elem+'/'+node+'/'+loadcase+'/'+time+'', None, None))
    def getBeamForcesDiagram(self, num, loadcase, type, offsetL, numStations, time): return self.nfrest('GET', '/res/beamdiagram/'+num+'/'+loadcase+'/'+str(type)+'/'+str(offsetL)+'/'+str(numStations)+'/'+time+'', None, None)
    def getBeamResMoments(self, elemID): return json.loads(self.nfrest('GET', '/res/check/beammoments/'+elemID+'', None, None))
    def getBeamResShear(self, elemID, loadcase, time): return json.loads(self.nfrest('GET', '/res/check/beamshearres/'+elemID+'/'+loadcase+'/'+time+'', None, None))
    def getBuiltInChecking(self): return json.loads(self.nfrest('GET', '/res/check/sets', None, None))
    def getCheckNameByMaterial(self, ID): return self.nfrest('GET', '/res/check/checkbymat/'+ID+'', None, None)
    def getCombinationCoeffPsi(self, subscript, type): return float(self.nfrest('GET', '/loadcase/getpsi/'+str(subscript)+'/'+str(type)+'', None, None))
    def getCombinationDesignType(self, name): return int(self.nfrest('GET', '/loadcase/combo/designtype/'+name+'', None, None))
    def getCombinationsByDesignType(self, type, servType): return json.loads(self.nfrest('GET', '/loadcases/descombos/designtype/'+str(type)+'/'+str(servType)+'', None, None))
    def getConnectedElements(self, node, onlyOfType): return json.loads(self.nfrest('GET', '/node/connectedelements/'+node+'/'+str(onlyOfType)+'', None, None))
    def getControlNode(self): return self.nfrest('GET', '/op/controlnode', None, None)
    def getCornerNodes(self, nodes, lcs): return json.loads(self.nfrest('GET', '/op/corners', None, dict([("nodes",json.dumps(nodes)),("lcs",json.dumps(lcs))])))
    def getCustomData(self, key): return self.nfrest('GET', '/model/customdata/'+key+'', None, None)
    def getDataPlot(self, xseries, yseries, imagePath, name, Xunits, Yunits): return bool(self.nfrest('GET', '/function/plotdata/'+name+'', None, dict([("path",imagePath),("xseries",json.dumps(xseries)),("yseries",json.dumps(yseries)),("Xunits",Xunits),("Yunits",Yunits)])))
    def getDefinedDesignMaterials(self): return json.loads(self.nfrest('GET', '/designmaterials', None, None))
    def getDefinedMaterials(self): return json.loads(self.nfrest('GET', '/materials', None, None))
    def getDefinedSections(self): return json.loads(self.nfrest('GET', '/sections', None, None))
    def getDesignMaterialsLibrary(self, filter, type): return json.loads(self.nfrest('GET', '/designmaterials/library/'+filter+'/'+str(type)+'', None, None))
    def getDesignMaterialsLibrary(self, filename, filter, type): return json.loads(self.nfrest('GET', '/designmaterials/libraryf/'+filename+'/'+filter+'/'+str(type)+'', None, None))
    def getElementArea(self, ID): return float(self.nfrest('GET', '/element/area/'+ID+'', None, None))
    def getElementCentroid(self, ID): return json.loads(self.nfrest('GET', '/element/centroid/'+ID+'', None, None))
    def getElementChecks(self, ID, lc, time): return self.nfrest('GET', '/res/check/elementA/'+ID+'/'+lc+'/'+time+'', None, None)
    def getElementConnectivity(self, ID): return json.loads(self.nfrest('GET', '/element/conn/'+ID+'', None, None))
    def getElementCustomProperty(self, elem, propName): return self.nfrest('GET', '/element/customprop/'+elem+'/'+propName+'', None, None)
    def getElementInfo(self, element): return json.loads(self.nfrest('GET', '/element/info/'+element+'', None, None))
    def getElementOffset(self, elem): return json.loads(self.nfrest('GET', '/element/beamoffset/'+elem+'', None, None))
    def getElementProperty(self, ID, name): return self.nfrest('GET', '/element/prop/'+ID+'/'+name+'', None, None)
    def getElementRebarSegments(self, elem): return json.loads(self.nfrest('GET', '/section/rebar/segments/'+elem+'', None, None))
    def getElementsChecks(self, lc, time): return json.loads(self.nfrest('GET', '/res/check/elementsA/'+lc+'/'+time+'', None, None))
    def getElementsChecksByMat(self, mat): return json.loads(self.nfrest('GET', '/res/check/elementsM/'+str(mat)+'', None, None))
    def getElementsFromGroup(self, name): return json.loads(self.nfrest('GET', '/group/elements/'+name+'', None, None))
    def getElementType(self, ID): return self.nfrest('GET', '/element/type/'+ID+'', None, None)
    def getElementVolume(self, ID): return float(self.nfrest('GET', '/element/volume/'+ID+'', None, None))
    def getEndRelease(self, beamID): return json.loads(self.nfrest('GET', '/element/beamendrelease/'+beamID+'', None, None))
    def getEnvelopeCombination(self, name): return self.nfrest('GET', '/loadcase/combo/getenv/'+name+'', None, None)
    def getExtrudedBeamPoints(self, elemID): return json.loads(self.nfrest('GET', '/element/extrudedbeam/'+elemID+'', None, None))
    def getFirstMode(self, ct): return float(self.nfrest('GET', '/res/firstmode/'+str(ct)+'', None, None))
    def getFloorLoadType(self, name): return self.nfrest('GET', '/load/floor/planetype/'+name+'', None, None)
    def getFloorPlanes(self): return json.loads(self.nfrest('GET', '/load/floor/planesget', None, None))
    def getForceUnit(self): return self.nfrest('GET', '/units/f', None, None)
    def getFreeElementID(self): return self.nfrest('GET', '/op/freeelementid', None, None)
    def getFreeNodeID(self): return self.nfrest('GET', '/op/freenodeid', None, None)
    def getFunctionGeneralData(self, funcID): return json.loads(self.nfrest('GET', '/function/gendata/'+str(funcID)+'', None, None))
    def getFunctionName(self, funcID): return self.nfrest('GET', '/function/name/'+str(funcID)+'', None, None)
    def getFunctionPlot(self, funcID, imagePath): return bool(self.nfrest('GET', '/function/plot/'+str(funcID)+'', None, dict([("path",imagePath)])))
    def getFunctions(self): return json.loads(self.nfrest('GET', '/functions', None, None))
    def getFunctionUnits(self, funcID): return self.nfrest('GET', '/function/units/'+str(funcID)+'', None, None)
    def getGreekLetter(self, input): return self.nfrest('GET', '/op/greek'+input+'', None, None)
    def getGroups(self): return json.loads(self.nfrest('GET', '/groups', None, None))
    def getLanguage(self): return self.nfrest('GET', '/op/opt/lang', None, None)
    def getLastBilinearMomentCurvature(self): return json.loads(self.nfrest('GET', '/op/sectioncalc/bilmomentcurvature', None, None))
    def getLastMomentCurvatureData(self): return json.loads(self.nfrest('GET', '/op/sectioncalc/momentcurvaturedata', None, None))
    def getLastRunLog(self): return json.loads(self.nfrest('GET', '/op/runlog', None, None))
    def getLenUnit(self): return self.nfrest('GET', '/units/l', None, None)
    def getLinearAddCombination(self, name): return self.nfrest('GET', '/loadcase/combo/get/'+name+'', None, None)
    def getLoad(self, i): return self.nfrest('GET', '/load/'+str(i)+'', None, None)
    def getLoadA(self, i): return json.loads(self.nfrest('GET', '/load/getA/'+str(i)+'', None, None))
    def getLoadcaseFactor(self, loadcase): return float(self.nfrest('GET', '/loadcase/getfactor/'+loadcase+'', None, None))
    def getLoadCases(self): return json.loads(self.nfrest('GET', '/loadcases', None, None))
    def getLoadCombinations(self, includeEnvelopes): return json.loads(self.nfrest('GET', '/loadcase/combos/'+str(includeEnvelopes)+'', None, None))
    def getLoadDurationClass(self, loadcase): return int(self.nfrest('GET', '/load/getduration/'+loadcase+'', None, None))
    def getLoadingData(self): return self.nfrest('GET', '/model/loadingdata', None, None)
    def getLoadsForElement(self, element): return json.loads(self.nfrest('GET', '/load/element/get/'+element+'', None, None))
    def getLoadsForNode(self, node): return json.loads(self.nfrest('GET', '/load/node/get/'+node+'', None, None))
    def getLoadsInLoadcase(self, loadcase): return json.loads(self.nfrest('GET', '/load/inloadcase/'+loadcase+'', None, None))
    def getLocalAxes(self, ID): return json.loads(self.nfrest('GET', '/element/lcs/'+ID+'', None, None))
    def getLocalAxesArray(self, ID): return json.loads(self.nfrest('GET', '/element/lcsA/'+ID+'', None, None))
    def getMacroelement(self, elemID): return int(self.nfrest('GET', '/element/macro/'+elemID+'', None, None))
    def getMaterialsLibrary(self, filter, type): return json.loads(self.nfrest('GET', '/materials/library/'+filter+'/'+str(type)+'', None, None))
    def getMaterialsLibrary(self, filename, filter, type): return json.loads(self.nfrest('GET', '/materials/libraryf/'+filename+'/'+filter+'/'+str(type)+'', None, None))
    def getMaxMinBeamForces(self, sectionID, type): return json.loads(self.nfrest('GET', '/res/maxminbeamforces/'+str(sectionID)+'/'+str(type)+'', None, None))
    def getMaxMinNodeDispl(self, dir, nodes): return json.loads(self.nfrest('POST', '/res/maxmindispl/'+str(dir)+'', nodes, None))
    def getMaxMinWoodArmerMoments(self, elementID): return json.loads(self.nfrest('GET', '/res/maxminwoodarmer/'+str(elementID)+'', None, None))
    def getMaxMinWoodArmerMoments(self, groupName): return json.loads(self.nfrest('GET', '/res/maxminwoodarmerg/'+groupName+'', None, None))
    def getMemberElements(self, member): return json.loads(self.nfrest('GET', '/model/member/elems/'+member+'', None, None))
    def getMemberLength(self, member): return float(self.nfrest('GET', '/model/member/leng/'+member+'', None, None))
    def getMembers(self): return json.loads(self.nfrest('GET', '/model/member/all', None, None))
    def getModalPeriod(self, num, loadcase): return float(self.nfrest('GET', '/res/period/'+str(num)+'/'+loadcase+'', None, None))
    def getNodalDisp(self, num, loadcase, time, direction): return float(self.nfrest('GET', '/res/displacement/'+num+'/'+loadcase+'/'+time+'/'+str(direction)+'', None, None))
    def getNodalReact(self, num, loadcase, time, direction): return float(self.nfrest('GET', '/res/reaction/'+num+'/'+loadcase+'/'+time+'/'+str(direction)+'', None, None))
    def getNodalShellForce(self, num, loadcase, time, type): return float(self.nfrest('GET', '/res/nodalshellforce/'+num+'/'+loadcase+'/'+time+'/'+type+'', None, None))
    def getNodalStress(self, num, loadcase, time, type): return float(self.nfrest('GET', '/res/nodalstress/'+num+'/'+loadcase+'/'+time+'/'+type+'', None, None))
    def getNodeChecks(self, ID, lc, time): return self.nfrest('GET', '/res/check/nodsA/'+ID+'/'+lc+'/'+time+'', None, None)
    def getNodeCoordinates(self, ID): return json.loads(self.nfrest('GET', '/node/ID'+ID+'', None, None))
    def getNodeInfo(self, node): return json.loads(self.nfrest('GET', '/node/info/'+node+'', None, None))
    def getNodePosition(self, ID): return self.nfrest('GET', '/node/ID'+ID+'', None, None)
    def getNodeProperty(self, ID, name): return self.nfrest('GET', '/node/prop/'+ID+'/'+name+'', None, None)
    def getNodesChecks(self, lc, time): return json.loads(self.nfrest('GET', '/res/check/nodesA/'+lc+'/'+time+'', None, None))
    def getNodesFromCoords(self, dir, coord, tol): return json.loads(self.nfrest('GET', '/op/mesh/nodesbycoords/'+str(dir)+'/'+str(coord)+'/'+str(tol)+'', None, None))
    def getNodesFromGroup(self, name): return json.loads(self.nfrest('GET', '/group/nodes/'+name+'', None, None))
    def getNodesOnSides(self, nodes, tol): return json.loads(self.nfrest('GET', '/op/mesh/borders/'+str(tol)+'', None, dict([("nodes",json.dumps(nodes))])))
    def getOSprocedureName(self): return self.nfrest('GET', '/op/export/osproc', None, None)
    def getParticipatingMassesRatios(self, mode, loadcase): return json.loads(self.nfrest('GET', '/res/partmasses/'+str(mode)+'/'+loadcase+'', None, None))
    def getParticipationFactors(self, mode, loadcase): return json.loads(self.nfrest('GET', '/res/partfactors/'+str(mode)+'/'+loadcase+'', None, None))
    def getReinfPropertiesNTC(self, matID, secID, CF, betaAng, Hshear, Bshear, outInMPa): return json.loads(self.nfrest('GET', '/material/frpdata/'+str(matID)+'/'+str(secID)+'/'+str(CF)+'/'+str(betaAng)+'/'+str(Hshear)+'/'+str(Bshear)+'/'+str(outInMPa)+'', None, None))
    def getResultHistory(self, loadcase, itemID, resultType, resultID1, resultID2): return json.loads(self.nfrest('GET', '/res/hist/'+loadcase+'/'+itemID+'/'+str(resultType)+'/'+str(resultID1)+'/'+str(resultID2)+'', None, None))
    def getRigidDiaphragms(self): return json.loads(self.nfrest('GET', '/op/mesh/rigiddiaph', None, None))
    def getRigidOffsets(self, beamID): return json.loads(self.nfrest('GET', '/element/beamendoffset/'+beamID+'', None, None))
    def getSectionColor(self, ID): return int(self.nfrest('GET', '/section/set/color/'+ID+'', None, None))
    def getSectionCutForce(self, groupName, loadcase, time, type): return float(self.nfrest('GET', '/res/sectioncutforce/'+groupName+'/'+loadcase+'/'+time+'/'+str(type)+'', None, None))
    def getSectionFigure(self, sectionID, figureID, isHole): return json.loads(self.nfrest('GET', '/section/figure/'+str(sectionID)+'/'+str(figureID)+'/'+str(isHole)+'', None, None))
    def getSectionOffset(self, ID): return json.loads(self.nfrest('GET', '/section/set/offset/'+ID+'', None, None))
    def getSectionProperties(self, ID): return json.loads(self.nfrest('GET', '/section/props/'+ID+'', None, None))
    def getSectionProperty(self, ID, name): return self.nfrest('GET', '/section/prop/'+ID+'/'+name+'', None, None)
    def getSectionRebarCoords(self, ID): return json.loads(self.nfrest('GET', '/section/rebar/coords/'+ID+'', None, None))
    def getSectionResDomainPoints(self, domainIndex, domainType, cleanResponseTolerance): return json.loads(self.nfrest('GET', '/res/check/plotsectiondomain/'+str(domainIndex)+'/'+str(domainType)+'/'+str(cleanResponseTolerance)+'', None, None))
    def getSectionResMoments(self, ID, station, calcType, N, Myy, Mzz): return self.nfrest('GET', '/op/sectioncalc/a/'+ID+'/'+str(station)+'/'+str(calcType)+'/'+str(N)+'/'+str(Myy)+'/'+str(Mzz)+'', None, None)
    def getSectionResMoments(self, sectionID, materialID, calcType, N, Myy, Mzz): return self.nfrest('GET', '/op/sectioncalc/b/'+sectionID+'/'+materialID+'/'+str(calcType)+'/'+str(N)+'/'+str(Myy)+'/'+str(Mzz)+'', None, None)
    def getSectionResShear(self, sectionID, N, Mzz, Myy, Vy, Vz): return json.loads(self.nfrest('GET', '/op/sectioncalc/shear/'+str(sectionID)+'/'+str(N)+'/'+str(Mzz)+'/'+str(Myy)+'/'+str(Vy)+'/'+str(Vz)+'', None, None))
    def getSectionResShear(self, sectionID, verName, N, Mzz, Myy, Vy, Vz): return json.loads(self.nfrest('GET', '/op/sectioncalc/shear/'+str(sectionID)+'/'+verName+'/'+str(N)+'/'+str(Mzz)+'/'+str(Myy)+'/'+str(Vy)+'/'+str(Vz)+'', None, None))
    def getSectionsLibrary(self, filter): return json.loads(self.nfrest('GET', '/sections/library/'+filter+'', None, None))
    def getSectionsLibrary(self, filename, filter): return json.loads(self.nfrest('GET', '/sections/libraryf/'+filename+'/'+filter+'', None, None))
    def getSectMomentCurvature(self, sectionID, N, Mzz, Myy, npts, Nserv, Mzzserv, Myyserv): return json.loads(self.nfrest('GET', '/op/sectioncalc/momentcurvature/'+str(sectionID)+'/'+str(N)+'/'+str(Mzz)+'/'+str(Myy)+'/'+str(npts)+'/'+str(Nserv)+'/'+str(Mzzserv)+'/'+str(Myyserv)+'', None, None))
    def getSeparator(self): return self.nfrest('GET', '/op/sep', None, None)
    def getShellEndRelease(self, ID): return json.loads(self.nfrest('GET', '/element/shellendrelease/'+ID+'', None, None))
    def getSoilPressureAtNode(self, node, loadcase, time): return float(self.nfrest('GET', '/res/soilpressureatnode/'+node+'/'+loadcase+'/'+time+'', None, None))
    def getSpringLocalAxes(self, elem): return json.loads(self.nfrest('GET', '/springproperty/axes/'+elem+'', None, None))
    def getSubsoilElements(self): return json.loads(self.nfrest('GET', '/element/add/subsoil', None, None))
    def getTimePeriods(self, lc): return json.loads(self.nfrest('GET', '/res/periods/'+lc+'', None, None))
    def getVersion(self): return float(self.nfrest('GET', '/version', None, None))
    def getWallGroups(self): return json.loads(self.nfrest('GET', '/element/walls/list', None, None))
    def getWallHeight(self, grpName): return float(self.nfrest('GET', '/element/walls/height/'+grpName+'', None, None))
    def getWalls(self): return json.loads(self.nfrest('GET', '/element/walls/elems', None, None))
    def getWallSection(self, grpName): return json.loads(self.nfrest('GET', '/element/walls/section/'+grpName+'', None, None))
    def hasResults(self, loadcase): return bool(self.nfrest('GET', '/res', None, dict([("lc",loadcase)])))
    def importAbaqusCalculix(self, path): return bool(self.nfrest('GET', '/op/import/abaqus', None, dict([("path",path)])))
    def importDolmen(self, path): return bool(self.nfrest('GET', '/op/import/dolmen', None, dict([("path",path)])))
    def importDXF(self, path): return bool(self.nfrest('GET', '/op/import/dxf', None, dict([("path",path)])))
    def importDXF(self, stream): return bool(self.nfrest('POST', '/op/import/dxfstream', stream, None))
    def importIFC(self, path, includeRigidLinks): return bool(self.nfrest('GET', '/op/import/ifc/'+str(includeRigidLinks)+'', None, dict([("path",path)])))
    def importMidas(self, path): return bool(self.nfrest('GET', '/op/import/midasfile', None, dict([("path",path)])))
    def importMidas(self, model): return bool(self.nfrest('POST', '/op/import/midastext', model, None))
    def importMidasResults(self, path): return bool(self.nfrest('GET', '/op/import/midasresult', None, dict([("path",path)])))
    def importMidasResults(self, text): return bool(self.nfrest('POST', '/op/import/midasresulttext', text, None))
    def importOpenSees(self, path): return bool(self.nfrest('GET', '/op/import/opensees', None, dict([("path",path)])))
    def importOpenSeesRecorder(self, path, type, useTimeFlag): return bool(self.nfrest('GET', '/op/import/recorder/'+str(type)+'/'+str(useTimeFlag)+'', None, dict([("path",path)])))
    def importSAF(self, path): return bool(self.nfrest('GET', '/op/import/saf', None, dict([("path",path)])))
    def importSAP2000(self, path): return bool(self.nfrest('GET', '/op/import/sap2000', None, dict([("path",path)])))
    def importSeismoStruct(self, path): return bool(self.nfrest('GET', '/op/import/seismostruct', None, dict([("path",path)])))
    def importSismicad(self, path, lenUnit, forceUnit): return bool(self.nfrest('GET', '/op/import/sismicad'+lenUnit+'/'+forceUnit+'', None, dict([("path",path)])))
    def importSismicadSects_Combo(self, path): return bool(self.nfrest('GET', '/op/import/sismicadset', None, dict([("path",path)])))
    def importSismicadSects_Combo(self, text): return bool(self.nfrest('POST', '/op/import/sismicadsettext', text, None))
    def importSofistik(self, path): return bool(self.nfrest('GET', '/op/import/sofistik', None, dict([("path",path)])))
    def importSR3(self, path): return bool(self.nfrest('GET', '/op/import/sr3', None, dict([("path",path)])))
    def importSR4(self, path): return bool(self.nfrest('GET', '/op/import/sr4', None, dict([("path",path)])))
    def importStraus7(self, path): return bool(self.nfrest('GET', '/op/import/straus7', None, dict([("path",path)])))
    def importStrausResults(self, path): return bool(self.nfrest('GET', '/op/import/straus7result', None, dict([("path",path)])))
    def importStrausResults(self, text): return bool(self.nfrest('POST', '/op/import/straus7resulttext', text, None))
    def importWinStrand(self, path): return bool(self.nfrest('GET', '/op/import/winstrand', None, dict([("path",path)])))
    def is64bit(self): return bool(self.nfrest('GET', '/op/is64bit', None, None))
    def isColumn(self, beamID): return bool(self.nfrest('GET', '/element/iscolumn/'+beamID+'', None, None))
    def isNodeLoaded(self, node): return bool(self.nfrest('GET', '/load/node/isloaded/'+node+'', None, None))
    def isRestrained(self, node): return bool(self.nfrest('GET', '/bc/node/'+node+'', None, None))
    def LangTrasl(self, input): return self.nfrest('POST', '/op/trasl', input, None)
    def LaunchLoadCase(self, loadcase, outOfProc, noWindow): return bool(self.nfrest('GET', '/op/launchlc/'+loadcase+'/'+str(outOfProc)+'/'+str(noWindow)+'', None, None))
    def LaunchModel(self, outOfProc, noWindow): return bool(self.nfrest('GET', '/op/launchmodel/'+str(outOfProc)+'/'+str(noWindow)+'', None, None))
    def listDesignMaterialCustomProperty(self, ID): return json.loads(self.nfrest('GET', '/designmaterial/proplist/'+str(ID)+'', None, None))
    def listMaterialCustomProperty(self, ID): return json.loads(self.nfrest('GET', '/material/proplist/'+str(ID)+'', None, None))
    def LoadCaseFromCombo(self, comboName): return self.nfrest('GET', '/loadcase/fromcombo/'+comboName+'', None, None)
    def mergeImportedLines(self, lineIDs): return bool(self.nfrest('GET', '/op/mesh/mergeimportedlines', None, dict([("lines",json.dumps(lineIDs))])))
    def mergeLines(self, lineIDs): return bool(self.nfrest('GET', '/op/mesh/mergelines', None, dict([("lines",json.dumps(lineIDs))])))
    def mergeModelData(self, modeldata): return bool(self.nfrest('PUT', '/model/data'+modeldata+'', None, None))
    def mergeModelResults(self, modelresults): return bool(self.nfrest('PUT', '/model/results'+modelresults+'', None, None))
    def mergeOverlappedNodes(self): return bool(self.nfrest('GET', '/op/mesh/mergenodes', None, None))
    def ModelToSection(self, openModelPath): return self.nfrest('GET', '/model/model2section', None, dict([("path",openModelPath)]))
    def moveNodes(self, nodes, displX, displY, displZ, absolutePosition): return bool(self.nfrest('GET', '/op/mesh/movenodes/'+str(displX)+'/'+str(displY)+'/'+str(displZ)+'/'+str(absolutePosition)+'', None, dict([("nodes",json.dumps(nodes))])))
    def newModel(self): return self.nfrest('GET', '/op/new', None, None)
    def openIDEAcodeCheck(self): return self.nfrest('GET', '/op/export/ccm', None, None)
    def openModel(self, filename): return bool(self.nfrest('GET', '/op/open', None, dict([("path",filename)])))
    def quad2tria(self, elem): return bool(self.nfrest('GET', '/op/mesh/quad2tria/'+elem+'', None, None))
    def readBeamForces(self, num, loadcase, time, N, Vy, Vz, Mt, Myy, Mzz, pos): return bool(self.nfrest('GET', '/res/import/beamforces/'+num+'/'+loadcase+'/'+time+'/'+str(N)+'/'+str(Vy)+'/'+str(Vz)+'/'+str(Mt)+'/'+str(Myy)+'/'+str(Mzz)+'/'+str(pos)+'', None, None))
    def recalculateSection(self, ID): return bool(self.nfrest('GET', '/section/recalc/'+str(ID)+'', None, None))
    def refreshHinges(self): return bool(self.nfrest('GET', '/hinge/refresh', None, None))
    def removeAllLoads(self): return bool(self.nfrest('DELETE', '/load/all', None, None))
    def removeAllLoadsForLoadcase(self, lc): return bool(self.nfrest('DELETE', '/load/alllc/'+lc+'', None, None))
    def removeBC(self, node): return bool(self.nfrest('DELETE', '/bc/'+node+'', None, None))
    def removeCompositeFlags(self, ID): return bool(self.nfrest('GET', '/section/set/removecomposite/'+str(ID)+'', None, None))
    def removeCustomData(self, key): return bool(self.nfrest('DELETE', '/model/customdata/'+key+'', None, None))
    def removeDesMaterialProperty(self, ID, name): return bool(self.nfrest('DELETE', '/designmaterial/prop/'+str(ID)+'/'+name+'', None, None))
    def removeElement(self, ID): return bool(self.nfrest('DELETE', '/element/'+ID+'', None, None))
    def removeElementsFromMember(self, member, elems): return bool(self.nfrest('DELETE', '/model/member/elems/'+member+'', None, dict([("elems",json.dumps(elems))])))
    def removeFloorLoad(self, name): return bool(self.nfrest('GET', '/load/floor/remove/'+name+'', None, None))
    def removeFloorPlane(self, name): return bool(self.nfrest('GET', '/load/floor/planeremove/'+name+'', None, None))
    def removeFreeNodes(self): return bool(self.nfrest('GET', '/op/mesh/removefreenodes', None, None))
    def removeHinges(self, beamID): return bool(self.nfrest('GET', '/hinge/remove/'+beamID+'', None, None))
    def removeLink(self, node): return bool(self.nfrest('DELETE', '/op/mesh/constraint/'+node+'', None, None))
    def removeLoad(self, ID): return bool(self.nfrest('DELETE', '/load/'+str(ID)+'', None, None))
    def removeLoadCase(self, name): return bool(self.nfrest('DELETE', '/loadcase/'+name+'', None, None))
    def removeLoadCaseFromCombination(self, name, loadcase): return bool(self.nfrest('GET', '/loadcase/combo/remove/'+name+'/'+loadcase+'', None, None))
    def removeLoadCaseToTimeHistoryAnalysis(self, name, loadcase): return bool(self.nfrest('GET', '/loadcase/combo/removeth/'+name+'/'+loadcase+'', None, None))
    def removeMaterial(self, materialID): return bool(self.nfrest('GET', '/material/remove/'+str(materialID)+'', None, None))
    def removeMaterialProperty(self, ID, name): return bool(self.nfrest('DELETE', '/material/prop/'+str(ID)+'/'+name+'', None, None))
    def removeMember(self, member): return bool(self.nfrest('GET', '/model/member/remove/'+member+'', None, None))
    def removeNodalMass(self, ID): return bool(self.nfrest('GET', '/mass/remove/'+ID+'', None, None))
    def removeNode(self, ID): return bool(self.nfrest('DELETE', '/node/ID'+ID+'', None, None))
    def removeNodeCS(self, num): return bool(self.nfrest('DELETE', '/node/cs/'+num+'', None, None))
    def removeOverlappedElements(self, tol): return bool(self.nfrest('GET', '/op/mesh/removeoverlappedelements'+str(tol)+'', None, None))
    def removeRigidDiaphragms(self): return bool(self.nfrest('DELETE', '/op/mesh/rigiddiaph', None, None))
    def removeSection(self, sectionID): return bool(self.nfrest('GET', '/section/remove/'+str(sectionID)+'', None, None))
    def removeSectionCover(self, sectionID): return bool(self.nfrest('DELETE', '/section/add/cover/'+str(sectionID)+'', None, None))
    def removeSectionFigure(self, sectionID, figureID, isEmpty): return bool(self.nfrest('GET', '/section/add/removefigure/'+str(sectionID)+'/'+str(figureID)+'/'+str(isEmpty)+'', None, None))
    def removeSectionProperty(self, ID, name): return bool(self.nfrest('DELETE', '/section/prop/'+ID+'/'+name+'', None, None))
    def removeSpringProperty(self, name): return bool(self.nfrest('DELETE', '/springproperty/'+name+'', None, None))
    def renameSection(self, sectionID, name, code): return bool(self.nfrest('GET', '/section/rename/'+str(sectionID)+'/'+name+'/'+code+'', None, None))
    def renumberElements(self, initialID, step): return bool(self.nfrest('GET', '/op/mesh/renumber/elements/'+str(initialID)+'/'+str(step)+'', None, None))
    def renumberElementsByCoordinates(self, dir1, dir2): return bool(self.nfrest('GET', '/op/mesh/renumber/elementsbycoords/'+str(dir1)+'/'+str(dir2)+'', None, None))
    def renumberNodes(self, initialID, step): return bool(self.nfrest('GET', '/op/mesh/renumber/nodes/'+str(initialID)+'/'+str(step)+'', None, None))
    def renumberNodesByCoordinates(self, dir1, dir2): return bool(self.nfrest('GET', '/op/mesh/renumber/nodesbycoords/'+str(dir1)+'/'+str(dir2)+'', None, None))
    def rotateNodes(self, nodes, axisX, axisY, axisZ, angle): return bool(self.nfrest('GET', '/op/mesh/rotatenodes/'+str(axisX)+'/'+str(axisY)+'/'+str(axisZ)+'/'+str(angle)+'', None, dict([("nodes",json.dumps(nodes))])))
    def RunLoadCase(self, loadcase, outOfProc, noWindow): return self.nfrest('GET', '/op/runlc/'+loadcase+'/'+str(outOfProc)+'/'+str(noWindow)+'', None, None)
    def RunModel(self, outOfProc, noWindow): return self.nfrest('GET', '/op/run/'+str(outOfProc)+'/'+str(noWindow)+'', None, None)
    def saveDocX(self): return bool(self.nfrest('GET', '/op/docx/save', None, None))
    def saveModel(self, filename): return bool(self.nfrest('GET', '/op/save', None, dict([("path",filename)])))
    def saveOptions(self): return bool(self.nfrest('GET', '/op/opt/saveopts', None, None))
    def saveSectionImage(self, sectionID, path): return bool(self.nfrest('GET', '/op/sectioncalc/image/'+str(sectionID)+'', None, dict([("path",path)])))
    def saveSectionImageWithBars(self, elemID, progr, path): return bool(self.nfrest('GET', '/op/sectioncalc/imagewithbars/'+elemID+'/'+str(progr)+'', None, dict([("path",path)])))
    def scaleNodes(self, nodes, scaleX, scaleY, scaleZ, scaleCenterX, scaleCenterY, scaleCenterZ): return bool(self.nfrest('GET', '/op/mesh/scalenodes/'+str(scaleX)+'/'+str(scaleY)+'/'+str(scaleZ)+'/'+str(scaleCenterX)+'/'+str(scaleCenterY)+'/'+str(scaleCenterZ)+'', None, dict([("nodes",json.dumps(nodes))])))
    def SectionToModel(self, sectionID, saveModelPath): return bool(self.nfrest('GET', '/model/section2model/'+sectionID+'', None, dict([("path",saveModelPath)])))
    def seriesFromFunction(self, funcID): return json.loads(self.nfrest('GET', '/function/series/'+str(funcID)+'', None, None))
    def setAluSection(self, ID, SectionClass, Jw): return bool(self.nfrest('GET', '/section/set/alu/'+str(ID)+'/'+str(SectionClass)+'/'+str(Jw)+'', None, None))
    def setAnalysisSequence(self, name, previousCase): return bool(self.nfrest('GET', '/loadcase/sequence/'+name+'/'+previousCase+'', None, None))
    def setBC(self, node, x, y, z, rx, ry, rz): return bool(self.nfrest('GET', '/bc/set/'+node+'/'+str(x)+'/'+str(y)+'/'+str(z)+'/'+str(rx)+'/'+str(ry)+'/'+str(rz)+'', None, None))
    def setBeamAngle(self, num, angle): return bool(self.nfrest('GET', '/element/beamangle/'+num+'/'+str(angle)+'', None, None))
    def setBucklingAnalysis(self, name, Nmodes, tol): return bool(self.nfrest('GET', '/loadcase/setbuck/'+name+'/'+str(Nmodes)+'/'+str(tol)+'', None, None))
    def setCombination(self, name, loadcase, factor, type, servType): return bool(self.nfrest('GET', '/loadcase/combo/set/'+name+'/'+loadcase+'/'+str(factor)+'/'+str(type)+'/'+str(servType)+'', None, None))
    def setCombinationCoeffPsi(self, subscript, type, value): return bool(self.nfrest('GET', '/loadcase/setpsi/'+str(subscript)+'/'+str(type)+'/'+str(value)+'', None, None))
    def setCombinationFactors(self, gG, gQ, psiVar, psiWind, psiSnow, gSW): return bool(self.nfrest('GET', '/loadcase/setcfactors/'+str(gG)+'/'+str(gQ)+'/'+str(gSW)+'', None, dict([("psiVar",json.dumps(psiVar)),("psiWind",json.dumps(psiWind)),("psiSnow",json.dumps(psiSnow))])))
    def setCompositeBeam(self, ID, MposFactor, MnegFactor): return bool(self.nfrest('GET', '/section/set/compositebeam/'+str(ID)+'/'+str(MposFactor)+'/'+str(MnegFactor)+'', None, None))
    def setCompositeColumn(self, ID, EcFactor, ReductionFactor): return bool(self.nfrest('GET', '/section/set/compositecolumn/'+str(ID)+'/'+str(EcFactor)+'/'+str(ReductionFactor)+'', None, None))
    def setConcretePropertiesNTC(self, matID, fc, isCharacteristic, unitsIn): return float(self.nfrest('GET', '/material/concretentc/'+str(matID)+'/'+str(fc)+'/'+str(isCharacteristic)+'', None, dict([("unitsIn",unitsIn)])))
    def setConstraint(self, n, master, x, y, z, rx, ry, rz): return bool(self.nfrest('GET', '/op/mesh/constraint/'+n+'/'+master+'/'+str(x)+'/'+str(y)+'/'+str(z)+'/'+str(rx)+'/'+str(ry)+'/'+str(rz)+'', None, None))
    def setElemAsJoint(self, num, status): return bool(self.nfrest('GET', '/element/setjoint/'+num+'/'+str(status)+'', None, None))
    def setElementCustomProperty(self, elem, propName, propValue): return bool(self.nfrest('POST', '/element/customprop/'+elem+'/'+propName+'/'+propValue+'', None, None))
    def setElementOffset(self, elem, offsetZ, offsetY): return bool(self.nfrest('POST', '/element/beamoffset/'+elem+'/'+str(offsetZ)+'/'+str(offsetY)+'', None, None))
    def setElementSection(self, elem, sectID): return bool(self.nfrest('GET', '/section/'+elem+'/'+str(sectID)+'', None, None))
    def setEndRelease(self, beamID, node, DOFmask, useStiffness): return bool(self.nfrest('POST', '/element/beamendrelease/'+beamID+'/'+node+'/'+str(useStiffness)+'', None, dict([("DOFmask",json.dumps(DOFmask))])))
    def setEnvelope(self, name, loadcase, factor, type, servType): return bool(self.nfrest('GET', '/loadcase/combo/setenv/'+name+'/'+loadcase+'/'+str(factor)+'/'+str(type)+'/'+str(servType)+'', None, None))
    def setFiberSection(self, ID, divZ, divY): return bool(self.nfrest('GET', '/section/set/fibers/'+str(ID)+'/'+str(divZ)+'/'+str(divY)+'', None, None))
    def setFirePoint(self, loadcase, fireNode, targetTemp, gradientY, gradientZ, tempAtten, dontLoadUnder): return json.loads(self.nfrest('GET', '/load/firepoint/'+loadcase+'/'+fireNode+'/'+str(targetTemp)+'/'+str(gradientY)+'/'+str(gradientZ)+'/'+str(tempAtten)+'/'+str(dontLoadUnder)+'', None, None))
    def setFloorLoad(self, name, loadcase, loadvalue, dirX, dirY, dirZ): return bool(self.nfrest('GET', '/load/floor/set/'+name+'/'+loadcase+'/'+str(loadvalue)+'/'+str(dirX)+'/'+str(dirY)+'/'+str(dirZ)+'', None, None))
    def setLanguage(self, code): return self.nfrest('POST', '/op/opt/lang/'+code+'', None, None)
    def setLoadA(self, load): return bool(self.nfrest('POST', '/load/setA', load, None))
    def setLoadcaseFactor(self, loadcase, factor): return bool(self.nfrest('GET', '/loadcase/setfactor/'+loadcase+'/'+str(factor)+'', None, None))
    def setLoadCasePhaseInCombination(self, name, loadcase, phase): return bool(self.nfrest('GET', '/loadcase/combo/setphase/'+name+'/'+loadcase+'/'+str(phase)+'', None, None))
    def setLoadCaseType(self, name, type): return bool(self.nfrest('GET', '/loadcase/settype/'+name+'/'+str(type)+'', None, None))
    def setLoadDurationClass(self, loadcase, durationClass): return bool(self.nfrest('GET', '/load/setduration/'+loadcase+'/'+str(durationClass)+'', None, None))
    def setLoadsToMass(self, loadcase, factor, remove): return bool(self.nfrest('GET', '/mass/load2mass/'+loadcase+'/'+str(factor)+'/'+str(remove)+'', None, None))
    def setMacroelement(self, elemID, macroType): return bool(self.nfrest('POST', '/element/macro/'+elemID+'/'+str(macroType)+'', None, None))
    def setModalAnalysis(self, name, Nmodes, tol): return bool(self.nfrest('GET', '/loadcase/setmodal/'+name+'/'+str(Nmodes)+'/'+str(tol)+'', None, None))
    def setNLDanalysis(self, name, tStep, nSteps, tol, iters, seriesID, Xfactor, Yfactor, Zfactor, RXfactor, RYfactor, RZfactor, seriesFactor, Mdamp, NlGeo): return bool(self.nfrest('GET', '/loadcase/setnldyn/'+name+'/'+str(tStep)+'/'+str(nSteps)+'/'+str(tol)+'/'+str(iters)+'/'+str(seriesID)+'/'+str(Xfactor)+'/'+str(Yfactor)+'/'+str(Zfactor)+'/'+str(RXfactor)+'/'+str(RYfactor)+'/'+str(RZfactor)+'/'+str(seriesFactor)+'/'+str(Mdamp)+'/'+str(NlGeo)+'', None, None))
    def setNLSanalysis(self, name, tStep, nSteps, tol, iters, seriesID, dispControlNode, dispControlDOF, NlGeo): return bool(self.nfrest('GET', '/loadcase/setnlstatic/'+name+'/'+str(tStep)+'/'+str(nSteps)+'/'+str(tol)+'/'+str(iters)+'/'+str(seriesID)+'/'+dispControlNode+'/'+str(dispControlDOF)+'/'+str(NlGeo)+'', None, None))
    def setNodeAsJoint(self, num, status): return bool(self.nfrest('GET', '/node/setjoint/'+num+'/'+str(status)+'', None, None))
    def setNodeCoordinates(self, ID, coords): return bool(self.nfrest('POST', '/node/ID'+ID+'', coords, None))
    def setNodeCS(self, num, x1, y1, z1, x2, y2, z2): return bool(self.nfrest('GET', '/node/cs/'+num+'/'+str(x1)+'/'+str(y1)+'/'+str(z1)+'/'+str(x2)+'/'+str(y2)+'/'+str(z2)+'', None, None))
    def setNodePosition(self, node): return bool(self.nfrest('POST', '/node/ID', node, None))
    def setPDeltaAnalysis(self, name, tol): return bool(self.nfrest('GET', '/loadcase/setpdelta/'+name+'/'+str(tol)+'', None, None))
    def setResponseSpectrumAnalysis(self, direction, loadcase, modesNumber, spectrumFuncID, modalDamping, factor): return bool(self.nfrest('GET', '/loadcase/setrs/'+str(direction)+'/'+loadcase+'/'+str(modesNumber)+'/'+str(spectrumFuncID)+'/'+str(modalDamping)+'/'+str(factor)+'', None, None))
    def setRigidLink(self, n1, n2): return bool(self.nfrest('PUT', '/op/mesh/rigidlink/'+n1+'/'+n2+'', None, None))
    def setRigidOffsets(self, beamID, values, isAbsLength): return bool(self.nfrest('POST', '/element/beamendoffset/'+beamID+'/'+str(isAbsLength)+'', None, dict([("values",json.dumps(values))])))
    def setSectionAngle(self, ID, a): return bool(self.nfrest('GET', '/section/set/angle/'+str(ID)+'/'+str(a)+'', None, None))
    def setSectionColor(self, ID, Red, Green, Blue): return bool(self.nfrest('POST', '/section/set/color/'+ID+'/'+str(Red)+'/'+str(Green)+'/'+str(Blue)+'', None, None))
    def setSectionMaterial(self, ID, materialID): return bool(self.nfrest('GET', '/section/set/material/'+str(ID)+'/'+str(materialID)+'', None, None))
    def setSectionOffset(self, ID, offsetZ, offsetY): return bool(self.nfrest('POST', '/section/set/offset/'+ID+'/'+str(offsetZ)+'/'+str(offsetY)+'', None, None))
    def setSectionProperty(self, ID, name, value): return int(self.nfrest('POST', '/section/prop/'+ID+'/'+name+'/'+str(value)+'', None, None))
    def setSectionRebarsToElements(self, ID): return bool(self.nfrest('GET', '/section/rebar/toelems/'+ID+'', None, None))
    def setSectionRebarsToElements(self, ID): return bool(self.nfrest('GET', '/section/rebar/toelems/'+str(ID)+'', None, None))
    def setSeismicFloorEccentricity(self, thID, ct, lam): return bool(self.nfrest('GET', '/loadcase/combo/setseismicecc/'+str(thID)+'/'+str(ct)+'/'+str(lam)+'', None, None))
    def setSeismicLoadcaseForCombos(self, direction, loadcase, enableFloorEccentricity5, seismicCombinationType): return bool(self.nfrest('GET', '/loadcase/combo/setseismiclc/'+str(direction)+'/'+loadcase+'/'+str(enableFloorEccentricity5)+'/'+str(seismicCombinationType)+'', None, None))
    def setSelfWeight(self, loadcase): return bool(self.nfrest('GET', '/load/setsw/'+loadcase+'', None, None))
    def setSelfWeightDirection(self, direction): return bool(self.nfrest('GET', '/load/setswdir/'+str(direction)+'', None, None))
    def setShearReinfRCdata(self, ID, data): return bool(self.nfrest('GET', '/section/set/shearreinfrc/'+str(ID)+'', None, dict([("data",json.dumps(data))])))
    def setShellEndRelease(self, ID, node, DOFmask): return bool(self.nfrest('POST', '/element/shellendrelease/'+ID+'/'+node+'', None, dict([("DOFmask",json.dumps(DOFmask))])))
    def setSpringLocalAxes(self, name, x1, y1, z1, x2, y2, z2): return bool(self.nfrest('POST', '/springproperty/axes/'+name+'/'+str(x1)+'/'+str(y1)+'/'+str(z1)+'/'+str(x2)+'/'+str(y2)+'/'+str(z2)+'', None, None))
    def setSRSScombination(self, name, loadcase, factor, type, servType): return bool(self.nfrest('GET', '/loadcase/combo/setsrss/'+name+'/'+loadcase+'/'+str(factor)+'/'+str(type)+'/'+str(servType)+'', None, None))
    def setSteelSection(self, ID, SectionClass, alphaLT, alphay, alphaz, Jw): return bool(self.nfrest('GET', '/section/set/steel/'+str(ID)+'/'+str(SectionClass)+'/'+str(alphaLT)+'/'+str(alphay)+'/'+str(alphaz)+'/'+str(Jw)+'', None, None))
    def setUnits(self, length, force): return bool(self.nfrest('GET', '/units/set/'+length+'/'+force+'', None, None))
    def setWall(self, elems, rotate90, isSlab): return self.nfrest('GET', '/element/walls/set/'+str(rotate90)+'/'+str(isSlab)+'', None, dict([("elems",json.dumps(elems))]))
    def showViewport(self, path, width, height): return bool(self.nfrest('GET', '/op/showvieport/'+path+'/'+str(width)+'/'+str(height)+'', None, None))
    def valueFromFunction(self, Xval, funcID): return float(self.nfrest('GET', '/function/value/'+str(Xval)+'/'+str(funcID)+'', None, None))
    def valueFromString(self, text, valueName): return self.nfrest('GET', '/op/import/valfromstring/'+text+'/'+valueName+'', None, None)
    def vertexFromNode(self, node): return self.nfrest('GET', '/node/vertex/'+node+'', None, None)
    @property
    def areaColor(self): return int(self.nfrest('GET','/model/colors/area'))
    @areaColor.setter
    def areaColor(self,value): self.nfrest('POST','/model/colors/area', heads={'val':str(value)})
    @property
    def autoMassInX(self): return bool(self.nfrest('GET','/mass/autoX'))
    @autoMassInX.setter
    def autoMassInX(self,value): self.nfrest('POST','/mass/autoX', heads={'val':str(value)})
    @property
    def autoMassInY(self): return bool(self.nfrest('GET','/mass/autoY'))
    @autoMassInY.setter
    def autoMassInY(self,value): self.nfrest('POST','/mass/autoY', heads={'val':str(value)})
    @property
    def autoMassInZ(self): return bool(self.nfrest('GET','/mass/autoZ'))
    @autoMassInZ.setter
    def autoMassInZ(self,value): self.nfrest('POST','/mass/autoZ', heads={'val':str(value)})
    @property
    def backgroundColor(self): return int(self.nfrest('GET','/model/colors/back'))
    @backgroundColor.setter
    def backgroundColor(self,value): self.nfrest('POST','/model/colors/back', heads={'val':str(value)})
    @property
    def baselineGrade(self): return int(self.nfrest('GET','/op/opt/baseline'))
    @baselineGrade.setter
    def baselineGrade(self,value): self.nfrest('POST','/op/opt/baseline', heads={'val':str(value)})
    @property
    def binFolder(self): return self.nfrest('GET','/op/opt/binfolder')
    @binFolder.setter
    def binFolder(self,value): self.nfrest('POST','/op/opt/binfolder', heads={'val':str(value)})
    @property
    def bordersColor(self): return int(self.nfrest('GET','/model/colors/border'))
    @bordersColor.setter
    def bordersColor(self,value): self.nfrest('POST','/model/colors/border', heads={'val':str(value)})
    @property
    def constraintsColor(self): return int(self.nfrest('GET','/model/colors/constraint'))
    @constraintsColor.setter
    def constraintsColor(self,value): self.nfrest('POST','/model/colors/constraint', heads={'val':str(value)})
    @property
    def defSolverType(self): return int(self.nfrest('GET','/op/opt/defsolvertype'))
    @property
    def designMaterialsID(self): return json.loads(self.nfrest('GET','/designmaterials'))
    @property
    def DocXfontSize(self): return int(self.nfrest('GET','/op/docx/fontsize'))
    @DocXfontSize.setter
    def DocXfontSize(self,value): self.nfrest('POST','/op/docx/fontsize', heads={'val':str(value)})
    @property
    def DocXformulaResolution(self): return int(self.nfrest('GET','/op/docx/formularesol'))
    @DocXformulaResolution.setter
    def DocXformulaResolution(self,value): self.nfrest('POST','/op/docx/formularesol', heads={'val':str(value)})
    @property
    def DocXtableAlignment(self): return int(self.nfrest('GET','/op/docx/tablealign'))
    @DocXtableAlignment.setter
    def DocXtableAlignment(self,value): self.nfrest('POST','/op/docx/tablealign', heads={'val':str(value)})
    @property
    def DocXtableFitting(self): return bool(self.nfrest('GET','/op/docx/tablefit'))
    @DocXtableFitting.setter
    def DocXtableFitting(self,value): self.nfrest('POST','/op/docx/tablefit', heads={'val':str(value)})
    @property
    def DocXtableFontSize(self): return int(self.nfrest('GET','/op/docx/tablefontsize'))
    @DocXtableFontSize.setter
    def DocXtableFontSize(self,value): self.nfrest('POST','/op/docx/tablefontsize', heads={'val':str(value)})
    @property
    def dontDeleteResults(self): return bool(self.nfrest('GET','/res/donotdelete'))
    @dontDeleteResults.setter
    def dontDeleteResults(self,value): self.nfrest('POST','/res/donotdelete', heads={'val':str(value)})
    @property
    def DXFoptions(self): return self.nfrest('GET','/op/opt/dxfoptions')
    @DXFoptions.setter
    def DXFoptions(self,value): self.nfrest('POST','/op/opt/dxfoptions', heads={'val':str(value)})
    @property
    def elemsList(self): return json.loads(self.nfrest('GET','/elements'))
    @property
    def elemsNumber(self): return self.nfrest('GET','/elements/number')
    @property
    def elemTextColor(self): return int(self.nfrest('GET','/model/colors/elemtext'))
    @elemTextColor.setter
    def elemTextColor(self,value): self.nfrest('POST','/model/colors/elemtext', heads={'val':str(value)})
    @property
    def envName(self): return self.nfrest('GET','/model/env')
    @property
    def hingesColor(self): return int(self.nfrest('GET','/model/colors/hinge'))
    @hingesColor.setter
    def hingesColor(self,value): self.nfrest('POST','/model/colors/hinge', heads={'val':str(value)})
    @property
    def IFC_format(self): return int(self.nfrest('GET','/op/opt/ifcformat'))
    @IFC_format.setter
    def IFC_format(self,value): self.nfrest('POST','/op/opt/ifcformat', heads={'val':str(value)})
    @property
    def IFC_includeAnalyticalModel(self): return bool(self.nfrest('GET','/op/opt/ifcanalytical'))
    @IFC_includeAnalyticalModel.setter
    def IFC_includeAnalyticalModel(self,value): self.nfrest('POST','/op/opt/ifcanalytical', heads={'val':str(value)})
    @property
    def IFC_WallMeshSize(self): return float(self.nfrest('GET','/op/opt/ifcwallmeshsize'))
    @IFC_WallMeshSize.setter
    def IFC_WallMeshSize(self,value): self.nfrest('POST','/op/opt/ifcwallmeshsize', heads={'val':str(value)})
    @property
    def isRemote(self): return bool(self.nfrest('GET','na'))
    @property
    def lineColor(self): return int(self.nfrest('GET','/model/colors/line'))
    @lineColor.setter
    def lineColor(self,value): self.nfrest('POST','/model/colors/line', heads={'val':str(value)})
    @property
    def massColor(self): return int(self.nfrest('GET','/model/colors/mass'))
    @massColor.setter
    def massColor(self,value): self.nfrest('POST','/model/colors/mass', heads={'val':str(value)})
    @property
    def materialsID(self): return json.loads(self.nfrest('GET','/materials'))
    @property
    def modeldata(self): return self.nfrest('GET','/model/data')
    @modeldata.setter
    def modeldata(self,value): self.nfrest('POST','/model/data',value)
    @property
    def modelName(self): return self.nfrest('GET','/model')
    @modelName.setter
    def modelName(self,value): self.nfrest('POST','/model', heads={'val':str(value)})
    @property
    def modelPath(self): return self.nfrest('GET','/model/path')
    @property
    def modelresults(self): return self.nfrest('GET','/model/results')
    @modelresults.setter
    def modelresults(self,value): self.nfrest('POST','/model/results',value)
    @property
    def nodeColor(self): return int(self.nfrest('GET','/model/colors/node'))
    @nodeColor.setter
    def nodeColor(self,value): self.nfrest('POST','/model/colors/node', heads={'val':str(value)})
    @property
    def nodesList(self): return json.loads(self.nfrest('GET','/nodes'))
    @property
    def nodesNumber(self): return self.nfrest('GET','/nodes/number')
    @property
    def nodeTextColor(self): return int(self.nfrest('GET','/model/colors/nodetext'))
    @nodeTextColor.setter
    def nodeTextColor(self,value): self.nfrest('POST','/model/colors/nodetext', heads={'val':str(value)})
    @property
    def numberFormat(self): return self.nfrest('GET','/op/opt/numberformat')
    @numberFormat.setter
    def numberFormat(self,value): self.nfrest('POST','/op/opt/numberformat', heads={'val':str(value)})
    @property
    def OS_beamWithHingesOption(self): return bool(self.nfrest('GET','/op/opt/os/beamwithhinges'))
    @OS_beamWithHingesOption.setter
    def OS_beamWithHingesOption(self,value): self.nfrest('POST','/op/opt/os/beamwithhinges', heads={'val':str(value)})
    @property
    def OS_concreteTensileStrength(self): return bool(self.nfrest('GET','/op/opt/os/tensilesrc'))
    @OS_concreteTensileStrength.setter
    def OS_concreteTensileStrength(self,value): self.nfrest('POST','/op/opt/os/tensilesrc', heads={'val':str(value)})
    @property
    def OS_IntegrationPointsOption(self): return int(self.nfrest('GET','/op/opt/os/intpoints'))
    @OS_IntegrationPointsOption.setter
    def OS_IntegrationPointsOption(self,value): self.nfrest('POST','/op/opt/os/intpoints', heads={'val':str(value)})
    @property
    def OS_NDfiberSectionsOption(self): return bool(self.nfrest('GET','/op/opt/os/ndfibersects'))
    @OS_NDfiberSectionsOption.setter
    def OS_NDfiberSectionsOption(self,value): self.nfrest('POST','/op/opt/os/ndfibersects', heads={'val':str(value)})
    @property
    def OS_saveStateVariables(self): return bool(self.nfrest('GET','/op/opt/os/statevars'))
    @OS_saveStateVariables.setter
    def OS_saveStateVariables(self,value): self.nfrest('POST','/op/opt/os/statevars', heads={'val':str(value)})
    @property
    def releasesColor(self): return int(self.nfrest('GET','/model/colors/release'))
    @releasesColor.setter
    def releasesColor(self,value): self.nfrest('POST','/model/colors/release', heads={'val':str(value)})
    @property
    def resCalc_cacheEnabled(self): return bool(self.nfrest('GET','/op/opt/rescalc/cacheenabled'))
    @resCalc_cacheEnabled.setter
    def resCalc_cacheEnabled(self,value): self.nfrest('POST','/op/opt/rescalc/cacheenabled', heads={'val':str(value)})
    @property
    def resCalc_concreteBehaviour(self): return int(self.nfrest('GET','/op/opt/rescalc/concbeh'))
    @resCalc_concreteBehaviour.setter
    def resCalc_concreteBehaviour(self,value): self.nfrest('POST','/op/opt/rescalc/concbeh', heads={'val':str(value)})
    @property
    def resCalc_domainCorrectionType(self): return int(self.nfrest('GET','/op/opt/rescalc/domcorr'))
    @resCalc_domainCorrectionType.setter
    def resCalc_domainCorrectionType(self,value): self.nfrest('POST','/op/opt/rescalc/domcorr', heads={'val':str(value)})
    @property
    def resCalc_elasticTolerance(self): return float(self.nfrest('GET','/op/opt/rescalc/eltoll'))
    @resCalc_elasticTolerance.setter
    def resCalc_elasticTolerance(self,value): self.nfrest('POST','/op/opt/rescalc/eltoll', heads={'val':str(value)})
    @property
    def resCalc_homogBarsFactor(self): return int(self.nfrest('GET','/op/opt/rescalc/homog'))
    @resCalc_homogBarsFactor.setter
    def resCalc_homogBarsFactor(self,value): self.nfrest('POST','/op/opt/rescalc/homog', heads={'val':str(value)})
    @property
    def resCalc_kMod(self): return float(self.nfrest('GET','/op/opt/rescalc/kmod'))
    @resCalc_kMod.setter
    def resCalc_kMod(self,value): self.nfrest('POST','/op/opt/rescalc/kmod', heads={'val':str(value)})
    @property
    def resCalc_rebarHardeningRatio(self): return float(self.nfrest('GET','/op/opt/rescalc/rebhard'))
    @resCalc_rebarHardeningRatio.setter
    def resCalc_rebarHardeningRatio(self,value): self.nfrest('POST','/op/opt/rescalc/rebhard', heads={'val':str(value)})
    @property
    def resCalc_resDomainSlices(self): return int(self.nfrest('GET','/op/opt/rescalc/domainslices'))
    @resCalc_resDomainSlices.setter
    def resCalc_resDomainSlices(self,value): self.nfrest('POST','/op/opt/rescalc/domainslices', heads={'val':str(value)})
    @property
    def resCalc_responseInTension(self): return bool(self.nfrest('GET','/op/opt/rescalc/tensresp'))
    @resCalc_responseInTension.setter
    def resCalc_responseInTension(self,value): self.nfrest('POST','/op/opt/rescalc/tensresp', heads={'val':str(value)})
    @property
    def resCalc_steelClass(self): return int(self.nfrest('GET','/op/opt/rescalc/steelclass'))
    @resCalc_steelClass.setter
    def resCalc_steelClass(self,value): self.nfrest('POST','/op/opt/rescalc/steelclass', heads={'val':str(value)})
    @property
    def resCalc_strandHardeningRatio(self): return float(self.nfrest('GET','/op/opt/rescalc/strhard'))
    @resCalc_strandHardeningRatio.setter
    def resCalc_strandHardeningRatio(self,value): self.nfrest('POST','/op/opt/rescalc/strhard', heads={'val':str(value)})
    @property
    def restraintsColor(self): return int(self.nfrest('GET','/model/colors/restraint'))
    @restraintsColor.setter
    def restraintsColor(self,value): self.nfrest('POST','/model/colors/restraint', heads={'val':str(value)})
    @property
    def saveStateVariables(self): return bool(self.nfrest('GET','/op/opt/os/statevars'))
    @saveStateVariables.setter
    def saveStateVariables(self,value): self.nfrest('POST','/op/opt/os/statevars', heads={'val':str(value)})
    @property
    def sectCalcAccuracy(self): return int(self.nfrest('GET','/op/opt/calcaccuracy'))
    @sectCalcAccuracy.setter
    def sectCalcAccuracy(self,value): self.nfrest('POST','/op/opt/calcaccuracy', heads={'val':str(value)})
    @property
    def sectCalcUseFibers(self): return bool(self.nfrest('GET','/op/opt/calcusefibers'))
    @sectCalcUseFibers.setter
    def sectCalcUseFibers(self,value): self.nfrest('POST','/op/opt/calcusefibers', heads={'val':str(value)})
    @property
    def sectionsID(self): return json.loads(self.nfrest('GET','/sections'))
    @property
    def selAreaColor(self): return int(self.nfrest('GET','/model/colors/selarea'))
    @selAreaColor.setter
    def selAreaColor(self,value): self.nfrest('POST','/model/colors/selarea', heads={'val':str(value)})
    @property
    def selectedElements(self): return json.loads(self.nfrest('GET','/op/selectedelements'))
    @selectedElements.setter
    def selectedElements(self,value): self.nfrest('POST','/op/selectedelements', heads={'val':str(value)})
    @property
    def selectedNodes(self): return json.loads(self.nfrest('GET','/op/selectednodes'))
    @selectedNodes.setter
    def selectedNodes(self,value): self.nfrest('POST','/op/selectednodes', heads={'val':str(value)})
    @property
    def selLineColor(self): return int(self.nfrest('GET','/model/colors/selline'))
    @selLineColor.setter
    def selLineColor(self,value): self.nfrest('POST','/model/colors/selline', heads={'val':str(value)})
    @property
    def selNodeColor(self): return int(self.nfrest('GET','/model/colors/selnode'))
    @selNodeColor.setter
    def selNodeColor(self,value): self.nfrest('POST','/model/colors/selnode', heads={'val':str(value)})
    @property
    def selSolidColor(self): return int(self.nfrest('GET','/model/colors/selsolid'))
    @selSolidColor.setter
    def selSolidColor(self,value): self.nfrest('POST','/model/colors/selsolid', heads={'val':str(value)})
    @property
    def selSpringColor(self): return int(self.nfrest('GET','/model/colors/node'))
    @selSpringColor.setter
    def selSpringColor(self,value): self.nfrest('POST','/model/colors/node', heads={'val':str(value)})
    @property
    def solidColor(self): return int(self.nfrest('GET','/model/colors/solid'))
    @solidColor.setter
    def solidColor(self,value): self.nfrest('POST','/model/colors/solid', heads={'val':str(value)})
    @property
    def solverType(self): return int(self.nfrest('GET','/op/opt/solvertype'))
    @property
    def springColor(self): return int(self.nfrest('GET','/model/colors/spring'))
    @springColor.setter
    def springColor(self,value): self.nfrest('POST','/model/colors/spring', heads={'val':str(value)})
    @property
    def tempFolder(self): return self.nfrest('GET','/op/opt/tempfolder')
    @tempFolder.setter
    def tempFolder(self,value): self.nfrest('POST','/op/opt/tempfolder', heads={'val':str(value)})
    @property
    def textColor(self): return int(self.nfrest('GET','/model/colors/text'))
    @textColor.setter
    def textColor(self,value): self.nfrest('POST','/model/colors/text', heads={'val':str(value)})
    @property
    def useFastEigensolver(self): return bool(self.nfrest('GET','/op/opt/os/fasteigen'))
    @useFastEigensolver.setter
    def useFastEigensolver(self,value): self.nfrest('POST','/op/opt/os/fasteigen', heads={'val':str(value)})
    @property
    def WallMeshSize(self): return float(self.nfrest('GET','/op/opt/wallmeshsize'))
    @WallMeshSize.setter
    def WallMeshSize(self,value): self.nfrest('POST','/op/opt/wallmeshsize', heads={'val':str(value)})

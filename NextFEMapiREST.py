import requests

class NextFEMrest:
    def __init__(self,_baseUrl,_user,_msg=True):
        self.baseUrl=str(_baseUrl)
        self.user=str(_user)
        self.msg=_msg

    def nfrest(self, method, command, body=None, heads=None):
        url = self.baseUrl + command
        headers = {"user": self.user}
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
        headers = {"user": self.user}
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
    def activeBarsDiameters(self): return self.nfrest('GET', '/element/rebar/barsdiam', None, None)
    def activeHoopsDiameters(self): return self.nfrest('GET', '/element/rebar/hoopsdiam', None, None)
    def addBeam(self, n1, n2, sect, mat, sect2): return self.nfrest('GET', '/element/add/beam/'+str(n1)+'/'+str(n2)+'/'+str(sect)+'/'+str(mat)+'/'+str(sect2)+'', None, None)
    def addBeamLoad(self, elem, value1, value2, position1, position2, direction, loadcase, local): return self.nfrest('GET', '/load/element/beamadd/'+str(elem)+'/'+str(value1)+'/'+str(value2)+'/'+str(position1)+'/'+str(position2)+'/'+str(direction)+'/'+str(loadcase)+'/'+str(local)+'', None, None)
    def addBeamLoad(self, elem, values, positions, direction, loadcase, local): return self.nfrest('GET', '/load/element/beamaddA/'+str(elem)+'/'+str(direction)+'/'+str(loadcase)+'/'+str(local)+'', None, dict([("values", values), ("positions", positions)]))
    def addBeamLoadU(self, elem, value, direction, loadcase, local): return self.nfrest('GET', '/load/element/beamaddU/'+str(elem)+'/'+str(value)+'/'+str(direction)+'/'+str(loadcase)+'/'+str(local)+'', None, None)
    def addBoxSection(self, Lz, Ly, tw, tf1, tf2): return self.nfrest('GET', '/section/add/box/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(tf2)+'', None, None)
    def addCircleInSection(self, sectionID, diameter, centerX, centerY, isEmpty, material, doNotCenter): return self.nfrest('GET', '/section/add/addcirc/'+str(sectionID)+'/'+str(diameter)+'/'+str(centerX)+'/'+str(centerY)+'/'+str(isEmpty)+'/'+str(material)+'/'+str(doNotCenter)+'', None, None)
    def addCircSection(self, D): return self.nfrest('GET', '/section/add/circ/'+str(D)+'', None, None)
    def addCSection(self, Lz, Ly, tw, tf1, tf2, Lz2): return self.nfrest('GET', '/section/add/cshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(tf2)+'/'+str(Lz2)+'', None, None)
    def addDCSection(self, Lz, Ly, tw, tf1, tf2, gap, Lz2): return self.nfrest('GET', '/section/add/doublecshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(tf2)+'/'+str(gap)+'/'+str(Lz2)+'', None, None)
    def addDesignMatFromLib(self, name): return self.nfrest('GET', '/designmaterial/add/fromlib/'+str(name)+'', None, None)
    def addDesMaterial(self, name, E, fk, ni, type): return self.nfrest('GET', '/material/add/des/'+str(name)+'/'+str(E)+'/'+str(fk)+'/'+str(ni)+'/'+str(type)+'', None, None)
    def addDLSection(self, Lz, Ly, tw, tf1, gap): return self.nfrest('GET', '/section/add/doublelshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(gap)+'', None, None)
    def addDTSection(self, Lz, Ly, tw, tf1, tf2, Lz2): return self.nfrest('GET', '/section/add/dtshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'/'+str(tf2)+'/'+str(Lz2)+'', None, None)
    def addEC8spectrum(self, ag, q, LS, damping, soilType, type1): return self.nfrest('GET', '/function/ec8spectrum/'+str(ag)+'/'+str(q)+'/'+str(LS)+'/'+str(damping)+'/'+str(soilType)+'/'+str(type1)+'', None, None)
    def addEdgeLoad(self, elem, values, edge, direction, loadcase, local): return self.nfrest('POST', '/load/element/edgeadd/'+str(elem)+'/'+str(edge)+'/'+str(direction)+'/'+str(loadcase)+'/'+str(local)+'', values, None)
    def addFillInSection(self, sectionID, x, y, material, doNotCenter): return self.nfrest('GET', '/section/add/fill/'+str(sectionID)+'/'+str(material)+'/'+str(doNotCenter)+'', None, dict([("x",x),("y",y)]))
    def addFloorPlane(self, name, type, n1, n2, n3, n4): return self.nfrest('GET', '/load/floor/planeadd/'+str(name)+'/'+str(type)+'/'+str(n1)+'/'+str(n2)+'/'+str(n3)+'/'+str(n4)+'', None, None)
    def addGroup(self, name): return self.nfrest('GET', '/group/add/'+str(name)+'', None, None)
    def addHoleInSection(self, sectionID, x, y, material, doNotCenter): return self.nfrest('GET', '/section/add/hole/'+str(sectionID)+'/'+str(material)+'/'+str(doNotCenter)+'', None, dict([("x",x),("y",y)]))
    def addIsoMaterial(self, name, E, ni, Wden, fk, conductivity, specificHeat, type): return self.nfrest('GET', '/material/add/iso/'+str(name)+'/'+str(E)+'/'+str(ni)+'/'+str(Wden)+'/'+str(fk)+'/'+str(conductivity)+'/'+str(specificHeat)+'/'+str(type)+'', None, None)
    def addLayeredPlanarSection(self, layerThicknesses, layerMaterials): return self.nfrest('GET', '/section/add/layeredplanar', None, dict([("layerThicknesses", layerThicknesses), ("layerMaterials", layerMaterials)]))
    def addLoadCase(self, name): return self.nfrest('GET', '/loadcase/add/'+str(name)+'', None, None)
    def addLoadCaseToCombination(self, name, loadcase, factor): return self.nfrest('GET', '/loadcase/combo/add/'+str(name)+'/'+str(loadcase)+'/'+str(factor)+'', None, None)
    def addLoadCaseToTimeHistoryAnalysis(self, name, loadcase, factor, THid): return self.nfrest('GET', '/loadcase/combo/addth/'+str(name)+'/'+str(loadcase)+'/'+str(factor)+'/'+str(THid)+'', None, None)
    def addLongitRebar(self, elem, X, Y, area, matID, Linit, Lfin, rectBase, strandTens): return self.nfrest('GET', '/element/rebar/long/'+str(elem)+'/'+str(X)+'/'+str(Y)+'/'+str(area)+'/'+str(matID)+'/'+str(Linit)+'/'+str(Lfin)+'/'+str(rectBase)+'/'+str(strandTens)+'', None, None)
    def addLongitRebarInSection(self, sectionID, X, Y, area, matID, rectBase, strandTens): return self.nfrest('GET', '/section/rebar/long/'+str(sectionID)+'/'+str(X)+'/'+str(Y)+'/'+str(area)+'/'+str(matID)+'/'+str(rectBase)+'/'+str(strandTens)+'', None, None)
    def addLongitRebarInSection(self, sectionID, X, Y, area, matID, rectBase, strandTens): return self.nfrest('GET', '/section/rebar/long/'+str(sectionID)+'/'+str(X)+'/'+str(Y)+'/'+str(area)+'/'+str(matID)+'/'+str(rectBase)+'/'+str(strandTens)+'', None, None)
    def addLSection(self, Lz, Ly, tw, tf1): return self.nfrest('GET', '/section/add/lshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'', None, None)
    def addMatFromLib(self, name): return self.nfrest('GET', '/material/add/fromlib/'+str(name)+'', None, None)
    def addMember(self, elems): return self.nfrest('GET', '/model/member/add', None, dict([("elems", elems)]))
    def addMeshedWall(self, ID, origX, origY, origZ, div1, div2, plan, leng, hei, angle, tilt, nodeOffset, isHorizontal): return self.nfrest('GET', '/op/mesh/addmeshedwall/'+str(ID)+'/'+str(origX)+'/'+str(origY)+'/'+str(origZ)+'/'+str(div1)+'/'+str(div2)+'/'+str(plan)+'/'+str(leng)+'/'+str(hei)+'/'+str(angle)+'/'+str(tilt)+'/'+str(nodeOffset)+'/'+str(isHorizontal)+'', None, None)
    def addNodalDisp(self, node, disp, direction, loadcase): return self.nfrest('GET', '/load/node/disp/'+str(node)+'/'+str(disp)+'/'+str(direction)+'/'+str(loadcase)+'', None, None)
    def addNodalLoad(self, node, value, direction, loadcase, local): return self.nfrest('GET', '/load/node/add/'+str(node)+'/'+str(value)+'/'+str(direction)+'/'+str(loadcase)+'/'+str(local)+'', None, None)
    def addNodalMass(self, ID, tmx, tmy, tmz, rmx, rmy, rmz): return self.nfrest('GET', '/mass/add/'+str(ID)+'/'+str(tmx)+'/'+str(tmy)+'/'+str(tmz)+'/'+str(rmx)+'/'+str(rmy)+'/'+str(rmz)+'', None, None)
    def addNodalSpring(self, n1, propName): return self.nfrest('GET', '/element/add/nodalspring/'+str(n1)+'/'+str(propName)+'', None, None)
    def addNode(self, x, y, z, lcs1X, lcs1Y, lcs1Z, lcs2X, lcs2Y, lcs2Z): return self.nfrest('GET', '/node/add/'+str(x)+'/'+str(y)+'/'+str(z)+'/'+str(lcs1X)+'/'+str(lcs1Y)+'/'+str(lcs1Z)+'/'+str(lcs2X)+'/'+str(lcs2Y)+'/'+str(lcs2Z)+'', None, None)
    def addNodeWithID(self, x, y, z, ID): return self.nfrest('GET', '/node/add/'+str(x)+'/'+str(y)+'/'+str(z)+'/'+str(ID)+'', None, None)
    def addNormalhinge(self, name, checkType, position, includeShear, includeTorsion, cKpl, FresRatio): return self.nfrest('GET', '/hinge/add/simple/'+str(name)+'/'+str(checkType)+'/'+str(position)+'/'+str(includeShear)+'/'+str(includeTorsion)+'/'+str(cKpl)+'/'+str(FresRatio)+'', None, None)
    def addNTCspectrum(self, lat, lon, LS, soil, Vr, St, hh, q0, isHregular, damping, customAg, VerticalComponent): return self.nfrest('GET', '/function/ntcspectrum/'+str(lat)+'/'+str(lon)+'/'+str(LS)+'/'+str(soil)+'/'+str(Vr)+'/'+str(St)+'/'+str(hh)+'/'+str(q0)+'/'+str(isHregular)+'/'+str(damping)+'/'+str(customAg)+'/'+str(VerticalComponent)+'', None, None)
    def addNVMhinge(self, name, checkType, position, includeShear, includeTorsion, cKpl, FresRatio, stopResidualBranch): return self.nfrest('GET', '/hinge/add/nvm/'+str(name)+'/'+str(checkType)+'/'+str(position)+'/'+str(includeShear)+'/'+str(includeTorsion)+'/'+str(cKpl)+'/'+str(FresRatio)+'/'+str(stopResidualBranch)+'', None, None)
    def addObject(self, o, other): return self.nfrest('POST', '/model/addobject/'+str(other)+'', o, None)
    def addOmegaSection(self, Lz, Ly, tw, d): return self.nfrest('GET', '/section/add/omega/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(d)+'', None, None)
    def addOrChangeDesMaterialProperty(self, ID, name, value, units): return self.nfrest('POST', '/designmaterial/prop/'+str(ID)+'/'+str(name)+'/'+str(value)+'/'+str(units)+'', None, None)
    def addOrChangeMaterialProperty(self, ID, name, value, units): return self.nfrest('POST', '/material/prop/'+str(ID)+'/'+str(name)+'/'+str(value)+'/'+str(units)+'', None, None)
    def addOrModifyCustomData(self, key, value): return self.nfrest('POST', '/model/customdata', value, None)
    def addPipeSection(self, D, t): return self.nfrest('GET', '/section/add/pipe/'+str(D)+'/'+str(t)+'', None, None)
    def addPlanarSection(self, t): return self.nfrest('GET', '/section/add/planar/'+str(t)+'', None, None)
    def addQuad(self, n1, n2, n3, n4, sect, mat): return self.nfrest('GET', '/element/add/quad/'+str(n1)+'/'+str(n2)+'/'+str(n3)+'/'+str(n4)+'/'+str(sect)+'/'+str(mat)+'', None, None)
    def addRebarPattern(self, elem, pattern, Linit, Lfin, numBars, rebCover, matID, area, netSpacing): return self.nfrest('GET', '/element/rebar/pattern/'+str(elem)+'/'+str(pattern)+'/'+str(Linit)+'/'+str(Lfin)+'/'+str(rebCover)+'/'+str(matID)+'/'+str(area)+'/'+str(netSpacing)+'', None, None)
    def addRebarPatternInSection(self, pattern, sectionID, numBars, rebCover, matID, area, netSpacing): return self.nfrest('GET', '/section/rebar/pattern/'+str(pattern)+'/'+str(sectionID)+'/'+str(numBars)+'/'+str(rebCover)+'/'+str(matID)+'/'+str(area)+'/'+str(netSpacing)+'', None, None)
    def addRectangleInSection(self, sectionID, b, h, centerX, centerY, isEmpty, material, doNotCenter): return self.nfrest('GET', '/section/add/addrect/'+str(sectionID)+'/'+str(b)+'/'+str(h)+'/'+str(centerX)+'/'+str(centerY)+'/'+str(isEmpty)+'/'+str(material)+'/'+str(doNotCenter)+'', None, None)
    def addRectSection(self, Lz, Ly): return self.nfrest('GET', '/section/add/rect/'+str(Lz)+'/'+str(Ly)+'', None, None)
    def addSectFromLib(self, name): return self.nfrest('GET', '/section/add/fromlib/'+str(name)+'', None, None)
    def addSectFromLib(self, name, doNotCenter): return self.nfrest('GET', '/section/add/fromlib/'+str(name)+'/'+str(doNotCenter)+'', None, None)
    def addSectionByPoints(self, x, y, CF_tw, CF_rc, material, doNotCenter): return self.nfrest('GET', '/section/add/bypoints/'+str(CF_tw)+'/'+str(CF_rc)+'/'+str(material)+'/'+str(doNotCenter)+'', None, dict([("x",x),("y",y)]))
    def addSectionCover(self, sectionID, coverMat, coverThickness): return self.nfrest('GET', '/section/add/cover/'+str(sectionID)+'/'+str(coverMat)+'/'+str(coverThickness)+'', None, None)
    def addSectionFromDXF(self, path, CF_tw, CF_rc, material): return self.nfrest('GET', '/section/add/fromdxf/'+str(CF_tw)+'/'+str(CF_rc)+'/'+str(material)+'', None, dict([("path", path)]))
    def addSeriesFunction(self, Xlist, Ylist, type, units): return self.nfrest('GET', '/function/add/'+str(type)+'', None, dict([("x",Xlist), ("y",Ylist), ("units",units)]))
    def addSineFunction(self, frequency, phase, stp, duration, maxAmplitude, isGrowing, type, units): return self.nfrest('GET', '/function/sine/'+str(frequency)+'/'+str(phase)+'/'+str(stp)+'/'+str(duration)+'/'+str(maxAmplitude)+'/'+str(isGrowing)+'/'+str(type)+'', None, dict([("units", units)]))
    def addSolid(self, nodes, mat): return self.nfrest('GET', '/element/add/solid/'+str(mat)+'', None, dict([("nodes", nodes)]))
    def addSpring(self, n1, n2, propName): return self.nfrest('GET', '/element/add/beam/'+str(n1)+'/'+str(n2)+'/'+str(propName)+'', None, None)
    def addSpringNLProperty(self, name, NLdofs, NLprops, local): return self.nfrest('POST', '/springproperty/nl/add/'+str(name)+'/'+str(NLdofs(0))+'/'+str(NLdofs(1))+'/'+str(NLdofs(2))+'/'+str(NLdofs(3))+'/'+str(NLdofs(4))+'/'+str(NLdofs(5))+'/'+str(local)+'', NLprops, None)
    def addSpringProperty(self, name, Kx, Ky, Kz, Krx, Kry, Krz, local): return self.nfrest('GET', '/springproperty/simple/add/'+str(name)+'/'+str(Kx)+'/'+str(Ky)+'/'+str(Kz)+'/'+str(Krx)+'/'+str(Kry)+'/'+str(Krz)+'/'+str(local)+'', None, None)
    def addSpringsOnOverlappedNodes(self, n, propName): return self.nfrest('POST', '/element/add/springsonnodes/'+str(propName)+'', n, None)
    def addStirrupBars(self, elem, LnumY, LnumZ, area, spacing, matID, Linit, Lfin): return self.nfrest('GET', '/element/rebar/stirrup/'+str(elem)+'/'+str(LnumY)+'/'+str(LnumZ)+'/'+str(area)+'/'+str(spacing)+'/'+str(matID)+'/'+str(Linit)+'/'+str(Lfin)+'', None, None)
    def addStirrupBarsInSection(self, sectionID, LnumY, LnumZ, area, spacing, matID): return self.nfrest('GET', '/section/rebar/stirrup/'+str(sectionID)+'/'+str(LnumY)+'/'+str(LnumZ)+'/'+str(area)+'/'+str(spacing)+'/'+str(matID)+'', None, None)
    def addSubsoilNodalSpringsOnElements(self, n, propName): return self.nfrest('POST', '/element/add/soilsprings/'+str(propName)+'', n, None)
    def addSubsoilZProperty(self, width, Rmodulus): return self.nfrest('GET', '/springproperty/subsoil/add/'+str(width)+'/'+str(Rmodulus)+'', None, None)
    def addSurfaceLoad(self, elem, values, direction, loadcase, local): return self.nfrest('POST', '/load/element/surfaceadd/'+str(elem)+'/'+str(direction)+'/'+str(loadcase)+'/'+str(local)+'', values, None)
    def addThermalDistLoad(self, elem, values, loadcase): return self.nfrest('POST', '/load/element/tempdistadd/'+str(elem)+'/'+str(loadcase)+'', values, None)
    def addTria(self, n1, n2, n3, sect, mat): return self.nfrest('GET', '/element/add/tria/'+str(n1)+'/'+str(n2)+'/'+str(n3)+'/'+str(sect)+'/'+str(mat)+'', None, None)
    def addTruss(self, n1, n2, sect, mat): return self.nfrest('GET', '/element/add/truss/'+str(n1)+'/'+str(n2)+'/'+str(sect)+'/'+str(mat)+'', None, None)
    def addTSection(self, Lz, Ly, tw, tf1): return self.nfrest('GET', '/section/add/tshape/'+str(Lz)+'/'+str(Ly)+'/'+str(tw)+'/'+str(tf1)+'', None, None)
    def addVolumeLoad(self, elem, value, direction, loadcase): return self.nfrest('GET', '/load/element/volumeadd/'+str(elem)+'/'+str(value)+'/'+str(direction)+'/'+str(loadcase)+'', None, None)
    def alignShellXaxis(self, num, x, y, z): return self.nfrest('GET', '/element/shellxaxis/'+str(num)+'/'+str(x)+'/'+str(y)+'/'+str(z)+'', None, None)
    def AnalyzeFireElement(self, elem, endTime, beamExposure, columnExposure, checkCombo, selectForcesCrit, fireCurve, outOfProc, noWindow, customFireCurve): return self.nfrest('GET', '/res/check/analyzefire/'+str(elem)+'/'+str(endTime)+'/'+str(beamExposure)+'/'+str(columnExposure)+'/'+str(checkCombo)+'/'+str(selectForcesCrit)+'/'+str(fireCurve)+'/'+str(outOfProc)+'/'+str(noWindow)+'/'+str(customFireCurve)+'', None, None)
    def appendDocXformula(self, TeXcode, alignment): return self.nfrest('POST', '/op/docx/appendformula/'+str(alignment)+'', TeXcode, None)
    def appendDocXimage(self, imagePath, ratio, alignment): return self.nfrest('GET', '/op/docx/appendimage/'+str(ratio)+'/'+str(alignment)+'', None, dict([("path", imagePath)]))
    def appendDocXtext(self, text, alignment): return self.nfrest('POST', '/op/docx/appendtext/'+str(alignment)+'', text, None)
    def applyButterworthFilter(self, values, samplingF, cutF, order, lowPass): return self.nfrest('POST', '/op/bwfilter/'+str(samplingF)+'/'+str(cutF)+'/'+str(order)+'/'+str(lowPass)+'', values, None)
    def applyEC8lateralForces(self, thID, loadCaseX, loadCaseY, propMasses, T1, ct, lam): return self.nfrest('GET', '/load/lateralforces/'+str(thID)+'/'+str(loadCaseX)+'/'+str(loadCaseY)+'/'+str(propMasses)+'/'+str(T1)+'/'+str(ct)+'/'+str(lam)+'', None, None)
    def assignHinge(self, beamID, hingeName): return self.nfrest('GET', '/hinge/assign/'+str(beamID)+'/'+str(hingeName)+'', None, None)
    def assignMaterialToElement(self, element, materialID): return self.nfrest('GET', '/material/assign/'+str(element)+'/'+str(materialID)+'', None, None)
    def assignSectionToElement(self, element, sectionID): return self.nfrest('GET', '/section/assign/'+str(element)+'/'+str(sectionID)+'', None, None)
    def assignSubsoilProperty(self, element, prop): return self.nfrest('GET', '/springproperty/subsoil/assign/'+str(element)+'/'+str(prop)+'', None, None)
    def assignToGroup(self, name, nodes, elements, clear): return self.nfrest('GET', '/group/assign/'+str(name)+'/'+str(clear)+'', None, dict([("nodes", nodes), ("elements", elements)]))
    def changeDefSolverType(self, type): return self.nfrest('GET', '/op/opt/changedefsolvertype/'+str(type)+'', None, None)
    def changeElementProperty(self, ID, prop, value): return self.nfrest('POST', '/element/prop/'+str(ID)+'/'+str(prop)+'/'+str(value)+'', None, None)
    def changeLoadValue(self, i, loadValue): return self.nfrest('GET', '/load/change/'+str(i)+'/'+str(loadValue)+'', None, None)
    def changeOrAddSectionPoint(self, sectionID, seriesID, ptID, x, y): return self.nfrest('GET', '/section/add/changeaddpt/'+str(sectionID)+'/'+str(ptID)+'/'+str(x)+'/'+str(y)+'', None, None)
    def changeSolver(self, type, path): return self.nfrest('GET', '/op/opt/changesolver/'+str(type)+'', None, dict([("path", path)]))
    def changeSpringNLProperty(self, name, NLdofs, NLprops): return self.nfrest('POST', '/springproperty/nl/change/'+str(name)+'/'+str(NLdofs(0))+'/'+str(NLdofs(1))+'/'+str(NLdofs(2))+'/'+str(NLdofs(3))+'/'+str(NLdofs(4))+'/'+str(NLdofs(5))+'', NLprops, None)
    def changeSpringNLPropertyDof(self, name, DoF, NLtype, NLprops): return self.nfrest('POST', '/springproperty/nl/change/'+str(name)+'/'+str(DoF)+'/'+str(NLtype)+'', NLprops, None)
    def changeSpringProperty(self, name, Kx, Ky, Kz, Krx, Kry, Krz): return self.nfrest('GET', '/springproperty/simple/change/'+str(name)+'/'+str(Kx)+'/'+str(Ky)+'/'+str(Kz)+'/'+str(Krx)+'/'+str(Kry)+'/'+str(Krz)+'', None, None)
    def checkElements(self, elems, lc, ts, stationType, verName, savelog, messages, defaultParams): return self.nfrest('GET', '/res/check/elements/'+str(lc)+'/'+str(ts)+'/'+str(stationType)+'/'+str(verName)+'/'+str(savelog)+'/'+str(messages)+'', None, dict([("defaultParams", defaultParams),("elems", elems)]))
    def checkElementsRatio(self, elems, lc, ts, stationType, verName, savelog, messages, defaultParams): return self.nfrest('GET', '/res/check/elementsRatio/'+str(lc)+'/'+str(ts)+'/'+str(stationType)+'/'+str(verName)+'/'+str(savelog)+'/'+str(messages)+'', None, dict([("defaultParams", defaultParams),("elems", elems)]))
    def checkFreeNodes(self): return self.nfrest('GET', '/op/mesh/findfreenodes', None, None)
    def checkLineElements(self): return self.nfrest('GET', '/op/mesh/lineelems', None, None)
    def checkModel(self, lc, ts, stationType, verName, savelog, messages, defaultParams): return self.nfrest('GET', '/res/check/model/'+str(lc)+'/'+str(ts)+'/'+str(stationType)+'/'+str(verName)+'/'+str(savelog)+'/'+str(messages)+'', None, dict([("defaultParams", defaultParams)]))
    def checkNodes(self, nodes, lc, ts, stationType, verName, savelog, messages, defaultParams): return self.nfrest('GET', '/res/check/nodes/'+str(lc)+'/'+str(ts)+'/'+str(verName)+'/'+str(savelog)+'/'+str(messages)+'', None, dict([("defaultParams", defaultParams),("nodes", nodes)]))
    def checkOverlappedElements(self): return self.nfrest('GET', '/op/mesh/findoverlappedelements', None, None)
    def clearElementCustomProperties(self, elem): return self.nfrest('DELETE', '/element/customprop/'+str(elem)+'', None, None)
    def clearElementRebar(self, elem): return self.nfrest('GET', '/element/rebar/clear/'+str(elem)+'', None, None)
    def clearSectionRebar(self, ID): return self.nfrest('GET', '/section/rebar/clear/'+str(ID)+'', None, None)
    def clearSectionRebar(self, ID): return self.nfrest('GET', '/section/rebar/clear/'+str(ID)+'', None, None)
    def clearSelection(self): return self.nfrest('GET', '/op/clearselection', None, None)
    def clearStoredDomains(self): return self.nfrest('GET', '/res/check/cleardomains', None, None)
    def colorizeModel(self, criterion, excl): return self.nfrest('GET', '/model/colors/colorize/'+str(criterion)+'', None, dict([("excl", excl)]))
    def convertToMeshedSection(self, sectionID): return self.nfrest('GET', '/op/mesh/meshedsection/'+str(sectionID)+'', None, None)
    def convertUnits(self, length, force): return self.nfrest('GET', '/units/convertunits/'+str(length)+'/'+str(force)+'', None, None)
    def convertValue(self, value, OldUnits, NewUnits): return self.nfrest('GET', '/units/convert/'+str(value)+'', None, dict([("OldUnits", OldUnits), ("NewUnits", NewUnits)]))
    def createDocX(self, path, text, template): return self.nfrest('GET', '/op/docx/create', None, dict([("path", path), ("template", template)]))
    def CustomLicense(self, lic): return self.nfrest('GET', '/op/lic', None, dict([("val", lic)]))
    def defaultColors(self): return self.nfrest('GET', '/model/colors/default', None, None)
    def deleteChecks(self): return self.nfrest('GET', '/res/delchecks', None, None)
    def deleteGroup(self, name): return self.nfrest('GET', '/group/delete/'+str(name)+'', None, None)
    def deleteResults(self): return self.nfrest('GET', '/res/delete', None, None)
    def divideHexa(self, hexaID, divX, divY, divZ): return self.nfrest('GET', '/op/mesh/dividehexa/'+str(hexaID)+'/'+str(divX)+'/'+str(divY)+'/'+str(divZ)+'', None, None)
    def divideLine(self, lines, fractions): return self.nfrest('GET', '/op/mesh/divideline', None, dict([("lines", lines), ("fractions", fractions)]))
    def divideLineByNodes(self, line, nodes): return self.nfrest('GET', '/op/mesh/dividelinebynodes/'+str(line)+'', None, dict([("nodes", nodes)]))
    def divideQuad(self, quadID, divX, divY): return self.nfrest('GET', '/op/mesh/dividequad/'+str(quadID)+'/'+str(divX)+'/'+str(divY)+'', None, None)
    def divideWedge(self, wedgeID, div): return self.nfrest('GET', '/op/mesh/dividewedge/'+str(wedgeID)+'/'+str(div)+'', None, None)
    def duplicateSection(self, originalID): return self.nfrest('GET', '/section/duplicate/'+str(originalID)+'', None, None)
    def exportGLTF(self, path, saveIFC): return self.nfrest('GET', '/op/export/gltf/'+str(saveIFC)+'', None, dict([("path", path)]))
    def exportIFC(self, path, saveAsXML): return self.nfrest('GET', '/op/export/ifc/'+str(saveAsXML)+'', None, dict([("path", path)]))
    def exportIOM(self, filename): return self.nfrest('GET', '/op/export/idea', None, dict([("path", filename)]))
    def exportMidas(self, path): return self.nfrest('GET', '/op/export/midas', None, dict([("path", path)]))
    def exportOpenSees(self, path, loadcase): return self.nfrest('GET', '/op/export/opensees/'+str(loadcase)+'', None, dict([("path", path)]))
    def exportRCbeamsDXF(self, path, elements): return self.nfrest('GET', '/element/exportdxf', None, dict([("path", path), ("elements", elements)]))
    def exportRCmemberDXF(self, path, member): return self.nfrest('GET', '/model/member/exportdxf/'+str(member)+'', None, dict([("path", path)]))
    def exportSAP2000(self, path): return self.nfrest('GET', '/op/export/sap2000', None, dict([("path", path)]))
    def exportSectionDXF(self, path, sID): return self.nfrest('GET', '/section/exportdxf/'+str(sID)+'', None, dict([("path", path)]))
    def exportWexBIM(self, path, saveIFC, copyViewer): return self.nfrest('GET', '/op/export/wexbim/'+str(saveIFC)+'/'+str(copyViewer)+'', None, dict([("path", path)]))
    def exportXMLresults(self, filename): return self.nfrest('GET', '/op/export/xmlres', None, dict([("path", filename)]))
    def functionFromFile(self, filename, type, units): return self.nfrest('GET', '/function/fromfile/'+str(type)+'', None, dict([("units",units), ("path",filename)]))
    def generateFrame(self, baysX, baysY, sn, ddx, ddy, ddz, sx, sy, sz, matx, maty, matz, lc1, lc2, lc3, Lval1, Lval2, Lval3, loadBeamX, rigidfloor): return self.nfrest('GET', '/op/mesh/generateframe/'+str(baysX)+'/'+str(baysY)+'/'+str(sn)+'/'+str(ddx)+'/'+str(ddy)+'/'+str(ddz)+'/'+str(sx)+'/'+str(sy)+'/'+str(sz)+'/'+str(matx)+'/'+str(maty)+'/'+str(matz)+'/'+str(lc1)+'/'+str(lc2)+'/'+str(lc3)+'/'+str(Lval1)+'/'+str(Lval2)+'/'+str(Lval3)+'/'+str(loadBeamX)+'/'+str(rigidfloor)+'', None, None)
    def generateLoadCombinations(self, type, comboPrefix): return self.nfrest('GET', '/loadcase/generate/'+str(type)+'/'+str(comboPrefix)+'', None, None)
    def getAlignedNodes(self, n1, n2, tol): return self.nfrest('GET', '/op/mesh/alignednodes/'+str(tol)+'', None, dict([("n1", n1), ("n2", n2)]))
    def getAnalysisTimeSteps(self, lc): return self.nfrest('GET', '/res/steps/'+str(lc)+'', None, None)
    def getAreaByNodes(self, nodes): return self.nfrest('POST', '/node/area', nodes, None)
    def getBC(self, node): return self.nfrest('GET', '/bc/get/'+str(node)+'', None, None)
    def getBeamDeflection(self, num, loadcase, time, type, station): return self.nfrest('GET', '/res/beamdeflection/'+str(num)+'/'+str(loadcase)+'/'+str(time)+'/'+str(type)+'/'+str(station)+'', None, None)
    def getBeamDeflections(self, num, loadcase, type, offsetL, numStations, time): return self.nfrest('GET', '/res/beamdeflections/'+str(num)+'/'+str(loadcase)+'/'+str(type)+'/'+str(offsetL)+'/'+str(numStations)+'/'+str(time)+'', None, None)
    def getBeamForce(self, num, loadcase, time, type, station): return self.nfrest('GET', '/res/beamforce/'+str(num)+'/'+str(loadcase)+'/'+str(time)+'/'+str(type)+'/'+str(station)+'', None, None)
    def getBeamForce2(self, num, loadcase, time, type, absissa): return self.nfrest('GET', '/res/beamforce2/'+str(num)+'/'+str(loadcase)+'/'+str(time)+'/'+str(absissa)+'', None, None)
    def getBeamForces(self, num, loadcase, station, time): return self.nfrest('GET', '/res/beamforces/'+str(num)+'/'+str(loadcase)+'/'+str(station)+'/'+str(time)+'', None, None)
    def getBeamForcesAtNode(self, elem, node, loadcase, time): return self.nfrest('GET', '/res/beamforcesatnode/'+str(elem)+'/'+str(node)+'/'+str(loadcase)+'/'+str(time)+'', None, None)
    def getBeamForcesDiagram(self, num, loadcase, type, offsetL, numStations, time): return self.nfrest('GET', '/res/beamdiagram/'+str(num)+'/'+str(loadcase)+'/'+str(type)+'/'+str(offsetL)+'/'+str(numStations)+'/'+str(time)+'', None, None)
    def getBeamResMoments(self, elemID): return self.nfrest('GET', '/res/check/beammoments/'+str(elemID)+'', None, None)
    def getBeamResShear(self, elemID, loadcase, time): return self.nfrest('GET', '/res/check/beamshearres/'+str(elemID)+'/'+str(loadcase)+'/'+str(time)+'', None, None)
    def getBuiltInChecking(self): return self.nfrest('GET', '/res/check/sets', None, None)
    def getCheckNameByMaterial(self, ID): return self.nfrest('GET', '/res/check/checkbymat/'+str(ID)+'', None, None)
    def getCombinationCoeffPsi(self, subscript, type): return self.nfrest('GET', '/loadcase/getpsi/'+str(subscript)+'/'+str(type)+'', None, None)
    def getCombinationDesignType(self, name): return self.nfrest('GET', '/loadcase/combo/designtype/'+str(name)+'', None, None)
    def getCombinationsByDesignType(self, type, servType): return self.nfrest('GET', '/loadcases/descombos/designtype/'+str(type)+'/'+str(servType)+'', None, None)
    def getConnectedElements(self, node, onlyOfType): return self.nfrest('GET', '/node/connectedelements/'+str(node)+'/'+str(onlyOfType)+'', None, None)
    def getControlNode(self): return self.nfrest('GET', '/op/controlnode', None, None)
    def getCornerNodes(self, nodes, lcs): return self.nfrest('GET', '/op/corners', None, dict([("nodes", nodes), ("lcs", lcs)]))
    def getCustomData(self, key): return self.nfrest('GET', '/model/customdata/'+str(key)+'', None, None)
    def getDataPlot(self, xseries, yseries, imagePath, name, Xunits, Yunits): return self.nfrest('GET', '/function/plotdata/'+str(name)+'', None, dict([("path", imagePath), ("xseries", xseries), ("yseries", yseries), ("Xunits", Xunits), ("Yunits", Yunits)]))
    def getDefinedDesignMaterials(self): return self.nfrest('GET', '/designmaterials', None, None)
    def getDefinedMaterials(self): return self.nfrest('GET', '/materials', None, None)
    def getDefinedSections(self): return self.nfrest('GET', '/sections', None, None)
    def getDesignMaterialsLibrary(self, filter, type): return self.nfrest('GET', '/designmaterials/library/'+str(filter)+'/'+str(type)+'', None, None)
    def getDesignMaterialsLibrary(self, filename, filter, type): return self.nfrest('GET', '/designmaterials/libraryf/'+str(filename)+'/'+str(filter)+'/'+str(type)+'', None, None)
    def getElementArea(self, ID): return self.nfrest('GET', '/element/area/'+str(ID)+'', None, None)
    def getElementCentroid(self, ID): return self.nfrest('GET', '/element/centroid/'+str(ID)+'', None, None)
    def getElementChecks(self, ID, lc, time): return self.nfrest('GET', '/res/check/elementA/'+str(ID)+'/'+str(lc)+'/'+str(time)+'', None, None)
    def getElementConnectivity(self, ID): return self.nfrest('GET', '/element/conn/'+str(ID)+'', None, None)
    def getElementCustomProperty(self, elem, propName): return self.nfrest('GET', '/element/customprop/'+str(elem)+'/'+str(propName)+'', None, None)
    def getElementInfo(self, element): return self.nfrest('GET', '/element/info/'+str(element)+'', None, None)
    def getElementOffset(self, elem): return self.nfrest('GET', '/element/beamoffset/'+str(elem)+'', None, None)
    def getElementProperty(self, ID, name): return self.nfrest('GET', '/element/prop/'+str(ID)+'/'+str(name)+'', None, None)
    def getElementRebarSegments(self, elem): return self.nfrest('GET', '/section/rebar/segments/'+str(elem)+'', None, None)
    def getElementsChecks(self, lc, time): return self.nfrest('GET', '/res/check/elementsA/'+str(lc)+'/'+str(time)+'', None, None)
    def getElementsChecksByMat(self, mat): return self.nfrest('GET', '/res/check/elementsM/'+str(mat)+'', None, None)
    def getElementsFromGroup(self, name): return self.nfrest('GET', '/group/elements/'+str(name)+'', None, None)
    def getElementType(self, ID): return self.nfrest('GET', '/element/type/'+str(ID)+'', None, None)
    def getElementVolume(self, ID): return self.nfrest('GET', '/element/volume/'+str(ID)+'', None, None)
    def getEndRelease(self, beamID): return self.nfrest('GET', '/element/beamendrelease/'+str(beamID)+'', None, None)
    def getEnvelopeCombination(self, name): return self.nfrest('GET', '/loadcase/combo/getenv/'+str(name)+'', None, None)
    def getExtrudedBeamPoints(self, elemID): return self.nfrest('GET', '/element/extrudedbeam/'+str(elemID)+'', None, None)
    def getFirstMode(self, ct): return self.nfrest('GET', '/res/firstmode/'+str(ct)+'', None, None)
    def getFloorLoadType(self, name): return self.nfrest('GET', '/load/floor/planetype/'+str(name)+'', None, None)
    def getFloorPlanes(self): return self.nfrest('GET', '/load/floor/planesget', None, None)
    def getForceUnit(self): return self.nfrest('GET', '/units/f', None, None)
    def getFreeElementID(self): return self.nfrest('GET', '/op/freeelementid', None, None)
    def getFreeNodeID(self): return self.nfrest('GET', '/op/freenodeid', None, None)
    def getFunctionGeneralData(self, funcID): return self.nfrest('GET', '/function/gendata/'+str(funcID)+'', None, None)
    def getFunctionName(self, funcID): return self.nfrest('GET', '/function/name/'+str(funcID)+'', None, None)
    def getFunctionPlot(self, funcID, imagePath): return self.nfrest('GET', '/function/plot/'+str(funcID)+'', None, dict([("path", imagePath)]))
    def getFunctions(self): return self.nfrest('GET', '/functions', None, None)
    def getFunctionUnits(self, funcID): return self.nfrest('GET', '/function/units/'+str(funcID)+'', None, None)
    def getGreekLetter(self, input): return self.nfrest('GET', '/op/greek', None, None)
    def getGroups(self): return self.nfrest('GET', '/groups', None, None)
    def getLanguage(self): return self.nfrest('GET', '/op/opt/lang', None, None)
    def getLastBilinearMomentCurvature(self): return self.nfrest('GET', '/op/sectioncalc/bilmomentcurvature', None, None)
    def getLastMomentCurvatureData(self): return self.nfrest('GET', '/op/sectioncalc/momentcurvaturedata', None, None)
    def getLastRunLog(self): return self.nfrest('GET', '/op/runlog', None, None)
    def getLenUnit(self): return self.nfrest('GET', '/units/l', None, None)
    def getLinearAddCombination(self, name): return self.nfrest('GET', '/loadcase/combo/get/'+str(name)+'', None, None)
    def getLoad(self, i): return self.nfrest('GET', '/load/'+str(i)+'', None, None)
    def getLoadA(self, i): return self.nfrest('GET', '/load/getA/'+str(i)+'', None, None)
    def getLoadcaseFactor(self, loadcase): return self.nfrest('GET', '/loadcase/getfactor/'+str(loadcase)+'', None, None)
    def getLoadCases(self): return self.nfrest('GET', '/loadcases', None, None)
    def getLoadCombinations(self, includeEnvelopes): return self.nfrest('GET', '/loadcase/combos/'+str(includeEnvelopes)+'', None, None)
    def getLoadDurationClass(self, loadcase): return self.nfrest('GET', '/load/getduration/'+str(loadcase)+'', None, None)
    def getLoadingData(self): return self.nfrest('GET', '/model/loadingdata', None, None)
    def getLoadsForElement(self, element): return self.nfrest('GET', '/load/element/get/'+str(element)+'', None, None)
    def getLoadsForNode(self, node): return self.nfrest('GET', '/load/node/get/'+str(node)+'', None, None)
    def getLoadsInLoadcase(self, loadcase): return self.nfrest('GET', '/load/inloadcase/'+str(loadcase)+'', None, None)
    def getLocalAxes(self, ID): return self.nfrest('GET', '/element/lcs/'+str(ID)+'', None, None)
    def getLocalAxesArray(self, ID): return self.nfrest('GET', '/element/lcsA/'+str(ID)+'', None, None)
    def getMacroelement(self, elemID): return self.nfrest('GET', '/element/macro/'+str(elemID)+'', None, None)
    def getMaterialsLibrary(self, filter, type): return self.nfrest('GET', '/materials/library/'+str(filter)+'/'+str(type)+'', None, None)
    def getMaterialsLibrary(self, filename, filter, type): return self.nfrest('GET', '/materials/libraryf/'+str(filename)+'/'+str(filter)+'/'+str(type)+'', None, None)
    def getMaxMinBeamForces(self, sectionID, type): return self.nfrest('GET', '/res/maxminbeamforces/'+str(sectionID)+'/'+str(type)+'', None, None)
    def getMaxMinNodeDispl(self, dir, nodes): return self.nfrest('POST', '/res/maxmindispl/'+str(dir)+'', nodes, None)
    def getMaxMinWoodArmerMoments(self, elementID): return self.nfrest('GET', '/res/maxminwoodarmer/'+str(elementID)+'', None, None)
    def getMaxMinWoodArmerMoments(self, groupName): return self.nfrest('GET', '/res/maxminwoodarmerg/'+str(groupName)+'', None, None)
    def getMemberElements(self, member): return self.nfrest('GET', '/model/member/elems/'+str(member)+'', None, None)
    def getMemberLength(self, member): return self.nfrest('GET', '/model/member/leng/'+str(member)+'', None, None)
    def getMembers(self): return self.nfrest('GET', '/model/member/all', None, None)
    def getModalPeriod(self, num, loadcase): return self.nfrest('GET', '/res/period/'+str(num)+'/'+str(loadcase)+'', None, None)
    def getNodalDisp(self, num, loadcase, time, direction): return self.nfrest('GET', '/res/displacement/'+str(num)+'/'+str(loadcase)+'/'+str(time)+'/'+str(direction)+'', None, None)
    def getNodalReact(self, num, loadcase, time, direction): return self.nfrest('GET', '/res/reaction/'+str(num)+'/'+str(loadcase)+'/'+str(time)+'/'+str(direction)+'', None, None)
    def getNodalShellForce(self, num, loadcase, time, type): return self.nfrest('GET', '/res/nodalshellforce/'+str(num)+'/'+str(loadcase)+'/'+str(time)+'/'+str(type)+'', None, None)
    def getNodalStress(self, num, loadcase, time, type): return self.nfrest('GET', '/res/nodalstress/'+str(num)+'/'+str(loadcase)+'/'+str(time)+'/'+str(type)+'', None, None)
    def getNodeChecks(self, ID, lc, time): return self.nfrest('GET', '/res/check/nodsA/'+str(ID)+'/'+str(lc)+'/'+str(time)+'', None, None)
    def getNodeCoordinates(self, ID): return self.nfrest('GET', '/node/ID', None, None)
    def getNodeInfo(self, node): return self.nfrest('GET', '/node/info/'+str(node)+'', None, None)
    def getNodePosition(self, ID): return self.nfrest('GET', '/node/ID', None, None)
    def getNodeProperty(self, ID, name): return self.nfrest('GET', '/node/prop/'+str(ID)+'/'+str(name)+'', None, None)
    def getNodesChecks(self, lc, time): return self.nfrest('GET', '/res/check/nodesA/'+str(lc)+'/'+str(time)+'', None, None)
    def getNodesFromCoords(self, dir, coord, tol): return self.nfrest('GET', '/op/mesh/nodesbycoords/'+str(dir)+'/'+str(coord)+'/'+str(tol)+'', None, None)
    def getNodesFromGroup(self, name): return self.nfrest('GET', '/group/nodes/'+str(name)+'', None, None)
    def getNodesOnSides(self, nodes, tol): return self.nfrest('GET', '/op/mesh/borders/'+str(tol)+'', None, dict([("nodes", nodes)]))
    def getOSprocedureName(self): return self.nfrest('GET', '/op/export/osproc', None, None)
    def getParticipatingMassesRatios(self, mode, loadcase): return self.nfrest('GET', '/res/partmasses/'+str(mode)+'/'+str(loadcase)+'', None, None)
    def getParticipationFactors(self, mode, loadcase): return self.nfrest('GET', '/res/partfactors/'+str(mode)+'/'+str(loadcase)+'', None, None)
    def getReinfPropertiesNTC(self, matID, secID, CF, betaAng, Hshear, Bshear, outInMPa): return self.nfrest('GET', '/material/frpdata/'+str(matID)+'/'+str(secID)+'/'+str(CF)+'/'+str(betaAng)+'/'+str(Hshear)+'/'+str(Bshear)+'/'+str(outInMPa)+'', None, None)
    def getResultHistory(self, loadcase, itemID, resultType, resultID1, resultID2): return self.nfrest('GET', '/res/hist/'+str(loadcase)+'/'+str(itemID)+'/'+str(resultType)+'/'+str(resultID1)+'/'+str(resultID2)+'', None, None)
    def getRigidDiaphragms(self): return self.nfrest('GET', '/op/mesh/rigiddiaph', None, None)
    def getRigidOffsets(self, beamID): return self.nfrest('GET', '/element/beamendoffset/'+str(beamID)+'', None, None)
    def getSectionColor(self, ID): return self.nfrest('GET', '/section/set/color/'+str(ID)+'', None, None)
    def getSectionCutForce(self, groupName, loadcase, time, type): return self.nfrest('GET', '/res/sectioncutforce/'+str(groupName)+'/'+str(loadcase)+'/'+str(time)+'/'+str(type)+'', None, None)
    def getSectionFigure(self, sectionID, figureID, isHole): return self.nfrest('GET', '/section/figure/'+str(sectionID)+'/'+str(figureID)+'/'+str(isHole)+'', None, None)
    def getSectionOffset(self, ID): return self.nfrest('GET', '/section/set/offset/'+str(ID)+'', None, None)
    def getSectionProperties(self, ID): return self.nfrest('GET', '/section/props/'+str(ID)+'', None, None)
    def getSectionProperty(self, ID, name): return self.nfrest('GET', '/section/prop/'+str(ID)+'/'+str(name)+'', None, None)
    def getSectionRebarCoords(self, ID): return self.nfrest('GET', '/section/rebar/coords/'+str(ID)+'', None, None)
    def getSectionResDomainPoints(self, domainIndex, domainType, cleanResponseTolerance): return self.nfrest('GET', '/res/check/plotsectiondomain/'+str(domainIndex)+'/'+str(domainType)+'/'+str(cleanResponseTolerance)+'', None, None)
    def getSectionResMoments(self, ID, station, calcType, N, Myy, Mzz): return self.nfrest('GET', '/op/sectioncalc/a/'+str(ID)+'/'+str(station)+'/'+str(calcType)+'/'+str(N)+'/'+str(Myy)+'/'+str(Mzz)+'', None, None)
    def getSectionResMoments(self, sectionID, materialID, calcType, N, Myy, Mzz): return self.nfrest('GET', '/op/sectioncalc/b/'+str(sectionID)+'/'+str(materialID)+'/'+str(calcType)+'/'+str(N)+'/'+str(Myy)+'/'+str(Mzz)+'', None, None)
    def getSectionResShear(self, sectionID, N, Mzz, Myy, Vy, Vz): return self.nfrest('GET', '/op/sectioncalc/shear/'+str(sectionID)+'/'+str(N)+'/'+str(Myy)+'/'+str(Mzz)+'/'+str(Vy)+'/'+str(Vz)+'', None, None)
    def getSectionResShear(self, sectionID, verName, N, Mzz, Myy, Vy, Vz): return self.nfrest('GET', '/op/sectioncalc/shear/'+str(sectionID)+'/'+str(verName)+'/'+str(N)+'/'+str(Myy)+'/'+str(Mzz)+'/'+str(Vy)+'/'+str(Vz)+'', None, None)
    def getSectionsLibrary(self, filter): return self.nfrest('GET', '/sections/library/'+str(filter)+'', None, None)
    def getSectionsLibrary(self, filename, filter): return self.nfrest('GET', '/sections/libraryf/'+str(filename)+'/'+str(filter)+'', None, None)
    def getSectMomentCurvature(self, sectionID, N, Mzz, Myy, npts, Nserv, Mzzserv, Myyserv): return self.nfrest('GET', '/op/sectioncalc/momentcurvature/'+str(sectionID)+'/'+str(N)+'/'+str(Mzz)+'/'+str(Myy)+'/'+str(npts)+'/'+str(Nserv)+'/'+str(Mzzserv)+'/'+str(Myyserv)+'', None, None)
    def getSeparator(self): return self.nfrest('GET', '/op/sep', None, None)
    def getShellEndRelease(self, ID): return self.nfrest('GET', '/element/shellendrelease/'+str(ID)+'', None, None)
    def getSoilPressureAtNode(self, node, loadcase, time): return self.nfrest('GET', '/res/soilpressureatnode/'+str(node)+'/'+str(loadcase)+'/'+str(time)+'', None, None)
    def getSpringLocalAxes(self, elem): return self.nfrest('GET', '/springproperty/axes/'+str(elem)+'', None, None)
    def getSubsoilElements(self): return self.nfrest('GET', '/element/add/subsoil', None, None)
    def getTimePeriods(self, lc): return self.nfrest('GET', '/res/periods/'+str(lc)+'', None, None)
    def getVersion(self): return self.nfrest('GET', '/version', None, None)
    def getWallGroups(self): return self.nfrest('GET', '/element/walls/list', None, None)
    def getWallHeight(self, grpName): return self.nfrest('GET', '/element/walls/height/'+str(grpName)+'', None, None)
    def getWalls(self): return self.nfrest('GET', '/element/walls/elems', None, None)
    def getWallSection(self, grpName): return self.nfrest('GET', '/element/walls/section/'+str(grpName)+'', None, None)
    def hasResults(self, loadcase): return self.nfrest('GET', '/res', None, dict([("lc", loadcase)]))
    def importAbaqusCalculix(self, path): return self.nfrest('GET', '/op/import/abaqus', None, dict([("path", path)]))
    def importDolmen(self, path): return self.nfrest('GET', '/op/import/dolmen', None, dict([("path", path)]))
    def importDXF(self, path): return self.nfrest('GET', '/op/import/dxf', None, dict([("path", path)]))
    def importDXF(self, stream): return self.nfrest('POST', '/op/import/dxfstream', stream, None)
    def importIFC(self, path, includeRigidLinks): return self.nfrest('GET', '/op/import/ifc/'+str(includeRigidLinks)+'', None, dict([("path", path)]))
    def importMidas(self, path): return self.nfrest('GET', '/op/import/midasfile', None, dict([("path", path)]))
    def importMidas(self, model): return self.nfrest('POST', '/op/import/midastext', model, None)
    def importMidasResults(self, path): return self.nfrest('GET', '/op/import/midasresult', None, dict([("path", path)]))
    def importMidasResults(self, text): return self.nfrest('POST', '/op/import/midasresulttext', text, None)
    def importOpenSees(self, path): return self.nfrest('GET', '/op/import/opensees', None, dict([("path", path)]))
    def importOpenSeesRecorder(self, path, type, useTimeFlag): return self.nfrest('GET', '/op/import/recorder/'+str(type)+'/'+str(useTimeFlag)+'', None, dict([("path", path)]))
    def importSAF(self, path): return self.nfrest('GET', '/op/import/saf', None, dict([("path", path)]))
    def importSAP2000(self, path): return self.nfrest('GET', '/op/import/sap2000', None, dict([("path", path)]))
    def importSeismoStruct(self, path): return self.nfrest('GET', '/op/import/seismostruct', None, dict([("path", path)]))
    def importSismicad(self, path, lenUnit, forceUnit): return self.nfrest('GET', '/op/import/sismicad', None, dict([("path", path)]))
    def importSismicadSects_Combo(self, path): return self.nfrest('GET', '/op/import/sismicadset', None, dict([("path", path)]))
    def importSismicadSects_Combo(self, text): return self.nfrest('POST', '/op/import/sismicadsettext', text, None)
    def importSofistik(self, path): return self.nfrest('GET', '/op/import/sofistik', None, dict([("path", path)]))
    def importSR3(self, path): return self.nfrest('GET', '/op/import/sr3', None, dict([("path", path)]))
    def importSR4(self, path): return self.nfrest('GET', '/op/import/sr4', None, dict([("path", path)]))
    def importStraus7(self, path): return self.nfrest('GET', '/op/import/straus7', None, dict([("path", path)]))
    def importStrausResults(self, path): return self.nfrest('GET', '/op/import/straus7result', None, dict([("path", path)]))
    def importStrausResults(self, text): return self.nfrest('POST', '/op/import/straus7resulttext', text, None)
    def importWinStrand(self, path): return self.nfrest('GET', '/op/import/winstrand', None, dict([("path", path)]))
    def is64bit(self): return self.nfrest('GET', '/op/is64bit', None, None)
    def isColumn(self, beamID): return self.nfrest('GET', '/element/iscolumn/'+str(beamID)+'', None, None)
    def isNodeLoaded(self, node): return self.nfrest('GET', '/load/node/isloaded/'+str(node)+'', None, None)
    def isRestrained(self, node): return self.nfrest('GET', '/bc/node/'+str(node)+'', None, None)
    def LangTrasl(self, input): return self.nfrest('POST', '/op/trasl', input, None)
    def LaunchLoadCase(self, loadcase, outOfProc, noWindow): return self.nfrest('GET', '/op/launchlc/'+str(loadcase)+'/'+str(outOfProc)+'/'+str(noWindow)+'', None, None)
    def LaunchModel(self, outOfProc, noWindow): return self.nfrest('GET', '/op/launchmodel/'+str(outOfProc)+'/'+str(noWindow)+'', None, None)
    def listDesignMaterialCustomProperty(self, ID): return self.nfrest('GET', '/designmaterial/proplist/'+str(ID)+'', None, None)
    def listMaterialCustomProperty(self, ID): return self.nfrest('GET', '/material/proplist/'+str(ID)+'', None, None)
    def LoadCaseFromCombo(self, comboName): return self.nfrest('GET', '/loadcase/fromcombo/'+str(comboName)+'', None, None)
    def mergeImportedLines(self, lineIDs): return self.nfrest('GET', '/op/mesh/mergeimportedlines', None, dict([("lines", lineIDs)]))
    def mergeLines(self, lineIDs): return self.nfrest('GET', '/op/mesh/mergelines', None, dict([("lines", lineIDs)]))
    def mergeModelData(self, modeldata): return self.nfrest('PUT', '/model/data', None, None)
    def mergeModelResults(self, modelresults): return self.nfrest('PUT', '/model/results', None, None)
    def mergeOverlappedNodes(self): return self.nfrest('GET', '/op/mesh/mergenodes', None, None)
    def ModelToSection(self, openModelPath): return self.nfrest('GET', '/model/model2section', None, dict([("path", openModelPath)]))
    def moveNodes(self, nodes, displX, displY, displZ, absolutePosition): return self.nfrest('GET', '/op/mesh/movenodes/'+str(displX)+'/'+str(displY)+'/'+str(displZ)+'/'+str(absolutePosition)+'', None, dict([("nodes", nodes)]))
    def newModel(self): return self.nfrest('GET', '/op/new', None, None)
    def openIDEAcodeCheck(self): return self.nfrest('GET', '/op/export/ccm', None, None)
    def openModel(self, filename): return self.nfrest('GET', '/op/open', None, dict([("path", filename)]))
    def quad2tria(self, elem): return self.nfrest('GET', '/op/mesh/quad2tria/'+str(elem)+'', None, None)
    def readBeamForces(self, num, loadcase, time, N, Vy, Vz, Mt, Myy, Mzz, pos): return self.nfrest('GET', '/res/import/beamforces/'+str(num)+'/'+str(loadcase)+'/'+str(time)+'/'+str(N)+'/'+str(Vy)+'/'+str(Vz)+'/'+str(Mt)+'/'+str(Myy)+'/'+str(Mzz)+'/'+str(pos)+'', None, None)
    def recalculateSection(self, ID): return self.nfrest('GET', '/section/recalc/'+str(ID)+'', None, None)
    def refreshHinges(self): return self.nfrest('GET', '/hinge/refresh', None, None)
    def removeAllLoads(self): return self.nfrest('DELETE', '/load/all', None, None)
    def removeAllLoadsForLoadcase(self, lc): return self.nfrest('DELETE', '/load/alllc/'+str(lc)+'', None, None)
    def removeBC(self, node): return self.nfrest('DELETE', '/bc/'+str(node)+'', None, None)
    def removeCompositeFlags(self, ID): return self.nfrest('GET', '/section/set/removecomposite/'+str(ID)+'', None, None)
    def removeCustomData(self, key): return self.nfrest('DELETE', '/model/customdata/'+str(key)+'', None, None)
    def removeDesMaterialProperty(self, ID, name): return self.nfrest('DELETE', '/designmaterial/prop/'+str(ID)+'/'+str(name)+'', None, None)
    def removeElement(self, ID): return self.nfrest('DELETE', '/element/'+str(ID)+'', None, None)
    def removeElementsFromMember(self, member, elems): return self.nfrest('DELETE', '/model/member/elems/'+str(member)+'', None, dict([("elems", elems)]))
    def removeFloorLoad(self, name): return self.nfrest('GET', '/load/floor/remove/'+str(name)+'', None, None)
    def removeFloorPlane(self, name): return self.nfrest('GET', '/load/floor/planeremove/'+str(name)+'', None, None)
    def removeFreeNodes(self): return self.nfrest('GET', '/op/mesh/removefreenodes', None, None)
    def removeHinges(self, beamID): return self.nfrest('GET', '/hinge/remove/'+str(beamID)+'', None, None)
    def removeLink(self, node): return self.nfrest('DELETE', '/op/mesh/constraint/'+str(node)+'', None, None)
    def removeLoad(self, ID): return self.nfrest('DELETE', '/load/'+str(ID)+'', None, None)
    def removeLoadCase(self, name): return self.nfrest('DELETE', '/loadcase/'+str(name)+'', None, None)
    def removeLoadCaseFromCombination(self, name, loadcase): return self.nfrest('GET', '/loadcase/combo/remove/'+str(name)+'/'+str(loadcase)+'', None, None)
    def removeLoadCaseToTimeHistoryAnalysis(self, name, loadcase): return self.nfrest('GET', '/loadcase/combo/removeth/'+str(name)+'/'+str(loadcase)+'', None, None)
    def removeMaterial(self, materialID): return self.nfrest('GET', '/material/remove/'+str(materialID)+'', None, None)
    def removeMaterialProperty(self, ID, name): return self.nfrest('DELETE', '/material/prop/'+str(ID)+'/'+str(name)+'', None, None)
    def removeMember(self, member): return self.nfrest('GET', '/model/member/remove/'+str(member)+'', None, None)
    def removeNodalMass(self, ID): return self.nfrest('GET', '/mass/remove/'+str(ID)+'', None, None)
    def removeNode(self, ID): return self.nfrest('DELETE', '/node/ID', None, None)
    def removeNodeCS(self, num): return self.nfrest('DELETE', '/node/cs/'+str(num)+'', None, None)
    def removeOverlappedElements(self, tol): return self.nfrest('GET', '/op/mesh/removeoverlappedelements', None, None)
    def removeRigidDiaphragms(self): return self.nfrest('DELETE', '/op/mesh/rigiddiaph', None, None)
    def removeSection(self, sectionID): return self.nfrest('GET', '/section/remove/'+str(sectionID)+'', None, None)
    def removeSectionCover(self, sectionID): return self.nfrest('DELETE', '/section/add/cover/'+str(sectionID)+'', None, None)
    def removeSectionFigure(self, sectionID, figureID, isEmpty): return self.nfrest('GET', '/section/add/removefigure/'+str(sectionID)+'/'+str(figureID)+'/'+str(isEmpty)+'', None, None)
    def removeSectionProperty(self, ID, name): return self.nfrest('DELETE', '/section/prop/'+str(ID)+'/'+str(ID)+'/'+str(name)+'', None, None)
    def removeSpringProperty(self, name): return self.nfrest('DELETE', '/springproperty/'+str(name)+'', None, None)
    def renameSection(self, sectionID, name, code): return self.nfrest('GET', '/section/rename/'+str(sectionID)+'/'+str(name)+'/'+str(code)+'', None, None)
    def renumberElements(self, initialID, step): return self.nfrest('GET', '/op/mesh/renumber/elements/'+str(initialID)+'/'+str(step)+'', None, None)
    def renumberElementsByCoordinates(self, dir1, dir2): return self.nfrest('GET', '/op/mesh/renumber/elementsbycoords/'+str(dir1)+'/'+str(dir2)+'', None, None)
    def renumberNodes(self, initialID, step): return self.nfrest('GET', '/op/mesh/renumber/nodes/'+str(initialID)+'/'+str(step)+'', None, None)
    def renumberNodesByCoordinates(self, dir1, dir2): return self.nfrest('GET', '/op/mesh/renumber/nodesbycoords/'+str(dir1)+'/'+str(dir2)+'', None, None)
    def rotateNodes(self, nodes, axisX, axisY, axisZ, angle): return self.nfrest('GET', '/op/mesh/rotatenodes/'+str(axisX)+'/'+str(axisY)+'/'+str(axisZ)+'/'+str(angle)+'', None, dict([("nodes", nodes)]))
    def RunLoadCase(self, loadcase, outOfProc, noWindow): return self.nfrest('GET', '/op/runlc/'+str(loadcase)+'/'+str(outOfProc)+'/'+str(noWindow)+'', None, None)
    def RunModel(self, outOfProc, noWindow): return self.nfrest('GET', '/op/run/'+str(outOfProc)+'/'+str(noWindow)+'', None, None)
    def saveDocX(self): return self.nfrest('GET', '/op/docx/save', None, None)
    def saveModel(self, filename): return self.nfrest('GET', '/op/save', None, dict([("path", filename)]))
    def saveOptions(self): return self.nfrest('GET', '/op/opt/saveopts', None, None)
    def saveSectionImage(self, sectionID, path): return self.nfrest('GET', '/op/sectioncalc/image/'+str(sectionID)+'', None, dict([("path", path)]))
    def saveSectionImageWithBars(self, elemID, progr, path): return self.nfrest('GET', '/op/sectioncalc/imagewithbars/'+str(elemID)+'/'+str(progr)+'', None, dict([("path", path)]))
    def scaleNodes(self, nodes, scaleX, scaleY, scaleZ, scaleCenterX, scaleCenterY, scaleCenterZ): return self.nfrest('GET', '/op/mesh/scalenodes/'+str(scaleX)+'/'+str(scaleY)+'/'+str(scaleZ)+'/'+str(scaleCenterX)+'/'+str(scaleCenterY)+'/'+str(scaleCenterZ)+'', None, dict([("nodes", nodes)]))
    def SectionToModel(self, sectionID, saveModelPath): return self.nfrest('GET', '/model/section2model/'+str(sectionID)+'', None, dict([("path", saveModelPath)]))
    def seriesFromFunction(self, funcID): return self.nfrest('GET', '/function/series/'+str(funcID)+'', None, None)
    def setAluSection(self, ID, SectionClass, Jw): return self.nfrest('GET', '/section/set/alu/'+str(ID)+'/'+str(SectionClass)+'/'+str(Jw)+'', None, None)
    def setAnalysisSequence(self, name, previousCase): return self.nfrest('GET', '/loadcase/sequence/'+str(name)+'/'+str(previousCase)+'', None, None)
    def setBC(self, node, x, y, z, rx, ry, rz): return self.nfrest('GET', '/bc/set/'+str(node)+'/'+str(x)+'/'+str(y)+'/'+str(z)+'/'+str(rx)+'/'+str(ry)+'/'+str(rz)+'', None, None)
    def setBeamAngle(self, num, angle): return self.nfrest('GET', '/element/beamangle/'+str(num)+'/'+str(angle)+'', None, None)
    def setBucklingAnalysis(self, name, Nmodes, tol): return self.nfrest('GET', '/loadcase/setbuck/'+str(name)+'/'+str(Nmodes)+'/'+str(tol)+'', None, None)
    def setCombination(self, name, loadcase, factor, type, servType): return self.nfrest('GET', '/loadcase/combo/set/'+str(name)+'/'+str(loadcase)+'/'+str(factor)+'/'+str(type)+'/'+str(servType)+'', None, None)
    def setCombinationCoeffPsi(self, subscript, type, value): return self.nfrest('GET', '/loadcase/setpsi/'+str(subscript)+'/'+str(type)+'/'+str(value)+'', None, None)
    def setCombinationFactors(self, gG, gQ, psiVar, psiWind, psiSnow, gSW): return self.nfrest('GET', '/loadcase/setcfactors/'+str(gG)+'/'+str(gQ)+'/'+str(gSW)+'', None, dict([("psiVar", psiVar), ("psiWind", psiWind), ("psiSnow", psiSnow)]))
    def setCompositeBeam(self, ID, MposFactor, MnegFactor): return self.nfrest('GET', '/section/set/compositebeam/'+str(ID)+'/'+str(MposFactor)+'/'+str(MnegFactor)+'', None, None)
    def setCompositeColumn(self, ID, EcFactor, ReductionFactor): return self.nfrest('GET', '/section/set/compositecolumn/'+str(ID)+'/'+str(EcFactor)+'/'+str(ReductionFactor)+'', None, None)
    def setConcretePropertiesNTC(self, matID, fc, isCharacteristic, unitsIn): return self.nfrest('GET', '/material/concretentc/'+str(matID)+'/'+str(fc)+'/'+str(isCharacteristic)+'', None, dict([("unitsIn", unitsIn)]))
    def setConstraint(self, n, master, x, y, z, rx, ry, rz): return self.nfrest('GET', '/op/mesh/constraint/'+str(n)+'/'+str(master)+'/'+str(x)+'/'+str(y)+'/'+str(z)+'/'+str(rx)+'/'+str(ry)+'/'+str(rz)+'', None, None)
    def setElemAsJoint(self, num, status): return self.nfrest('GET', '/element/setjoint/'+str(num)+'/'+str(status)+'', None, None)
    def setElementCustomProperty(self, elem, propName, propValue): return self.nfrest('POST', '/element/customprop/'+str(elem)+'/'+str(propName)+'/'+str(propValue)+'', None, None)
    def setElementOffset(self, elem, offsetZ, offsetY): return self.nfrest('POST', '/element/beamoffset/'+str(elem)+'/'+str(offsetZ)+'/'+str(offsetY)+'', None, None)
    def setElementSection(self, elem, sectID): return self.nfrest('GET', '/section/'+str(sectID)+'/assign/'+str(elem)+'', None, None)
    def setEndRelease(self, beamID, node, DOFmask, useStiffness): return self.nfrest('POST', '/element/beamendrelease/'+str(beamID)+'/'+str(node)+'/'+str(useStiffness)+'', None, dict([("DOFmask", DOFmask)]))
    def setEnvelope(self, name, loadcase, factor, type, servType): return self.nfrest('GET', '/loadcase/combo/setenv/'+str(name)+'/'+str(loadcase)+'/'+str(factor)+'/'+str(type)+'/'+str(servType)+'', None, None)
    def setFiberSection(self, ID, divZ, divY): return self.nfrest('GET', '/section/set/fibers/'+str(ID)+'/'+str(divZ)+'/'+str(divY)+'', None, None)
    def setFirePoint(self, loadcase, fireNode, targetTemp, gradientY, gradientZ, tempAtten, dontLoadUnder): return self.nfrest('GET', '/load/firepoint/'+str(loadcase)+'/'+str(fireNode)+'/'+str(targetTemp)+'/'+str(gradientY)+'/'+str(gradientZ)+'/'+str(tempAtten)+'/'+str(dontLoadUnder)+'', None, None)
    def setFloorLoad(self, name, loadcase, loadvalue, dirX, dirY, dirZ): return self.nfrest('GET', '/load/floor/set/'+str(name)+'/'+str(loadcase)+'/'+str(loadvalue)+'/'+str(dirX)+'/'+str(dirY)+'/'+str(dirZ)+'', None, None)
    def setLanguage(self, code): return self.nfrest('POST', '/op/opt/lang/'+str(code)+'', None, None)
    def setLoadA(self, load): return self.nfrest('POST', '/load/setA', load, None)
    def setLoadcaseFactor(self, loadcase, factor): return self.nfrest('GET', '/loadcase/setfactor/'+str(loadcase)+'/'+str(factor)+'', None, None)
    def setLoadCasePhaseInCombination(self, name, loadcase, phase): return self.nfrest('GET', '/loadcase/combo/setphase/'+str(name)+'/'+str(loadcase)+'/'+str(phase)+'', None, None)
    def setLoadCaseType(self, name, type): return self.nfrest('GET', '/loadcase/settype/'+str(name)+'/'+str(type)+'', None, None)
    def setLoadDurationClass(self, loadcase, durationClass): return self.nfrest('GET', '/load/setduration/'+str(loadcase)+'/'+str(durationClass)+'', None, None)
    def setLoadsToMass(self, loadcase, factor, remove): return self.nfrest('GET', '/mass/load2mass/'+str(loadcase)+'/'+str(factor)+'/'+str(remove)+'', None, None)
    def setMacroelement(self, elemID, macroType): return self.nfrest('POST', '/element/macro/'+str(elemID)+'/'+str(macroType)+'', None, None)
    def setModalAnalysis(self, name, Nmodes, tol): return self.nfrest('GET', '/loadcase/setmodal/'+str(name)+'/'+str(Nmodes)+'/'+str(tol)+'', None, None)
    def setNLDanalysis(self, name, tStep, nSteps, tol, iters, seriesID, Xfactor, Yfactor, Zfactor, RXfactor, RYfactor, RZfactor, seriesFactor, Mdamp, NlGeo): return self.nfrest('GET', '/loadcase/setnldyn/'+str(name)+'/'+str(tStep)+'/'+str(nSteps)+'/'+str(tol)+'/'+str(iters)+'/'+str(seriesID)+'/'+str(Xfactor)+'/'+str(Yfactor)+'/'+str(Zfactor)+'/'+str(RXfactor)+'/'+str(RYfactor)+'/'+str(RZfactor)+'/'+str(seriesFactor)+'/'+str(Mdamp)+'/'+str(NlGeo)+'', None, None)
    def setNLSanalysis(self, name, tStep, nSteps, tol, iters, seriesID, dispControlNode, dispControlDOF, NlGeo): return self.nfrest('GET', '/loadcase/setnlstatic/'+str(name)+'/'+str(tStep)+'/'+str(nSteps)+'/'+str(tol)+'/'+str(iters)+'/'+str(seriesID)+'/'+str(dispControlNode)+'/'+str(dispControlDOF)+'/'+str(NlGeo)+'', None, None)
    def setNodeAsJoint(self, num, status): return self.nfrest('GET', '/node/setjoint/'+str(num)+'/'+str(status)+'', None, None)
    def setNodeCoordinates(self, ID, coords): return self.nfrest('POST', '/node/ID', coords, None)
    def setNodeCS(self, num, x1, y1, z1, x2, y2, z2): return self.nfrest('GET', '/node/cs/'+str(num)+'/'+str(x1)+'/'+str(y1)+'/'+str(z1)+'/'+str(x2)+'/'+str(y2)+'/'+str(z2)+'', None, None)
    def setNodePosition(self, node): return self.nfrest('POST', '/node/ID', node, None)
    def setPDeltaAnalysis(self, name, tol): return self.nfrest('GET', '/loadcase/setpdelta/'+str(name)+'/'+str(tol)+'', None, None)
    def setResponseSpectrumAnalysis(self, direction, loadcase, modesNumber, spectrumFuncID, modalDamping, factor): return self.nfrest('GET', '/loadcase/setrs/'+str(direction)+'/'+str(loadcase)+'/'+str(modesNumber)+'/'+str(spectrumFuncID)+'/'+str(modalDamping)+'/'+str(factor)+'', None, None)
    def setRigidLink(self, n1, n2): return self.nfrest('PUT', '/op/mesh/rigidlink/'+str(n1)+'/'+str(n2)+'', None, None)
    def setRigidOffsets(self, beamID, values, isAbsLength): return self.nfrest('POST', '/element/beamendoffset/'+str(beamID)+'/'+str(isAbsLength)+'', None, dict([("values", values)]))
    def setSectionAngle(self, ID, a): return self.nfrest('GET', '/section/set/angle/'+str(ID)+'/'+str(a)+'', None, None)
    def setSectionColor(self, ID, Red, Green, Blue): return self.nfrest('POST', '/section/set/color/'+str(ID)+'/'+str(Red)+'/'+str(Green)+'/'+str(Blue)+'', None, None)
    def setSectionMaterial(self, ID, materialID): return self.nfrest('GET', '/section/set/material/'+str(ID)+'/'+str(materialID)+'', None, None)
    def setSectionOffset(self, ID, offsetZ, offsetY): return self.nfrest('POST', '/section/set/offset/'+str(ID)+'/'+str(offsetZ)+'/'+str(offsetY)+'', None, None)
    def setSectionProperty(self, ID, name, value): return self.nfrest('POST', '/section/prop/'+str(ID)+'/'+str(name)+'/'+str(value)+'', None, None)
    def setSectionRebarsToElements(self, ID): return self.nfrest('GET', '/section/rebar/toelems/'+str(ID)+'', None, None)
    def setSectionRebarsToElements(self, ID): return self.nfrest('GET', '/section/rebar/toelems/'+str(ID)+'', None, None)
    def setSeismicFloorEccentricity(self, thID, ct, lam): return self.nfrest('GET', '/loadcase/combo/setseismicecc/'+str(thID)+'/'+str(ct)+'/'+str(lam)+'', None, None)
    def setSeismicLoadcaseForCombos(self, direction, loadcase, enableFloorEccentricity5, seismicCombinationType): return self.nfrest('GET', '/loadcase/combo/setseismiclc/'+str(direction)+'/'+str(loadcase)+'/'+str(enableFloorEccentricity5)+'/'+str(seismicCombinationType)+'', None, None)
    def setSelfWeight(self, loadcase): return self.nfrest('GET', '/load/setsw/'+str(loadcase)+'', None, None)
    def setSelfWeightDirection(self, direction): return self.nfrest('GET', '/load/setswdir/'+str(direction)+'', None, None)
    def setShearReinfRCdata(self, ID, data): return self.nfrest('GET', '/section/set/shearreinfrc/'+str(ID)+'', None, dict([("data", data)]))
    def setShellEndRelease(self, ID, node, DOFmask): return self.nfrest('POST', '/element/shellendrelease/'+str(ID)+'/'+str(node)+'', None, dict([("DOFmask", DOFmask)]))
    def setSpringLocalAxes(self, name, x1, y1, z1, x2, y2, z2): return self.nfrest('POST', '/springproperty/axes/'+str(name)+'/'+str(x1)+'/'+str(y1)+'/'+str(z1)+'/'+str(x2)+'/'+str(y2)+'/'+str(z2)+'', None, None)
    def setSRSScombination(self, name, loadcase, factor, type, servType): return self.nfrest('GET', '/loadcase/combo/setsrss/'+str(name)+'/'+str(loadcase)+'/'+str(factor)+'/'+str(type)+'/'+str(servType)+'', None, None)
    def setSteelSection(self, ID, SectionClass, alphaLT, alphay, alphaz, Jw): return self.nfrest('GET', '/section/set/steel/'+str(ID)+'/'+str(SectionClass)+'/'+str(alphaLT)+'/'+str(alphay)+'/'+str(alphaz)+'/'+str(Jw)+'', None, None)
    def setUnits(self, length, force): return self.nfrest('GET', '/units/set/'+str(length)+'/'+str(force)+'', None, None)
    def setWall(self, elems, rotate90, isSlab): return self.nfrest('GET', '/element/walls/set/'+str(rotate90)+'/'+str(isSlab)+'', None, dict([("elems", elems)]))
    def showViewport(self, path, width, height): return self.nfrest('GET', '/op/showvieport/'+str(width)+'/'+str(height)+'', None, None)
    def valueFromFunction(self, Xval, funcID): return self.nfrest('GET', '/function/value/'+str(Xval)+'/'+str(funcID)+'', None, None)
    def valueFromString(self, text, valueName): return self.nfrest('GET', '/op/import/valfromstring/'+str(valueName)+'', None, None)
    def vertexFromNode(self, node): return self.nfrest('GET', '/node/vertex/'+str(node)+'', None, None)
    @property
    def areaColor(self): return self.nfrest('GET','/model/colors/area')
    @areaColor.setter
    def areaColor(self,value): self.nfrest('POST','/model/colors/area', heads={'val':str(value)})
    @property
    def autoMassInX(self): return self.nfrest('GET','/mass/autoX')
    @autoMassInX.setter
    def autoMassInX(self,value): self.nfrest('POST','/mass/autoX', heads={'val':str(value)})
    @property
    def autoMassInY(self): return self.nfrest('GET','/mass/autoY')
    @autoMassInY.setter
    def autoMassInY(self,value): self.nfrest('POST','/mass/autoY', heads={'val':str(value)})
    @property
    def autoMassInZ(self): return self.nfrest('GET','/mass/autoZ')
    @autoMassInZ.setter
    def autoMassInZ(self,value): self.nfrest('POST','/mass/autoZ', heads={'val':str(value)})
    @property
    def backgroundColor(self): return self.nfrest('GET','/model/colors/back')
    @backgroundColor.setter
    def backgroundColor(self,value): self.nfrest('POST','/model/colors/back', heads={'val':str(value)})
    @property
    def baselineGrade(self): return self.nfrest('GET','/op/opt/baseline')
    @baselineGrade.setter
    def baselineGrade(self,value): self.nfrest('POST','/op/opt/baseline', heads={'val':str(value)})
    @property
    def binFolder(self): return self.nfrest('GET','/op/opt/binfolder')
    @binFolder.setter
    def binFolder(self,value): self.nfrest('POST','/op/opt/binfolder', heads={'val':str(value)})
    @property
    def bordersColor(self): return self.nfrest('GET','/model/colors/border')
    @bordersColor.setter
    def bordersColor(self,value): self.nfrest('POST','/model/colors/border', heads={'val':str(value)})
    @property
    def constraintsColor(self): return self.nfrest('GET','/model/colors/constraint')
    @constraintsColor.setter
    def constraintsColor(self,value): self.nfrest('POST','/model/colors/constraint', heads={'val':str(value)})
    @property
    def defSolverType(self): return self.nfrest('GET','/op/opt/defsolvertype')
    @property
    def designMaterialsID(self): return self.nfrest('GET','/designmaterials')
    @property
    def DocXfontSize(self): return self.nfrest('GET','/op/docx/fontsize')
    @DocXfontSize.setter
    def DocXfontSize(self,value): self.nfrest('POST','/op/docx/fontsize', heads={'val':str(value)})
    @property
    def DocXformulaResolution(self): return self.nfrest('GET','/op/docx/formularesol')
    @DocXformulaResolution.setter
    def DocXformulaResolution(self,value): self.nfrest('POST','/op/docx/formularesol', heads={'val':str(value)})
    @property
    def DocXtableAlignment(self): return self.nfrest('GET','/op/docx/tablealign')
    @DocXtableAlignment.setter
    def DocXtableAlignment(self,value): self.nfrest('POST','/op/docx/tablealign', heads={'val':str(value)})
    @property
    def DocXtableFitting(self): return self.nfrest('GET','/op/docx/tablefit')
    @DocXtableFitting.setter
    def DocXtableFitting(self,value): self.nfrest('POST','/op/docx/tablefit', heads={'val':str(value)})
    @property
    def DocXtableFontSize(self): return self.nfrest('GET','/op/docx/tablefontsize')
    @DocXtableFontSize.setter
    def DocXtableFontSize(self,value): self.nfrest('POST','/op/docx/tablefontsize', heads={'val':str(value)})
    @property
    def dontDeleteResults(self): return self.nfrest('GET','/res/donotdelete')
    @dontDeleteResults.setter
    def dontDeleteResults(self,value): self.nfrest('POST','/res/donotdelete', heads={'val':str(value)})
    @property
    def DXFoptions(self): return self.nfrest('GET','/op/opt/dxfoptions')
    @DXFoptions.setter
    def DXFoptions(self,value): self.nfrest('POST','/op/opt/dxfoptions', heads={'val':str(value)})
    @property
    def elemsList(self): return self.nfrest('GET','/elements')
    @property
    def elemsNumber(self): return self.nfrest('GET','/elements/number')
    @property
    def elemTextColor(self): return self.nfrest('GET','/model/colors/elemtext')
    @elemTextColor.setter
    def elemTextColor(self,value): self.nfrest('POST','/model/colors/elemtext', heads={'val':str(value)})
    @property
    def envName(self): return self.nfrest('GET','/model/env')
    @property
    def hingesColor(self): return self.nfrest('GET','/model/colors/hinge')
    @hingesColor.setter
    def hingesColor(self,value): self.nfrest('POST','/model/colors/hinge', heads={'val':str(value)})
    @property
    def IFC_format(self): return self.nfrest('GET','/op/opt/ifcformat')
    @IFC_format.setter
    def IFC_format(self,value): self.nfrest('POST','/op/opt/ifcformat', heads={'val':str(value)})
    @property
    def IFC_includeAnalyticalModel(self): return self.nfrest('GET','/op/opt/ifcanalytical')
    @IFC_includeAnalyticalModel.setter
    def IFC_includeAnalyticalModel(self,value): self.nfrest('POST','/op/opt/ifcanalytical', heads={'val':str(value)})
    @property
    def IFC_WallMeshSize(self): return self.nfrest('GET','/op/opt/ifcwallmeshsize')
    @IFC_WallMeshSize.setter
    def IFC_WallMeshSize(self,value): self.nfrest('POST','/op/opt/ifcwallmeshsize', heads={'val':str(value)})
    @property
    def isRemote(self): return self.nfrest('GET','na')
    @property
    def lineColor(self): return self.nfrest('GET','/model/colors/line')
    @lineColor.setter
    def lineColor(self,value): self.nfrest('POST','/model/colors/line', heads={'val':str(value)})
    @property
    def massColor(self): return self.nfrest('GET','/model/colors/mass')
    @massColor.setter
    def massColor(self,value): self.nfrest('POST','/model/colors/mass', heads={'val':str(value)})
    @property
    def materialsID(self): return self.nfrest('GET','/materials')
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
    def nodeColor(self): return self.nfrest('GET','/model/colors/node')
    @nodeColor.setter
    def nodeColor(self,value): self.nfrest('POST','/model/colors/node', heads={'val':str(value)})
    @property
    def nodesList(self): return self.nfrest('GET','/nodes')
    @property
    def nodesNumber(self): return self.nfrest('GET','/nodes/number')
    @property
    def nodeTextColor(self): return self.nfrest('GET','/model/colors/nodetext')
    @nodeTextColor.setter
    def nodeTextColor(self,value): self.nfrest('POST','/model/colors/nodetext', heads={'val':str(value)})
    @property
    def numberFormat(self): return self.nfrest('GET','/op/opt/numberformat')
    @numberFormat.setter
    def numberFormat(self,value): self.nfrest('POST','/op/opt/numberformat', heads={'val':str(value)})
    @property
    def OS_beamWithHingesOption(self): return self.nfrest('GET','/op/opt/os/beamwithhinges')
    @OS_beamWithHingesOption.setter
    def OS_beamWithHingesOption(self,value): self.nfrest('POST','/op/opt/os/beamwithhinges', heads={'val':str(value)})
    @property
    def OS_concreteTensileStrength(self): return self.nfrest('GET','/op/opt/os/tensilesrc')
    @OS_concreteTensileStrength.setter
    def OS_concreteTensileStrength(self,value): self.nfrest('POST','/op/opt/os/tensilesrc', heads={'val':str(value)})
    @property
    def OS_IntegrationPointsOption(self): return self.nfrest('GET','/op/opt/os/intpoints')
    @OS_IntegrationPointsOption.setter
    def OS_IntegrationPointsOption(self,value): self.nfrest('POST','/op/opt/os/intpoints', heads={'val':str(value)})
    @property
    def OS_NDfiberSectionsOption(self): return self.nfrest('GET','/op/opt/os/ndfibersects')
    @OS_NDfiberSectionsOption.setter
    def OS_NDfiberSectionsOption(self,value): self.nfrest('POST','/op/opt/os/ndfibersects', heads={'val':str(value)})
    @property
    def OS_saveStateVariables(self): return self.nfrest('GET','/op/opt/os/statevars')
    @OS_saveStateVariables.setter
    def OS_saveStateVariables(self,value): self.nfrest('POST','/op/opt/os/statevars', heads={'val':str(value)})
    @property
    def releasesColor(self): return self.nfrest('GET','/model/colors/release')
    @releasesColor.setter
    def releasesColor(self,value): self.nfrest('POST','/model/colors/release', heads={'val':str(value)})
    @property
    def resCalc_cacheEnabled(self): return self.nfrest('GET','/op/opt/rescalc/cacheenabled')
    @resCalc_cacheEnabled.setter
    def resCalc_cacheEnabled(self,value): self.nfrest('POST','/op/opt/rescalc/cacheenabled', heads={'val':str(value)})
    @property
    def resCalc_concreteBehaviour(self): return self.nfrest('GET','/op/opt/rescalc/concbeh')
    @resCalc_concreteBehaviour.setter
    def resCalc_concreteBehaviour(self,value): self.nfrest('POST','/op/opt/rescalc/concbeh', heads={'val':str(value)})
    @property
    def resCalc_domainCorrectionType(self): return self.nfrest('GET','/op/opt/rescalc/domcorr')
    @resCalc_domainCorrectionType.setter
    def resCalc_domainCorrectionType(self,value): self.nfrest('POST','/op/opt/rescalc/domcorr', heads={'val':str(value)})
    @property
    def resCalc_elasticTolerance(self): return self.nfrest('GET','/op/opt/rescalc/eltoll')
    @resCalc_elasticTolerance.setter
    def resCalc_elasticTolerance(self,value): self.nfrest('POST','/op/opt/rescalc/eltoll', heads={'val':str(value)})
    @property
    def resCalc_homogBarsFactor(self): return self.nfrest('GET','/op/opt/rescalc/homog')
    @resCalc_homogBarsFactor.setter
    def resCalc_homogBarsFactor(self,value): self.nfrest('POST','/op/opt/rescalc/homog', heads={'val':str(value)})
    @property
    def resCalc_kMod(self): return self.nfrest('GET','/op/opt/rescalc/kmod')
    @resCalc_kMod.setter
    def resCalc_kMod(self,value): self.nfrest('POST','/op/opt/rescalc/kmod', heads={'val':str(value)})
    @property
    def resCalc_rebarHardeningRatio(self): return self.nfrest('GET','/op/opt/rescalc/rebhard')
    @resCalc_rebarHardeningRatio.setter
    def resCalc_rebarHardeningRatio(self,value): self.nfrest('POST','/op/opt/rescalc/rebhard', heads={'val':str(value)})
    @property
    def resCalc_resDomainSlices(self): return self.nfrest('GET','/op/opt/rescalc/domainslices')
    @resCalc_resDomainSlices.setter
    def resCalc_resDomainSlices(self,value): self.nfrest('POST','/op/opt/rescalc/domainslices', heads={'val':str(value)})
    @property
    def resCalc_responseInTension(self): return self.nfrest('GET','/op/opt/rescalc/tensresp')
    @resCalc_responseInTension.setter
    def resCalc_responseInTension(self,value): self.nfrest('POST','/op/opt/rescalc/tensresp', heads={'val':str(value)})
    @property
    def resCalc_steelClass(self): return self.nfrest('GET','/op/opt/rescalc/steelclass')
    @resCalc_steelClass.setter
    def resCalc_steelClass(self,value): self.nfrest('POST','/op/opt/rescalc/steelclass', heads={'val':str(value)})
    @property
    def resCalc_strandHardeningRatio(self): return self.nfrest('GET','/op/opt/rescalc/strhard')
    @resCalc_strandHardeningRatio.setter
    def resCalc_strandHardeningRatio(self,value): self.nfrest('POST','/op/opt/rescalc/strhard', heads={'val':str(value)})
    @property
    def restraintsColor(self): return self.nfrest('GET','/model/colors/restraint')
    @restraintsColor.setter
    def restraintsColor(self,value): self.nfrest('POST','/model/colors/restraint', heads={'val':str(value)})
    @property
    def saveStateVariables(self): return self.nfrest('GET','/op/opt/os/statevars')
    @saveStateVariables.setter
    def saveStateVariables(self,value): self.nfrest('POST','/op/opt/os/statevars', heads={'val':str(value)})
    @property
    def sectCalcAccuracy(self): return self.nfrest('GET','/op/opt/calcaccuracy')
    @sectCalcAccuracy.setter
    def sectCalcAccuracy(self,value): self.nfrest('POST','/op/opt/calcaccuracy', heads={'val':str(value)})
    @property
    def sectCalcUseFibers(self): return self.nfrest('GET','/op/opt/calcusefibers')
    @sectCalcUseFibers.setter
    def sectCalcUseFibers(self,value): self.nfrest('POST','/op/opt/calcusefibers', heads={'val':str(value)})
    @property
    def sectionsID(self): return self.nfrest('GET','/sections')
    @property
    def selAreaColor(self): return self.nfrest('GET','/model/colors/selarea')
    @selAreaColor.setter
    def selAreaColor(self,value): self.nfrest('POST','/model/colors/selarea', heads={'val':str(value)})
    @property
    def selectedElements(self): return self.nfrest('GET','/op/selectedelements')
    @selectedElements.setter
    def selectedElements(self,value): self.nfrest('POST','/op/selectedelements', heads={'val':str(value)})
    @property
    def selectedNodes(self): return self.nfrest('GET','/op/selectednodes')
    @selectedNodes.setter
    def selectedNodes(self,value): self.nfrest('POST','/op/selectednodes', heads={'val':str(value)})
    @property
    def selLineColor(self): return self.nfrest('GET','/model/colors/selline')
    @selLineColor.setter
    def selLineColor(self,value): self.nfrest('POST','/model/colors/selline', heads={'val':str(value)})
    @property
    def selNodeColor(self): return self.nfrest('GET','/model/colors/selnode')
    @selNodeColor.setter
    def selNodeColor(self,value): self.nfrest('POST','/model/colors/selnode', heads={'val':str(value)})
    @property
    def selSolidColor(self): return self.nfrest('GET','/model/colors/selsolid')
    @selSolidColor.setter
    def selSolidColor(self,value): self.nfrest('POST','/model/colors/selsolid', heads={'val':str(value)})
    @property
    def selSpringColor(self): return self.nfrest('GET','/model/colors/node')
    @selSpringColor.setter
    def selSpringColor(self,value): self.nfrest('POST','/model/colors/node', heads={'val':str(value)})
    @property
    def solidColor(self): return self.nfrest('GET','/model/colors/solid')
    @solidColor.setter
    def solidColor(self,value): self.nfrest('POST','/model/colors/solid', heads={'val':str(value)})
    @property
    def solverType(self): return self.nfrest('GET','/op/opt/solvertype')
    @property
    def springColor(self): return self.nfrest('GET','/model/colors/spring')
    @springColor.setter
    def springColor(self,value): self.nfrest('POST','/model/colors/spring', heads={'val':str(value)})
    @property
    def tempFolder(self): return self.nfrest('GET','/op/opt/tempfolder')
    @tempFolder.setter
    def tempFolder(self,value): self.nfrest('POST','/op/opt/tempfolder', heads={'val':str(value)})
    @property
    def textColor(self): return self.nfrest('GET','/model/colors/text')
    @textColor.setter
    def textColor(self,value): self.nfrest('POST','/model/colors/text', heads={'val':str(value)})
    @property
    def useFastEigensolver(self): return self.nfrest('GET','/op/opt/os/fasteigen')
    @useFastEigensolver.setter
    def useFastEigensolver(self,value): self.nfrest('POST','/op/opt/os/fasteigen', heads={'val':str(value)})
    @property
    def WallMeshSize(self): return self.nfrest('GET','/op/opt/wallmeshsize')
    @WallMeshSize.setter
    def WallMeshSize(self,value): self.nfrest('POST','/op/opt/wallmeshsize', heads={'val':str(value)})

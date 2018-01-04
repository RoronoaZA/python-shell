#coding=utf-8
import xml.etree.ElementTree as ET
import sys

def ChangeElement(root):
    global isroot,isrootval
    dict = root.attrib
    root.attrib = {}
    if root.tag == "Struct":
        root.tag = "DataModel"
        for att in dict:
            if att == 'derive':
                root.set("ref",dict[att])
            elif att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            elif att == 'isRoot':
                isroot = dict[att]
            elif att =='name':
                isrootval = dict[att]
                root.set(att,dict[att])
            else:
                root.set(att,dict[att])
    if root.tag == "String":
        for att in dict:
            if att == 'charCode':
                root.set('type',dict[att])
            elif att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'BitField':
        root.tag = 'Flags'
        for att in dict:
            if att == 'length':
                root.set('size',dict[att])
            elif att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'Bits':
        root.tag = 'Flag'
        for att in dict:
            if att == 'length':
                root.set('size',dict[att])
            elif att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'Block':
        for att in dict:
            if att == 'type':
                root.set('ref',dict[att])
            elif att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'Constraint':
        root.tag = 'Relation'
        for att in dict:
            if att == 'relativeOffset':
                root.set('relativeTo',dict[att])
            elif att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'Blob':
        for att in dict:
            if att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'Int8':
        root.tag = 'Number'
        root.set('size','8')
        for att in dict:
            if att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'Int16':
        root.tag = 'Number'
        root.set('size','16')
        for att in dict:
            if att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'Int32':
        root.tag = 'Number'
        root.set('size','32')
        for att in dict:
            if att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'Int64':
        root.tag = 'Number'
        root.set('size','64')
        for att in dict:
            if att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    if root.tag == 'Enum':
        root.tag = 'Choice'
        for att in dict:
            if att == 'isStatic':
                if dict[att] == 'true':
                    root.set('mutable', 'false')
                else:
                    root.set('mutable', 'true')
            elif att == 'isArray':
                a, b = dict[att].split('-')
                root.set('minOccurs', a)
                root.set('maxOccurs', b)
            else:
                root.set(att,dict[att])
    



def deepfirstfind(root):
    roots = root.getchildren()
    for child in roots:
        deepfirstfind(child)
        ChangeElement(child)
    return

if __name__ == "__main__":
    try:
        pathin = sys.argv[1]
        pathout = sys.argv[2]
        type_ex = sys.argv[3]
    except:
        sys.exit()
    tree = ET.parse(pathin)
    root = tree.getroot()
    deepfirstfind(root)
    root.tag = 'Peach'
    root.set("xmlns","http://peachfuzzer.com/2012/Peach")
    root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:schemaLocation","http://peachfuzzer.com/2012/Peach ../peach.xsd")
    s = ET.SubElement(root,'StateModel')
    st = ET.SubElement(s,'State')
    ac = ET.SubElement(st,'Action')
    dam = ET.SubElement(ac,'DataModel')
    s.set('name','TheState')
    s.set('initialState','Initial')
    st.set('name','Initial')
    ac.set('type','output')
    if(isroot == "true"):
        dam.set('ref',isrootval)
    te = ET.SubElement(root,'Test')
    stm = ET.SubElement(te,'StateModel')
    Pu = ET.SubElement(te,'Publisher')
    Pa = ET.SubElement(Pu,'Param')
    te.set('name','Default')
    stm.set('ref','TheState')
    Pu.set('class','File')
    Pa.set('name','FileName')
    Pa.set('value','fuzzed.'+type_ex)
    tree.write(pathout, encoding="utf-8", xml_declaration=True)

# XML

from xml.etree.ElementTree import Element, dump

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
dump(note)





from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"

dump(note)



dummy = Element("dummy")
note.insert(1, dummy)
note.remove(dummy)





## 애트리뷰트 추가하기
from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
#note = Element("note", date = "20120104")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"
note.attrib["date"] = "20120104"

dump(note)


####################################################################################################
from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
note.attrib["date"] = "20120104"

to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"
dump(note)


#############################################################
from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
note.attrib["date"] = "20120104"

to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"

def indent(elem, level=0):
    i = '\n' + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i+" "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(note)
dump(note)

from xml.etree.ElementTree import ElementTree
ElementTree(note).write("note.xml")


#######################################

from xml.etree.ElementTree import parse
tree = parse("note.xml")
note = tree.getroot()

print(note.get("date"))
print(note.get("foo", "default"))
print(note.keys())
print(note.items())


from_tag = note.find("from")
from_tags = note.findall("from")
from_text = note.findtext("from")
print(from_tag)
print(from_tags)
print(from_text)

childs = note.getiterator()
print(childs)
childs = note.getchildren()
print(childs)

print(note.getiterator("from"))

for parent in tree.getiterator():
    for child in parent:
        pass # work on parent/child tuple

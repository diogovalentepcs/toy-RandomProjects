import os
import unicodedata

def strip_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

def getName(line):
    fileName = ""
    for word in line.split():
        for char in word:
            if char.isupper():
                fileName = fileName + word
    fileName = fileName + ".md"
    fileName = strip_accents(fileName)
    return fileName


network_path="/Users/diogovalentepcs/Projects/ShARE/Tools/"
member_path="/Users/diogovalentepcs/Projects/ShARE/Tools/members"

filelist = [ f for f in os.listdir(member_path) if f.endswith(".md") ]
for f in filelist:
    os.remove(os.path.join(member_path, f))

for filename in os.listdir(network_path):
    if filename.endswith(".txt"): 
        f = open(os.path.join(network_path, filename), "r")
        for line in f:
            if "name" in line:
                f_member = open(os.path.join(member_path, getName(line)), "w+")
                f_member.write("%s\n%s\n" % ("---", "networkID: " + filename[:-4]))
            if len(line.strip()) != 0 :
                f_member.write(line)
            else:
                f_member.write("---")





import os
import sys
import urllib.parse

def writeHeader(f, currDir):
    header = """<!DOCTYPE html>
<html>
<head>
<title>%s</title>
</head>
<body>\n"""
    f.write(header % (currDir))

def writeFooter(f):
    footer = """</body>
</html>\n"""
    f.write(footer)

def writeDirLinks(f, dirs):
    f.write("<p>\n")
    for currDir in dirs:
        f.write("<a href=\"%s/index.html\">%s</a>\n" % (urllib.parse.quote(currDir), currDir))
    f.write("</p>\n")

def writeFileLinks(f, files):
    f.write("<p>\n")
    for file in files:
        f.write("<a href=\"%s\">%s</a>\n" % (urllib.parse.quote(file), file))
    f.write("</p>\n")

def writeIndex(currDir, dirs, files):
    f = open(os.sep.join([currDir, "index.html"]), "w")
    writeHeader(f, currDir)
    writeDirLinks(f, dirs)
    f.write("<p>-------------</p>\n")
    writeFileLinks(f, files)
    writeFooter(f)
    f.close()


if not len(sys.argv) > 1:
    sys.stderr.write("Usage %s <startDir>\n")
    exit(1)

startDir = sys.argv[1]

# Traverse root directory, and list directories as dirs and files as files
# Skip hidden dires / files
for root, dirs, files in os.walk(startDir):
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']
    writeIndex(root, dirs, files)





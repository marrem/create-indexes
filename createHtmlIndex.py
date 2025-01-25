import os
import sys
import urllib.parse

def writeHeader(f, currDir):
    header = """<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8" />
  <title>%s</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta name="description" content="" />
  <link rel="icon" href="favicon.png">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">


</head>

<body>
"""
    f.write(header % (currDir))

def writeFooter(f):
    footer = """
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>

    </body>

</html>\n"""
    f.write(footer)

def writeDirLinks(f, dirs):
    f.write("<p>\n")
    f.write("<ul class=\"list-group\">\n")
    for currDir in dirs:
        f.write("<li class=\"list-group-item\">")
        f.write("<a href=\"%s/index.html\">%s</a>" % (urllib.parse.quote(currDir), currDir))
        f.write("</li>\n")
    f.write("</ul>\n")
    f.write("</p>\n")

def writeFileLinks(f, files):
    f.write("<p>\n")
    f.write("<ul class=\"list-group\">\n")
    for file in files:
        f.write("<li class=\"list-group-item\">")
        f.write("<a href=\"%s\">%s</a>\n" % (urllib.parse.quote(file), file))
        f.write("</li>\n")
    f.write("</ul>\n")
    f.write("</p>\n")

def writeIndex(currDir, dirs, files):
    f = open(os.sep.join([currDir, "index.html"]), "w")
    writeHeader(f, currDir)
    writeDirLinks(f, dirs)
    f.write("<div class=\"vr\"></div>\n")
    writeFileLinks(f, files)
    writeFooter(f)
    f.close()


if not len(sys.argv) > 1:
    sys.stderr.write("Usage %s <startDir>\n" % sys.argv[0])
    exit(1)

startDir = sys.argv[1]

# Traverse root directory, and list directories as dirs and files as files
# Skip hidden dires / files
for root, dirs, files in os.walk(startDir):
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']
    writeIndex(root, dirs, files)





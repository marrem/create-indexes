# create-indexes

Simple python (3) script to create `index.html` files in every directory of a directory hierarchy.
The `index.html` files contain links to the directories and files contained in the directory.

Usage example:

```
$ tree
.
├── README.md
├── createHtmlIndex.py
├── dir met spaties
│   └── bestand met spaties
└── een
    ├── drie
    │   └── vier
    │       └── file2
    ├── file1
    ├── nogwat
    └── twee
        └── file3

7 directories, 6 files


$ python createHtmlIndex.py .


$ tree
.
├── README.md
├── createHtmlIndex.py
├── dir met spaties
│   ├── bestand met spaties
│   └── index.html
├── een
│   ├── drie
│   │   ├── index.html
│   │   └── vier
│   │       ├── file2
│   │       └── index.html
│   ├── file1
│   ├── index.html
│   ├── nogwat
│   │   └── index.html
│   └── twee
│       ├── file3
│       └── index.html
└── index.html

7 directories, 13 files


$ cat index.html
<!DOCTYPE html>
<html>
<head>
<title>.</title>
</head>
<body>
<p>
<a href="dir%20met%20spaties/index.html">dir met spaties</a>
<a href="een/index.html">een</a>
</p>
<p>-------------</p>
<p>
<a href="README.md">README.md</a>
<a href="createHtmlIndex.py">createHtmlIndex.py</a>
</p>
</body>
</html>


$ cat een/index.html
<!DOCTYPE html>
<html>
<head>
<title>./een</title>
</head>
<body>
<p>
<a href="drie/index.html">drie</a>
<a href="nogwat/index.html">nogwat</a>
<a href="twee/index.html">twee</a>
</p>
<p>-------------</p>
<p>
<a href="file1">file1</a>
</p>
</body>
</html>
$


```





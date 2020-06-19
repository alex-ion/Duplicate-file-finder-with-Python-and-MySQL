# Duplicate-file-finder-with-Python-and-MySQL
A project written in Python after I had finnished the MySQL module at BitAcad for finding duplicated files on my SSD drive,
using 10+ million queries. I know it could have had another aproach for this purpose, but I was very curios to embed SQL
in a Python script for my very first project of this type.

The advantage of doing this, is that even if the script fails, the first time it is manually started, it knows at what point it 
should start the checks.

The logic used to consider that 2 files are duplicated is:
- those files (from different folders) have the same name and same size
- those files have the same creation date and same size
- those files have the same modify date and same size

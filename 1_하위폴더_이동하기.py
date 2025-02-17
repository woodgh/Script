#!/usr/bin/python
#-*-coding:utf-8-*-
import os
import shutil

curDir = os.getcwd()
dstDir = 'F:\\temp\\'

for root, _, files in os.walk(curDir):
    for file in files:
        srcFils = os.path.join(root, file)
        dstFile = os.path.join(dstDir, file)

        if srcFils == os.path.abspath(__file__):
            continue

        shutil.move(srcFils, dstFile)

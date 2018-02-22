#!/usr/bin/python3

# slplit clips .py
#	takes input text files including movie path and timestamps to clip with comments to rename the clip + file format output

import csv


import os
from datetime import datetime
from subprocess import call
from pathlib import Path

def splitClip(fin,fout,t0,dt):
    fin = os.path.abspath(fin)
    fout = os.path.abspath(fout)

    cond1 = not(chkfile(fin))
    cond2 = chkfile(fout)

    if cond1:
        print("Input File Not Found : "+fin)
    if cond2:
        print("Output File Found : "+fout)

    if not cond1 and not cond2:
        cmd = 'ffmpeg -i "'+fin+'" -ss '+t0+' -t '+dt+' "'+fout+'"'
        print(cmd)
        os.system(cmd)

def main(inputFile):
    print('****************')
    print('Initializing ...')
    print('Input File : '+inputFile)

    with open(inputFile) as f:
        csvreader = csv.reader(f,delimiter='\t')
        for line in csvreader:
            if len(line)>1:
                if line[0] == 'clip':
                    clip = line[1]
                    #print('Clip : '+clip)
                if line[0] == 'outDir':
                    outDir = line[1]
                    #print('OutDir : '+outDir)
                if line[0] == 'split':
                    t_i = line[1]
                    t_f = line[2]
                    fmt = '%M:%S'
                    #print(t_i+' -> '+t_f)
                    dt = datetime.strptime(t_f,fmt)-datetime.strptime(t_i,fmt)
                    chkdir(outDir)
                    #print(outDir)
                    splitClip(clip,outDir+'/'+line[3],t_i,str(dt))

def chkdir(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise
def chkfile(path):
    try:
        with open(path) as f:
            return(True)
    except:
        return(False)

# main('/home/alaut/Desktop/ac3/utah.dat')
main('/home/alaut/Videos/Highlights/2017.04.01 - Jay Peak.dat')
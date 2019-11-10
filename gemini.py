#!/usr/bin/python3
# *** coding: utf-8 ***
# *** Author: Goldy Thundiyil Joseph ***
# *** Gemini is a program which generates thumbnail from image. ***


from PIL import Image
import os
import sys


def banner():  # Banner for name of the program.
    print('''
                                                              
     _/_/_/                            _/            _/   
  _/          _/_/    _/_/_/  _/_/        _/_/_/          
 _/  _/_/  _/_/_/_/  _/    _/    _/  _/  _/    _/  _/     
_/    _/  _/        _/    _/    _/  _/  _/    _/  _/      
 _/_/_/    _/_/_/  _/    _/    _/  _/  _/    _/  _/       
            Generates thumbnails for image(s).
    ''')


def find_files(infile, f_size, outformat):  # routines to find all files in the directory.
    for (root, _, files) in os.walk(infile):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.tiff') \
                or file.endswith('.tif'):
                infile = os.path.join(root, file)
                (width, height) = Image.open(infile).size
                imageProcessing(f_size, width, height)
                fileSave(infile, outformat)    


def imageProcessing(f_size, width, height):  # condition to calculate the scale ratio.
    global s_size
    if width > height:
        n_height = float(f_size) * float(width / height)
        s_size = (float(f_size), float(n_height))
    elif width == height:
        s_size = (float(f_size), float(f_size))
    else:
        n_width = float(f_size) * float(width / height)
        s_size = (float(n_width), float(f_size))


def fileSave(infile, outformat):  # generation of thumbnail.
    img = Image.open(infile)
    outfile = os.path.splitext(infile)[0] + '_thumbnail' + '.' \
        + outformat
    img.thumbnail(s_size, Image.ANTIALIAS)
    img.save(outfile, outformat)
    print ('size of ' + infile + ' reduced from ' + str(Image.open(infile).size) + ' to ' \
        + str(Image.open(outfile).size))


def main():
    try:
        banner()
        infile = input('Path to the file(s):')
        outformat = input('Desired output format:')
        f_size = int(input('Max size for scaling:'))
        try:
            if os.path.isfile(infile): 
                (width, height) = Image.open(infile).size
                imageProcessing(f_size, width, height)
                fileSave(infile, outformat)
            elif os.path.isdir(infile):
                find_files(infile, f_size, outformat)
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)
    except KeyboardInterrupt:
        print('\n')
        sys.exit(0)

if __name__ == '__main__':  # pragma: nocover
    main()

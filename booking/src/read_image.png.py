#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os

def image_tostring(path):
    # 调用tesseract shell
    binPath=os.path.abspath('..')+('/bin/Tesseract-OCR/')
    # print(binPath)
    command = ('%stesseract.exe %s tmp')%(binPath,path)
    os.system(command)
    file = open('tmp.txt')
    code = file.read().strip()
    file.close()
    os.remove('tmp.txt')
    return code


if __name__ == '__main__':
    print(image_tostring('image.png'))
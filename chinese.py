#coding=utf-8
import sys
import os



def is_chinese_item(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else :
        return False

def is_chinese_word(line):
    for item in line :
        if not is_chinese_item(item) :
            return False
    return True

if __name__ == '__main__' :
    fin = open(sys.argv[1], 'r')
    lines = fin.readlines()
    for line in lines :
        line = line.rstrip()
        line = line.decode('gb18030')
        for item in line :
            if not is_chinese(item) :
                print item.encode('gb18030')
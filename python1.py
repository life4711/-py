#coding=utf-8
import sys
import os
import  chinese
import math
def is_chinese_item(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
def is_chinese_word(line):
    for item in line:
        if not is_chinese_item(item):
            return False
    return True
map_head_freq={}
map_tail_freq={}
map_term_freq={}
map_bigram_begin = {}
map_bigram_freq = {}
map_word_freq = {}
t_head_freq = 0
t_tail_freq = 0
t_term_num = 0

def cal(line):
    global t_head_freq,t_tail_freq
    list = line.split('\t')
    bef = ''
    for i in range(0,len(list)):
        item = list[i]
        item_uni = item.decode('utf-8')
        if is_chinese_word(item_uni) :
            for word_uni in item_uni:
                word = word_uni.encode('utf-8')
                if word not in map_word_freq:
                    map_word_freq[word]=1
                map_word_freq[word] += 1
        else:
            bef = ''
def print_word_prop(file_name):
    fout = open(file_name,'w')
    for item in map_word_freq:
        if len(item.strip())==0:
            continue
        fout.write("%s\t%f\n" %(item,math.log(map_word_freq[item],2)))
    fout.close()

if __name__ == '__main__':
    fin = open('1.txt','r')
    lines = fin.readlines()
    for line in lines:
        line = line.rstrip()
        cal(line)
    print_word_prop('word_prop')
    print 'finished!'
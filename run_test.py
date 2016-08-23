#coding:utf-8
import os
import copy
import sys
from process_pic import *
from chi_code import *

_in_dir = 'F:/tesseract/tu/'
def recognize_word(pic_dir):
    save_dir = 'result'
    pic_name = pic_dir.split('/')[-1].split('.')[0]
    pic_dir = pic_dir.split('.')[0]+'.png'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    cmd = 'tesseract '+pic_dir+' '+save_dir+'/'+pic_name+ ' -l chi_sim'
    print cmd
    os.system(cmd)

def standard_pro(item):
    word = open('result/'+item+'.txt')
    all_words =word.readlines()
    #p_words = copy.deepcopy()
    count = 0
    pro_words = []
    for i in range(0,len(all_words)):
        now_tmp = all_words[i].decode('utf-8')
        chang = len(now_tmp)
        now_tmp = list(now_tmp)
        new_t = []
        last_word = None
        for j in range(0,len(now_tmp)):
            if  is_other(now_tmp[j]) and now_tmp[j]!=u' ':
                pass
            else:
                if now_tmp[j] == u' ':
                    if last_word != u' ':
                        new_t += now_tmp[j]
                else:
                    new_t += now_tmp[j]
            if len(new_t)>0:
                last_word = new_t[len(new_t)-1]
        if len(new_t)>1:
            pro_words.append(new_t)
    word.close()

    for line in pro_words:
        for one in line:
            print one,
        print ' '
    return pro_words

def test():
    #code = sys.getd
    item = 'test7.jpg'
    pic_name = item.split('.')[0]
    img =readimg(_in_dir+item)
    img = face_detect(img)
    #min1,arg = arg_blue(img)
    img = color_filt3(img)

    two_value_pro(img,pic_name)

    recognize_word('tmp/'+item)
    pro_words = standard_pro(item.split('.')[0])
    out = open('result/'+item.split('.')[0]+'.txt','wb')
    for line in pro_words:
        for one in line:
            out.write(one.encode('utf-8'))
        out.write('\n')

test()
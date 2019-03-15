#-*- coding=utf8 -*-
import jieba,os,csv

def add_dict():   
    dic = csv.reader(open("DICT_NOW.csv","r",encoding='utf8'))
    # row: ['肾抗针', 'DRU']
    for row in dic:
        if len(row) ==2:
            #把字典加进去
            jieba.add_word(row[0].strip(),tag=row[1].strip())
            #需要调整词频，确保它的词频足够高，能够被分出来。
            #比如双肾区，如果在jiaba原有的字典中，双肾的频率是400，区的频率是500，而双肾区的频率是100，那么即使加入字典，也会被分成“双肾/区”
            jieba.suggest_freq(row[0].strip(),tune=True)

def word_seg(sentence):
    
    str_list = list(jieba.cut(sentence, cut_all=False, HMM=False))
    result = " ".join(str_list)
    return result
                    
if __name__=="__main__":
    
    add_dict()   
    c_root = os.getcwd()+os.sep+"source_data"+os.sep
    fout = open("cut_dict.txt","w",encoding="utf8")
    
    for file in os.listdir(path=c_root):
        if "txtoriginal.txt" in file:
            fp = open(c_root+file,"r",encoding="utf8")
            str_list=[]
            for line in fp.readlines():
                if line.strip() :                   
                    result = word_seg(line)
                    fout.write(result+'\n')                    
            fp.close()
              
    fout.close()
    
    
    
    
                    
                
        
        
        



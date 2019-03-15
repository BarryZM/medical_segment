#-*- coding=utf8 -*-
import jieba,os

def word_seg(sentence):
    
    str_list = list(jieba.cut(sentence, cut_all=False, HMM=False))
    result = " ".join(str_list)
    return result
                  
if __name__=="__main__":
    
    c_root = os.getcwd()+os.sep+"source_data"+os.sep
    fout = open("cut_direct.txt","w",encoding="utf8")
    
    for file in os.listdir(path=c_root):
        if "txtoriginal.txt" in file:
            fp = open(c_root+file,"r",encoding="utf8")
           
            for line in fp.readlines():
                if line.strip() : 
                    result = word_seg(line)
                    fout.write(result+'\n')     
            fp.close()
    
    fout.close()
    
    
    

                    
                
        
        
        



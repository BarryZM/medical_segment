#-*- coding=utf8 -*-
import jieba,os,csv,re
import jieba.posseg as pseg

def add_dict():
    # 导入自定义字典，这是在检查分词结果后自己创建的字典
    jieba.load_userdict("userdict.txt")
    dict1 = open("userdict.txt","r",encoding='utf8')
    #需要调整自定义词的词频，确保它的词频足够高，能够被分出来。
    #比如双肾区，如果在jiaba原有的字典中，双肾的频率是400，区的频率是500，而双肾区的频率是100，那么即使加入字典，也会被分成“双肾/区”
    [jieba.suggest_freq(line.strip(), tune=True) for line in dict1]
    
    #加载命名实体识别字典
    dic2 = csv.reader(open("DICT_NOW.csv","r",encoding='utf8'))
    for row in dic2:
        if len(row) ==2:
            jieba.add_word(row[0].strip(),tag=row[1].strip())
            jieba.suggest_freq(row[0].strip(),tune=True)
    
    # 用正则表达式匹配到的词，作为字典        
    fout_regex = open('regex_dict.txt','w',encoding='utf8')
    for file in os.listdir(path=c_root):
        if "txtoriginal.txt" in file:
            fp = open(c_root+file,"r",encoding="utf8")          
            for line in fp.readlines():
                if line.strip() :
                    #正则表达式匹配
                    p1 = re.compile(r'\d+[次度]').findall(line)
                    p2 = re.compile(r'([a-zA-Z0-9+]+[\.^]*[A-Za-z0-9%(℃)]+(?![次度]))').findall(line)
                    p_merge = p1+p2
                    for word in p_merge:
                        jieba.add_word(word.strip())
                        jieba.suggest_freq(word.strip(),tune=True)
                        fout_regex.write(word+'\n')
            fp.close()
    fout_regex.close()
    
 # 用停用词表过滤掉停用词
def stop_words():
    # "ChineseStopWords.txt"是非常全的停用词表，然后效果不好。
    #stopwords = [word.strip() for word in open("ChineseStopWords.txt","r",encoding='utf-8').readlines()]
    stopwords = [word.strip() for word in open("stop_words.txt","r",encoding='utf-8').readlines()]
    return stopwords

#进行分词
def word_seg(sentence):
    
    str_list = list(jieba.cut(sentence, cut_all=False, HMM=False))
    str_list = [word.strip() for word in str_list if word not in stopwords]
    result = " ".join(str_list)
    return result
                    
if __name__=="__main__":
    
    stopwords = stop_words()
    c_root = os.getcwd()+os.sep+"source_data"+os.sep
    fout = open("cut_stopwords.txt","w",encoding="utf8")
    add_dict() 
    
    for file in os.listdir(path=c_root):
        if "txtoriginal.txt" in file:
            fp = open(c_root+file,"r",encoding="utf8")
            for line in fp.readlines():
                if line.strip() :
                    result = word_seg(line)
                    fout.write(result+'\n\n')                    
            fp.close()
               
    fout.close()

'''
Description: 
Version: 1.0
Autor: xihuishaw
Date: 2022-01-17 17:16:26
LastEditors: xihuishaw
LastEditTime: 2022-01-17 17:27:27
'''
# %%
from re import T
import numpy as np 
import pandas as pd 
import os
import gc
import matplotlib.pyplot as plt
import jieba
import distance 
import seaborn as sns
from collections import Counter
%matplotlib inline
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号


# %%
data_dir = 'D:/study_hard/statistic/千言数据集'
data_list = ['bq_corpus','lcqmc','paws-x-zh']
# data_dir = 'E:/学习/千言数据集/'

# %%
# 先读一个数据集，后面统一读

train = pd.read_csv(data_dir+'/bq_corpus/train.tsv',sep='\t',error_bad_lines=False,names=['q1','q2','label']).dropna()
test = pd.read_csv(data_dir+'/bq_corpus/test.tsv',sep='\t',error_bad_lines=False,names=['q1','q2']).dropna()
test['label'] = -1 
dev = pd.read_csv(data_dir+'/bq_corpus/dev.tsv',sep='\t',error_bad_lines=False,names=['q1','q2','label']).dropna()

train.head(),train.shape

# %%

## jieba分词 
# cut_all=True，全模式，“我来到北京清华大学”-->“ 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学”
def jieba_cut(sentence):
    word_list = jieba.lcut(sentence,cut_all=True) 
    return word_list 

   
# 分词后，两句子相同词占所有词（去重）的比例
def percent(q1_cut,q2_cut):
    inter_num = len(set(q1_cut) & set(q2_cut))
    percent = inter_num/len(set(q1_cut))
    return percent

## 获取停词 
# https://github.com/goto456/stopwords
def stopwords():
    stop_words =[]
    with open('cn_stopwords.txt','r',encoding='UTF-8') as f:
        for i in f.readlines():
            i = i.replace('\n','')
            stop_words.append(i)
    return stop_words

# 词共享 比例
def word_match_share(row,stops):
    q1words = {}
    q2words = {}
    # 剔除停词
    for word in str(row['q1_cut']):
        if word not in stops:
            q1words[word] = 1
    for word in str(row['q2_cut']):
        if word not in stops:
            q2words[word] = 1
    if len(q1words) == 0 or len(q2words) == 0:
        # The computer-generated chaff includes a few questions that are nothing but stopwords
        return 0
    shared_words_in_q1 = [w for w in q1words.keys() if w in q2words]
    shared_words_in_q2 = [w for w in q2words.keys() if w in q1words]
    R = (len(shared_words_in_q1) + len(shared_words_in_q2))/(len(q1words) + len(q2words))
    return R

# 准备语料
def all_words(train):
    corpus = []
    # 遍历每行，q1分词，q2分词，合并
    for row_id in range(len(train)):
        row = train.iloc[row_id]
        all_words = list()
        all_words.extend([word for word in row['q1_cut'] if word not in stopwords()])
        all_words.extend([word for word in row['q2_cut'] if word not in stopwords()])
        corpus.append(' '.join(all_words))
    return corpus

# 定义权重
# 词个数为1的，权重为0，大于1的，权重为 1/(count+10000)
def get_weight(cnt, eps=10000, min_count=2):
    if cnt < min_count:
        return 0
    else:
        return 1 / (cnt + eps)


def tfidf_word_match_share(row,weight):
    q1words = {word:1 for word in row['q1_cut'] if word not in stopwords()}
    q2words = {word:1 for word in row['q2_cut'] if word not in stopwords()}
    if len(q1words)==0 or len(q2words)==0:
        return 0 
    
    # 获取共享词的权重
    shared_weights = [weight.get(w,0) for w in q1words.keys() if w in q2words] + [weight.get(w,0) for w in q2words.keys() if w in q1words]
    # 总权重
    total_weights = [weight.get(w, 0) for w in q1words] + [weight.get(w, 0) for w in q2words]
    # 共享词权重比例
    R = np.sum(shared_weights) / np.sum(total_weights)
    return R


def handle_feature(train):
    # 字符个数
    train['q1_len'] = train['q1'].apply(len)
    train['q2_len'] = train['q2'].apply(len)  

    train['q1_cut'] = train['q1'].apply(lambda x:jieba_cut(x)) 
    train['q2_cut'] = train['q2'].apply(lambda x:jieba_cut(x)) 
    # 分词后的词个数
    train['q1_cut_len'] = train['q1_cut'].apply(len)
    train['q2_cut_len'] = train['q2_cut'].apply(len)  

    # 编辑距离 
    # Levenshtein Distance 被称为编辑距离（Edit Distance），一个度量两个字符序列之间差异的字符串度量标准
    train['Lev_distance'] = train.apply(lambda x:distance.levenshtein(x['q1'],x['q2']),axis=1)
    train['q1_cut_percent'] = train.apply(lambda x: percent(x['q1_cut'],x['q2_cut']),axis=1)
    train['q2_cut_percent'] = train.apply(lambda x: percent(x['q2_cut'],x['q1_cut']),axis=1)

    train['word_match'] = train.apply(lambda x: word_match_share(x,stopwords()),axis=1)

    corpus = all_words(train)
    corpus = (' '.join(corpus).split())
    word_cnt = Counter(corpus)

    # 生成词权重，词--权重
    weight =  { word:get_weight(cnt) for word ,cnt in word_cnt.items()}
    train['tfidf_word_match'] = train.apply(lambda x:tfidf_word_match_share(x,weight),axis=1)
    return train
                
# %%
# train = handle_feature(train)
# train.head()

stopwords()

# %%


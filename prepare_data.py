#!/usr/bin/python
# -*-coding:utf-8-*-
import json
import random
with open('/Users/ishammohamed/PycharmProjects/untitled1/data/combined_description_after_stemming_dirty.json') as f:
  data = json.load(f)
with open('/Users/ishammohamed/PycharmProjects/untitled1/data/labels.json') as f:
  labels = json.load(f)
dataset_name = 'dirty'
sentences=[]
for item in data:
	sentences.append(' '.join(item))
train_or_test_list=[]
t= ['train', 'test']
for _ in range(int(len(sentences)*.2)):
	train_or_test_list.append('test')
for _ in range(int(len(sentences) * .8)+1):
	train_or_test_list.append('train')
random.shuffle(train_or_test_list)
print (len(train_or_test_list),len(sentences),len(labels))
meta_data_list = []

for i in range(len(sentences)):
	meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels[i]
	meta_data_list.append(meta)

meta_data_str = '\n'.join(meta_data_list)

f = open('data/' + dataset_name + '.txt', 'w')
f.write(meta_data_str)
f.close()


corpus_str = '\n'.join(sentences)

f = open('data/corpus/' + dataset_name + '.txt', 'w')
f.write(corpus_str)
f.close()
import os
import numpy as np
import csv
PATH = 'data'
Train_PATH = os.path.join(PATH,'C1-P1_Train')
Dev_PATH = os.path.join(PATH,'C1-P1_Dev')

with open(os.path.join(PATH,'train.csv'), newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]
del data[0]
New_train = os.path.join(PATH,'train')

os.makedirs(New_train)
os.makedirs(os.path.join(New_train,'A'))
os.makedirs(os.path.join(New_train,'B'))
os.makedirs(os.path.join(New_train,'C'))
for name,ty in data:
    os.rename(os.path.join(Train_PATH,name),os.path.join(os.path.join(New_train,ty),name))

with open(os.path.join(PATH,'dev.csv'), newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]
del data[0]
New_dev = os.path.join(PATH,'dev')

os.makedirs(New_dev)
os.makedirs(os.path.join(New_dev,'A'))
os.makedirs(os.path.join(New_dev,'B'))
os.makedirs(os.path.join(New_dev,'C'))
for name,ty in data:
    os.rename(os.path.join(Dev_PATH,name),os.path.join(os.path.join(New_dev,ty),name))

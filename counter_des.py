import pandas as pd
import os
os.chdir("/Users/ishammohamed/PycharmProjects/untitled1/dataset")
arr = os.listdir()
print(*arr,sep=",")
classes=["Bypass","Exec Code","XSS","CSRF","Dir. Trav.","DoS","File Inclusion","+Info","+Priv","Http R.Spl.",
				 "Mem. Corr.","Overflow","Sql"]
#index of filename in matrix
filename_index_dict={}
i=0
for item in arr:
	filename_index_dict[item]=i
	i+=1
print(filename_index_dict)
#initialize matrix
res=[]
for _ in range(13):
	res.append([0,0,0,0,0,0,0,0,0,0,0,0,0])
data1={}
for item in arr:
	data=pd.read_csv(item,usecols=['description'])
	l=[des.strip().lower() for des in data["description"]]
	data1[item]=l
#print(*res,sep="\n")

def lev_dis(source, target):
    if source == target:
        return 100

    length = len(source) if len(source)>len(target) else len(target)

    # Prepare a matrix
    slen, tlen = len(source), len(target)
    dist = [[0 for i in range(tlen+1)] for x in range(slen+1)]
    for i in range(slen+1):
        dist[i][0] = i
    for j in range(tlen+1):
        dist[0][j] = j

    # Counting distance, here is my function
    for i in range(slen):
        for j in range(tlen):
            cost = 0 if source[i] == target[j] else 1
            dist[i+1][j+1] = min(
                            dist[i][j+1] + 1,   # deletion
                            dist[i+1][j] + 1,   # insertion
                            dist[i][j] + cost   # substitution
                        )
    ret = dist[-1][-1]

    return 100 - int((ret/length)*100)
for item in data1.keys():
	print(item)
	i=0
	l=len(data1[item])
	for des in data1[item]:
		s = des.strip().split()
		#print("searching description",item,i,"/",l)
		i+=1
		for files in data1.keys():
			if files==item:
				continue
			#print("searching file",files)
			lf=len(data1[files])
			j=0
			for tart in data1[files]:
				print("searching description", item, i, "/", l,"in",files,j,"/",lf)
				j+=1
				t=tart.strip().split()
				if lev_dis(s,t)>80:
					r=filename_index_dict[item]
					c=filename_index_dict[files]
					res[r][c]+=1
print(*res,sep='n')
"""
for item in data1.keys():
	print(item)
	i=0
	l=len(data1[item])
	for des in data1[item]:
		print("searching description",item,i,"/",l)
		i+=1
		for files in data1.keys():
			#print("searching file",files)
			if des in data1[files]:
				r=filename_index_dict[item]
				c=filename_index_dict[files]
				res[r][c]+=1
print(*res,sep='n')
"""


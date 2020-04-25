import pandas as pd
import os
os.chdir("/Users/ishammohamed/PycharmProjects/untitled1/dataset")
arr = os.listdir()
print(*arr,sep=",")
l=[]
classes=["Bypass","XSS","CSRF","Mem. Corr.","+Info","Sql","+Priv","Exec Code", "Overflow",
				 "File Inclusion","DoS","Http R.Spl.","Dir. Trav."]
"""
{'bypass.csv': 0, 'cross_site_scripting.csv': 1, 'csrf.csv': 2, 'memory_corruption.csv': 3, 
'gain_information.csv': 4, 'sql_injection.csv': 5, 'gain_privilege.csv': 6, 'code_execution.csv': 7, 
'overflow.csv': 8, 'file_inclusion.csv': 9, 'DOS.csv': 10, 'http_response_splitting.csv': 11, 
'directory_traversal.csv': 12}
"""
#index of classes in matrix
class_index_dict={}
i=0
for item in classes:
	class_index_dict[item]=i
	i+=1
print(class_index_dict)
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
#print(*res,sep="\n")
for item in arr:
	data = pd.read_csv(item,usecols=['vtype'])
	for label in data["vtype"]:
		s = label.strip()
		for cls in classes:
			if s.find(cls) != -1:
				r=filename_index_dict[item]
				c=class_index_dict[cls]
				res[r][c]+=1
print(*res,sep="\n")



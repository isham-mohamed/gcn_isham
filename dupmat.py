import pandas as pd 

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

mat=[]
def findOverlap(data_dic):

	#key index, value class name or label
	#eg 1 : code_execution
	ind_dic = dict(zip(list(data_dic.keys()),[i for i in range(13)]))


	#matrix init
	global mat # = []
	for _ in range(13):
		mat.append([0 for _ in range(13)])

	#return ind_dic

	for s_class_name,s_descriptions in data_dic.items():
		current_row = ind_dic[s_class_name]
		print()
		print("current_row (source) : ",s_class_name)
		print("===============================\n")
		print()
		for s_des in s_descriptions:
			s_des = s_des.strip().split()
			for t_class_name,t_descriptions in data_dic.items():
				current_col = ind_dic[t_class_name]

				if current_col == current_row:
					continue

				print("current_col (target) : ",t_class_name)
				print()
				length_of_target = len(t_descriptions)
				t_count = 0
				for t_des in t_descriptions:
					t_count += 1
					t_des = t_des.strip().split()
					print("target no : ",t_count,"/",length_of_target)
					#print()
					if lev_dis(s_des,t_des) > 90:
						print("im in")
						mat[current_row][current_col] += 1

	return mat


def readCve():
	import os
	os.chdir("/Users/ishammohamed/PycharmProjects/untitled1/dataset")
	loc = os.listdir()
	print(*loc, sep=",")


	names = ['code_execution',
			 'dos',
			 'overflow',
			 'cross_site_scripting',
			 'gain_information',
			 'sql_injection',
			 'bypass',
			 'memory_corruption',
			 'gain_privilege',
			 'directory_traversal',
			 'csrf',
			 'file_inclusion',
			 'http_response_splitting']	

	data=[]
	for ele in loc:
		data.append(pd.read_csv(ele)["description"])

	data_dic = dict(zip(names,data))


	print("reading complete")

	return data_dic

mat = findOverlap(readCve())
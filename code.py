import sys,os,csv ,itertools
from itertools import combinations

path=os.getcwd()
sys.path.append(path)

csv_path= path + r"/full_sorted.csv"

with open(csv_path,newline='') as f:
    reader=csv.reader(f)
    data= list(reader)

for record in data:
    serial_no=record[0]
    enrollment=record[1]
    name=record[2]
    branch=record[3]
    Class=record[4]
    batch=record[5]
    print(serial_no,enrollment,name,branch,Class,batch)
   
        


import csv

with open('HeightWeight.csv' , newline='') as f:
    reader = csv.reader(f)
    new_data = list(reader)

new_data.pop(0)
new_file =[]
# print(new_data)
for i in range(len(new_data)):
    n_num = new_data[i][1]
    new_file.append(float(n_num))

n = len(new_file)
total = 0
for x in new_file:
    total += x
    
mean = total/n
print("Mean Is" + str(mean))
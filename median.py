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
new_file.sort()

if n%2 == 0:
    median1 = float(new_file[n//2])
    median2 = float(new_file[n//2 - 1])
    median = (median1 + median2)

else:
    median=new_file[n//2]

print("Median Is" + str(median))
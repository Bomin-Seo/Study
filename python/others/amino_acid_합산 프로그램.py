import pandas as pd
from csv import reader
from pandas import DataFrame

file = pd.read_csv('파일 저장 위치')

period = []
amount_list = []
quantity_list = []
file_name = "amino_2016_서울.csv"

with open(file_name, "r", encoding='UTF8') as csv_file:
    csv_reader = reader(csv_file)
    for row in csv_reader:
      period.append(row[:])

period = period[0]
period = period[3:]

data = pd.read_csv(file_name, skiprows = 1)
modified = data.drop(['ATC코드', 'ATC코드명', '시도명칭'], axis = 1)
modified = modified.drop(0, axis = 0)

data = modified.iloc[:, 1:modified.shape[1]:2].values

for i in range(len(data)):
     for j in range(len(data[0])):
        data[i][j] = int(data[i][j].replace(',',''))

for i in range(len(data)):
    quantity = 0
    for j in range(len(data[0])):
        quantity += data[i][j]

    quantity_list.append(quantity)


data = modified.iloc[:, 2:modified.shape[1]:2].values

for i in range(len(data)):
    for j in range(len(data[0])):
       data[i][j] = int(data[i][j].replace(',', ''))

for i in range(len(data)):
    amount = 0
    for j in range(len(data[0])):
      amount += data[i][j]
    amount_list.append(amount)

period = period[1][:5]

ans = {'시군구명칭' : modified['시군구명칭'].values, period + ' 총 수량' : quantity_list, period + ' 총 금액' : amount_list}
ans = DataFrame(ans)

file_name = file_name[:-4]
ans.to_csv(file_name + '_통계.csv', encoding='utf-8-sig')
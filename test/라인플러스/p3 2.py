table1 = {'header':[], 'data':[]}
row1 = int(input())
table1['header'] = input().split()
for _ in range(row1-1):
    table1['data'].append(input().split())
table1['data'] = sorted(table1['data'], key = lambda x: x[0])

row2 = int(input())
for col in input().split(): 
    if col != 'id':
        table1['header'].append(col)
for _ in range(row2-1):
    new = input().split()
    new_id =int(new[0])
    if len(table1['data']) >= new_id:
        table1['data'][new_id-1].extend(new[1:])
        

print(" ".join(table1['header']))
col_num = len(table1['header'])
for datum in table1['data']:
    if len(datum) < col_num:
        for _ in range(col_num - len(datum)):
            datum.append('NULL')
    print(" ".join(datum))

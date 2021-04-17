from conf.database import execute_sql, get_data, get_uuid


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
 
def get_list():
    sql_data = 'SELECT id, stock_code FROM t_jj_corp_info'
    array = get_data(sql_data)
    return array

 
if __name__ == '__main__':
 
    rows = get_list()
    array = []
    for row in rows:
        array.append(row[1])
    n = 20
 
    chunks = list(partition(array, n))

    for chunk in chunks:
        print(','.join(chunk))

    # print(chunks)

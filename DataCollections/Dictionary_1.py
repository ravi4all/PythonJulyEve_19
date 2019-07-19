'''
emp = {
    "names":["raman","suman","naman","kapil","kamal"],
    "dept":["IT","IT","HR","SALES","MARKETING"],
    "sal":[25000,34000,32000,40000,28000]
}

for i in range(len(emp["names"])):
    if emp["sal"][i] > 30000:
        print(emp["names"][i], emp["dept"][i], emp["sal"][i])
'''

products = [
    {"p_id":101,"p_name":"Apple Iphone XS","p_price":90000},
    {"p_id":102,"p_name":"Apple Iphone XS Max","p_price":120000},
    {"p_id":103,"p_name":"Samsung Galaxy S5","p_price":76000},
    {"p_id":104,"p_name":"Redmi Note 6","p_price":17000},
    {"p_id":105,"p_name":"Redmi Note 7","p_price":22000},
    ]
for i in range(len(products)):
    if products[i]["p_price"] < 25000:
        print(products[i])

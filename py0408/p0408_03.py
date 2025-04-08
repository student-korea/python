a = [10,5,2,4,7]
print(min(a))
print(max(a))
print(sum(a))
a.sort(reverse=True)
print(a)

a_dict=[
    {"no":1,"name":"Eric"},
    {"no":2,"name":"Hina"},
    {"no":3,"name":"Rei"},
    {"no":4,"name":"Debi"},
    {"no":5,"name":"Alice"}
]
print(max(a_dict,key=lambda x:x['no']))
print(max(a_dict,key=lambda x:x['name']))

a_dict.sort(key=lambda x:x['no'])
a_dict.sort(key=lambda x:x['no'],reverse=True)
print(a_dict)
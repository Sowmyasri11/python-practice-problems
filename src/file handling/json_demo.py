import json

emp={'emp_id':101, 'emp_name':'sowmi','salary':50000}

print(emp)

print(type(emp))
json_emp=json.dumps(emp)
print(json_emp)
print(type(json_emp))

emp_dict=json.loads(json_emp)
print(emp_dict)
print(type(emp_dict))


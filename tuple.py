input = {"name": ["Jan", "Feb", "March" ], "month": [1, 2, 3]}
# output ={1: "Jan", 2: "Feb", 3: "March"}
a = input.get('month')
b = input.get('name')
print(b)

d= {k:v for k in input.get('month') for v in input.get('name')}
print(d)

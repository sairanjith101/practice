names = { 3 : 'Apple', 5 : 'Water Melon', 10 : 'Orange', 2 : 'Fig' }

result = []

for key,value in names.items():
    slice_name = value[:key] + value[key+1:]
    print(slice_name)
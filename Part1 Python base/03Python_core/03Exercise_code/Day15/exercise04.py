tuple01 = (21, 65, 78, 24)
iterator01 = tuple01.__iter__()

while True:
    try:
        item = iterator01.__next__()
        print(item)
    except StopIteration:
        break

dict01 = {"name": "wang", "age": 24}

iterator02 = dict01.__iter__()

while True:
    try:
        key = iterator02.__next__()
        print(key, dict01[key])
    except StopIteration:
        break

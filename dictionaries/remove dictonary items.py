thisdict = {"brand": "ford", "model": " mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)

thisdict = {"brand": "ford", "model": " mustang", "year": 1964}
thisdict.popitem()
print(thisdict)

thisdict = {"brand": "ford", "model": " mustang", "year": 1964}
del thisdict["model"]
print(thisdict)

thisdict = {"brand": "ford", "model": " mustang", "year": 1964}
thisdict.clear()
print(thisdict)
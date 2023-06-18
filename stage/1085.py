x, y, w, h = map(int, input().split())

lists = []
lists.append(x)
lists.append(y)
lists.append(h-y)
lists.append(w-x)
print(min(lists))

import sys
from ast import literal_eval
input = sys.stdin.readline
merchantNames = literal_eval(input())
mer_len = [len(x) for x in merchantNames]
mer_idx = mer_len.index(max(mer_len))
merchant = [x for x in merchantNames if merchantNames[mer_idx][:4] in x]
full_names = [merchantNames[mer_idx]]
for mer in merchant:
    if len(mer)>len(full_names[0]):
        full_names[0] = mer
    elif len(mer)==len(full_names[0]):
        full_names.append(mer)

special =  ['&','(',')','.',',','-']
if any(str in full_names for str in special):
    full


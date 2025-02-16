import requests

filename = "proxy.txt"

response = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt")
content = response.text
with open(filename, 'w') as f:
  f.write(content)


a = open("proxy.txt").read().splitlines()

def splitList(lst,lgh):
    return [lst[y*lgh:lgh*(y+1)] for y in range(-(len(lst)//-lgh))]
lis = splitList(a,len(a)//2)

with open("p2", "w") as txt_file:
    for line in lis[0]:
        txt_file.write("".join(line) + "\n")
with open("p1", "w") as txt_file:
    for line in lis[1]:
        txt_file.write("".join(line) + "\n")
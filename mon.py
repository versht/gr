import requests,sys

response = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt")

def buat(nbr,lis):
   fil = f"p{nbr}"
   list = lis[int(nbr)]
   with open(fil, "w") as txt_file:
      print(fil,len(list))
      for line in list:
        txt_file.write("".join(line) + "\n")
a = response.text.splitlines()

def splitList(lst,lgh):
    return [lst[y*lgh:lgh*(y+1)] for y in range(-(len(lst)//-lgh))]
k = 10
lis = splitList(a,len(a)//k)
for i in range(0,k):
   buat(i,lis)

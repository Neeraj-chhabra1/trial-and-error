myfile= open("running-config.cfg")


def process_line(word):
 str=word.split()
 lst=str[2:]
 mytpl = tuple(lst)
 return(mytpl)

def check(line):
 if "no ip address" in line:
  return
 elif "ip address" in line:  
  return(process_line(line))
 else:
  return

myfinlist=[]
for line in myfile:
 mytpl3=check(line)
 if mytpl3 != None:
  myfinlist.append(mytpl3)
print(myfinlist)


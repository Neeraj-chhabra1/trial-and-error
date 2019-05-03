myfile=open("running-config.cfg")
myfile2=open("inf.confg", "w+")
def Intf_name(word):
  str=word.split()
  lst=str[1]
  with open('inf.confg', 'a') as fil:
   fil.write(lst)
   fil.write("\n")
  
def process_line(word):
 if "interface" in word:
   Intf_name(word)

for line in myfile:
 process_line(line)

import os 
os.system("grep \"interface\" running-config.cfg | awk \'{print $2}\' ")


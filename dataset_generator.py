import re 
file1 = open('/var/log/httpd/access_log.txt', 'r') 
count = 0

p = re.compile(r'^\d+.\d+.\d+.\d+') 
z = re.compile(r"\[([A-Za-z0-9+\-\:\/ ]+)\]") 
u = re.compile(r"\"([A-Za-z0-9+\:\/.:_; ]+)\"") 
ip = []


for line in file1: 
    count += 1
    c = p.findall(line)
    da = z.findall(line)
    ur = u.findall(line)
    if len(c) == 0 :
        pass
    else:
        c.append(da[0])
        c.append(ur[0])
        ip.append(c)
        print(c)
        
file1.close() 

import pandas as pd    

df = pd.DataFrame(ip, columns=['IP', 'DATE', 'o'])
csv_data = df.to_csv(index=False)
df.to_csv('/root/task5/ip_set.csv', index=False)
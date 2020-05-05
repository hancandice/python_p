
import os

for roots,dirs,files in os.walk("/Users"):
    for file in files:
        extension = os.path.splitext(file)[1]
        if extension == '.py':
            print("%s/%s" %(roots,file))




        


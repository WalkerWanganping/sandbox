# sandbox
#Name: 1919_laffy

#渔湖特产烧仙草，男人喝了更女人，女人喝了更男人，，，
import os  
  
print("The files and folders in {} are:".format(os.getcwd()))  
items = os.listdir('.')  
for item in items:  
    print(item)

#initialize flask envirionemnt
import os
# create requirements file to install
# insert the minimal dependencies to install there
os.system("touch requirements.txt")
with open('requirements.txt','w') as file:
    file.write("Flask")
    pass
os.system("python3 -module venv env")
os.system("source env/bin/activate") #activate env
os.system("pip install -r requirements.txt") # install dependencies
os.mkdir("./app") # create app folder
os.mkdir("./migrations") # create migraion dir
os.mkdir("./static") # create availbility for statics
os.mkdir("./templates") # templated to be used
os.mkdir("./shared")

# this code needs and improvments
"""
for example when executing one task another should wait to execute next 
when creating file requiremnt file , it should add more than one depency dynamically
when creating  static, temlates, shared it should initialize the __init__.py file in order
to marker as module , 
and then it should write the python flask initial code 

another great improvements , which of the following do you wanna go with 
Flask for webdevelopment 
Flask for APIRest 

if so create the appropriate folder structure 
"""
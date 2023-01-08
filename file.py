import os
import shutil
fff=open('new_hm.txt','w+')
fff.write('hello Hamoud,how are you')
fff.close
current=os.getcwd() # it's display  the current work directory
print(current)
all=os.listdir() #it will display all the files and directories  in the current directory
print(all)
private_path=os.listdir('D:')
print(private_path)

for folder,subfolder,files  in os.walk(os.getcwd()):
    print(f"\t currently looking in {folder}")
    print('\n')
    for sub_Fol in subfolder:
        print(f" \t subfolder in {sub_Fol}")
        print('\n')
    for file in files:
        print(f" \t file in {file}")

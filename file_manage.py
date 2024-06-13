import os,sys
from gui_file import filemanger

FILE_PATH=input("Enter the file name: ")

def load_file(filepath):
    return os.listdir(filepath)


def file_extensions(files):
    ext=set()
    for i in files:
        splitted_file=i.rsplit(".",1)

        # if len(splitted_file)>=2:
        #     key=splitted_file[-1]

        ext.add(splitted_file[-1])
        
    return ext


def create_folder(key):
    paths={}
    for k in key:
        folder_path=f"{FILE_PATH}\\{k}"
        paths[k]=folder_path


        try:
            os.mkdir(folder_path)
        except:
            pass 
    return paths


def mange_duplicates(folder_path,file_not_created):
    count=0
    file_n,file_e=file_not_created.rsplit(".",1)
    # for
    # print(file_n,file_e)
    files_in_folder=os.listdir(folder_path)
    for i in files_in_folder:
        file_present=i.rsplit(".",1)[0].rsplit("#",1)[0]
        
        
        
        if file_n==file_present:
            count+=1
    


    new_file_folder=f'{folder_path}\\{file_n}#{count}.{file_e}'

    return new_file_folder



def move_file(file,file_paths):
    
    for i in file:
        splitted_file=i.rsplit(".",1)
        

        if len(splitted_file)>=2:
            ext=splitted_file[-1]

            folder_path=file_paths[ext]

            old_path=f"{FILE_PATH}\\{i}"
            new_path=f'{folder_path}\\{i}'

            #now i will try to rename the path so it will directly move the file but if it doesnt work meaning the file is already thier
            try:
                os.rename(old_path,new_path)
                
            except:
                new_path=mange_duplicates(folder_path,i)
                os.rename(old_path,new_path)
                
            
            

#==============================================================
fm=filemanger()
print(fm.path)
file=load_file(fm.path)

extension_files=file_extensions(file)
folder_paths=create_folder(list(extension_files))
move_file(file,folder_paths)

print(f"All Your Files Have Been Sorted in the given path {FILE_PATH} Happy Coding")

# print(os.listdir(r"D:\learnpython\custom_tkinter"))



"""
1. first i have created a function that will load only the files from the given directory as input
2. second i have taken the extension of all the files to get what type of extension are present so that i can create a folder based on that name
3. then i have created a folder using os.makedir and to create a folder with the name of that extension and store it in the dictonary so that i can take a file 
and then take its extension and get the folder it has to be sent eg{"pdf":D:\\resource\\pdf}
4.  then i have moved the files from their old path to new path i could have done it with shutil.move but i used os.rename which works just fine 
5. then i have added a feature that will mcanage duplicates file if it has same name so we dont have to rename the file again and again
"""






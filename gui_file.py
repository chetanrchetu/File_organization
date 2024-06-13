import customtkinter as ctk 
import tkinter as tk
import os

class filemanger(ctk.CTk):
    def __init__(self,):
        #get all the init value of the parent class in this case the ctk.CTk
        super().__init__()
        self.geometry('500x500')
        self.title('FileManger')
        self.minsize(500,500)
        self.maxsize(500,500)
        
        self.mainframe=ctk.CTkFrame(master=self,fg_color='#D2B4DE')
        self.mainframe.pack(expand=True,fill='both')

        self.font=ctk.CTkFont(family='fantasy',size=50,underline=True)
        ctk.CTkLabel(self.mainframe,font=self.font,text='File Manger',text_color='black').place(relx=0.25,rely=0.0,)

        self.stringvalue=tk.StringVar()
        self.entry=ctk.CTkEntry(master=self.mainframe,textvariable=self.stringvalue,fg_color='#566573')
        self.entry.place(relx=0.2,rely=0.2,relwidth=0.5,relheight=0.07)

        self.button=ctk.CTkButton(master=self.mainframe,text='Sort',fg_color='#566573',command=self.send_path)
        self.button.place(relx=0.7,rely=0.2,relheight=0.07)
        self.bind('<Return>',lambda e:self.send_path())
        self.mainloop()
        

    def send_path(self,):
        self.path=str(self.stringvalue.get())
        self.stringvalue.set("")

        #now we will perform the rest of the sorting inside function in side a function
        self.FILE_PATH=self.path
        self.sorting_function(self.path)


    
    


    def load_file(self,filepath):
        return os.listdir(filepath)
    
    def file_extensions(self,files):
        ext=set()
        for i in files:
            splitted_file=i.rsplit(".",1)

            # if len(splitted_file)>=2:
            #     key=splitted_file[-1]

            ext.add(splitted_file[-1])
            
        return ext
    
    def create_folder(self,key):
        paths={}
        for k in key:
            folder_path=f"{self.FILE_PATH}\\{k}"
            paths[k]=folder_path


            try:
                os.mkdir(folder_path)
            except:
                pass 
        return paths
    
    def mange_duplicates(self,folder_path,file_not_created):
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
    
    def move_file(self,file,file_paths):
        
        for i in file:
            splitted_file=i.rsplit(".",1)
            

            if len(splitted_file)>=2:
                ext=splitted_file[-1]

                folder_path=file_paths[ext]

                old_path=f"{self.FILE_PATH}\\{i}"
                new_path=f'{folder_path}\\{i}'

                #now i will try to rename the path so it will directly move the file but if it doesnt work meaning the file is already thier
                try:
                    os.rename(old_path,new_path)
                    
                except:
                    new_path=self.mange_duplicates(folder_path,i)
                    os.rename(old_path,new_path)

    def sorting_function(self,path):
        file=self.load_file(path)
        extension_files=self.file_extensions(file)
        folder_paths=self.create_folder(list(extension_files))
        self.move_file(file,folder_paths)
    
        self.progress=ctk.CTkProgressBar(master=self.mainframe,orientation='horizontal',mode='indeterminate',indeterminate_speed=3,
                                         fg_color='grey',progress_color='black',corner_radius=3,)
        self.progress.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)
        self.start()

        

    def start(self,):
        self.progress.start()
        self.progress.after(10000,self.stop)

    def stop(self,):
        self.progress.stop()
        self.progress.place_forget()
        font=ctk.CTkFont(family='fantasy',size=25,underline=True)
        ctk.CTkLabel(self.mainframe,text="All Your Files Have Been Sorted",font=font,text_color='black').place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)

        
    
        


                
            
filemanger()
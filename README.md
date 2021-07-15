# shutdown-virus [ Trojan ]
This is a shutdown virus which only works on windows.

First we need to understand how this virus works. 
startup folder is nothing but everytime you turn on your computer the files in that folder will be executed  by the os automatically.
# what if we plant a shutdown virus in startup folder !!??

In startup_virus.py we are creating a .bat file in startup folder and writing a batch command to shutdown the computer.
Batch file is a simple file containing system commands that are executed by system.batch files have .bat extension. They only work on windows os.

Requried packages :\
                        win32api -> pip install pywin32\
                        cx_freeze -> pip install cx-Freeze

After creating the file and writing the command to it using python  do not run the python code.

In setup.py file we are converting the startup_virus.py to an exe file.but why are we doing this ? 
In order to run this python code where python is not installed, exe file comes into the picture.

Make sure both the python files are in same directory or the file locations are properly configured if not in same location.

![alt text](https://github.com/Himmalay-Devulapalli/shutdown-virus/blob/main/output/dir.png)

open terminal where setup.py file is located and run the following command
                   python setup.py build
                   
After the process successfully ends,you can see a new folder named build is created in the same directory.Explore the sub-directory and you can find the exe file or our 
python code.If you run the exe file it is just same as running the shutdown_virus.py file.

![alt text](https://github.com/Himmalay-Devulapalli/shutdown-virus/blob/main/output/virus_file.png)

Run the exe file and open startup folder by using win+r and type shell:startup.

In the startup folder you can see the .bat file that will  shutdown the computer.

As we planted the file in startup folder, everytime the computer starts, files in startup folder will be executed and computer will shutdown when the .bat file is executed.

# Removing the virus 
In case you need to remove the virus from computer start your computer in safe mode where the files in startup folder will not be executed.
Remove the  .bat file from startup folder.

If you are using a good anti-virus it will automatically detect the virus and delets the exe file 

![alt text](https://github.com/Himmalay-Devulapalli/shutdown-virus/blob/main/output/antivirus.png)

As soon as i run the exe file antivirus deleted the exe file with this warning.

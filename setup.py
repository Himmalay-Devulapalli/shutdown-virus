from cx_Freeze import setup,Executable
setup(name ="startup",
           version ="0.1",
           description = " ",
           executables=[Executable("startup_virus.py")])



#navigate to dir of the location containing this file and py source file and run the command ->'python setup.py build'
#both setup.py and py source files should be in one folder 
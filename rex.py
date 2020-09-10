import pyttsx3
import os
while True:
  print("MAKE A WISH ARCCORDING TO YOU :",end='')
  p=input()

  if((("Run" in p) or ("Execute" in p)) and (("Chrome" in p) or ("Microsoft Edge" in p)) or ("1" in p)):        #code to run Downloaded SOFTWERE
    os.system("Chrome")

  elif((("Run" in p) or ("Execute" in p)) and (("notepad" in p) or ("word editor" in p)) or ("2" in p)):
    os.system("notepad")  

  elif((("Run" in p) or ("Execute" in p)) and (("Wordpad" in p) or ("word modifier" in p)) or ("3" in p)):        #code which run Inbuild program
    os.system("wordpad") 

  elif((("Run" in p) or ("Open" in p)) and (("C language" in p) or ("C compiler" in p))or ("4" in p)):
   os.system("C:\YOGISOFT\Turboc8.exe")
    
  elif((("Run" in p) or ("Open" in p)) and (("Teamviewer" in p) or ("teamviewer" in p)) or ("5" in p)):
   os.system("TeamViewer")

  elif((("Run" in p) or ("Open" in p)) and (("youtube" in p) or ("online videos" in p)) or ("6" in p)):               #code to run The shortcut Link
   os.system("start youtube")
   
  elif((("Run" in p) or ("Open" in p)) and (("music" in p) or ("song" in p)) or ("7" in p)):                          # music
   os.system("start music")

  elif((("Run" in p) or ("Execute" in p)) and (("Libre office" in p) or ("libre" in p )) or ("8" in p)):
   os.system("start LibreOffice") 
  else:
    print("Don't Support") 

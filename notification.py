import platform 
import os

def showNotification(title, message):
   plt = platform.system()
   if plt=="Windows":
      from win11toast import toast
      toast("{title}", "{message}", duration="long", buttons=["reminder"])
   elif plt == "Linux":
      print("Linux")
      command = f'notify-send "{title}" "{message}" -t 10'
      os.system(command)
   elif plt =="Darwin":
      command = f'''osascript -e '"{message}" "{title}"'; '''
      os.system(command)

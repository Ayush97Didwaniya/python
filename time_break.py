import time
import webbrowser
total_break=3
break_count=0
print("this program start on"+time.ctime())
while(break_count<total_break):
   time.sleep(10)
   webbrowser.open("https://www.youtube.com/watch?v=FM7MFYoylVs&list=RDQMaezvECclAdM&index=1");
   break_count=break_count + 1


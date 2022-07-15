import os
import subprocess

# change the current directory 
# to specified directory 
os.current_dir(r"D:\Bear Bot") 
p = subprocess.Popen(os.path.join(current_dir,"Bearbot.exe"),cwd=current_dir)
# ...
return_code = p.wait()
import subprocess #สำหรับ run terminal command

if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["ls","-ltr"]) # เขียนเป็น list
    subprocess.run(["rm","-r","/home/nattntn/testfolder1"])
    

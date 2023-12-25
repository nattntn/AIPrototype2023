import subprocess #สำหรับ run terminal command

if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["python","firstpy.py", "--num", "100","--xx", "90"])
    subprocess.run([print(f'first run num = {input_v.num} xx={input_v.xx} ')])
    subprocess.run([print("--"*80)])
    subprocess.run(["python","firstpy.py", "--num", "-10","--xx", "-90"])
    subprocess.run(["python","firstpy.py", "--num", "0"])
    

import subprocess #สำหรับ run terminal command # นำที่มี Output/~output มาแสดง

if __name__ == "__main__":
    #basic terminal command
    #subprocess.run(["ls", "-ltr"]) # เขียนเป็น list ช่องว่าง ใช้  ,
    #subprocess.run(["rm","-r","~/testfolder1"])#ลบ testfolder1
    print('first run num = 100 xx= 90')
    subprocess.run(["python","firstpy.py", "--num", "100","--xx", "90"])
    print("-"*80)
    print('second run num = -10 xx= -90')
    subprocess.run(["python","firstpy.py", "--num", "-10","--xx", "-90"])
    print("-"*80)
    print('third run num = 0')
    subprocess.run(["python","firstpy.py", "--num", "0"])
    print("-"*80)

    #use output from other program
    process_output = subprocess.Popen(["python","firstpy.py", "--num", "0"],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
    out, err = process_output.communicate()
    print(out.decode('utf-8')) # เรียกดู output
    print(len(out.decode('utf-8'))) # นับจำนวนพยางค์ชนะ Output


    ##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello world!)
    


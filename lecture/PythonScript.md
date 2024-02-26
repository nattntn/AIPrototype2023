# อธิบายว่าวันที่ 12/12/66 จะเรียนอะไร

> ปกติเวลาเขียน code จะมีทั้งแบบ **.ipynb** กับ **.py**  
> วันนี้จะมาเรียนเขียน Python Scrip (.py) ที่run บน command line  
> และ step  ในการเขียน code ก่อนไป run บน server จริง ๆ

# Step ในการ code file.py

1. เปิด terminal ในเครื่องเรา  ``` $ cd outside/Ubuntu/AIPrototype2023```
2. ```$ git pull```  ดึงไฟล์ล่าสุดจาก internet ลงมา **ต้องทำก่อน code ทุกครั้ง**
3. ssh เข้า VM
4. มาอยู่ที่หน้า  terminal ที่อยู่เครื่องเรา
5. สร้างไฟล์ . py ในเครื่องเรา

    ```
   $ code firstpy.py
   # ถ้ายังไม่มี file คำสั่ง code จะสร้าง file  ใหม่
   # ถ้ามี file แล้ว คำสั่ง code จะไปดึง file name นี้มาแก้ไข
   ```
   พิมพ์  ``` print("First py")``` แล้ว save in VS code
   
7. ออกมา ```$ ls``` ดูfile ใน terminal
8. up ขึ้น GitHub
 
   ```
   $ git status
   $ git add {file name}
   $ git commit -m "comment"
   $ git push
   ```
   
9. เข้า ไปที่ VM แล้วดูว่าเรามี env  อะไรที่สร้างไว้เเล้ว
 
   ```
   (base)  : $ conda env list
   ```
   
10. activate env

     ```
    $ conda activate deeptooth38
    ````
     
12. run firstpy.py

     ```
    (deeptooth38)  :$ python firstpy.py
    ```
    output
    > First py

# [Python Main Function](https://www.geeksforgeeks.org/python-main-function/)
> Main Function ใช้ควบคุม flow ของ program โดยลำดับการทำงานจะทำตาม Main fc
> ดังนั้น จึง**จำเป็น**ต้องมี Main fc เพื่อที่เวลาเริ่ม program มา จะได้รู้ว่าต้อง run อะไรก่อน โดยดูจาก main fc (ถ้าไม่มีอะไรต้อง run ก่อน)

 ```javascript
// Python program to demonstrate 
// main() function 


print("Hello") 

// Defining main function 
def main(): 
	print("hey there")  // have only process


// Using the special variable 
// __name__ 
if __name__=="__main__": 
	main()
```
Output  
> Hello  
> hey there


# รับ input จากภายนอก  
[Argparse](https://docs.python.org/3/library/argparse.html)
> code ที่ดี ถ้าเสร็จแล้วไม่ควรมาแก้ซ้ำๆ ถ้าจะแก้แค่ input เฉยๆ 
``` javascript
import argparse  

def parse_input(): // จำแนก input 
    parser = argparse.ArgumentParser() // เรียก Parser มาใช้

// กำหนด argument ของ input กี่ตัวก็ได้แล้วแต่เรา

    parser.add_argument( // กำหนด argument โดย input ตัวแรกจะใส่คำว่า "--num" เพื่อให้เอาตัวเลขไปใช้ใน code ของเราได้
        '--num',
        type=int,
        required=True, // ถ้าไม่ใส่argument นี้ code จะ error
        help= 'input for the multiplyby9 function' // เพื่อเอาไว้ดูว่า argument นี้เราเอาไว้เติมอะไร    
    )
    parser.add_argument( //ใส่  input เข้าไปอีกตัว
        '--xx',
        type=int,
        default=7,
        help= 'input for xx'     
    )
    args = parser.parse_args()
    return args // return ค่าที่เก็บมา

def printHello():
    print("Hello world!") // have only process

def multiplyby9(inputV):
    print(9*inputV) // have input and process

if __name__ == "__main__":
    input_v = parse_input() // ดึง input ที่ใส่เข้ามาก่อน
    print(f'the input XX is {input_v.xx}')//.xx เอา ตห.ที่ xx  มาแสดงผล
    print('we are in the main function')
    multiplyby9(input_v.num)
    printHello()
```

``--`` input หลายตัว   
``-`` input ตัวเดียว
## ตอนใช้งาน
```$ python firstpy.py --num {numberที่ต้องการ}```  
```$ python firstpy.py --help```
output 
> the input XX is {xx}  
> we are in the main function
> 9*inputV (ตัวเลขที่คูณแล้ว)  
> Hello world!

# ใช้_Python_สั่งงาน_Program_อื่น_25/12/66
[subprocess package](https://docs.python.org/3/library/subprocess.html)
- run code ซ้ำ ๆ ธรรมดา
- .Popen  ดึง output จาก Program อื่น มาใช้ต่อ
  
> file python  แบบพิเศษที่สามารถไปเรียกใช้ **program** อื่น หรือ **python** อื่นๆ ที่เขียนจบแล้วมาใช้ร่วม เพื่อลดการเขียน Code ซ้ำซ้อน  
> เราจะต้องใช้ subprocess เมื่อ...  
> ต้องการ run งานร่วมกับ Program สำเร็จรูปอื่น ๆ หรือ code python  อื่น ๆ ที่เขียนเสร็จแล้ว

## basic terminal command
### ถ้า run ```$ python python_subprocess``` แบบให้ดูรายละเอียดไฟล์
```javascript
import subprocess // สำหรับ run terminal command (ทุกอันที่สามารถ run บน terminal ได้เราจะสามารถใช้ subprocess run ได้)// นำที่มี Output/~output มาแสดง

if __name__ == "__main__":
    //basic terminal command
    subprocess.run(["ls", "-ltr"]) // command ใน subprocess จะเขียนเป็น list ช่องว่าง ใช้  ,
```
git push to GitHub  
เข้า VM ```ssh``  
git pull  
output  
> <img src="https://github.com/nattntn/AIPrototype2023/blob/main/lecture/output_subprocess.jpg" width = "600" heigth="600"/>

### ถ้า run ```$ python python_subprocess``` แบบให้ดูรายละเอียดไฟล์ แล้วถ้ามี testfolder1 ให้ลบ
```javascript
import subprocess // สำหรับ run terminal command (ทุกอันที่สามารถ run บน terminal ได้เราจะสามารถใช้ subprocess run ได้)// นำที่มี Output/~output มาแสดง

if __name__ == "__main__":
    //basic terminal command
    subprocess.run(["ls", "-ltr"]) // command ใน subprocess จะเขียนเป็น list ช่องว่าง ใช้  ,
    subprocess.run(["rm","-r","/้home/nattntn/testfolder1"])//ลบ testfolder1
```
git push to GitHub  
เข้า VM ```ssh``  
git pull  
output  
### ถ้า run ```$ python python_subprocess``` แล้วให้มัน run file ``firstpy.py``

```javascript
import subprocess // สำหรับ run terminal command (ทุกอันที่สามารถ run บน terminal ได้เราจะสามารถใช้ subprocess run ได้)// นำที่มี Output/~output มาแสดง

if __name__ == "__main__":
    print('first run num = 100 xx= 90') \\ แค่ print
    subprocess.run(["python","firstpy.py", "--num", "100","--xx", "90"])
    print("-"*80)
    print('second run num = -10 xx= -90')
    subprocess.run(["python","firstpy.py", "--num", "-10","--xx", "-90"])
    print("-"*80)
    print('third run num = 0')
    subprocess.run(["python","firstpy.py", "--num", "0"])
    print("-"*80)
```

git push to GitHub  
เข้า VM ```ssh``  
git pull  
output  
> <img src="https://github.com/nattntn/AIPrototype2023/blob/main/lecture/output_subprocess_2.jpg" width = "600" heigth="600"/>

### ถ้า run ```$ python python_subprocess``` แล้วให้มันสามารถเอา output จาก Program อื่นไปใช้งานต่อได้ 
```Popen``` --> เพื่อไปรับ  output
```javascript
import subprocess // สำหรับ run terminal command (ทุกอันที่สามารถ run บน terminal ได้เราจะสามารถใช้ subprocess run ได้)// นำที่มี Output/~output มาแสดง

if __name__ == "__main__":
    //use output from other program
    process_output = subprocess.Popen(["python","firstpy.py", "--num", "0"],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
//process_output เก็บ output , error 
    out, err = process_output.communicate()
    print(out.decode('utf-8')) // เรียกดู output
    print(len(out.decode('utf-8'))) // นับจำนวนพยางค์ชนะ Output


    //HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello world!)
```
git push to GitHub  
เข้า VM ```ssh``  
git pull  
output  
> <img src="https://github.com/nattntn/AIPrototype2023/blob/main/lecture/output_subprocess_3.jpg" width = "600" heigth="600"/>


# HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello world!)
[python_subprocess_HW1](https://github.com/nattntn/AIPrototype2023/blob/main/python_subprocess_HW1.py)
 1. ``$ vi python_subprocess_HW1.py`` แก้เลข ต่างๆ
 2. `` git checkout python_subprocess_HW1.py`` ให้ไฟล์นี้กลับไปเหมือนตอนแรกที่ยังไม่แก้เลข
 3. ``git pull`` ดูการเปลี่ยนแปลง

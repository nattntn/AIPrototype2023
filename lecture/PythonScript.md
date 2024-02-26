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
6. ออกมา ```$ ls``` ดูfile ใน terminal
7. up ขึ้น GitHub
   ```
   $ git status
   $ git add {file name}
   $ git commit -m "comment"
   $ git push
   ```
8. เข้า ไปที่ VM แล้วดูว่าเรามี env  อะไรที่สร้างไว้เเล้ว
   ```
   (base)  : $ conda env list
   ```
9. activate env
    ```
    $ conda activate deeptooth38
    ````
10. run firstpy.py
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

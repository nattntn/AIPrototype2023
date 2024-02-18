# Install miniconda
[miniconda](https://docs.anaconda.com/free/miniconda/)
- 1. Install on cloud (VM)
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```
Paste and enter
```
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```
done!!
- 2. Exit VM
- 3. เข้า VM ใหม่ เพื่อให้ package ที่โหลดเพิ่มไปทำงาน
     ถ้าใช้ได้เเล้วจะเป็นแบบ
     >> (base) nattntn@nattntn:~$
   - check version and test code
     ```
     (base) nattntn@nattntn:~$ python
     >>> print('xx')
         xx
     >>> exit() # ออกจาก python
     ```
- ย้ายไฟล์จาก cloud ของเพื่อน ลงเครื่องของเรา
  **ย้ายที่เครื่อง**
  ```
  $ nattntn@LAPTOP.......:~$ scp nattntn@IP:/home/yoke/{ชื่อไฟล์} /home/nattntn
  ```

# Install program in Linux 
- Format
  ```
  $ sudo snap install {ชื่อโปรแกรม}
  #ex
  $ sudo snap install ffmpeg  # มันจะทำการ download จาก internet ให้เลย
  #or
  $ atp install {ชื่อโปรแกรม}
  ```
- **ทุกโปรแกรมจะมีคำสั่ง $man**
  ```
  $ man ls  # = manual ดูว่ามีคำสั่งอะไรให้เลือกใช้บ้าง
  # or
  $ {ชื่อโปรแกรม} -h # บอกว่าโปรแกรมนี้มี option  อะไรให้ใช้บ้าง
  $ ffmpeg -h
  ```
  - ex
  ```
  $ ls -l # ดูรายละเอียดไฟล์
  $ ls -lt # ดูรายละเอียดไฟล์แบบใหม่สุดอยู่บน
  $ ls -ltr # ดูรายละเอียดไฟล์แบบใหม่สุดอยู่ล่าง
  $ ls -ltrh # ดูรายละเอียดไฟล์แบบภาษาพูด --> ขนาดไฟล์ที่คนพูดกัน --> h=human
  ```
# Install package (ที่จำเป็น)
> Linux เวลาคนใช้ จะใช้ร่วมกันหลายคน **ดังนั้น**ถ้าเราโหลด program มาแบบ **sudo** คนอื่นก็จะสามารถใช้โปรแกรมเราได้ด้วย  
> *แต่ถ้าไม่อยากให้คนอื่นใช้ด้วย/งานเรา version ไม่ตรงกับงานคนอื่น* ก็สร้าง **"Environment"** ขึ้นมา เป็นโลกของเรา 1ใบ python ของเราคนเดียว

โดยปกติ
```>> (base) ```  คือ python version หลักที่ทุกคนใช้กัน ```ssh``` เข้ามาก็ใช้ได้เลยไม่ต้องมี env อะไร โดยจะเป็น **version ใหม่ล่าสุด**  
แต่บางอัน เช่น tensorflow ก็ใช้ได้เเค่กับ python version 3.8 ก็เลยต้องสร้าง env 😿
  
  
  
  
  
  
  
     

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
   - check version python and test code
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

## [Create environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)
**ต้องมี miniconda** **ต้องอยู่ใน VM**  
- 1. สร้าง Environment (แค่ตอนเริ่ม)
     ```
     $ conda create -n {ชื่อ env} python = {versionที่ต้องการ}
     #ex
     $ conda create -n deeptooth38 python = 3.8 # 3.8 จะโหลด v. ใหม่ล่าสุดของ 3.8 มา หรือถ้าเราต้องการเจาะจงก็ระบุลงไปได้เลย เช่น 3.8.2
     ```
- 2. เข้าไปใช้งาน env
       ```
       $ conda activate {ชื่อ env}
       # ex
       $ conda activate deeptooth38
       ```
       หน้าตาหลังจากเข้ามา ```(deeptooth38) nattntn@nattntn:$```
- 3. เลิกใช้งาน env (ก่อนจะไปใช้ env อื่น)
      ```
      $ conda deactivate {ชื่อ env}
      # ex
      $ conda deactivate deeptooth38
       ```
## Format install package
อยู่ใน VM และเข้า env แล้ว
```
$ conda install {ชื่อpackage}
```

## Install Pandas package
```
$ conda install pandas(=versionที่ต้องการ ถ้าไม่ระบุจะเป็น version ใหม่ล่าสุด)
```
- check ว่า install ได้
  ```
  $ import pandas #ได้
  ```
## Install Jupyter notebook package
```
$ conda install notebook
```
**แต่ยังไม่สามารถเรียกใช้ได้ ต้องใช้คำสั่งพิเศษในการเข้าใช้งาน ```ssh -L ```(tunnel)**
### [Tunnel](https://www.techtarget.com/searchsecurity/tutorial/How-to-use-SSH-tunnels-to-cross-network-boundaries#:~:text=The%20%2DL%20option%20is%20used,to%20access%20a%20remote%20resource.)
> The -L option is used to bind a port on the local machine with a remote port at the remote destination IP address. The port is bound through the connection to the user account at the ssh_server.

- syntax:
  ```
  $ ssh -L local_port:remote_destination:remote_port user@ssh_server
  ```
  
       
  
  
  
  
  
  
     

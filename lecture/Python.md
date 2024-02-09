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
  nattntn@LAPTOP.......:~$ scp nattntn@IP:/home/yoke/{ชื่อไฟล์} /home/nattntn
  ```
  
  
  
     

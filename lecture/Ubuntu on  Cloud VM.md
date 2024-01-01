![VM](https://github.com/nattntn/AIPrototype2023/blob/main/lecture/VM.jpg)
 # 1.การสร้าง VM
เข้า Azure -> Education -> VM -> Create a virtual machine
> password: Nat{National ID}_
 # 2. login/logout  VM จาก PC
 ```
 $ssh username@IP #login
 $exit #logout //จบ section
 ```
 # 3. Move file/folder in PC to Cloud and vice versa 
 __ตอนย้ายต้องอยู่ในเครื่องเท่านั้น!!__
* Format
  ```
  $scp {ที่อยู่ต้นทาง} {ที่อยู่ปลายทาง}
  ```
* ส่งไฟล์จากเครื่องเราไปบน Cloud
  ```
  $scp ./xxx nattntn@IP:/xxx/xxx/.
  $scp -r testfolder1/ nattntn@IP:/home/nattntn/. # cp folder in PC to Cloud
  ```
* ดึงไฟล์จาก cloud มาเครื่องเรา
  ```
  $scp nattntn@IP:/xxx/xxx/yyy.py /home/nattntn
  $scp nattntn@IP:/home/yoke/print.py /home/nattntn # move file from folder name york  on nattntn Cloud to PC
  ```
 # 4. Cloud Shell (ใช้ Terminal on Internet)
 > Shell.Azure.com
* ครั้งแรก ssh เข้า VM ก่อน
  ```
   $ssh username@IP #login
   $exit #logout //จบ section
  ```
* Upload file <ต้องอยู่บน shell แล้วค่อย scp to cloud >
  ```
  # 1. upload file on shell
  # 2. scp file to cloud
  $scp rog.png nattntn@IP:/~/. # ย้ายมาhome // ทำบนshell
  ```
  # 5. สร้างเครื่องที่ให้เพื่อนเข้ามาใช้บน Cloud เราร่วมกันได้
  * 1. สร้างเครื่องให้เพื่อน
    ```
    $sudo adduser {ชื่อเครื่อง} #sudo = super user (เจ้าของเครื่อง) do
    # password
    ```
  * 2. ให้เพื่อนลองเข้า Cloud ที่เราสร้าง บน เครื่องเพื่อน
    ```
    $ssh {ชื่อเครื่องที่สร้าง}@IP #IP super user
    $htop # ดูว่าเพื่อนเข้ามายัง
    ```
  * 3. แก้ไข Permission ของเครื่องที่สร้าง
    super user แก้ไขได้
    ```
    $sudo chmod 755 yoke # chmod = change mode // 7 = owner(r|w|x), 5 = group (r|-|x),5 =other (r|-|x)
    ```
    
    
  
  
 
 

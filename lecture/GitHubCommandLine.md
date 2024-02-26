# Setting your Git username for every repository on your computer (1st)
**on vm**

## [Set a Git username:](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git)
```
git config --global user.name "nattntn"   # "{ชื่อgithubเรา}"
```

## [Set a Git email:](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)
```
git config --global user.email "natthanich.h@kkumail.com" # "YOUR_EMAIL_sign in git"
```

# Clone GitHub 
- 1. สร้าง folder รวบรวม code
```
$ mkdir codes
```
- 2. เข้า GitHub ที่ต้องการ clone
- 3. กด ที่  **<> codes** ---> **HTTPS**---> **copy**
 
     
     <img src="https://github.com/nattntn/AIPrototype2023/blob/main/lecture/clone%20git.png" width="400" height="400" />
- 4. clone (load repository to your PC)
     ```
     $ git clone https://github.com/nattntn/AIPrototype2023.git
     ```
# Up file/code to GitHub on Internet
- 1. แก้ README (ลอง)
     ```
     $ vi README.md
     ```
- 2. check ว่า file ไหนถูกแก้ไขไปบ้าง
     ```
     $ git status
     ```
- 3. save file ลงบน GitHub on Internet
     ```
     $ git add "{filename}"
     $ git commit -m "{comment}"
     $ git push  # push file to GitHub
     ```
     > username: nattntn  
     > password: [personal access token on GitHub](https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed?fbclid=IwAR0AMgckkSa4nNCk67TvtlVrZLl1LF_t3ssdQ5mq32emEpDgSLTT_LHYLOE)  
     > <img src="https://github.com/nattntn/AIPrototype2023/blob/main/lecture/personal%20access%20token%20on%20github.png" width = "400" heigth="200"/>


# Clone GitHub to your PC
**on PC**
## 1.เชื่อม Folder ที่ทำให้ PC(your window) เห็น Terminal(Ubuntu)
**ทำให้เราสามารถแก้ Code บน VS Code ได้**
- 1. ออกมาให้เห็น File บน systems
     ```
     $ cd ../..
     ```
- 2. เข้าไปใน drive ในเครื่องทั้งหมด (c d e)
     ```
     $ cd /mnt
     ```
 - 3. เข้าไปใน drive C
      ```
      $ cd /c
      ```
 - 4. สร้าง drive ที่เชื่อมกันระหว่าง forder ของ window กับ Terminal
      ```
      :/mnt/c$ mkdir Ubuntu #มี Ubuntu ในเครื่องแล้ว
      ```
 - 5. ``cd``กลับมาอยู่ที่ /home/nattntn
 - 6. สร้าง forder บน Terminal ที่จะเอาไว้เชื่อมกับ PC
   ```
   $ mkdir Outside
   ```
- 7. link drive in your PC and terminal
     *format*
     ```
     ln -s {drive ต้นทางที่จะ link} {ที่อยู่ปลายทางที่จะเก็บ} # ln = link, s = Symbolic (link แบบไม่ย้ายไฟล์มา)
     ```
     *ex.*
     ```
     /home/nattntn/outside:$ ln -s /mnt/c/Ubundu /home/nattntn/outside
     ```
     **ตอนนี้ เมื่อเราลากไฟล์อะไรมาใส่ใน file Ubuntu on window  มันก็จะมาอยู่บน teminal file outside ของเราด้วย**
      
   
     


     

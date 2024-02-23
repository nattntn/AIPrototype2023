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
     


     

### TITLE
>Tin học văn phòng cơ bản
### DESCRIPTION
>Sau khi tham gia một khóa Tin học văn phòng cơ bản, Hòa đã có thể tự tạo một tệp tài liệu độc hại và anh ta có ý định sẽ dùng nó để hack cả thế giới

>Tải challenge: https://drive.google.com/file/d/1WrLFE5qA-qJ6iLEQYQqCo0Xb99Yz8mTH/view?usp=drive_link (pass: cookiehanhoan)
### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
>very easy
### Pass
>cookiehanhoan
### Tool
>[oletools](https://github.com/decalage2/oletools/wiki/Install)
### FLAG
>CHH{If_u_w4nt_1_will_aft3rnull_u}
### SOLVED
When you open the file, you will get the Challenge.doc. Instantly, I know there's something sus with that doc file, and it's likely embedded with malicious VBA macros. So I used __oletools__ to extract the VBA macros:
```
olevba Challenge.doc
```
Read the malicious code and get the flag!!

P/S: If you can't identify it right away, view it:
```
file Challenge.doc
```
You will get __.dotm__ file extension and it is __Word macro-enabled template__. Sus right away!!

![image](https://github.com/user-attachments/assets/f1683362-2095-47ca-9378-f85a23212f73)


#### END!!

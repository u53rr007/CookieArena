### TITLE
>File Extension
### DESCRIPTION
>Is real photo?
### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
>easy
### Pass
cookiehanhoan
### Tool
>Linux, cmd
### FLAG
>CHH{B3_c4r3ful_w1th_f1l3_exT3ns10n}
### SOLVED
Download the girl-xinh.zip file. It contains the girl-xinh.jpg file, but when opened, it is not in the right format.

![image](https://github.com/user-attachments/assets/02ae97e0-92f8-4c56-887f-f5ff5042f174).

Use the __file__ command to determine exactly what it is.
```
file girl-xinh.jpg
```
It is a __PE executable__ file.
![image](https://github.com/user-attachments/assets/6bd1ab58-5878-4f68-b1ee-a1c6fc4e4420)

Copy it to a Windows machine and run it using cmd and you will get the flag.

#### END!!


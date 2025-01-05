### TITLE
>Deleted SMS
### DESCRIPTION
>We receive information about thieves using text messages to exchange sensitive information. Before leaving, they deleted messages to erase traces. Is deleting this data safe? Please help us restore that secret message.

>Flag Format: CHH{XXXXX}

### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
>easy but tricky
### Pass
>cookiehanhoan
### Tool
>[hexed.it](https://hexed.it/)
### FLAG
>CHH{you_caN_reCOVeRy_sQ1i73}
### SOLVED
Download the file, and you get the MyPhone file. If you don't know what file type it is, use the file command in Linux to find out.
```
file MyPhone
```
![image](https://github.com/user-attachments/assets/8eb0f7eb-9c8d-4cd7-9549-7d8722a9729a)

So it is a SQLite database. If you pay a little more attention to the description, you can see it told us to try to recover the deleted sms, in this case, maybe deleted records in the database. So I went on Google to do some research about some forensic tools that can recover the deleted records in SQLite. At first, I used this tool [fqlite](https://github.com/pawlaszczyk/fqlite) and tried to recover the deleted records. It successfully recovers some records but as you can see it looks sus. 

![image](https://github.com/user-attachments/assets/1d2864b5-8218-4464-b919-e2914ea5d179)

Then I put those values onto __CyberChef__ and deciphered them using __ROT13__.

![image](https://github.com/user-attachments/assets/5a099f37-ecbe-4f17-8c93-83a7f9a33a4e)

As you can see it was some hint related to our flag. But as I dig deeper nothing can be found. So out of nowhere, I decided to look at the hex view of this database, and suddenly something sus caught my eye.

![image](https://github.com/user-attachments/assets/669971fe-296e-4a98-9022-59f6d0802a45)

 It seems like our flag format. I put that on __CyberChef__ and deciphered it using __ROT13__ and IT IS THE FLAG! So it is easy to use __hexedit__ in the first place.
#### END!!

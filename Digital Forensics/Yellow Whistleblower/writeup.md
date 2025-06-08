### TITLE
>Yellow Whistleblower
### DESCRIPTION
>A Machine Identification Code (MIC), also known as printer steganography, yellow dots, tracking dots, or secret dots, is a digital watermark that certain color laser printers and copiers leave on every printed page, allowing identification of the device which was used to print a document and giving clues to the originator.

>Developed by Xerox and Canon in the mid-1980s, its existence became public only in 2004. In 2018, scientists developed privacy software to anonymize prints to support whistleblowers publishing their work.

>The flag format is CHH{Manufacturer-YYYYMMDD-HHMM}
>YYYY: Year
>MM: Month
>DD: Day
>HH: Hour
>MM: Minute
>Manufacturer: Name of printer (eg, Epson, Dell, HP,..)

### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
> easy
### Pass
>cookiehanhoan
### Tool
> [pdf2png](https://pdf2png.com/), [deda extraction tool](https://github.com/dfd-tud/deda)
### FLAG
>CHH{Epson-20200205-1020}
### SOLVED
Download the file; what you get is a PDF file. Normal file, nothing suspicious with the file and its type. Open it and inside is just 1 page with the title "huong dan ve ga" but the description will give you an instruction to find what you need. MIC?? Hah? So Google it with some simple keyword. I googled it with the keyword: "__Machine Identification Code decoder__" and it gave me more information about that technique. 

![{2C2A04BB-2132-4035-9355-8977C41BE3E0}](https://github.com/user-attachments/assets/0e0abc86-7db2-44d1-8af3-6eb3e654d245)

Hmmm, not what I needed. So add the word "gitHub" and maybe you will find some repos to decode it.

![{47DE0D3E-D2EB-45C3-927D-9E76851DC20B}](https://github.com/user-attachments/assets/1580d62e-acec-4b51-9ae9-5ee9aaf119b0)

Oh, here it is. So I cloned it and ran but that tool didn't scan your PDF and extract the yellow printing dots rather it was just a layout for you to fill in those dots manually when you already had them. So I purely just tried some more GitHub repos until I found a repo that could extract MIC but I read the tool usage and found out that it just accepts input as an image file type (.jpg, .png), not .pdf. So I use an online tool to convert .PDF to .PNG. 
After downloading the new PNG file I noticed something off. The portrait of the image seems bigger than the previous PDF one. So I zoomed in to take a closer look and there are a bunch of yellow dots that follow a pattern.

![{80B00FDD-CE3A-4C32-BF89-594646D7168F}](https://github.com/user-attachments/assets/f75625d9-683d-4439-b1f4-8bada20ec85b)

Haha, here it is. So I used the Deda GitHub repo to extract it. First, clone it and follow its installation instructions.
```
$ git clone https://github.com/dfd-tud/deda.git
$ pip3 install --user deda
```
After that, use the command deda_parse_print on the PNG file and you get the timestamp and the manufacturer which is also the flag of this chall.
```
deda_parse_print huong-dan-ve-ga-cookiehanhoan-1.png
```

![image](https://github.com/user-attachments/assets/b1f86679-88ca-4641-ac78-4e99a4cef70e)

### END!!

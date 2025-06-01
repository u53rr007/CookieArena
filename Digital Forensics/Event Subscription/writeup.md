### TITLE
>Event Subscription
### DESCRIPTION
>Đội CSIRT của chúng tôi được yêu cầu xử lý sự cố trên một máy chủ mà chúng tôi đã xử lý xong cách đây vài ngày. Vì vậy chúng tôi tin rằng vẫn còn một cơ chế persistence nào đó của kẻ tấn công mà chúng tôi đã bỏ sót

### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
> easy
### Pass
>cookiehanhoan
### Tool
> [cyberchef](https://cyberchef.org/), [WMI_Forensics](https://github.com/davidpany/WMI_Forensics)
### FLAG
>CHH{WMI_Th3_5te4lthy_c0mP0n3Ntt}
### SOLVED
Download the file and you get the Repository folder inside, which contains a bunch of files that I don't know. So I tried to google it to find anything. With a simple search "What is index.BTR file" I found this:

![{97A5731F-787B-4461-8AAD-34D9B5979D0F}](https://github.com/user-attachments/assets/aa593cee-2f77-4c39-9374-f243d54f2fee)

So this is a Windows Management Instrumentation (WMI) repo in Windows. Then I looked back at the description, it mentions something about persistence in the WMI repo. Ok! Use your Google searching skill with some keywords like: "__WMI forensic__" or "__WMI persistence forensic__". You will likely find this GitHub repo:
[WMI_Forensics](https://github.com/davidpany/WMI_Forensics).

![{417F63FC-00A3-4BC7-9CEB-78D8345EFC73}](https://github.com/user-attachments/assets/29648c5c-64fe-498d-8865-19ba9d09bd0d)

Inside we will have an interesting Python script that can help us: PyWMIPersistenceFinder.py. Scroll down to look for the usage of this script. That easy we already have the OBJECT.DATA file.

![{3A60E14F-D142-48E4-818A-B983114E74A4}](https://github.com/user-attachments/assets/a7ab7351-45bc-4126-bcb6-c378d41c07b8).

Run the script with python2 because python3 will cause an error and this script is written in python2 language:
```
$ git clone https://github.com/davidpany/WMI_Forensics.git
$ python2 PyWMIPersistenceFinder.py OBJECT.DATA
```
The output you get will have a bunch of text and there is 1 consumer that has a sus argument - a PowerShell command that encodes something!

![image](https://github.com/user-attachments/assets/e603ddfe-e81e-4837-a4c3-4e54ad8ed165)

I immediately realized that it was a base64 encode but if you can't you can simply Google to find out what encode type to use with the PowerShell flag "-e". [Powershell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_powershell_exe?view=powershell-5.1).

![{4F2A3A18-3FA9-4CC5-B859-57033EDD7B3E}](https://github.com/user-attachments/assets/18db3fd1-687e-4e3b-87c7-f40eb78e50a9)


Use Cyberchef or any base64 decode tool to decode that string and you will get the flag BUT with null bytes separate them apart so delete those bytes or use the "Remove null bytes" options in Cyberchef.
### END!!

### TITLE
>Trivial Flag Transfer Protocol
### DESCRIPTION
>FTP protocol is plaintext data; you can easily see the data transfer between the client and server. Using Wireshark to analyse the pcap file, extract the data and find the FLAG,

>Flag format is picoCTF{XXX}

>Author: Dany

### CATEGORY
> Forensics
### HINT
>None
### DIFFICULTY
>easy kind of
### Pass
>cookiehanhoan
### Tool
>steghide, wireshark
### FLAG
>picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
### SOLVED
Download the file and you get the tftp.pcapng file. Open it in Wireshark and also based on the title you can focus your attention on the TFTP protocol. Filter it and follow the stream. You can see some kind of files being transported.
![image](https://github.com/user-attachments/assets/f8cc7eb1-a27f-49e1-a156-d7bfcf6605a0)

Since TFTP doesn't encrypt the files while transporting you can easily export the files for further inspection.

__File > Export Objects > TFTP__

![image](https://github.com/user-attachments/assets/bd58ad26-1cae-4768-854b-bf92defd89d6)

Download all those packets. First, read the __instruction.txt__ you can see it under some kind of encode or cipher. Go to CyberChef and see what it is. So it is __Rot13__!
Decipher it! It is just English sentences but written in one chunk with no space. The instructions mention some kind of plan.
![image](https://github.com/user-attachments/assets/54c02bda-b97e-4d0b-bd3d-6be5c3ce8494)

There is a __plan__ file. Open it and it seems to be another ROT13 cipher.

![image](https://github.com/user-attachments/assets/892df21e-df62-477b-aae1-6c5cab9c15b5)

So the instructions tell us to check out those 3 __.bmp__ files. But after a whole bunch of time trying to extract the metadata, and hex out of it nothing can be found.
There is a __program.deb__ file left untouched. After opening and inspecting further, it seemed like a __steghide__ library but nothing interesting was found. But look back at the __plan__ instruction you can see something sus.
The word __DUEDILIGENCE__.

![image](https://github.com/user-attachments/assets/871c3c80-39e9-45ca-9174-62c5402a37a3)

It is the passphrase for __steghide__. So using steghide with that passphrase extract the data from those 3 images.
```
steghide extract -sf picture3.bmp -p DUEDILIGENCE
```
The first 2 images have nothing inside. The __picture3.bmp__ has the __flag.txt__ contains the flag.
#### END!!

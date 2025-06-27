### TITLE
>Corrupted PCAP
### DESCRIPTION
>The capture file appears to be damaged or corrupt. Could you find the FLAG?

>Format Flag: CHH{XXX}
### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
>not quite easy
### Pass
>cookiehanhoan
### Tool
>[fix pcap file](https://f00l.de/hacking/pcapfix.php)
### FLAG
>CHH{ha!_you_found_it!}
### SOLVED
Download the file, and we have a pcap file. When I opened it, it said this file was corrupted.
![{2869B13B-4EC4-4E34-9739-C367B879C4E1}](https://github.com/user-attachments/assets/4b1fbb51-99e0-46eb-88a6-27719bf13eda)

I tried to Google how to fix it with the simple keyword "fix corrupt pcap file". There are a few Github repos that can fix it, but I used this online pcapfix for quickness: https://f00l.de/hacking/pcapfix.php.
![{4D23DCCD-EFDA-46DD-B0C8-6DD7C52CCAF7}](https://github.com/user-attachments/assets/47a3099c-ca5e-457d-be91-c63f57d70997)

After selecting the file and repairing it successfully, I opened the file again and it opened without any errors. I performed some techniques to check the pcap file such as:
- Statistics > Protocol Hierarchy (to check the protocols in this pcap file).
![{13C1A091-7938-4652-8A66-FF81DCE0952A}](https://github.com/user-attachments/assets/94a30d2c-110e-4ba0-b670-b9d379be6185)

- File > Export Objects (check the files that can be exported).
![{DD5BED79-D1AB-4ED9-8E39-FD453B61FA50}](https://github.com/user-attachments/assets/b6b85287-f5b1-41d4-9ed9-0742697824b5)
- Check the HTTP protocol and HTTP stream to see if anything is interesting.
- Search for the "CHH{" flag clue.
![{057395BA-28A9-4394-8624-C9DDFFD87FC7}](https://github.com/user-attachments/assets/f234feb6-8d11-42fa-a46d-53d06f0077a1)

After checking, I found that the HTTP protocol has quite a lot of packets being transferred back and forth, which is quite interesting. But when I dug deeper in that direction, I got nothing back. Then I thought about the attacker being tunneling something. And I searched for DNS Tunneling but DNS showed nothing unusual. After finding nothing I went back to HTTP and was stuck there for quite a while before I hit this TCP segment.
![image](https://github.com/user-attachments/assets/697f52a6-e7f7-4428-8eee-e017764bdd62)

The payload of this TCP segment mentions something about the flag and the TCP connection to port 2222 is also quite sus. When transferring between packets, there is a small byte segment that changes at the ":" position. Let's try to extract that byte segment and see.

![{89707D8C-1B00-4F8A-B572-7F7CF2EBAF03}](https://github.com/user-attachments/assets/00b8682e-8247-492a-a644-c441f298f772)

Use Tshark with the command:
```
tshark -r output.pcap -Y "tcp.dstport == 2222 and not tcp.analysis.retransmission" -T fields -e ip.id > output.txt
```
Because the changed part is in the identification field, we extract that part. After extracting, we put the hex into cyberchef to decode and...
![{950BE9F6-87B1-4A2F-B98F-33E5340EEE9F}](https://github.com/user-attachments/assets/1b6d9cf7-fe24-4b6b-9612-b6bb4c5008ad)

It doesn't look like the flag, it's kinda messy. Ah!! It's because the hex is written in Big Endian, now we convert each pair of letters to Little Endian, and it will give us the flag.

### END!!

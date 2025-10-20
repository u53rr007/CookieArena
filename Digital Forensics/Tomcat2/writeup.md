### TITLE
>Tomcat
### DESCRIPTION
>Hackers attacked our Tomcat Web server. Our monitoring system collects network traffic during hacker intrusion. Please help us determine the attack method and what the stolen data is in the /flag.txt file.

>Format Flag: CHH{XXX}
### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
> piece of cake
### Pass
>cookiehanhoan
### Tool
> [Wireshark](https://www.wireshark.org/download.html)
### FLAG
> CHH{70MCAT_REvERSe_5He1l}
### SOLVED
Starting with the PCAP file, I looked at the Protocol Hierarchy and Export Objects, but didn't see anything special. A quick scan of the packets revealed many HTTP connections between the two IPs, 192.168.10.148 and 192.168.10.174, which showed signs of being related to Tomcat (as the challenge name suggests). Use "Follow HTTP Stream" to see details.

<img width="1536" height="773" alt="image" src="https://github.com/user-attachments/assets/87b2b78f-e3c0-4693-b989-dd730c7c7f99" />

The first streams show that the attacker is doing a reconnaissance of endpoints like tomcat.css, tomcat.svg, etc, to detect vulnerabilities. Then, the attacker targets /manager/html with an __Authorization__ header, but the first attempts receive 401 Unauthorized. In stream __#31__, authentication is successful with Basic auth; Base64 decoding results in "tomcat:s3cret" string.

<img width="1536" height="807" alt="image" src="https://github.com/user-attachments/assets/1a992b23-e48d-402f-a634-101da2b9c15e" />

Using this credential, the attacker accesses /manager/images (looking to upload a shell) and is indeed able to upload a variety of file extensions.

<img width="1536" height="813" alt="image" src="https://github.com/user-attachments/assets/1f4e5b4f-9642-45e3-bcd5-5adddcb82cd5" />

In stream __#34__, he uploads a .war file (most likely a webshell) via /manager/html/upload, then tries to execute it at the /hello-world endpoint, and it succeeds.

<img width="1536" height="815" alt="image" src="https://github.com/user-attachments/assets/a451b5ff-367a-4421-b883-f079f76d4122" />

Next, the attacker uploads a few more .war files to the same path and runs /revshell with Connection: keep-alive to open a reverse shell.

<img width="1536" height="813" alt="image" src="https://github.com/user-attachments/assets/da756c7e-5159-4c38-8657-7480e5b6973e" />

After the reverse shell connection is established, observe other packets to see traffic to/from port 4444 (very sus, often used for reverse shell, probably Metasploit).

<img width="1536" height="795" alt="image" src="https://github.com/user-attachments/assets/f3fe7fce-5b36-40e0-ab27-2411565268e6" />

 Filter by port 4444 and "Follow TCP Stream", to TCP stream #39, see the attacker running cat flag.txt; the content is Base64 encoded — decoded to flag.
 ```
tcp.srcport == 4444 || tcp.dstport == 4444
```

<img width="1920" height="1019" alt="{F2D672FE-94EF-452B-BC38-8B8AD39E5E1E}" src="https://github.com/user-attachments/assets/64a7d11e-3987-4261-a338-6de90ac70d5b" />

<img width="1536" height="815" alt="image" src="https://github.com/user-attachments/assets/3c0a1a3d-e42f-4ccd-bb2b-609c7f0ca516" />

> [!IMPORTANT]
>  You’re seeing an __insecure configuration__ of the Tomcat Manager app exposed to the network with default/weak credentials (tomcat:s3cret). Once logged into /manager/html, an attacker can upload a WAR as a web shell.

P/S: There is a much faster and easier way to solve this challenge.
Filter for TCP packet in Wireshark that contains the word "flag" in them.
```
TCP contains "flag"
```
### END!!

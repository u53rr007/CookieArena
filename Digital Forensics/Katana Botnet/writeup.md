### TITLE
>Katana Botnet
### DESCRIPTION
>Gần đây chúng tôi phát hiện một số dịch vụ bất thường chạy trên máy chủ Linux của chúng tôi. Chúng tôi nghi ngờ nó đang bị lạm dụng để phân phối các tải trọng độc hại. Sau khi rà soát máy chủ, chúng tôi tìm thấy một tệp có vẻ là nguồn gốc của sự cố. Hãy giúp chúng tôi phân tích để tìm ra địa chỉ CnC đang lưu trữ tải trọng

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
> [Cyberchef](https://cyberchef.org/)
### FLAG
> CHH{Mirai_aka_Katana_b0tn3t}
### SOLVED

Download and open the tar file; it already contains the malware's source code written in Python. Opening it and skimming the malware code, we can see a variable containing base64.

<img width="1006" height="606" alt="image" src="https://github.com/user-attachments/assets/8dbefb64-aa2e-476c-adac-e684f610f269" />

Using CyberChef to decode that base64 segment, we see that the malware performs a wget to a suspicious Pastebin page. Accessing that Pastebin page, we will see the flag. Add an extra step to decode the URL to get the complete flag.

<img width="1222" height="345" alt="image" src="https://github.com/user-attachments/assets/e98348aa-63e3-408d-989e-98268c082a96" />

<img width="1540" height="185" alt="image" src="https://github.com/user-attachments/assets/9f74ca12-dae7-41cd-a83c-8e68fa3e594e" />

> [!IMPORTANT]
>  Information about Katana Botnet: [Katana aka Mirai](https://blog.cloudflare.com/inside-mirai-the-infamous-iot-botnet-a-retrospective-analysis/)

### END!!

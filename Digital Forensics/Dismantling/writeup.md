### TITLE
>Dismantling
### DESCRIPTION
>Be careful with Alternative Protocol

### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
>easy
### Pass
>cookiehanhoan
### Tool
>[cyberchef](https://cyberchef.org/), [Wireshark](https://www.wireshark.org/download.html), [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures)
### FLAG
>CHH{L1v3_@nd_d13_bY_7h3_Bl4de}
### SOLVED
Download the file, and we see a pcap file. Open that file in Wireshark and do some basic analysis, e.g., look at the Protocol Hierarchy, HTTP stream to see if anything is interesting. At first glance, everything is fine except DNS. The DNS protocol is quite sus with strange domain names being queried from IP 192.168.25.135.

<img width="1536" height="743" alt="image" src="https://github.com/user-attachments/assets/b63bc199-6834-414f-9308-a6a1c16cc7ac" />

Filter with: "dns && ip.src == 192.168.25.135" to see that in addition to querying sus domain names, this IP also spoofs by querying quite normal-looking domain names to deceive.

<img width="1534" height="720" alt="image" src="https://github.com/user-attachments/assets/ce3206bd-7a0f-4a02-a473-57ff8a3b493d" />

So we filter the results only to show domains containing "cookiearena.org".
```
dns.qry.name contains "cookiearena.org" && ip.src==192.168.25.135
```

<img width="1920" height="898" alt="{34B5E0AC-C594-4FA8-9FCA-F9024AD05C68}" src="https://github.com/user-attachments/assets/35b4b094-2a1e-4bce-a90d-3c5c1fa9591d" />

Combine with Tshark to extract the query name.

```
tshark -r Dismantling.pcap -Y "dns.qry.name contains "cookiearena.org" && ip.src==192.168.25.135" -T fields -e dns.qry.name > dns.txt
```
<img width="874" height="840" alt="{E91B264F-4808-47DA-8701-6EBFC123718D}" src="https://github.com/user-attachments/assets/3f1a9466-a776-40dd-b55a-ccde24c12774" />

Now the domain still contains cookiearena, write a short Python script to remove them (remove.py).

<img width="544" height="740" alt="{F8907EF9-A89C-4B0C-9285-144BDC7B425C}" src="https://github.com/user-attachments/assets/51592511-6b02-4b61-b7ae-fe51150d8228" />

After deleting, we see a familiar hex string with the opening bytes "504b", which means this is a zip file.

<img width="1529" height="526" alt="{2F4FC543-9C6F-4A0E-883B-AEFFB661BB8D}" src="https://github.com/user-attachments/assets/e75d14cd-2372-4736-81c2-3ceaef121ba2" />

Upload to CyberChef to convert to raw, but when checking, CyberChef reports that this is a Microsoft Office file.

<img width="1225" height="414" alt="image" src="https://github.com/user-attachments/assets/6f418011-32c4-4176-a75d-0c14833ccc20" />

Hmm. Try using the file command to check again:
```
file download
```

<img width="712" height="121" alt="{8C774E3B-B88C-4AB6-86ED-B3EB5AEF27E7}" src="https://github.com/user-attachments/assets/be79b89f-9eb0-433f-91ee-d9050f3874cb" />

Ohh!! So this is an Excel file, so change the extension to xlsx to open it with Excel, and we will see the flag appear in the gender field.

<img width="1920" height="1021" alt="{13CCDEFC-96FD-41FB-AD6A-BEE18E063A2D}" src="https://github.com/user-attachments/assets/1b0828ee-16b0-4d1c-92af-8e3d3cad6acd" />

### END!!!

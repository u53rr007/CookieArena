### TITLE
>Simple HTTP Proxy
### DESCRIPTION
> Take a look at the source code and make a valid HTTP Request to get the FLAG content

### CATEGORY
> Misc
### DIFFICULTY
>very easy but it kind of tricky
### Pass
> cookiehanhoan
### Tool
> python script
### FLAG
>CHH{HTTP_via_RaW_Sock3T_c66178ea34c9ac78911dea7d8f4a1ffb}
### SOLVED
Run the challenge, and you get the website with the downloadable file containing the website back-end script. Firstly, examine the web. You immediately bump into the __/socket__ directory that says "Raw Socket Sender". Interesting!!
![image](https://github.com/user-attachments/assets/f6e58a09-4bd5-4bd9-82b9-ad990fbf4db6)
There is nothing more on the web so continue to examine the back-end script. After analyzing all the files, we focus our attention on the __run.py__ that runs something behind on the web. Summarize that file:
+ __Web Server Setup__: Runs a Flask web server on 0.0.0.0:1337, making it accessible on all network interfaces.
+ __/socket Route__: Allows users to send arbitrary TCP requests to a specified host and port.
  ![image](https://github.com/user-attachments/assets/3ee46d2c-7efb-446e-a7ba-a2e37d31d1e0)
+ __/admin Route__: Only accessible if multiple security checks pass.
 ![image](https://github.com/user-attachments/assets/78c0e9e7-3ec4-4b2d-aa93-18ce17b8cad5)

So after inspection you can clearly see the __/socket__ can vulnerable to SSRF (Server-Side Request Forgery) and using that we can bypass the remote_addr = 127.0.0.1 (localhost) and all other security checks in __/admin__. Then, write a payload (__adminBypass.py__) or using Burp Suite to send the request and get the flag.

__P/S__: The funny part is that I stuck at the last check of the __if request.form.get('userid') != 'admin'__ for 2 hours straight and finally figured out that the server has the __trailing space__ in the data part.

"userid=admin"   ❌

"userid=admin "  ✅

>Ref: [Server-side request forgery](https://portswigger.net/web-security/ssrf)

### END!!

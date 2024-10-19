### TITLE
>Can you see me ?
### DESCRIPTION
> Doing with image files should be the first step for anyone who learning cybersecurity

### CATEGORY
> Steg
### HINT
>[Writeup cre: n9tr4o](https://forum.cookiearena.org/t/stenography-can-you-see-me/61?utm_source=get_more_hint)
### DIFFICULTY
>very easy but it kind of hard
### Pass
> cookiehanhoan
### Tool
> aperisolve.com, pngcheck, hexed.it
### FLAG
>EHC{b1n4ry_1s_f4nt4st1c}
### SOLVED
First, you receive an image named s3cr3t.png; open it, and it's just some weird image.  Continue to run it through __aperisolve.com__, found out an interesting comment that said: "__y0u_c4n_n0t_cr4ck_th1s_f1l3_w1th_th3_d3f4ut_w0rdl1st_0n_k4l1__". At first, I didn't understand what it meant!!

![image](https://github.com/user-attachments/assets/d06e36d1-e58b-4c12-a867-ab037c0e15d4)

Then I try to run Steghide using the comment as a passphrase, but it doesn't work. If you look closely, an interesting thing found on Aperisolve is that this image is somehow corrupted.

![image](https://github.com/user-attachments/assets/97f05767-8136-4a53-9498-088fef1b10d7)

Run it using __pngcheck__ with the command:
```
pngcheck s3cr3t.png
```
It then pops up an invalid chunk of data inside the image which makes this file corrupted with the bytes of __00 4e 00 47__.

![image](https://github.com/user-attachments/assets/ea8c855c-1951-4824-bbe9-96c2de5ac383)

Open the image on __hexed.it__ for further inspection. Navigate to those bytes and...... It is another image inside an image!! You can see that through the file signature or the magic bytes that create the __PNG__ header. But those magic bytes are not correctly placed and that is why it makes the original file corrupted.

![image](https://github.com/user-attachments/assets/edd9fca8-be91-49ab-b630-60827c9281bb)

Next, separate that image from the origin to create an uncorrupted image. At the end of the image have 2 IEND signatures (end of image file) which end with the 0x82 byte. 

So separate the second image from the origin begin at __00 89 00 50 --> first 00 60 00 82__ to get the full original image.

![image](https://github.com/user-attachments/assets/c87bd23c-9db5-4b8f-88ae-c68b371c7743)

After getting the uncorrupted version of the first image I started to analyze the image but nothing more was found. Then I pay attention to the second image. 

The second image was cut by the __0x00__ byte in between each byte.

![image](https://github.com/user-attachments/assets/4892be25-d990-47a3-9d49-f87fc44d95d6)

You can see the pattern of the 0x00 byte being inserted into the even columns, so write a script to delete that (__Remove0.py__).

After deletion, you get a picture of a yellow square but after careful inspection, you will notice that it is not a normal yellow square when zoomed in it appears to have white dots scattered around. 

![image](https://github.com/user-attachments/assets/615dba05-37a1-454f-a250-5f290e72b217)

 It has a message hidden under those bits. So write a script to extract the value of RGB inside that image. 
 
 After running the script, you will see just the __Blue__ channel value change, the Red and Green stay the same. So write another script to extract the Blue value into an array. (__RGBExtraction.py__)
```
python3 RGBExtraction.py > output.txt
```
Paste the value onto __Cyberchef__ using __From decimal__ and __To hex__, you will see the hex value. Surprisingly, it is a .zip file with the magic bytes of __50 4B 03 04__.
![image](https://github.com/user-attachments/assets/9d07d083-9203-4aa3-8238-3284377a9d95)

But once again, it's being cut by the 0x00 byte. So use the previous script (__Remove0.py__) to delete it and get the .zip file. But once you extract the file, it prompts for password input. OH!! Using the comment from the original image for the password you will get the flag.txt containing the flag.
#### END!!

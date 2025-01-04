### TITLE
>From The Above
### DESCRIPTION
>Every day multiple NOAA weather satellites pass above you. Each NOAA weather satellite broadcasts an Automatic Picture Transmission (APT) signal, which contains a live weather image of your area.

>We have an APT audio recording. Could you decode it? When you got a message Flag{XXX}, please submit the flag with format CHH{XXX}

### CATEGORY
>Forensics
### HINT
>None
### DIFFICULTY
>very easy
### Pass
>cookiehanhoan
### Tool
>[noaa-apt image decoder](https://noaa-apt.mbernardi.com.ar/)
### FLAG
>CHH{h3ll0_fr0m_th3_0th3r_Sky}
### SOLVED
Download the file, and you will get the ufo.wav file. Since it is audio, try opening it using Audacity, but besides the audio wave, there is nothing more. So take a look back at the description. They mention something about __the APT signal__. So I then Googled to find a way to decode that signal. Try __APT signal decode__ or __NOAA weather signal decode__, and you will see a NOAA image decoder. 

![image](https://github.com/user-attachments/assets/3041846f-6190-40c7-a103-29c0ae59e55d)

After download and install. Run it with the input of our ufo.wav audio file. After processing it, we found an image of the flag but it was upside down and a little blurry.
![image](https://github.com/user-attachments/assets/d3b68017-e51c-4c9b-9cf2-a9ff6bb328f7)

So try to flip it back and then you get the flag.

#### END!!

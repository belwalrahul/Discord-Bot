# Discord-Bot
Creating Discord bots

## musicbot.py

### Installation
Inorder to run this script, you have to install these packages:
- discord.py (pip install -U discord.py)
- discord.py[voice] (pip install -U discord.py[voice])
- youtube_dl (pip install -U youtube_dl)

Also you have download "ffmpeg" but it does not end there.
- after downloading extract the zip and copy everything inside "bin" folder and paste it where pip installs the libraries, which is usually -> "C:\Users\<user name>\AppData\Local\Programs\Python\<your python version>\Scripts".
- or you can give "bin" path in your environment path variable


### Usage
Follow the above installation and run the script just like any other python script.
Below are some commands that the bot listens to (the prefix for the bot commands is "."):
#### join
- Makes the bot join the vocie channel of the user typing the command.
 - Syntax: .join
#### play
- Plays the music from the youtube link that is passed as an argument.
 - Syntax: .play <youtube_link>
#### pause
- Pause the music if playing.
 - Syntax: .pause
#### resume
- Resume the music if paused.
 - Syntax: .resume
#### stop
- Stops the music, how is it different from pause? You cannot resume it, it just removes the song from the queue.
 - Syntax: .stop
#### leave
- Makes the bot leave the voice channel.
 - Syntax: .leave
#### yt
- Searches youtube for the passed argument string and returns the link of top search result (you can give spaces i.e. there can be multiple words).
 - Syntax: .yt <your search string>
#### extract
- Extracts audio from the youtube link passed as an argument and saves it in you destination folder you mentioned in the code.
 - Syntax: .extract <youtube_link>
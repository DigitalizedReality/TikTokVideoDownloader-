**THINGS TO DO BEFORE/WHILE RUNNING CODE:**

1.) I recommend installing UblockOrigin's [`Chromium. zip`](https://github.com/gorhill/uBlock/releases). This is so that if you're using this code, you won't have to install UblockOrigin every time. Instead, you can just unpack the file into the 'Extensions' tab. If you don't know how to unpack extensions, I can provide the steps below:

Download the Latest Chromium.zip --> Extract Files--> Run Code--> Open new tab--> Press the puzzle piece in the top right (aka the extensions tab) --> Click on "Manage extensions" --> In the top right click on "Developer mode" and turn it on. --> In the top left, there will be a button to "Load Unpacked". Click it.  --> Select the Folder that you got after extracting Chromium.zip. --> Press "Select Folder". --> You're done! Close the "Extensions" tab and return to Ublock Origin's chromewebstore page. **THIS IS REQUIRED**


2.) Uncheck Chrome's "Show downloads when they're done" setting. The little pop-up crashes the code.

Open new tab -->Go to Chrome's "Settings" --> Search "Downloads" --> Scroll down --> Toggle OFF "Show downloads when they're done" --> **Return to Ublock Origin's home webstore page**. --> You're done! Continue with what the Python console tells you to do.

3.) Follow what the python console tells you. It should be enough... Sorry if it isn't understandable.


**Known issues:** 
1.) Bad wifi. Code relies on about 10-15 seconds of wait time, if the website doesn't load in that time, the code will show an error.

2.) CAPTCHA. Tiktok doesn't like bots, so you'll need to watch and check up on the code ever so often to make sure the CAPTCHA doesn't pop up and ruin the code. You'll have to restart all over again if that happens. Though not often, if you're downloading 30+ videos, it will probably open up one captcha in the middle of it. You'll have 5ish seconds to close it, or else the code will crash.

3.)Misspelling or wrong username/password. I didn't code any retry attempts, so if you get something wrong while writing a username or pass, the code will crash.

4.) Didn't install adblocker. The website used to install the videos has a ton of pop-up ads, which is why UBLOCK ORIGIN is REQUIRED. Without it, a pop-up ad will break the code. Selenium opens a fresh Chrome browser, so you'll need to install an ad blocker every time. Even if you already have one installed, you need to do it again on the window Selenium opens.

5.) You touched/opened/closed something while the code was running. When the code is running, please don't touch anything in the browser unless a CAPTCHA pops up. Otherwise, you have 5-10 seconds to solve the captcha and let the code continue running.   The only time you're allowed to open/close tabs is during the beginning when setting up UBLOCK and turning off Chrome settings. Then, **YOU MUST RETURN TO UBLOCK'S CHROME WEBSTORE PAGE**. Sorry, but the code will crash if the web store page is closed.

6.) For some reason, the slideshow downloader acts funny, so most of the time it won't download the specified slideshows. In case this happens, the Python console prints out the slideshows so that you can copy and download them manually. Sorry, I'm only a beginner dev. I don't know how to solve many issues :(


Notes from the dev: Hello :3! I'm a noob dev trying to build my experience by creating useless projects. I've always wanted to download videos I saved on tiktok, so I decided to try to do that for the first time. This project is more so for me, as it has many flaws and is annoying to use, but feel free to try it out and tell me it sucks. I _probably_ won't be updating it anymore as it does its job (at least for me) so sorry if the code no longer works. If you want to improve this project, feel free to copy the code! Just put me in the credits or tag me. I'd love to see someone more experienced fix my code. I'll definitely check out your project too, so that I can learn a thing or two about writing efficient and readable code.

If many people request it, I can possibly change the crappy code to download LIKED videos too. Note: The program doesn't selectively install videos, it installs ALL videos IN ORDER until it reaches the "Stop link". If you want me to explain what the code does simply, I'll update this page.

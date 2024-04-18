import selenium.common
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

login_type = input("How would you like to login? 'phone' or 'email'? \n P.S this data isn't stored anywhere and you'll have to renter it every time.")


DESIRED_WEB_LOCATION = input("Paste full http Link to your tiktok account page.")
DOWNLOADS_FOLDER = input("Paste your FULL desired download path.")

chrome_options = Options()
# Specify the download directory
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": DOWNLOADS_FOLDER,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


#TODO: Install ublock origin
driver.get("https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm")
if input(f"Install Ublock origin pls. :3 \n Once you're done, Simply type in 'yes'.").lower() == "yes":
    driver.switch_to.new_window('tab')

else:
    input("It won't work without it :( \n The pop-up ads will crash the code... pls install it.")
    driver.switch_to.new_window('tab')
# Opens website and waits to load all the elements so that the login sequence can begin
driver.get(DESIRED_WEB_LOCATION)
driver.implicitly_wait(10)


# Clicks on the "login with phone" option, since all others redirect to a diff website.
input("please reload the website if it hasn't loaded (this only affects poor wifi). If it already has, then simply press enter.")
login_page = driver.find_element(By.XPATH, value='//*[@id="loginContainer"]/div/div/div[1]/div[2]/div[2]')
login_page.click()
driver.implicitly_wait(5)

if login_type == "phone":
    # Locates the text input boxes for later, so that the phone number and code can be inputted.
    enter_phone_number = driver.find_element(By.NAME, value='mobile')
    driver.implicitly_wait(3)
    enter_code = driver.find_element(By.XPATH,
                                     value='/html/body/div[5]/div[3]/div/div/div/div[1]/div/form/div[3]/div/div/input')

    # Enters phone number and waits
    PHONE_NUMBER = input(
        "Please enter your phone number. If you don't live in the US, please manually change the +1 to the correct option. Sorry.")
    enter_phone_number.click()
    enter_phone_number.send_keys(PHONE_NUMBER)
    driver.implicitly_wait(3)

    phone_login_type = input("Would you like to login with 'password' or 'sms' code?").lower()
    if phone_login_type == 'sms':
        # Sends SMS code to PHONENUMBER to verify identity, along with waiting for the code to be inputted.
        driver.find_element(By.XPATH, value='//*[@id="loginContainer"]/div/form/div[3]/div/button').click()
        inputted_code = input("Enter Code sent here (You have 30 seconds minimum):")
        driver.implicitly_wait(60)

        # Enters the code provided and presses continue
        enter_code.click()
        enter_code.send_keys(inputted_code)
        driver.implicitly_wait(5)

    elif phone_login_type == "password":
        driver.find_element(By.XPATH, value='//*[@id="loginContainer"]/div[2]/form/a').click()
        driver.implicitly_wait(50)
        enter_pass = driver.find_element(By.XPATH, value='//*[@id="loginContainer"]/div[2]/form/div[3]/div/input')
        phone_password = input("Please enter your password. THIS IS NOT SAVED ON ANYWHERE AND IS RAN LOCALLY.")
        enter_pass.send_keys(phone_password)
        driver.implicitly_wait(30)

elif login_type == "email":
    driver.find_element(By.XPATH, value='//*[@id="loginContainer"]/div/form/div[1]/a').click()
    email_user = driver.find_element(By.XPATH, value='//*[@id="loginContainer"]/div[2]/form/div[1]/input')
    enter_pass = driver.find_element(By.XPATH, value='//*[@id="loginContainer"]/div[2]/form/div[2]/div/input')
    email_user.send_keys(input("Please enter your username/email."))
    enter_pass.send_keys(input("Please enter your password. THIS DATA IS NOT STORED ANYWHERE AND WILL NEED TO BE RENTERED AGAIN."))
    time.sleep(5)

# Clicks on the login button.
login_button = driver.find_element(By.XPATH, value='//*[@id="loginContainer"]/div/form/button')
login_button.click()
driver.implicitly_wait(30)

#Opens FAV tab
##TODO: This will probably make an error, all code below wasn't checked.

if input("Press close on the pop up window blocking the favorites bar? ('yes' or 'no' only").lower() == 'yes':
    print("Confirmed. Attempting to click on the favorites bar...")
    driver.implicitly_wait(20)
else:
    input("Press close on the pop up window blocking the favorites bar.")
favorites_tab = driver.find_element(By.XPATH, value='//*[@id="main-content-others_homepage"]/div/div[2]/div/p[2]')
try:
    favorites_tab.click()
    print("First click attempted.")
except selenium.common.exceptions.StaleElementReferenceException:
    favorites_tab.click()
    favorites_tab.click()
else:
    driver.implicitly_wait(30)

# TODO: This link/value will possibly change, so just a heads up for future vids
# Opens first video?

x_coordinate = 350
y_coordinate = 430

# Create an ActionChains object
actions = ActionChains(driver)

# Move the mouse to the specified coordinates and click
actions.move_by_offset(x_coordinate, y_coordinate).click().perform()

driver.implicitly_wait(20)



# Gets current url and saves it to a variable, so that it can be posted later.
all_urls = []

# TODO: This part will probably be the one automated, so it should be separate from everything else.
# TODO: Ask the user at what video would they like the downloading/copying to stop and save it to "STOP_LINK" , otherwise this thing will probably install their entire favorited fyp *skull*
STOP_LINK = input("IMPORTANT: Go to the video at which you want the downloading to stop at, and COPY ITS FULL FULL LINK/URL. After you copied it, Paste here:")


# TODO: Make it press the down button/arrow to go to the next video.
next_button = driver.find_element(By.XPATH, value='//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]')


# TODO: HELLA IMPORTANT!!!!!!!!!!!!! Copy link again and CHECK IF THE LINK MATCHES THE "STOP_LINK". Otherwise, save it to "all_urls"
current_link = driver.current_url
all_urls.append(current_link)
# Counts amount of links copied, so that you know how many vids you'll get.
amount_of_Links = 1


# This is the automated process of copying links and adding them to a list, so that they can be ctrl v into a downloader.
condition = True
while condition:
    input("Most of the time TiktoK will put a capcha on the first or so video. Mess around until you get the captcha and complete it. DO NOT proceed until a captcha pops up. Otherwise, the code will crash.")
    time.sleep(10)
    driver.implicitly_wait(100)
    next_button = driver.find_element(By.XPATH, value='//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]')
    driver.implicitly_wait(100)
    next_button.click()
    driver.implicitly_wait(20)
    current_link = driver.current_url
    if current_link == STOP_LINK:
        all_urls.append(STOP_LINK)
        print("You have reached the current video specified.")
        print(f"{amount_of_Links} Links copied.")
        condition = False
        break
    else:
        print(f"Current video downloaded. aka: {current_link}")
        all_urls.append(current_link)
        amount_of_Links += 1
print(all_urls)

driver.switch_to.new_window('tab')
driver.get("https://ssstik.io/en")

contains_slideshow = [x for x in all_urls if "photo" in x]
all_urls = [item for item in all_urls if item not in contains_slideshow]

paste_link_here = driver.find_element(By.XPATH, value='//*[@id="main_page_text"]')
submit_button = driver.find_element(By.XPATH, value='//*[@id="submit"]')


videos_downloaded = 0
if input("Did you close the pop-up? (yes or no only").lower() == 'yes':
    print("Thanks :3")
else:
    driver.implicitly_wait(10)

input("Hopefully everything is working so far, please press enter.")
print(all_urls)
print(contains_slideshow)
for link_selected in range(0, len(all_urls)):
    time.sleep(15)
    paste_link_here = driver.find_element(By.XPATH, value='//*[@id="main_page_text"]')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="submit"]')
    paste_link_here.send_keys(all_urls[link_selected])
    submit_button.click()
    time.sleep(5)
    driver.implicitly_wait(10)
    download_button = driver.find_element(By.XPATH, value='//*[@id="dl_btns"]/a[1]')
    download_button.click()
    videos_downloaded += 1
    time.sleep(5)
    driver.implicitly_wait(100)
    driver.find_element(By.XPATH, value='//*[@id="ad-vignette-footer"]/button').click()
    driver.implicitly_wait(100)
    menu_button = driver.find_element(By.XPATH, value='//*[@id="sss_body"]/header/div/div/a/div')
    menu_button.click()

print(contains_slideshow)

for link_selecteds in range(0, len(contains_slideshow)):
    print(link_selecteds)
    print(contains_slideshow[link_selecteds])
    time.sleep(10)
    paste_link_here = driver.find_element(By.XPATH, value='//*[@id="main_page_text"]')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="submit"]')
    paste_link_here.click()
    paste_link_here.send_keys(contains_slideshow[link_selecteds])
    time.sleep(5)
    submit_button.click()
    driver.implicitly_wait(20)
    time.sleep(5)
    generate_slides = driver.find_element(By.XPATH, value='//*[@id="slides_generate"]')
    generate_slides.click()
    time.sleep(20)
    driver.implicitly_wait(30)
    videos_downloaded += 1
    menu_button = driver.find_element(By.XPATH, value='//*[@id="sss_body"]/header/div/div/a/div')
    menu_button.click()


if input(f"{videos_downloaded} Videos/Slideshows installed. Is this the correct amount?").lower() == 'yes':
    print("Thanks for using my crappy software.")
    driver.quit()
else:
    input("Error occurred. :(")

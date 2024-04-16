import schedule
import time
import random
import pywhatkit as kit
import pyautogui

phone_number = "+code-phone numebr"
message = ["Babu. Padh dherai time xaina","Padi rahaxas ni tah?","Mobile dherai na chala!","time is passing but are you?","Fail hune bichar xa??","kyu nahi horahi padai?"]

# Function to send WhatsApp message
def send_whatsapp_message():
    n = random.randint(0, len(message) - 1)
    print("Sending WhatsApp message...")
    
    kit.sendwhatmsg(phone_number, message[n])
    time.sleep(10)  # Adding a delay to give time for WhatsApp to open
    pyautogui.press('enter')  # Simulating 'Enter' key to send the message

# Schedule the message to be sent every 30 minutes
schedule.every(1).minutes.do(send_whatsapp_message)

# Keep the program running
while True:
    print("Code is running...")
    time.sleep(1)

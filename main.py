import pyautogui
import time

# type your message below
message = "Replace Your Message with this text"
n = 200  # replace '200' with the number of times you want to send the message

print("START")
count = 5
while (count != 0):
    time.sleep(1)
    count -= 1
print("\n COMPLETE")

for i in range(0, int(n)):
    pyautogui.typewrite(message + '\n')

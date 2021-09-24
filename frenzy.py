import pyautogui
import time
import mouse
import keyboard
import win32api, win32con


def click(x, y):
	win32api.SetCursorPos((x, y))
	lmb()

def lmb():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(0.005)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def main():
	while not keyboard.is_pressed('q'):
		while keyboard.is_pressed('p'):
			pic = pyautogui.screenshot(region=(740, 340, 430, 430))
			width, height = pic.size
			jump = 135
			
			for x in range(0, width, jump):

				for y in range(0, height, jump):

					R, G, B = pic.getpixel((x, y))

					if R in range(10) and G in range(10) and B in range(10):
						click(x + 740, y + 340)
						break

				else:
					continue

				break

			# time.sleep(0.2)
			# uncomment the line before if the bot starts clicking on white tiles
			# you can adjust the delay for your liking

main()


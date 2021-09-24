import pyautogui
import time
import mouse
import keyboard
import win32api, win32con


# region=(629, 233, 645, 645)


def click(x, y):
	win32api.SetCursorPos((x, y))
	# moveCursor((x, y))
	lmb()

def lmb():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(0.005)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def moveCursor(pos, delay=0):

	curr_pos = win32api.GetCursorPos()
	x = pos[0] - curr_pos[0]
	y = pos[1] - curr_pos[1]

	x_dir = 1
	y_dir = 1

	x_neg = str(x).startswith('-')
	y_neg = str(y).startswith('-')

	if x_neg:
		x_dir = -1

	if y_neg:
		y_dir = -1

	# x axis
	for x_ in range(curr_pos[0], pos[0], x_dir):
		win32api.SetCursorPos((x_, curr_pos[1]))
		time.sleep(delay)



	curr_pos = win32api.GetCursorPos()

	# y axis
	for y_ in range(curr_pos[1], pos[1], y_dir):
		win32api.SetCursorPos((curr_pos[0], y_))
		time.sleep(delay)


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

main()


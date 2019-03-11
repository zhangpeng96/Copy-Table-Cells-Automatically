import pyperclip
import keyboard
from prettytable import PrettyTable
import os, csv, time
import win32con 
import win32api

def clc():
    os.system("cls")

def pasteWin32():
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(86,0,0,0)
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

def counter(pointer, lcol):
    row = pointer['row']
    col = pointer['col']

    if (col+1) >= lcol:
        row = row + 1
        col = 0
    else:
        col = col + 1
    pointer = {'row': row, 'col': col}

    return pointer


def trigger():
    global pointer, lines
    if pointer['col'] == 0:
        x = PrettyTable(["**持续时长**", "开始时间", "文本"])
        x.add_row(lines[pointer['row']].values())
    elif pointer['col'] == 1:
        x = PrettyTable(["持续时长", "**开始时间**", "文本"])
        x.add_row(lines[pointer['row']].values())
    elif pointer['col'] == 2:
        x = PrettyTable(["持续时长", "开始时间", "**文本**"])
        x.add_row(lines[pointer['row']].values())
    else:
        x = PrettyTable(["持续时长", "开始时间", "文本"])
    
    copyText = list(lines[pointer['row']].values())[pointer['col']]
    pyperclip.copy(copyText)
    clc()
    print(x)
    print(copyText)
    pasteWin32()
    pointer = counter(pointer, 3)
    time.sleep(0.5)



if __name__ == '__main__':
    
    lines = []
    pointer = {'row': 0, 'col': 0}

    with open('snh48.csv','r',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row)
            lines.append(row)


    print('输入热键：')
    shortcut = keyboard.read_hotkey()
    print('热键为：', shortcut)

    keyboard.add_hotkey(shortcut, trigger)

    print("按 ESC 退出")
    keyboard.wait('esc')

# for line in lines:

#     # print(line['length'] + '\t' + line['start'])
#     print(x)
#
#     






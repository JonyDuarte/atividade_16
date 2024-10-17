# importar a biblioteca de automação
# há necessidade de instalação 'pip install pyautogui'
import pyautogui as auto

auto.PAUSE = 0.5

auto.press("win")
auto.write("edge")
auto.press("enter")
auto.write("python.org")
auto.press("enter")
auto.hotkey("alt","space")
auto.press("x")
auto.hotkey("ctrl", "t")
auto.write("google.com.br")
auto.press("enter")
auto.write("Logo Python")
auto.press("enter")

for i  in range(14):
    auto.press("tab")

auto.press("enter")


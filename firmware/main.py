import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.LED import LED

keyboard = KMKKeyboard()

# matrix
keyboard.row_pins = (board.D6, board.D2, board.D1, board.D3)
keyboard.col_pins = (board.D0, board.D9, board.D8, board.D7, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T,
        KC.A, KC.S, KC.D, KC.F, KC.G,
        KC.Z, KC.X, KC.C, KC.V, KC.B,
        KC.LCTRL, KC.GUI, KC.LALT, KC.SPACE, KC.RCTRL,
    ]
]

# 128x32 OLED display

keyboard.SCL = board.D5
keyboard.SDA = board.D4

display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[
        TextEntry(text="""
krunchpad 20
5x4 macropad
        """),
    ],
    height=32,
)
keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
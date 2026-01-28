import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.LED import LED
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
keyboard.modules.append(encoder_handler)

# matrix
keyboard.row_pins = (board.D6, board.D2, board.D1, board.D3)
keyboard.col_pins = (board.D0, board.D9, board.D8, board.D7, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.P0, KC.P1, KC.P4, KC.P7, KC.KC.NLCK,
        KC.P0, KC.P2, KC.P5, KC.P8, KC.PSLS,
        KC.PDOT, KC.P3, KC.P6, KC.P9, KC.PAST,
        KC.PENT, KC.PENT, KC.PPLS, KC.PPLS, KC.PMNS,
    ]
]

# volume knob
'''
encoder_handler.pins = ((board.D5, board.D4),)
encoder_handler.map = [
    ((KC.MW_DN, KC.MW_UP),), # Mouse wheel zooming
    ((KC.VOLD, KC.VOLU),),   # Volume control
    ]
'''

# 128x32 OLED display
'''
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
'''

if __name__ == '__main__':
    keyboard.go()

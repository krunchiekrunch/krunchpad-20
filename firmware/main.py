import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
# from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
macros = Macros()
mouse = MouseKeys()
# encoder_handler = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules.append(macros)
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())
# keyboard.modules.append(encoder_handler)
keyboard.modules.append(Layers())
keyboard.modules.append(tapdance)

# matrix
keyboard.row_pins = (board.D6, board.D2, board.D1, board.D3)
keyboard.col_pins = (board.D0, board.D9, board.D8, board.D7, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,
        KC.Q, KC.W, KC.E, KC.R, KC.T,
        KC.A, KC.S, KC.D, KC.F, KC.G,
        KC.Z, KC.X, KC.C, KC.V, KC.B,
    ]
]

# volume knob
'''
encoder_handler.pins = ((board.D5, board.D4),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),   # Volume control
    ]
'''

# 128x32 OLED display
display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[
        TextEntry(text="""
1 2 3 4 5
Q W E R T
A S D F G
        """),
    ],
    width=128,
    height=32,
    brightness=0.1,
)
keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
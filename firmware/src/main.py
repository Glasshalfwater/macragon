""" KMK firmware written for a hexagonal macropad controlled by a Waveshare RP2040-zero. 
Includes control of a RGB LED strip of SK6812MINI-Bs, and 
multiple keyboard layers that the LEDs are synced to, and
the ability to toggle between them"""

import board  

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Key
from kmk.scanners import DiodeOrientation
from kmk.scanners import MatrixScanner
from kmk.modules.macros import Macros, Press, Release, Delay, Tap
from kmk.modules.tapdance import TapDance
from kmk.modules.layers import Layers
from kmk.extensions.rgb import RGB 
  
NUM_LEDS = 7, 

RGB_CHAIN_HEAD_PIN = board.GP6
BIT_CLOCK_PIN = board.GP9
WORD_SELECT_PIN = board.GP10
DATA_IN_PIN = board.GP11
 
layers_module = Layers()

keyboard = KMKKeyboard()
keyboard.modules.append(Macros())
keyboard.modules.append(TapDance())
keyboard.modules.append(Layers())

col_pins = (board.GP1, board.GP3, board.GP5)
row_pins = (board.GP0, board.GP2, board.GP4)

diode_orientation = DiodeOrientation.ROW2COL


class LayerColor(RGB):
    def set_light_layer(self, layer):
        if layer == 0:
            self.set_animation(3)
        elif layer == 1:
            self.set_hsv_fill(109, 135, 186) # Onshape's green color

rgb = LayerColor(
    RGB_CHAIN_HEAD_PIN, 
    NUM_LEDS,  
    val_default = 150
    )

keyboard.extensions.append(rgb)

class ColorLayers(Layers):
    def activate_color_layer(self, keyboard, layer, idx=None):
        super().activate_layer(keyboard, layer, idx)
        rgb.set_light_layer(layer)
    
    def deactivate_color_layer(self, keyboard, layer):
        super().deactivate_layer(keyboard, layer)
        rgb.set_light_layer(keyboard.active_layers[0])

keyboard.modules.append(ColorLayers())

rgb_layers = ColorLayers(Layers())


# Onshape commands

# Macro to open whatever programs you might need for work, currently setup for a current fallout workflow
WORK_SETUP_INIT = KC.MACRO(
    # Web Tabs
    Press(KC.LGUI),
    Press(KC.S),
    Release(KC.LGUI),
    Release(KC.S),
    Tap("Firefox"),
    Tap(KC.ENTER),
    Delay(500), # Adjust if starts skipping steps?
    Tap(KC.LCTL(KC.T)),
    Tap("cvilleschools.onshape.com"),
    Tap(KC.ENTER),
    Delay(100),
    Tap(KC.LCTL(KC.T)),
    Tap("mail.google.com"),
    Tap(KC.ENTER),
    Delay(100),
    Tap(KC.LCTL(KC.T)),
    Tap("fallout.hackclub.com"),
    Tap(KC.ENTER),
    Delay(100),
    
    #Tap(KC.LCTL(KC.T)),
    #insert onelogin if necessary

    # CAD
    Tap(KC.ENTER),
    Press(KC.LGUI),
    Press(KC.S),
    Release(KC.LGUI),
    Release(KC.S),
    Tap("EasyEDA Pro"),
    Tap(KC.ENTER),
    
    # Software, IDE's etc.
    Press(KC.LGUI),
    Press(KC.S),
    Release(KC.LGUI),
    Release(KC.S),
    Tap("Visual Studio Code")
    )

DEFAULT_SETUP_INIT = KC.MACRO(
    Press(KC.LGUI),
    Press(KC.S),
    Release(KC.LGUI),
    Release(KC.S),
    Tap("Google Chrome"), # Ensure that will actually load into a browser w/ search bar open at start
    Tap(KC.ENTER),
    Delay(500),
    Tap("https://www.youtube.com/watch?v=2qBlE2-WL60"), # Placeholder, albeit might forget to tell friends, convieniently ad-free. Can be replaced w/ cute cat vids link
    Tap(KC.ENTER)
)

# RGB Color Layer Control Macro
LAYER_INCREMENT = KC.MACRO(
    rgb_layers.deactivate_color_layer(keyboard.active_layers[0]),
    KC.TG(keyboard.active_layers[0] + 1),
    rgb_layers.activate_color_layer(keyboard.active_layers[0] + 1)
)

LAYER_DECREMENT = KC.MACRO(
    rgb_layers.deactivate_color_layer(keyboard.active_layers[0]),
    KC.TG(keyboard.active_layers[0] - 1),
    rgb_layers.activate_color_layer(keyboard.active_layers[0] - 1)
)

# Microphone code sadly disabled until next iteration, because currently I don't think circuitpython can output usb audio to Windows
"""
def activate_microphone():
    # Insert  circuitpython interaction code for mic
    mic = pio_i2s.I2S()
"""

# Button configs, KC.NO s are because of hexagon layout, t = top, b = bottom, l/m/r indicates left/middle/right
# DEFAULT LAYER
button_tl_zero = KC.LEFT
button_tm_zero = KC.UP
button_tr_zero = KC.RIGHT
button_ml_zero = KC.LCTL(KC.LSHIFT(KC.LEFT))
button_m_zero = KC.TD(KC.RGB_MOD, LAYER_INCREMENT)
button_mr_zero = KC.LCTL(KC.LSHIFT(KC.LEFT))
button_bm_zero = KC.DOWN

# ONSHAPE LAYER
button_tl_one = KC.LSHIFT(KC.A) # Rebound to central point arc
button_tm_one = KC.LSHIFT(KC.ENTER) # End current mate and start new one
button_tr_one = KC.LCTL(KC.LSHIFT(KC.H)) # H for Hexagon, rebound to polygon tool
button_ml_one = KC.LCTL(KC.LSHIFT(KC.L)) # Rebound to slot tool
button_m_one = KC.TD(LAYER_DECREMENT, DEFAULT_SETUP_INIT, WORK_SETUP_INIT)
button_mr_one = KC.LSHIFT(KC.M) # Rebound to mirror
button_bm_one = KC.LCTRL(KC.LSHIFT(KC.Y)) # Rebound to symmetric

keyboard.keymap = [
    # Default Layer (0)
    [   
        button_tl_zero, button_tm_zero, button_tr_zero,
        button_ml_zero, button_m_zero, button_mr_zero,
        KC.NO, button_bm_zero, KC.NO
    ],
    # Onshape Layer (1)
    [
        button_tl_one, button_tm_one, button_tr_one,
        button_ml_one, button_m_one, button_mr_one,
        KC.NO, button_bm_one,KC.NO
    ]
]

if __name__ == '__main__':
    keyboard.go()
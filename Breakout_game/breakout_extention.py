from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from breakoutgraphics import BreakoutGraphics

INITIAL_Y_SPEED = 7.0
GIFT_WIDTH = 5
GIFT_HEIGHT = 5

class Breakout_Extention():
    def __init__(self, gift_width = GIFT_WIDTH, gift_height = GIFT_HEIGHT):
        # 先啟動super class
        super().__init__()
        self.box = GRect(gift_width, gift_height)
        self.box.filled = True


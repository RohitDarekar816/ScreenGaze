#!/usr/bin/env python3
"""Test the improved UI rendering."""
import cv2
import numpy as np
import sys
sys.path.insert(0, '/home/rohit/learn/ScreenGaze')
from face_tracker import _draw_text_panel, _center_window

# Create test window
window_name = "ScreenGaze — Setup (Test)"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
cv2.resizeWindow(window_name, 900, 650)

# Center window
from screeninfo import get_monitors
monitors = list(get_monitors())
if monitors:
    primary = monitors[0]
    x = primary.x + (primary.width - 900) // 2
    y = primary.y + (primary.height - 650) // 2
    cv2.moveWindow(window_name, x, y)

# Test the setup screen
lines = [
    "C   Calibrate now (map your face to each screen)",
    "S   Use saved calibration",
    "D   Defaults (no calibration)",
    "ESC   Exit",
]

print("Showing improved UI test...")
print("Press 'q' to quit")

while True:
    # Create black background
    frame = np.zeros((650, 900, 3), dtype=np.uint8)
    
    # Draw the text panel
    _draw_text_panel(frame, lines, y_start=150, line_height=65, font_scale=1.0, thickness=2, title="ScreenGaze Setup")
    
    # Show frame
    cv2.imshow(window_name, frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
print("Test complete!")

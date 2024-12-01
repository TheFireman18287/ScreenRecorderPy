import mss
import numpy as np
import cv2
import pyautogui

def main():
    # Initialize MSS for screen capture
    sct = mss.mss()

    # Define the monitor to capture (primary monitor in this case)
    monitor = sct.monitors[1]  # Change to other indices if needed

    while True:
        # Capture the screen
        screenshot = sct.grab(monitor)

        # Convert the image to a NumPy array
        frame = np.array(screenshot, dtype=np.uint8)

        # Convert BGRA to BGR (remove alpha channel for OpenCV display)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        # Get the cursor position
        cursor_x, cursor_y = pyautogui.position()

        # Draw the cursor on the frame (adjust for monitor offset if needed)
        cursor_size = 10
        cursor_color = (0, 0, 255)  # Red
        cv2.circle(frame, (cursor_x, cursor_y), cursor_size, cursor_color, -1)

        # Display the frame in a window
        cv2.imshow("Live Screen Feed with Cursor", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup OpenCV resources
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

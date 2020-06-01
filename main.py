#!/usr/bin/env python3
# Project: prisec (privacy securer)
# Author: Pooya Shams kolahi

import os
import cv2
import numpy as np

# settings
# camera_index = 0
camera_index = "http://192.168.1.3:4747/mjpegfeed"
show_window = False
FPS = 3
number_of_frames_to_focus = 50
time_stamp_height = 10
blur_kernel_width = 17
blur_kernel_height = 17
exit_keys = [ord('q'), 27]
window_name = "AntiSPY!"

# hyper parameters (for my own fucking room)
lower = np.array([20, 20, 20])
upper = np.array([255, 255, 255])
dilations = 8
erosions = 4


def do_job():
    """ does whatever it should do whenever someone enters the room """
    os.system("xdotool keydown ctrl+alt keydown Down keyup ctrl+alt keyup Down")
    os.system("playerctl pause")
    os.system("amixer set Master mute > /dev/null 2> /dev/null")
    print("donejob")


def filter_frame(frame):
    frame = frame[time_stamp_height:, :, :]
    frame = cv2.GaussianBlur(frame, (blur_kernel_width, blur_kernel_height), 0)
    return frame


def one_loop(cap, first_frame):
    key = cv2.waitKey(FPS)

    if key in exit_keys:
        return False

    _, main_frame = cap.read()
    if main_frame is None:
        return False
    frame = filter_frame(main_frame)

    diff = cv2.absdiff(first_frame, frame)

    bin_img = cv2.inRange(diff, lower, upper)

    bin_img = cv2.dilate(bin_img, None, iterations=dilations)
    bin_img = cv2.erode(bin_img, None, iterations=erosions)

    cnts, _ = cv2.findContours(
        bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if show_window:
        cv2.imshow(window_name, bin_img)

    if len(cnts) > 0:
        return False

    return True


def mainloop(cap, first_frame):
    running = True
    while running:
        running = one_loop(cap, first_frame)


def main():
    try:
        cap = cv2.VideoCapture(camera_index)
        _, frame = cap.read()
        first_frame = frame
        first_frame = filter_frame(frame)
        for _ in range(number_of_frames_to_focus):
            one_loop(cap, first_frame)
        cv2.waitKey(FPS)
        _, frame = cap.read()
        first_frame = frame
        first_frame = filter_frame(frame)
        print("running")
        cv2.waitKey(FPS)
        mainloop(cap, first_frame)

    except Exception as e:
        print(e)
        do_job()
        input("done")
        exit()

    do_job()
    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    main()

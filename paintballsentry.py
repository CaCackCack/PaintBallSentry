import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt

teams = argparse.ArgumentParser(prog="Paintball Sentry 0.0.3", usage="%(prog)s --e[color of enemy]", description="This is an early prototype of a program operating a Paintball Sentry gun. The software is still in pre-alpha and very limited, and its only current function is to detect a certain color out of a camera feed. If you have any suggestions, bugs to report, or anything, just send a message in the server! \n\n -ChipsAndIDip")
teams.add_argument("--e", type=str, default="blue", help="sentry will shoot on sight;options include [red, blue, green, yellow]")

color_protocol = teams.parse_args()


cap = cv2.VideoCapture(0)
colors = {"red":([3, 0, 40], [140, 51, 254]), "blue":([91, 39, 2], [246, 203, 124]), "yellow":([32, 165, 218], [102, 224, 240]),"green":([0, 32, 0],[74, 174, 49])}
if color_protocol.e not in colors:
    raise ValueError("Input provided was invalid; please use the command \"--h\" to see options.")
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    mask = cv2.inRange(frame, np.array(colors[color_protocol.e][0], dtype="uint8"), np.array(colors[color_protocol.e][1], dtype="uint8"))
    
    output = cv2.bitwise_and(frame, frame, mask=mask)
    final_output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(final_output, 30, 100)
    cv2.imshow("raw feed", frame)
    cv2.imshow("targeting", edges)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

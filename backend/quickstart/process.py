import os
import cv2
import glob
import sys
import numpy as np
from finger_gen.util import crop_fingertip
from finger_gen.util import preprocessing
# from finger_gen.edge_connect import main as generate_finger


def run(img_dir, test_dir, save_dir):
    finger_tips = crop_fingertip.get_fingertip(img_dir)

    if os.path.isfile(img_dir):
        original_img = cv2.imread(img_dir)

    for name in finger_tips.keys():
        items = finger_tips[name]
        count = 0

        if os.path.isdir(img_dir):
            original_img = cv2.imread(os.path.join(img_dir, name))

        original_img = cv2.flip(original_img, 1)
        for item in items:
            img, top_left, down_right = item
            img = cv2.resize(img, (256, 256))

            finger, mask = preprocessing.get_mask(img, 0.9)
            edge =  preprocessing.extract_edge(finger)
            enhanced =  preprocessing.Enhancement(edge, mask)

            img_name = "img.png"

            cv2.imwrite(os.path.join(test_dir, "img.png"), img)
            cv2.imwrite(os.path.join(test_dir, "mask.png"), mask)
            cv2.imwrite(os.path.join(test_dir, "edge.png"), enhanced)
            
            command = "python edge_connect/test.py --model 2 --checkpoints ../finger_gen/edge-connect/checkpoints  --input {test_dir}/{img_name}  --mask {test_dir}/mask.png --edge {test_dir}/edge.png  --output {output_dir}".format(
                output_dir=test_dir, img_name=img_name, test_dir=test_dir
            )
            os.system(command)

            changed = cv2.imread(os.path.join(test_dir, img_name))

            changed = cv2.resize(
                changed, (down_right[1] - top_left[1], down_right[0] - top_left[0])
            )

            original_img[
                top_left[1] : down_right[1], top_left[0] : down_right[0]
            ] = changed

        cv2.imwrite(
            save_dir,
            original_img,
        )


if __name__ == "__main__":

    run(r"C:\Users\rswfa\Documents\GitHub\FingerGen_Backend\backend\media\modified.png ",r"C:\Users\rswfa\Documents\GitHub\FingerGen_Backend\backend\media", r"C:\Users\rswfa\Documents\GitHub\FingerGen_Backend\backend\media\hohoho")
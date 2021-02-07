from pathlib import Path

class Config:
    # Dataset
    num_classes = 1
    MOT_root = r"E:\MOTChallenge\MOT20\train\MOT20-01\"
    MOT_images = MOT_root + "img1"
    MOT_label = MOT_root + "gt"

    
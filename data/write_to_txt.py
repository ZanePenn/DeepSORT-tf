## convert MOT2020 to a single txt file for trainning (VOC style: MOT tlwh to VOC xyxy)
import sys
sys.path.append("..")

import pathlib
import configuration as Config

MOT_root = pathlib.Path(Config.MOT_root_train)
with open(Config.txt_train_data, 'wt') as f:
    for dir in MOT_root.iterdir():
        img_path = dir / "img1"
        

        for one_image in img_path.glob("*"):
            print("Converting: {}".format(one_image))
            one_image_id = one_image.name.lstrip("0")[:-4]
            det_file = dir / 'det' / 'det.txt'

            file_ID = str(dir)[-2:]
            if file_ID == '01' or file_ID == '02':
                bboxes_for_one_image = str(one_image) + " 1920 1080"
            elif file_ID =='03':
                bboxes_for_one_image = str(one_image) + " 1173 880"
            else:
                bboxes_for_one_image = str(one_image) + " 1654 1080"

            for line in det_file.open():
                frameID = line.split(',')[0]
                if int(frameID) == int(one_image_id):
                    bbox_tlwh = line.split(',')[2:6]
                    bbox_xyxy = [float(bbox_tlwh[0]), float(bbox_tlwh[1]), float(bbox_tlwh[0])+float(bbox_tlwh[2]), float(bbox_tlwh[1]) + float(bbox_tlwh[3])]
                    bbox_xyxy = " ".join(str(x) for x in bbox_xyxy) + " 0"
                    bbox_xyxy = " " + bbox_xyxy
                    bboxes_for_one_image += bbox_xyxy

            f.write(bboxes_for_one_image)
            f.write('\n')
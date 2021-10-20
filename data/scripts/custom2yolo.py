import os
import json

print(os.getcwd())
train_path = "../../../data/custom_glomerulus/train"
test_path = "../../../data/custom_glomerulus/test"
label_id = {
    "normal": 0,
    "yellow": 1,
    "black": 2,
    "green": 3,
    "blue": 4,
    "darkblue": 5,
    "red": 6,
}

train_gt = sorted(os.listdir(os.path.join(train_path, "jsons")))
test_gt = sorted(os.listdir(os.path.join(test_path, "jsons")))

for i in range(len(train_gt)):
    with open(os.path.join(train_path, "jsons", train_gt[i])) as f:
        annos = json.load(f)

    img_h = annos["imageHeight"]
    img_w = annos["imageWidth"]
    objs = []

    for anno in annos["shapes"]:
        label = label_id.get(anno["label"])
        x_centre = (anno["points"][0][0] + anno["points"][1][0]) / 2 / img_w
        y_centre = (anno["points"][0][1] + anno["points"][1][1]) / 2 / img_h
        width = (anno["points"][1][0] - anno["points"][0][0]) / img_w
        height = (anno["points"][1][1] - anno["points"][0][1]) / img_h
        
        objs.append([label, x_centre, y_centre, width, height])

    file_name = train_gt[i].split(".")[0] + ".txt"
    with open(os.path.join(train_path, "labels", file_name), "w") as f:
        objs = [" ".join([str(i) for i in obj]) for obj in objs]
        f.write("\n".join(objs))

for i in range(len(test_gt)):
    with open(os.path.join(test_path, "jsons", test_gt[i])) as f:
        annos = json.load(f)

    img_h = annos["imageHeight"]
    img_w = annos["imageWidth"]
    objs = []

    for anno in annos["shapes"]:
        label = label_id.get(anno["label"])
        x_centre = (anno["points"][0][0] + anno["points"][1][0]) / 2 / img_w
        y_centre = (anno["points"][0][1] + anno["points"][1][1]) / 2 / img_h
        width = (anno["points"][1][0] - anno["points"][0][0]) / img_w
        height = (anno["points"][1][1] - anno["points"][0][1]) / img_h
        
        objs.append([label, x_centre, y_centre, width, height])

    file_name = test_gt[i].split(".")[0] + ".txt"
    with open(os.path.join(test_path, "labels", file_name), "w") as f:
        objs = [" ".join([str(i) for i in obj]) for obj in objs]
        f.write("\n".join(objs))
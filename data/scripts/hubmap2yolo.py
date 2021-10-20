import os
import json
import glob


root_path = "/mnt/HDD4/hwan/proj_detection/data/hubmap_1024_1024"
label_id = {
    "normal": 0,
}

imgs = glob.glob(os.path.join(root_path, 'train/images', '*.jpg'))
gts = glob.glob(os.path.join(root_path, 'train', '*.json'))

print(f"Begin coversion in {root_path}...")
for j in gts:
    with open(j) as f:
        annos = json.load(f)

    img_h = annos["image"][0]["height"]
    img_w = annos["image"][0]["width"]
    objs = []

    for anno in annos["annotations"]:
        label = 0
        x_centre = (anno["bbox"][0] + anno["bbox"][2]) / 2 / img_w
        y_centre = (anno["bbox"][1] + anno["bbox"][3]) / 2 / img_h
        width = (anno["bbox"][2] - anno["bbox"][0]) / img_w
        height = (anno["bbox"][3] - anno["bbox"][1]) / img_h
        
        objs.append([label, x_centre, y_centre, width, height])

    if not objs: continue
    file_name = annos["image"][0]["file_name"].split(".")[0] + ".txt"
    with open(os.path.join(root_path, "train/labels", file_name), "w") as f:
        objs = [" ".join([str(i) for i in obj]) for obj in objs]
        f.write("\n".join(objs))
print("conversion finished!")

val_file = "1e2425f28"
train_imgs = sorted(filter(lambda x: not x.split("/")[-1].startswith(val_file), imgs))
val_imgs = sorted(filter(lambda x: x.split("/")[-1].startswith(val_file), imgs))

print(f"write train/val img path... (id:{val_file})")
with open(os.path.join(root_path, "train", "train_imgs.txt"), "w") as f:
        f.write("\n".join(train_imgs))

with open(os.path.join(root_path, "train", "val_imgs.txt"), "w") as f:
        f.write("\n".join(val_imgs))
print(f"finish writing train/val img path!")
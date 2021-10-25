#!/bin/bash

python train.py --weights yolov5s.pt --data ./data/hubmap.yaml --img 640 --batch 64 --epochs 300 --device 1 --project ./runs/hubmap --name all_s_640

# python train.py --freeze 10 --weights yolov5s.pt --data ./data/hubmap.yaml --img 640 --batch 64 --epochs 50 --device 1 --project ./runs/hubmap --name 10_s_640

# python train.py --freeze 10 --weights yolov5s6.pt --data ./data/hubmap.yaml --img 1280 --batch 32 --epochs 50 --device 1 --project ./runs/hubmap --name 10_s_1280

# python train.py --freeze 24 --weights yolov5s.pt --data ./data/hubmap.yaml --img 640 --batch 64 --epochs 600 --device 1 --project ./runs/hubmap --name 24_s_640

# python train.py --freeze 24 --weights yolov5s6.pt --data ./data/hubmap.yaml --img 1280 --batch 32 --epochs 300 --device 1 --project ./runs/hubmap --name 24_s_1280

# python train.py --freeze 10 --weights yolov5x.pt --data ./data/hubmap.yaml --img 640 --batch 32 --epochs 50 --device 1 --project ./runs/hubmap --name 10_x_640
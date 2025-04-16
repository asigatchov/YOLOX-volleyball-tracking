#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        #self.data_dir = "/home/nssd/gled/vb/dataset-vb/backline/annotaned_ball_yolov8_dataset_v2_coco"
        self.data_dir = "annotaned_ball_yolov8_dataset_v2_coco"
        self.train_ann = "instances_train2017.json"
        self.val_ann = "instances_val2017.json"

        self.num_classes = 1

        self.max_epoch = 8
        self.data_num_workers = 6
        self.eval_interval = 1
        # увеличиваем размер входного изображения
        self.input_size = (1280, 1280)  # (height, width)
        self.test_size = (1280, 1280)  # (height, width)
        self.multiscale_range = 0

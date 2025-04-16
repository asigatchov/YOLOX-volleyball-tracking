#python3 -m yolox.tools.train -f exps/example/custom/yolox_s.py -b 4 --fp16 -o  -c yolox_s.pth   #YOLOX_outputs/yolox_s/epoch_196_ckpt.pth


python3 -m yolox.tools.train -f exps/example/custom/yolox_s.py -b 8 --fp16 -o  --resume -c yolox_s_ball.pth # YOLOX_outputs/yolox_s/latest_ckpt.pth 

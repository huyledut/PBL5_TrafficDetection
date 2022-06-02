# "PBL5_SignTrafficDetection" 
## Instalation

clone the repository:
```cmd
git clone https://github.com/huyledut/PBL5_TrafficDetection.git

cd PBL5_SignTrafficDetection

pip install -U -r requirements.txt
```
## Dataset
- [Dataset link](https://drive.google.com/drive/folders/1GlaC6t74RvjIMXXdYCn5DTwYtqwPjbIc?usp=sharing)
- Add train_data, test_data, best.pt to "PBL5_SignTrafficDetection"

## Configure
- Custom_data.yaml: Path train, val, test

## Train
```commandline
python train.py --img 640 --batch 16 --epochs 50 --data path'custom_data.yaml' --weights yolov5s.pt
```
## Inference
```commandline
python detect.py --weights path'best.pt' --source 0  # webcam
                          img.jpg  # image
                          vid.mp4  # video
                          path/  # directory
                          path/*.jpg  # glob
                          'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                          'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

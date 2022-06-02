
from statistics import mode
import cv2
import torch
import io
import socket
import struct
from PIL import Image
from _thread import *

def receive(connection): 
    connection_rb = connection.makefile('rb')
    while True:
        count_img =1
        cnn = connection_rb.read(4)
        if cnn != b'':
            image_len = struct.unpack('<L', cnn)[0]
            image_stream = io.BytesIO()
            image_stream.write(connection_rb.read(image_len))
            image_stream.seek(0)
            image = Image.open(image_stream)
            print('Receive image'+ str(count_img)+ ' size is %dx%d' % image.size)
            # path = 'images/image' + str(count_img) +'.jpeg'
            path = "images/picture.jpg"
            image.save(path)
            inference_image(connection)
            count_img +=1
        else:
            break
    connection_rb.close()

def send_message(connection, message):
    try:
        connection.send(message.encode('utf-8'))
    except Exception as e:
        print('Failed to do something: ' + str(e))    

def inference_image(connection):
    global model
    im1 = cv2.imread('images/picture.jpg')[..., ::-1]
    results = model(im1, 640)

    labels = results.pandas().xyxy[0]['name'].to_numpy()
    if len(labels) != 0 :
        message = ""
        for item in labels :
            message +="Bien bao: " + item +"\n"
        send_message(connection, message)
        print(message)
    else:
        print("don't detect")
    results.save()

if __name__ == '__main__':
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    
    # model = torch.hub.load('', 'custom', path='trained_models/custom_yolov5s.pt', source='local')
    model = torch.hub.load('', 'custom', path='trained_models/custom_yolov5n.pt', source='local')
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 9000))
    server_socket.listen(0)
    while True:
        connection = server_socket.accept()[0]
        start_new_thread(receive, (connection, ))





import cv2
from flask import Flask, Response

#(맥 기준으로)pip3 install opencv-python flask 명령어로 flask 설치
app=Flask(__name__)

camera = cv2.VideoCapture(0)
#카메라 장치 구별 



def jerry_doing():
    while True:
        success, frame = camera.read() #프래임 별로 캡쳐
        if not success:
            break
        else:
            ret, buffer  = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
#yield 쓰려 하는데 버퍼링 떄문에 늘어지면 다른걸로 바꾸자 !
            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n\ ' + frame + b'\r\n' )
            #프레임 영상으로 변경
def index():
    return "제리는 무엇을 하고 있을까?"
#서버명
def video_jerry():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


#서버 호스트 
if __nam__ == '__main__':
    app.run(host"127.0.0.1", port=1106)
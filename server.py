import cv2
from flask import Flask, Response

app=Flask(__name__)

camera = cv2.VideoCapture(0)



def jerry_doing():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer  = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
#yield 쓰려 하는데 버퍼링 떄문에 늘어지면 다른걸로 바꾸자 !
            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n\ ' + frame + b'\r\n' )
            
def index():
    return "제리는 무엇을 하고 있을까?"

def video_jerry():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host"127.0.0.1", port=1106)
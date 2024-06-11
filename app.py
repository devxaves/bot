from flask import Flask, request, render_template, send_file
import cv2
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    username = "Hi "+request.form['text']
    cap = cv2.VideoCapture('capture1.mp4')
    output_file = 'output.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (600, 400))
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.resize(frame, (600, 400))
        cv2.putText(frame, username, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
        out.write(frame)
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) 
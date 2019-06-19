from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/api/testApi', methods=['POST'])
def post():
    req = request
    npArr = np.fromstring(req.data, np.uint8)
    
    img = cv2.imdecode(npArr, cv2.IMREAD_COLOR)

    i=SessionCount()
    cv2.imwrite('C:/Users/TRU55/Desktop/Saved_Folder/ApiHandledCopys{}.jpg'.format(i),img)
    cv2.waitKey(0)
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    resp = jsonpickle.encode(response)

    return Response(response=resp, status=200, mimetype="application/json")

def SessionCount():
    with open("store.txt",'r') as sc: 
        a = sc.readlines()
    b = int(a[0])
    b = b+1
    with open("store.txt",'w') as sc:
        sc.write(str(b))
    return a[0]  

app.run(debug=True,host="0.0.0.0", port=5000)
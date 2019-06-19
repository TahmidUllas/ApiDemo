import requests
import json
import cv2

def post_Image():
	url = 'http://localhost:5000'
	test_url = url + '/api/testApi'
	content_type = 'image/jpeg'
	headers = {'content-type': content_type}
	images=['demo1.jpg','demo2.jpg','demo3.jpg']
	for i in range(len(images)):
		img = cv2.imread(images[i])
		_, img_encoded = cv2.imencode('.jpg', img)
		resp = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
		print(json.loads(resp.text))

post_Image()

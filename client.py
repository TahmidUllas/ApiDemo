import requests
import json
import cv2

def post_Image():
	url = 'http://localhost:5000'
	mailId=['example@Gmail.com','example@yahoo.com']  #Array of mail Id-s to mail the images to a specific user
	for item in mailId:	
		test_url = url + '/api/testApi/'+item  #endpoint with query param
		images=['fatbot.jpg']
		for i in range(len(images)):
			img = cv2.imread(images[i])
			_, img_encoded = cv2.imencode('.jpg', img)
			resp = requests.request(method='GET',url=test_url,data=img_encoded.tostring())  # to get response 
			print(json.loads(resp.text))

post_Image()

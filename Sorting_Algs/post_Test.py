import requests
import logging
import os

def postFile(filePath, postUrl):
    print("Posting the zip file to GDS as multipart request")
    fileName = os.path.basename(filePath)
    print('Handling request file path: %s and file name: %s', filePath, fileName)

    multipart_form_data = {
        'file': (fileName, open(filePath, 'rb')),
    }

    try:
        response = requests.post(postUrl, files=multipart_form_data, verify=False)
        print('Return response code: %s and response message: %s', response.status_code, response.text)
    except Exception:
        print("Exception occurred")

url = 'https://staging.itpt.its.com:8443/cos/ext/intf/fileprocessor?locationToUpload=/usr/local/itpt/ERP2/FromITS/PgsDisplayLocation/Data'

# fileLocation = r"C:\Users\tansari\Desktop\dummy\README.txt"
fileLocation = r"C:\Users\cdileepkumar\Desktop\Readme.txt"
postFile(fileLocation, url)

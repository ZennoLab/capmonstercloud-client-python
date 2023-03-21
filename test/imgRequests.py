import asyncio
import base64
import os
import unittest
import urllib

from capmonstercloudclient.requests import HcaptchaComplexImageTaskRequest, RecaptchaComplexImageTaskRequest
from capmonstercloudclient import CapMonsterClient, ClientOptions


def read_image(image_url: str,):
    image_bytes = urllib.request.urlopen(image_url).read()
    imageb64 = base64.b64encode(image_bytes).decode('utf-8')
    return imageb64

recaptcha_metadata = {
    "Task": "Click on traffic lights",
    "Grid": "3x3",
    "TaskDefinition": "/m/015qff"
    }
hcaptcha_metadata = {
    'Task': 'Please click each image containing a mountain'
    }

hcaptcha_img_urls = ["https://i.postimg.cc/kg71cbRt/image-1.jpg", 
                     "https://i.postimg.cc/6381Zx2j/image.jpg"] 
hcaptcha_images = []
for img_url in hcaptcha_img_urls:
    hcaptcha_images.append(read_image(img_url))


recaptcha_img_urls = ["https://i.postimg.cc/yYjg75Kv/payloadtraffic.jpg"]
recaptcha_images = []
for img_url in recaptcha_img_urls:
    recaptcha_images.append(read_image(img_url))

api_key = os.getenv('API_KEY')
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36."

class TestRequests(unittest.IsolatedAsyncioTestCase):
    
    def testSolvingHcaptchaWithUrls(self):
        fields = ['answer', 'metadata']
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options=options)
        request = HcaptchaComplexImageTaskRequest(metadata=hcaptcha_metadata,
                                                  imagesUrls=hcaptcha_img_urls,
                                                  userAgent=userAgent)
        result = asyncio.run(client.solve_captcha(request))
        keys = list(result.keys())
        for f in fields:
            self.assertTrue(f in keys)
        self.assertTrue(all([isinstance(x, bool) for x in result['answer']]))
        
    
    def testSolvingHcaptchaWithBase64(self):
        fields = ['answer', 'metadata']
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options=options)
        request = HcaptchaComplexImageTaskRequest(metadata=hcaptcha_metadata,
                                                  imagesBase64=hcaptcha_images)
        result = asyncio.run(client.solve_captcha(request))
        keys = list(result.keys())
        for f in fields:
            self.assertTrue(f in keys)
        self.assertTrue(all([isinstance(x, bool) for x in result['answer']]))
        
    
    def testSolvingRecaptchaWithUrls(self):
        fields = ['answer', 'metadata']
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options=options)
        request = RecaptchaComplexImageTaskRequest(metadata=recaptcha_metadata,
                                                   imagesUrls=recaptcha_img_urls,
                                                   userAgent=userAgent)
        result = asyncio.run(client.solve_captcha(request))
        keys = list(result.keys())
        for f in fields:
            self.assertTrue(f in keys)
        self.assertTrue(all([isinstance(x, bool) for x in result['answer']]))
    
    def testSolvingRecaptchaWithBase64(self):
        fields = ['answer', 'metadata']
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options=options)
        request = RecaptchaComplexImageTaskRequest(metadata=recaptcha_metadata,
                                                   imagesBase64=recaptcha_images)
        result = asyncio.run(client.solve_captcha(request))
        keys = list(result.keys())
        for f in fields:
            self.assertTrue(f in keys)
        self.assertTrue(all([isinstance(x, bool) for x in result['answer']]))

if __name__ == '__main__':
    unittest.main()
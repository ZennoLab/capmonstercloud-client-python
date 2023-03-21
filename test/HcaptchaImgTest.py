import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import HcaptchaComplexImageTaskRequest
from capmonstercloudclient.exceptions import NumbersImagesErrors, TaskNotDefinedError, ZeroImagesErrors, \
    UserAgentNotDefinedError

class HcaptchaImageRequestTest(unittest.TestCase):
    
    websiteUrlExample = 'https://lessons.zennolab.com/captchas/hcaptcha/?level=easy'
    imageUrlsExamples = ["https://i.postimg.cc/kg71cbRt/image-1.jpg", 
                         "https://i.postimg.cc/6381Zx2j/image.jpg"]
    metadataExample = {'Task': 'Please click each image containing a mountain'}
    
    def testImagesTypes(self):
        
        with self.assertRaises(ValidationError):
            request = HcaptchaComplexImageTaskRequest(websiteUrl=HcaptchaImageRequestTest.websiteUrlExample,
                                                      metadata=HcaptchaImageRequestTest.metadataExample,
                                                      imagesBase64='[]')
        
        with self.assertRaises(ValidationError):
            request = HcaptchaComplexImageTaskRequest(websiteUrl=HcaptchaImageRequestTest.websiteUrlExample,
                                                      metadata=HcaptchaImageRequestTest.metadataExample,
                                                      imagesUrls='[]',
                                                      userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.")
    
    def testImagesFilling(self):
        
        with self.assertRaises(ZeroImagesErrors, 
                               msg='Empty array imagesUrls must be cause ZeroImagesErrors'):
            request = HcaptchaComplexImageTaskRequest(websiteUrl=HcaptchaImageRequestTest.websiteUrlExample,
                                                      metadata=HcaptchaImageRequestTest.metadataExample,
                                                      imagesUrls=[],
                                                      userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.")
        
        with self.assertRaises(ZeroImagesErrors, 
                               msg='Empty array imagesBase64 must be cause ZeroImagesErrors'):
            request = HcaptchaComplexImageTaskRequest(websiteUrl=HcaptchaImageRequestTest.websiteUrlExample,
                                                      metadata=HcaptchaImageRequestTest.metadataExample,
                                                      imagesBase64=[])
        
        with self.assertRaises(ZeroImagesErrors, 
                               msg='Both empty arrays imagesBase64 and imagesUrls must be cause ZeroImagesErrors'):
            request = HcaptchaComplexImageTaskRequest(websiteUrl=HcaptchaImageRequestTest.websiteUrlExample,
                                                      metadata=HcaptchaImageRequestTest.metadataExample)
            request.getTaskDict()
        
    def testNumbersImages(self):
        
        with self.assertRaises(NumbersImagesErrors, 
                               msg='Empty array must be cause ZeroImagesErrors'):
            request = HcaptchaComplexImageTaskRequest(websiteUrl=HcaptchaImageRequestTest.websiteUrlExample,
                                                      metadata=HcaptchaImageRequestTest.metadataExample,
                                                      imagesUrls=HcaptchaImageRequestTest.imageUrlsExamples*20,
                                                      userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.")
        
        
        with self.assertRaises(NumbersImagesErrors, 
                               msg='Empty array must be cause ZeroImagesErrors'):
            request = HcaptchaComplexImageTaskRequest(websiteUrl=HcaptchaImageRequestTest.websiteUrlExample,
                                                      metadata=HcaptchaImageRequestTest.metadataExample,
                                                      imagesBase64=['base64image']*19)
        
    def testAllRequiredFieldsFilling(self):
        required_fields = ['class', 'type', 'websiteUrl', 'metadata']
        request = HcaptchaComplexImageTaskRequest(websiteUrl=HcaptchaImageRequestTest.websiteUrlExample,
                                                  metadata=HcaptchaImageRequestTest.metadataExample,
                                                  imagesUrls=HcaptchaImageRequestTest.imageUrlsExamples,
                                                  userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.")
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(i in list(request_dict.keys()), 
                            msg=f'Required field {i} not in {request_dict}')
            
    def testTaskDefined(self):
        with self.assertRaises(TaskNotDefinedError, 
                               msg='Expect that empty "Task" field will be cause TaskNotDefinedError'):
            request = HcaptchaComplexImageTaskRequest(imagesUrls=HcaptchaImageRequestTest.imageUrlsExamples,
                                                      metadata={},
                                                      userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.")
            
    def testUserAgentWithUrl(self):
        with self.assertRaises(UserAgentNotDefinedError):
            request = HcaptchaComplexImageTaskRequest(metadata=HcaptchaImageRequestTest.metadataExample,
                                                      imagesUrls=HcaptchaImageRequestTest.imageUrlsExamples)
            request.getTaskDict()
            
    def testSuccessRequestDict(self):
        required_fields = ['class', 'type', 'websiteUrl', 'metadata', 'imageUrls', 'userAgent']
        required_metadata = ['Task']
        request = HcaptchaComplexImageTaskRequest(metadata=HcaptchaImageRequestTest.metadataExample,
                                                  imagesUrls=HcaptchaImageRequestTest.imageUrlsExamples,
                                                  userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
                                                  websiteUrl=HcaptchaImageRequestTest.websiteUrlExample)
        body = request.getTaskDict()
        keys = list(body.keys())
        metadata_keys = list(body['metadata'].keys())
        
        for rf in required_fields:
            self.assertTrue(rf in keys)
        for rm in required_metadata:
            self.assertTrue(rm in metadata_keys)
            
        self.assertEqual(HcaptchaImageRequestTest.metadataExample[required_metadata[0]], 
                         body['metadata']['Task'])
        self.assertEqual(body['class'], 'hcaptcha')
        self.assertEqual(body['type'], 'ComplexImageTask')

if __name__ == '__main__':
    unittest.main()
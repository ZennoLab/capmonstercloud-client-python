import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import TenDiCustomTaskRequest
from capmonstercloudclient.exceptions import NumbersImagesErrors, TaskNotDefinedError, ZeroImagesErrors, \
    UserAgentNotDefinedError

class TenDiCustomTaskRequestTest(unittest.TestCase):
    
    websiteUrlExample = 'https://example.com'
    websiteKeyExample = '189123456'
    userAgentExample = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

    def testCaptchaInputTypes(self):
        
        with self.assertRaises(ValidationError):
            request = TenDiCustomTaskRequest(websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample)
        
        with self.assertRaises(ValidationError):
            request = TenDiCustomTaskRequest(
                                                websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
                                                )
        

        request = TenDiCustomTaskRequest(websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
                                                  websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
                                                  userAgent=TenDiCustomTaskRequestTest.userAgentExample
                                            )
    
    def testAllRequiredFieldsFilling(self):
        required_fields = ['class', 'type', 'websiteURL', 'websiteKey']
        request = TenDiCustomTaskRequest(websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
                                            websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample)
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(i in list(request_dict.keys()), 
                            msg=f'Required field {i} not in {request_dict}')

        self.assertEqual(request_dict['class'], 'TenDI')
        self.assertEqual(request_dict['type'], 'CustomTask')
            

if __name__ == '__main__':
    unittest.main()
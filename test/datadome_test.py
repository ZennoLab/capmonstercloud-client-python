import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import DataDomeCustomTaskProxylessRequest
from capmonstercloudclient.exceptions import NumbersImagesErrors, TaskNotDefinedError, ZeroImagesErrors, \
    UserAgentNotDefinedError

class DataDomeCustomTaskRequestTest(unittest.TestCase):
    
    websiteUrlExample = 'https://antoinevastel.com/bots/datadome'
    metadataExample =  {'captchaUrl': 'https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAJxx4dfgwjzwAQW0ctQ%3D%3D&hash=D66B23AC3F48A302A7654416846381&cid=d3k5rbDsu8cq0kmPHISS3hsC3f4qeL_K12~G33PrE4fbkmDYSul6l0Ze_aG5sUHLKG0676UpTv6GFvUgIActglZF33GTodOoRhEDkMMsuWTodlYa3YYQ9xKy9J89PAWh&t=fe&referer=https%3A%2F%2Fantoinevastel.com%2Fbots%2Fdatadome&s=21705&e=04fc682817ba89bf8fa4b18031fa53294fa0fb7449d95c036a1986413e6dfc7d',
                        'datadomeCookie': 'datadome=d3k5rbDsu8cq0kmPHISS3hsC3f4qeL_K12~G33PrE4fbkmDYSul6l0Ze_aG5sUHLKG0676UpTv6GFvUgIActglZF33GTodOoRhEDkMMsuWTodlYa3YYQ9xKy9J89PAWh'}
    
    def testCaptchaInputTypes(self):
        
        metadataListUrl = DataDomeCustomTaskRequestTest.metadataExample.copy()
        metadataListUrl['captchaUrl'] = list(metadataListUrl['captchaUrl'])

        metadataListImage = DataDomeCustomTaskRequestTest.metadataExample.copy()
        metadataListImage.pop('captchaUrl')
        metadataListImage['htmlPageBase64'] = metadataListUrl['captchaUrl']
        
        metadataListExtra = DataDomeCustomTaskRequestTest.metadataExample.copy()
        metadataListExtra['htmlPageBase64'] = metadataListExtra['captchaUrl']
        with self.assertRaises(ValidationError):
            request = DataDomeCustomTaskProxylessRequest(websiteUrl=DataDomeCustomTaskRequestTest.websiteUrlExample,
                                                metadata=metadataListUrl,
                                                )
        
        with self.assertRaises(ValidationError):
            request = DataDomeCustomTaskProxylessRequest(websiteUrl=DataDomeCustomTaskRequestTest.websiteUrlExample,
                                                metadata=metadataListImage,
                                                )
        
        with self.assertRaises(ValidationError):
            request = DataDomeCustomTaskProxylessRequest(websiteUrl=DataDomeCustomTaskRequestTest.websiteUrlExample,
                                                metadata=metadataListExtra,
                                                )
    
    def testAllRequiredFieldsFilling(self):
        required_fields = ['class', 'type', 'websiteURL', 'metadata']
        metadata_fields = ['datadomeCookie']
        one_of_fields = [['captchaUrl', 'htmlPageBase64']]
        request = DataDomeCustomTaskProxylessRequest(websiteUrl=DataDomeCustomTaskRequestTest.websiteUrlExample,
                                            metadata=DataDomeCustomTaskRequestTest.metadataExample)
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(i in list(request_dict.keys()), 
                            msg=f'Required field {i} not in {request_dict}')
            
        metadata_dict = request_dict['metadata']
        for i in metadata_fields:
            self.assertTrue(i in list(metadata_dict.keys()), 
                            msg=f'Required field {i} not in {request_dict}')

        for i in one_of_fields:
            self.assertTrue(len(set(i).intersection(metadata_dict.keys())) == 1)    

        self.assertEqual(request_dict['class'], 'DataDome')
        self.assertEqual(request_dict['type'], 'CustomTask')
            

if __name__ == '__main__':
    unittest.main()
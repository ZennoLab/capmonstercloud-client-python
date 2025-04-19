import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import AmazonWafRequest
from capmonstercloudclient.exceptions import NumbersImagesErrors, TaskNotDefinedError, ZeroImagesErrors, \
    UserAgentNotDefinedError

class AmazonWafRequestTest(unittest.TestCase):
    
    websiteUrlExample = 'https://example.com'
    websiteKeyExample = '189123456'
    challengeScriptExample = 'challenge_test'
    captchaScriptExample = '123'
    contextExample = 'context'
    ivExample = 'ivexample_`¬'

    def testCaptchaInputTypes(self):
        
        with self.assertRaises(ValidationError):
            request = AmazonWafRequest(websiteUrl=AmazonWafRequestTest.websiteUrlExample)
        
        with self.assertRaises(ValidationError):
            request = AmazonWafRequest(
                                                websiteKey=AmazonWafRequestTest.websiteKeyExample,
                                                )
        with self.assertRaises(ValidationError):
            request = AmazonWafRequest(websiteUrl=AmazonWafRequestTest.websiteUrlExample,
                                                        websiteKey=AmazonWafRequestTest.websiteKeyExample,
                                                        challengeScript=AmazonWafRequestTest.challengeScriptExample,
                                                        captchaScript=int(AmazonWafRequestTest.captchaScriptExample),
                                                        context=AmazonWafRequestTest.contextExample,
                                                        iv=AmazonWafRequestTest.ivExample
                                                        )
        

        request = AmazonWafRequest(websiteUrl=AmazonWafRequestTest.websiteUrlExample,
                                             websiteKey=AmazonWafRequestTest.websiteKeyExample,
                                             challengeScript=AmazonWafRequestTest.challengeScriptExample,
                                             captchaScript=AmazonWafRequestTest.captchaScriptExample,
                                             context=AmazonWafRequestTest.contextExample,
                                             iv=AmazonWafRequestTest.ivExample
                                            )
    
    def testAllRequiredFieldsFilling(self):
        required_fields = ['websiteURL', 'type', 'websiteKey', 'challengeScript', 'captchaScript',
                           'context', 'iv']
        request = AmazonWafRequest(websiteUrl=AmazonWafRequestTest.websiteUrlExample,
                                             websiteKey=AmazonWafRequestTest.websiteKeyExample,
                                             challengeScript=AmazonWafRequestTest.challengeScriptExample,
                                             captchaScript=AmazonWafRequestTest.captchaScriptExample,
                                             context=AmazonWafRequestTest.contextExample,
                                             iv=AmazonWafRequestTest.ivExample,
                                             cookieSolution=True
                                            )
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(i in list(request_dict.keys()), 
                            msg=f'Required field {i} not in {request_dict}')

        self.assertEqual(request_dict['type'], 'AmazonTaskProxyless')
            

if __name__ == '__main__':
    unittest.main()
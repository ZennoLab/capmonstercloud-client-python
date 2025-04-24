import unittest
from copy import deepcopy

from pydantic import ValidationError
from capmonstercloudclient.requests import ImpervaCustomTaskRequest


class ImpervaRequestTest(unittest.TestCase):
    
    websiteUrlExample = 'site.com'
    userAgentExample = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    incapsulaScriptUrlExample = 'dmFyIF8weGQ2ZmU9Wydce..eDUzXHg2YVx4NGYnKV09XzB4Mjk3MTIxO319KCkpOw=='
    incapsulaCookieExample = 'l/LsGnrvyB9lNhXI8borDKa2IGcAAAAAX0qAEHheCWuNDquzwb44cw='
    reese84UrlEndpointExample = "Built-with-the-For-hopence-Hurleysurfecting-the-"

    def test_imperva(self,
                       ):
        required_fields = ['type',
                           'websiteURL', 
                           'metadata']
        metadata_required_fields = ['incapsulaScriptUrl', 'incapsulaCookie']
        metadata_example = {"incapsulaScriptUrl": self.incapsulaScriptUrlExample,"incapsulaCookie": self.incapsulaCookieExample}
        request = ImpervaCustomTaskRequest(websiteUrl=self.websiteUrlExample, metadata=metadata_example)
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(f in list(task_dictionary.keys()), 
                            msg=f'Required captcha input key "{f}" does not include to request.')
        for f in metadata_required_fields:
            self.assertTrue(f in list(task_dictionary['metadata'].keys()), 
                            msg=f'Required captcha input key "{f}" does not include to request.')
    
    def test_imperva_metadata(self,):
        base_kwargs = {"websiteUrl": self.websiteUrlExample, "metadata": {}}
        self.assertRaises(TypeError, ImpervaCustomTaskRequest, **base_kwargs)
        base_kwargs['metadata']['incapsulaScriptUrl'] = self.incapsulaScriptUrlExample
        self.assertRaises(TypeError, ImpervaCustomTaskRequest, **base_kwargs)
        base_kwargs['metadata']['incapsulaCookie'] = self.incapsulaCookieExample
        ImpervaCustomTaskRequest(**base_kwargs)
        base_kwargs['metadata']['reese84UrlEndpoint'] = self.reese84UrlEndpointExample
        ImpervaCustomTaskRequest(**base_kwargs)

    def test_imperva_missing(self,):
        required_fields = ['type',
                           'websiteURL', 
                           'metadata']
        base_kwargs = {}
        metadata_example = {"incapsulaScriptUrl": self.incapsulaScriptUrlExample,"incapsulaCookie": self.incapsulaCookieExample}
        self.assertRaises(ValidationError, ImpervaCustomTaskRequest, **base_kwargs)
        base_kwargs.update({'websiteUrl': self.websiteUrlExample})
        self.assertRaises(ValidationError, ImpervaCustomTaskRequest, **base_kwargs)
        base_kwargs.update({'metadata': metadata_example})
        ImpervaCustomTaskRequest(**base_kwargs)

if __name__ == '__main__':
    unittest.main()
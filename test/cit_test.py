import unittest
import urllib
import base64
from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import RecognitionComplexImageTaskRequest
from capmonstercloudclient.exceptions import NumbersImagesErrors, TaskNotDefinedError, ZeroImagesErrors, \
    UserAgentNotDefinedError

def read_image(image_url: str,):
    image_bytes = urllib.request.urlopen(image_url).read()
    return base64.b64encode(image_bytes).decode('utf-8')

class RecognitionCITImageRequestTest(unittest.TestCase):
    
    websiteUrlExample = 'https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=middle'
    imageUrlsExamples = ['https://i.postimg.cc/H8yBD5FJ/0-2.png', 'https://i.postimg.cc/rz0hrXz8/0-0.png',
                         'https://i.postimg.cc/qgP1cbC2/0-1.png']
    imageBase64Examples = [read_image(i) for i in imageUrlsExamples]
    metadataExample = {"Task": "oocl_rotate_double_new"}
    
    def testImagesTypes(self):
        
        with self.assertRaises(ValidationError):
            request = RecognitionComplexImageTaskRequest(metadata=RecognitionCITImageRequestTest.metadataExample,
                                                       imagesBase64='[]')
        
    
    def testImagesFilling(self):
         
        with self.assertRaises(ZeroImagesErrors, 
                               msg='Empty array imagesBase64 must be cause ZeroImagesErrors'):
            request = RecognitionComplexImageTaskRequest(metadata=RecognitionCITImageRequestTest.metadataExample,
                                                       imagesBase64=[])
                
    def testAllRequiredFieldsFilling(self):
        required_fields = ['class', 'type', 'metadata']
        metadata_fields = ['Task']
        request = RecognitionComplexImageTaskRequest(
                                                   metadata=RecognitionCITImageRequestTest.metadataExample,
                                                   imagesBase64=RecognitionCITImageRequestTest.imageBase64Examples)
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(i in list(request_dict.keys()), 
                            msg=f'Required field {i} not in {request_dict}')
            
        metadata_dict = request_dict['metadata']
        for i in metadata_fields:
            self.assertTrue(i in list(metadata_dict.keys()), 
                            msg=f'Required field {i} not in {request_dict}')
            
        self.assertEqual(request_dict['class'], 'recognition')
        self.assertEqual(request_dict['type'], 'ComplexImageTask')
            
    def testTaskDefined(self):
        with self.assertRaises(TaskNotDefinedError, 
                               msg='Expect that empty "Task" field will be cause TaskNotDefinedError'):
            request = RecognitionComplexImageTaskRequest(metadata={},
                                                         imagesBase64=RecognitionCITImageRequestTest.imageBase64Examples)
        
        with self.assertRaises(TaskNotDefinedError):
            request = RecognitionComplexImageTaskRequest(metadata={'dsfsdf': 'sdfsdf'},
                                                       imagesUrls=RecognitionCITImageRequestTest.imageUrlsExamples)

    def testExtraMetadata(self):
        with self.assertRaises(TypeError, 
                               msg='Expect that extra metadata fields will be cause TypeError'):
            request = RecognitionComplexImageTaskRequest(metadata={"Task": "oocl_rotate_new", 'asd': 'asd'},
                                                         imagesBase64=RecognitionCITImageRequestTest.imageBase64Examples)
        
if __name__ == '__main__':
    unittest.main()
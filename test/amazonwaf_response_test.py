import unittest
import asyncio
import os

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import AmazonWafProxylessRequest
from capmonstercloudclient import CapMonsterClient, ClientOptions

def get_all_keys(dictionary):
    all_values = []
    def recursive_items(dictionary):
        for key, value in dictionary.items():
            if type(value) is dict:
                all_values.append(key)
                recursive_items(value)
            else:
                all_values.append(key)
        return all_values
    return recursive_items(dictionary)

class AmazonWafOutsTest(unittest.TestCase):
    
    def testOuts(self):
        required_outs = ['captcha_voucher', 'existing_token', 'cookies', 'aws-waf-token']
        api_key = os.getenv('API_KEY')
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options)
        goku_props = {
          "key":"AQIDAHjcYu/GjX+QlghicBgQ/7bFaQZ+m5FKCMDnO+vTbNg96AGmvCkduxEuykZKc0K40UwtAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM+H2/bzoimaPlOij3AgEQgDsAEZjIlq+1m1nBhpIfMKW5CRjtglgrtZVQ1qzzOD12VaRtyo37TyZNSWehn9LZjlsRHCvkEuVNxYrQLQ==",
          "iv":"CgAHrDMYFFAAAD69",
          "context":"hPWsn2RGeTkDkphwlj11dOk4T2nmJjCUzXFoPnhio4Osqt29lETt0U4/Ie0waoNwuxg/YobRAkPaS4pGC5+XDtSWuEjIOVGEWIrL4icEv19/EuBg1v3Vh0AU+UB/Wk1n63rxlFwU+EwKWjWdkYWFw79vTrr/zrBao1+rzlsKWvrF5CJEJFUvnHz1cU1UQ9M0hBW8diVhKPvf67E9Tf58wwOcNK5tfAX+uhg3G84XpPvh+6bobZleX4Nrz8lER3wNfOcYexyhouErEoowh2DBnnlrsm/OenFFuyRKqgJvHJL7rws="
        }

        challenge = "https://41bcdd4fb3cb.610cd090.us-east-1.token.awswaf.com/41bcdd4fb3cb/0d21de737ccb/cd77baa6c832/challenge.js"
        captcha = "https://41bcdd4fb3cb.610cd090.us-east-1.captcha.awswaf.com/41bcdd4fb3cb/0d21de737ccb/cd77baa6c832/captcha.js"
        request = AmazonWafProxylessRequest(websiteUrl='https://efw47fpad9.execute-api.us-east-1.amazonaws.com/latest',
                                             websiteKey=goku_props['key'],
                                             challengeScript=challenge,
                                             captchaScript=captcha,
                                             context=goku_props['context'],
                                             iv=goku_props['iv'],
                                             cookieSolution=True
                                            )
        result = asyncio.run(client.solve_captcha(request))
        print(result)
        # for i in required_outs:
        #     self.assertTrue(i in get_all_keys(result))

            
if __name__ == '__main__':
    unittest.main()
        
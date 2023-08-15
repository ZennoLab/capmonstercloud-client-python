# Zennolab.CapMonsterCloud.Client

Official python client library for [capmonster.cloud](https://capmonster.cloud/) captcha recognition service

## Installation

    python3 -m pip install capmonstercloudclient

## Usage

***
    import asyncio

    from capmonstercloudclient import CapMonsterClient, ClientOptions
    from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

    client_options = ClientOptions(api_key=<YOUR_API_KEY>)
    cap_monster_client = CapMonsterClient(options=client_options)

    async def solve_captcha():
        return await cap_monster_client.solve_captcha(recaptcha2request)

    recaptcha2request = RecaptchaV2ProxylessRequest(websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
                                                    websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd")

    responses = asyncio.run(solve_captcha())
    print(responses)
***

Supported captcha recognition requests:

- [FunCaptchaProxylessRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/643629079/FunCaptchaTaskProxyless+solving+FunCaptcha)
- [FunCaptchaRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/735805497/FunCaptchaTask+solving+FunCaptcha)
- [GeeTestProxylessRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/1940291626/GeeTestTaskProxyless+GeeTest+captcha+recognition+without+proxy)
- [GeeTestRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/1940357159/GeeTestTask+GeeTest+captcha+recognition)
- [HCaptchaProxylessRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/1203240977/HCaptchaTaskProxyless+hCaptcha+puzzle+solving)
- [HCaptchaRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/1203240988/HCaptchaTask+hCaptcha+puzzle+solving)
- [ImageToTextRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/589863/ImageToTextTask)
- [RecaptchaV2ProxylessRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/373161985/NoCaptchaTaskProxyless+solving+Google+recaptcha)
- [RecaptchaV2Request](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/680689685/NoCaptchaTask+solving+Google+recaptcha)
- [RecaptchaV3ProxylessRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/566853650/RecaptchaV3TaskProxyless+solving+Google+ReCaptcha+v.3)
- [RecaptchaV2EnterpriseProxylessRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/2178383893/RecaptchaV2EnterpriseTaskProxyless+solving+Google+reCAPTCHA+Enterprise+without+proxy)
- [RecaptchaV2EnterpriseRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/2179104769/RecaptchaV2EnterpriseTask+solving+Google+reCAPTCHA+Enterprise)
- [TurnstileProxylessRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/2257879047/TurnstileTaskProxyless+solving+Turnstile+without+proxy)
- [TurnstileRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/2313814017/TurnstileTask+Cloudflare+Challenge)
- [RecaptchaComplexImageTaskRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/2279538739/ComplexImageTask+Recaptcha+Google+captcha+solution)
- [HcaptchaComplexImageTaskRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/2279604241/ComplexImageTask+HCaptcha+hCaptcha+captcha+solution)
- [FunCaptchaComplexImageTaskRequest](https://zennolab.atlassian.net/wiki/spaces/APIS/pages/2291400705/ComplexImageTask+Funcaptcha+Funcaptcha+solving)
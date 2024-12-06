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

- [GeeTestProxylessRequest](https://docs.capmonster.cloud/docs/captchas/geetest-task)
- [GeeTestRequest](https://docs.capmonster.cloud/docs/captchas/geetest-task)
- [ImageToTextRequest](https://docs.capmonster.cloud/docs/captchas/image-to-text)
- [RecaptchaV2ProxylessRequest](https://docs.capmonster.cloud/docs/captchas/no-captcha-task)
- [RecaptchaV2Request](https://docs.capmonster.cloud/docs/captchas/no-captcha-task)
- [RecaptchaV3ProxylessRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v3-task)
- [RecaptchaV2EnterpriseProxylessRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v2-enterprise-task)
- [RecaptchaV2EnterpriseRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v2-enterprise-task)
- [TurnstileProxylessRequest](https://docs.capmonster.cloud/docs/captchas/tunrstile-task)
- [TurnstileRequest](https://docs.capmonster.cloud/docs/captchas/tunrstile-task)
- [RecaptchaComplexImageTaskRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-click)
- [DataDomeCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/datadome)
- [TenDiCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tendi)
- [BasiliskCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/Basilisk-task)
- [AmazonWafRequest](https://docs.capmonster.cloud/docs/captchas/amazon-task)

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

- [GeeTestProxylessRequest](https://zenno.link/doc-geetest-en)
- [GeeTestRequest](https://zenno.link/doc-geetest-proxy-en)
- [HCaptchaProxylessRequest](https://zenno.link/doc-hcaptcha-en)
- [HCaptchaRequest](https://zenno.link/doc-hcaptcha-proxy-en)
- [ImageToTextRequest](https://zenno.link/doc-ImageToTextTask-en)
- [RecaptchaV2ProxylessRequest](https://zenno.link/doc-recaptcha2-en)
- [RecaptchaV2Request](https://zenno.link/doc-recaptcha2-proxy-en)
- [RecaptchaV3ProxylessRequest](https://zenno.link/doc-recaptcha3-en)
- [RecaptchaV2EnterpriseProxylessRequest](https://zenno.link/doc-recaptcha2e-en)
- [RecaptchaV2EnterpriseRequest](https://zenno.link/doc-recaptcha2e-proxy-en)
- [TurnstileProxylessRequest](https://zenno.link/doc-turnstile-en)
- [TurnstileRequest](https://zenno.link/doc-turnstile-proxy-en)
- [RecaptchaComplexImageTaskRequest](https://zenno.link/doc-complextask-rc-en)
- [HcaptchaComplexImageTaskRequest](https://zenno.link/doc-complextask-hc-en)
- [DataDomeCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/datadome)
- [TenDiCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tendi)
- [BasiliskCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/Basilisk-task)
- [AmazonWafRequest](https://docs.capmonster.cloud/docs/captchas/amazon-task)

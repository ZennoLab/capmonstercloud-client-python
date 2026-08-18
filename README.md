# CapMonster Cloud Python SDK: AI Captcha Solver & Anti-Bot Bypass

<p align="center">
  <a href="https://capmonster.cloud/en/?utm_source=github&utm_medium=readme&utm_campaign=python_repo">
    <img src="https://img.shields.io/badge/CapMonster%20Cloud-Python%20Captcha%20Solver-00B2FF?style=for-the-badge&logo=python&logoColor=white" alt="CapMonster Cloud Python SDK" height="40">
  </a>
</p>

<p align="center">
  <strong>Fast, AI-driven CAPTCHA solving client for Python. Seamlessly bypass Cloudflare Turnstile, reCAPTCHA v2/v3/Enterprise, DataDome, GeeTest, and Amazon WAF in web scraping and browser automation.</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/v/capmonstercloudclient.svg?style=flat-square&color=blue" alt="PyPI version"></a>
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/dm/capmonstercloudclient.svg?style=flat-square&color=green" alt="PyPI downloads"></a>
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/pyversions/capmonstercloudclient.svg?style=flat-square" alt="Python Versions"></a>
  <a href="https://github.com/ZennoLab/capmonstercloud-client-python/stargazers"><img src="https://img.shields.io/github/stars/ZennoLab/capmonstercloud-client-python?style=flat-square&color=yellow" alt="GitHub Stars"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square" alt="License: MIT"></a>
</p>

---

Official asynchronous Python SDK for [CapMonster Cloud](https://capmonster.cloud/?utm_source=github&utm_medium=readme&utm_campaign=python_repo). Easily plug ultra-fast AI captcha recognition into **Playwright, Selenium, Puppeteer, Scrapy, BeautifulSoup, and Requests** automation workflows without human-in-the-loop delays.

**[👉 Get your Free API Key & Free Trial Balance on CapMonster Cloud](https://dash.capmonster.cloud/Account/SignUp?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)**

---

## ⚡ Highlights & Benchmarks

- ⚡ **Sub-Second Speed:** 100% automated neural networks solve captchas in as fast as 0.3–2.5 seconds.
- 🤖 **Zero Human Workers:** Reliable, consistent uptime without mechanical turk latencies.
- 🌐 **Native Automation Wrappers:** Plug-and-play code snippets for **Playwright & Selenium**.
- 🛡️ **Modern Anti-Bot Bypass:** Full support for Cloudflare Turnstile, DataDome, GeeTest v4, Amazon WAF, and Imperva.
- 💰 **Lowest Cost per 1,000 Solutions:** High accuracy rate with competitive pay-as-you-go pricing.

---

## 📦 Installation

```bash
pip install capmonstercloudclient
```

---

## 🚀 Quick Start Examples

### 1. Simple Async Example (reCAPTCHA v2 Proxyless)

```python
import asyncio
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

# 1. Initialize client with your API key
options = ClientOptions(api_key="YOUR_CAPMONSTER_API_KEY")
client = CapMonsterClient(options=options)

async def main():
    # 2. Build the task payload
    request = RecaptchaV2ProxylessRequest(
        websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
        websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd"
    )
    
    # 3. Solve captcha and receive token
    result = await client.solve_captcha(request)
    print("reCAPTCHA Token:", result.get("gRecaptchaResponse"))

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Playwright / Selenium Turnstile & reCAPTCHA Integration

```python
import asyncio
from playwright.async_api import async_playwright
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import TurnstileProxylessRequest

options = ClientOptions(api_key="YOUR_CAPMONSTER_API_KEY")
client = CapMonsterClient(options=options)

async def run_scraper():
    # Request Turnstile solution
    turnstile_req = TurnstileProxylessRequest(
        websiteUrl="https://target-website.com/login",
        websiteKey="0x4AAAAAAABnPIDnK2k_e-2"
    )
    solution = await client.solve_captcha(turnstile_req)
    token = solution.get("token")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://target-website.com/login")
        
        # Inject the solved token into the page
        await page.evaluate(f'document.querySelector("[name=cf-turnstile-response]").value = "{token}";')
        await page.click("#submit-button")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_scraper())
```

---

## 🛡️ Supported CAPTCHA Types & Documentation

| Protection Type | Task Request Class | Proxyless Support | Docs Link |
| :--- | :--- | :---: | :--- |
| **Cloudflare Turnstile** | `TurnstileProxylessRequest` / `TurnstileRequest` | ✅ Yes | [Documentation](https://docs.capmonster.cloud/docs/captchas/turnstile-task) |
| **reCAPTCHA v2** | `RecaptchaV2ProxylessRequest` / `RecaptchaV2Request` | ✅ Yes | [Documentation](https://docs.capmonster.cloud/docs/captchas/recaptcha-v2-task) |
| **reCAPTCHA v3 / Enterprise** | `RecaptchaV3ProxylessRequest` / `RecaptchaV2EnterpriseRequest` | ✅ Yes | [Documentation](https://docs.capmonster.cloud/docs/captchas/recaptcha-v3-task) |
| **GeeTest (v3, v4)** | `GeeTestProxylessRequest` / `GeeTestRequest` | ✅ Yes | [Documentation](https://docs.capmonster.cloud/docs/captchas/geetest-task) |
| **DataDome** | `DataDomeCustomTaskRequest` | 🌐 Proxy Required | [Documentation](https://docs.capmonster.cloud/docs/captchas/datadome) |
| **Amazon WAF** | `AmazonWafRequest` | ✅ Yes | [Documentation](https://docs.capmonster.cloud/docs/captchas/amazon-task) |
| **Imperva / Incapsula** | `ImpervaCustomTaskRequest` / `Proxyless` | ✅ Yes | [Documentation](https://docs.capmonster.cloud/docs/captchas/incapsula) |
| **Binance CAPTCHA** | `BinanceTaskRequest` / `Proxyless` | ✅ Yes | [Documentation](https://docs.capmonster.cloud/docs/captchas/binance) |
| **Standard Image-to-Text** | `ImageToTextRequest` | ✅ Yes | [Documentation](https://docs.capmonster.cloud/docs/captchas/image-to-text) |
| **Complex Image Grid** | `RecaptchaComplexImageTaskRequest` | ✅ Yes | [Documentation](https://docs.capmonster.cloud/docs/captchas/complex-image-task) |

---

## 🛠️ Architecture & Pipeline Flow

```text
[ Scraping Script (Python / Playwright) ]
                  │
                  ▼
   [ Extract sitekey & website URL ]
                  │
                  ▼
  [ 🤖 CapMonsterClient SDK ] ──► POST task to CapMonster Cloud API
                  │
                  ▼
  [ Instant Neural Network Solve ] ──► Async token retrieval (< 1s)
                  │
                  ▼
[ Inject Token into Form & Submit ] ──► Bypass complete!
```

---

## ⚙️ Best Practices & Troubleshooting

- **Token Expiration:** Most tokens (reCAPTCHA, Turnstile) are valid for 120 seconds. Inject and submit the token immediately after solving.
- **Proxy Matching:** For high-security targets (DataDome, Cloudflare Strict), use the same residential proxy in both the scraping session and the CapMonster request task.
- **Account Balance:** Make sure your balance is positive. You can monitor and top up credits directly in your [Dashboard](https://dash.capmonster.cloud/?utm_source=github&utm_medium=readme&utm_campaign=python_repo).

---

## 📚 Resources & Community

- 📖 [Official CapMonster Cloud Documentation](https://docs.capmonster.cloud/)
- 🎯 [Full Captcha API Specifications](https://docs.capmonster.cloud/docs/captchas/)
- 💬 [Support & Developer Community](https://capmonster.cloud/en/?utm_source=github&utm_medium=readme&utm_campaign=python_repo#support)

---

## ⭐ Star History

If this library helps your automation workflows, please give us a star!

[![Star History Chart](https://api.star-history.com/svg?repos=ZennoLab/capmonstercloud-client-python&type=Date)](https://star-history.com/#ZennoLab/capmonstercloud-client-python&Date)

---

## 📄 License

[MIT](LICENSE) © [ZennoLab](https://zennolab.com/) / [CapMonster Cloud](https://capmonster.cloud/)

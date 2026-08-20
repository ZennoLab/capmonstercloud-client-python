# CapMonster Cloud Python SDK: AI Captcha Solver & Anti-Bot Bypass

<p align="center">
  <a href="https://capmonster.cloud/en/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme">
    <img src="https://img.shields.io/badge/CapMonster%20Cloud-Python%20Captcha%20Solver-00B2FF?style=for-the-badge&logo=python&logoColor=white" alt="CapMonster Cloud Python SDK" height="40">
  </a>
</p>

<p align="center">
  <strong>Fast, AI-driven CAPTCHA solving client for Python. Seamlessly bypass Cloudflare Turnstile, reCAPTCHA v2/v3/Enterprise, DataDome, GeeTest, and Amazon WAF in web scraping and browser automation.</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/v/capmonstercloudclient.svg?style=flat-square&color=blue" alt="PyPI version"></a>
  <a href="https://pepy.tech/project/capmonstercloudclient"><img src="https://static.pepy.tech/badge/capmonstercloudclient/month" alt="PyPI downloads"></a>
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/pyversions/capmonstercloudclient.svg?style=flat-square" alt="Python Versions"></a>
  <a href="https://github.com/CapMonsterCloud/capmonster-python-captcha-solver/stargazers"><img src="https://img.shields.io/github/stars/CapMonsterCloud/capmonster-python-captcha-solver?style=flat-square&color=yellow" alt="GitHub Stars"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square" alt="License: MIT"></a>
</p>

---

Official asynchronous Python SDK for [CapMonster Cloud](https://capmonster.cloud/en/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme). Easily plug ultra-fast AI captcha recognition into **Playwright, Selenium, Puppeteer, Scrapy, BeautifulSoup, and Requests** automation workflows without human-in-the-loop delays.

**[👉 Get your Free API Key & Free Trial Balance on CapMonster Cloud](https://dash.capmonster.cloud/Account/SignUp?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)**

---

## ⚡ Highlights & Benchmarks

- ⚡ **Sub-Second Speed:** Automated AI models solve captchas in 300 ms to 6 seconds depending on the system load.
- 🤖 **Zero Human Workers:** 100% automated machine learning pipeline with no manual latencies.
- 🌐 **Browser Automation Ready:** Works out-of-the-box with **Playwright, Selenium, and Puppeteer**.
- 🛡️ **Modern Anti-Bot Bypass:** Full support for Cloudflare Turnstile, reCAPTCHA Enterprise, GeeTest, and Amazon WAF.
- 💰 **Cost-Effective:** Low-cost pricing structure based on pay-as-you-go balance.

---

## 📦 Installation

```bash
pip install capmonstercloudclient
```

---

## 🚀 Quick Start & Usage Examples

### 1. Asynchronous reCAPTCHA v2 Solving

```python
import asyncio
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

# Initialize client with your API key from dashboard
options = ClientOptions(api_key="YOUR_CAPMONSTER_API_KEY")
client = CapMonsterClient(options=options)

async def main():
    # Build the task payload
    request = RecaptchaV2ProxylessRequest(
        websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
        websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd"
    )
    
    # Send task and receive token
    result = await client.solve_captcha(request)
    print("reCAPTCHA Token:", result.get("gRecaptchaResponse"))

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Browser Automation (Playwright + Cloudflare Turnstile)

```python
import asyncio
from playwright.async_api import async_playwright
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import TurnstileProxylessRequest

options = ClientOptions(api_key="YOUR_CAPMONSTER_API_KEY")
client = CapMonsterClient(options=options)

async def run_scraper():
    # Solve Turnstile challenge via CapMonster Cloud
    turnstile_req = TurnstileProxylessRequest(
        websiteUrl="https://target-website.com/login",
        websiteKey="0x4AAAAAAABnPIDnK2k_e-2"
    )
    solution = await client.solve_captcha(turnstile_req)
    token = solution.get("token")

    # Inject token into Playwright browser session
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://target-website.com/login")
        
        await page.evaluate(f'document.querySelector("[name=cf-turnstile-response]").value = "{token}";')
        await page.click("#submit-button")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_scraper())
```

---

## 🛡️ Supported CAPTCHA Types

All task types conform to the official [CapMonster Cloud API Documentation](https://docs.capmonster.cloud/docs/captchas/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme):

| Protection Type | Task Request Class | Proxyless Mode |
| :--- | :--- | :---: |
| **Cloudflare Turnstile** | `TurnstileProxylessRequest` / `TurnstileRequest` | ✅ Supported |
| **reCAPTCHA v2** | `RecaptchaV2ProxylessRequest` / `RecaptchaV2Request` | ✅ Supported |
| **reCAPTCHA v3** | `RecaptchaV3ProxylessRequest` | ✅ Supported |
| **reCAPTCHA Enterprise** | `RecaptchaV2EnterpriseProxylessRequest` / `RecaptchaV2EnterpriseRequest` | ✅ Supported |
| **GeeTest (v3, v4)** | `GeeTestProxylessRequest` / `GeeTestRequest` | ✅ Supported |
| **Amazon WAF** | `AmazonWafRequest` | ✅ Supported |
| **DataDome** | `DataDomeCustomTaskRequest` | 🌐 Proxy Required |
| **Imperva / Incapsula** | `ImpervaCustomTaskRequest` / `ImpervaCustomTaskProxylessRequest` | ✅ Supported |
| **Binance CAPTCHA** | `BinanceTaskRequest` / `BinanceTaskProxylessRequest` | ✅ Supported |
| **Standard Text CAPTCHA** | `ImageToTextRequest` | ✅ Supported |
| **Complex Image Tasks** | `RecaptchaComplexImageTaskRequest` | ✅ Supported |

---

## 🛠️ How It Works

```text
[ Script / Scraper ]
         │
         ▼
[ Extract sitekey & website URL ]
         │
         ▼
[ CapMonsterClient API ] ──► POST createTask to https://api.capmonster.cloud
         │
         ▼
[ Neural Network Processing ] ──► Poll getTaskResult (300ms - 6s)
         │
         ▼
[ Receive Token & Autosubmit ] ──► Complete bypass
```

---

## ⚙️ Best Practices

- **Token Expiration:** Most tokens (reCAPTCHA, Turnstile) remain valid for 120 seconds. Inject and submit the solution immediately after receiving the response.
- **Proxy Usage:** For custom tasks and strict protections, use the same proxy in your scraping session and the CapMonster task payload.
- **Balance Monitoring:** Ensure your account balance remains positive in the [Dashboard](https://dash.capmonster.cloud/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme).

---

## 📚 Official Documentation & Links

- 📖 [Getting Started Guide](https://docs.capmonster.cloud/docs/getting-start/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)
- 🎯 [Supported Captchas Overview](https://docs.capmonster.cloud/docs/captchas/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)
- ⚙️ [API Methods Reference](https://docs.capmonster.cloud/docs/methods/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)
- 💬 [Support & Community](https://capmonster.cloud/en/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme#support)

---

## 📄 License

[MIT](./LICENSE) © [ZennoLab](https://zennolab.com/) / [CapMonster Cloud](https://capmonster.cloud/en/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)

# Use WeProxy with Python

[![WeProxy — Python proxy example](./assets/banner.png)](https://weproxy.io/?utm_source=github&utm_medium=referral&utm_campaign=python-proxy)

[![Website](https://img.shields.io/badge/Website-weproxy.io-111111?style=for-the-badge)](https://weproxy.io/?utm_source=github&utm_medium=referral&utm_campaign=python-proxy)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Integrations](https://img.shields.io/badge/Docs-Integrations-2563eb?style=for-the-badge)](https://weproxy.io/en/integrations?utm_source=github&utm_medium=referral&utm_campaign=python-proxy)

Automate egress through [WeProxy](https://weproxy.io) with the standard **`requests`** library — the default choice for Python scrapers, notebooks, and ETL jobs.

---

## What you get

A single script that:

- Builds `http://USER:PASS@gw.weproxy.com.tr:8989`  
- Passes it as both `http` and `https` entries in `proxies=`  
- Hits an IP echo URL and prints the exit address  

Ideal as a connectivity canary before you wire WeProxy into Scrapy, httpx, or custom crawlers.

## Requirements

- Python **3.9+**  
- Panel credentials from [my.we1.town](https://my.we1.town)  

## Install

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

Export credentials (the sample reads the process environment, not the file parser):

```bash
export WEPROXY_USER="your-user"
export WEPROXY_PASS="your-pass"
```

PowerShell:

```powershell
$env:WEPROXY_USER="your-user"
$env:WEPROXY_PASS="your-pass"
```

## Run

```bash
python src/check_ip.py
```

## Core snippet

```python
import requests

proxy = "http://USER:PASSWORD@gw.weproxy.com.tr:8989"
proxies = {"http": proxy, "https": proxy}

print(requests.get("https://api.ipify.org", proxies=proxies, timeout=30).text)
```

Env-aware version: [`src/check_ip.py`](./src/check_ip.py).

## Patterns beyond the demo

| Use case | Hint |
| --- | --- |
| Session reuse | `requests.Session()` + same `proxies` dict |
| Retries | Wrap with `urllib3` Retry or tenacity; treat 407 as auth bug |
| Async | `httpx` / `aiohttp` with proxy URL — same gateway string |
| Scrapy | Set `http_proxy` / middleware auth from panel secrets |
| SOCKS5 | Needs `requests[socks]` **and** a SOCKS-enabled package |

Product line (residential vs datacenter) changes **credentials**, not the Python API. Compare on [Pricing](https://weproxy.io/en/pricing) and [Rotating residential](https://weproxy.io/en/proxies/rotating-ipv4-residential).

## Troubleshooting

| Symptom | Likely cause |
| --- | --- |
| `ProxyError` | Bad host/port, network path, or suspended package |
| `407` | Wrong user/pass |
| Hangs | Raise `timeout=`; free proxies hang — paid gateway should not |
| Different IP each run | Expected on rotating packages |

cURL sanity check:

```bash
curl -x http://USER:PASSWORD@gw.weproxy.com.tr:8989 https://api.ipify.org
```

## Project layout

```text
python-proxy/
├── assets/banner.png
├── src/check_ip.py
├── requirements.txt
├── .env.example
└── README.md
```

## Related

- [nodejs-proxy](https://github.com/weproxy-io/nodejs-proxy) · [php-proxy](https://github.com/weproxy-io/php-proxy)  
- [residential-proxies](https://github.com/weproxy-io/residential-proxies) · [free-proxy-list](https://github.com/weproxy-io/free-proxy-list)  
- [Integrations](https://weproxy.io/en/integrations) · [Tools](https://weproxy.io/en/tools)  

## License

MIT — see [LICENSE](./LICENSE).

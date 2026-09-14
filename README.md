# Use WeProxy with Python

[![WeProxy — Python proxy example](./assets/banner.png)](https://weproxy.io/?utm_source=github&utm_medium=referral&utm_campaign=python-proxy)

[![Website](https://img.shields.io/badge/Website-weproxy.io-111111?style=for-the-badge)](https://weproxy.io/?utm_source=github&utm_medium=referral&utm_campaign=python-proxy) [![Integrations](https://img.shields.io/badge/Docs-Integrations-2563eb?style=for-the-badge)](https://weproxy.io/en/integrations?utm_source=github&utm_medium=referral&utm_campaign=python-proxy)

Minimal `requests` example: print your exit IP through the [WeProxy](https://weproxy.io) HTTP proxy gateway.

## Requirements

- Python 3.9+
- WeProxy credentials from [my.we1.town](https://my.we1.town)

## Install

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

```bash
cp .env.example .env
```

Export credentials (this sample reads process environment, not the `.env` file directly):

```bash
export WEPROXY_USER="your-user"
export WEPROXY_PASS="your-pass"
```

PowerShell:

```powershell
$env:WEPROXY_USER="your-user"
$env:WEPROXY_PASS="your-pass"
```

Gateway defaults:

```text
Host: gw.weproxy.com.tr
Port: 8989
```

## Run

```bash
python src/check_ip.py
```

## Code

```python
import requests

proxy = "http://USER:PASSWORD@gw.weproxy.com.tr:8989"
proxies = {"http": proxy, "https": proxy}

print(requests.get("https://api.ipify.org", proxies=proxies, timeout=30).text)
```

Full script: [`src/check_ip.py`](./src/check_ip.py).

## Residential vs datacenter

Use panel credentials for the product you purchased — e.g. [rotating residential](https://weproxy.io/en/proxies/rotating-ipv4-residential) or [rotating datacenter](https://weproxy.io/en/proxies/rotating-ipv4-datacenter). Gateway host/port stay the same.

SOCKS5 requires a SOCKS-capable package and typically `requests[socks]`; this sample uses HTTP proxy mode.

## Links

- [WeProxy](https://weproxy.io)
- [Pricing](https://weproxy.io/en/pricing)
- [Integrations](https://weproxy.io/en/integrations)

## Suggested GitHub topics

`python` · `requests` · `proxy` · `residential-proxy` · `socks5` · `http-proxy`

## License

MIT — see [LICENSE](./LICENSE).

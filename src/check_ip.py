"""
Minimal WeProxy example: fetch your exit IP through the HTTP proxy gateway.

Set WEPROXY_USER and WEPROXY_PASS from the customer panel (https://my.we1.town),
or pass a full WEPROXY_URL.
"""

from __future__ import annotations

import os
import sys

import requests

HOST = os.getenv("WEPROXY_HOST", "gw.weproxy.com.tr")
PORT = os.getenv("WEPROXY_PORT", "8989")
USER = os.getenv("WEPROXY_USER", "USER-package-residential")
PASS = os.getenv("WEPROXY_PASS", "PASSWORD")
ECHO_URL = os.getenv("WEPROXY_ECHO_URL", "https://api.ipify.org")
PROXY_URL = os.getenv("WEPROXY_URL")


def main() -> int:
    if USER == "USER-package-residential" or PASS == "PASSWORD":
        print(
            "Using placeholder credentials. "
            "Set WEPROXY_USER / WEPROXY_PASS (or WEPROXY_URL) before production use.",
            file=sys.stderr,
        )

    proxy = PROXY_URL or f"http://{USER}:{PASS}@{HOST}:{PORT}"
    proxies = {"http": proxy, "https": proxy}

    try:
        response = requests.get(ECHO_URL, proxies=proxies, timeout=30)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Request failed: {exc}", file=sys.stderr)
        return 1

    print(f"Exit IP: {response.text.strip()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

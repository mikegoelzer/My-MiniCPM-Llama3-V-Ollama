#!/usr/bin/env python3

import sys
import requests
import json

def main():
    url = "http://localhost:11435/api/generate"
    payload = {
        "model": "minicpm-v2.5",
        "prompt": "Why is the sky blue?",
        "options": {
            "num_ctx": 4096
        }
    }

    with requests.post(url, json=payload, stream=True) as response:
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                print(data['response'], end='', flush=True)
                if data['done']:
                    break

    print()
    return 0

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
import argparse
import httpx
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Call FastAPI /down endpoint to download a TikTok video"
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Base URL of the FastAPI service (e.g. http://127.0.0.1:8000/down)",
    )
    parser.add_argument(
        "--link",
        required=True,
        help="TikTok video URL to download",
    )
    args = parser.parse_args()

    payload = {"link": args.link}

    try:
        resp = httpx.post(args.url, json=payload, timeout=60.0)
        resp.raise_for_status()
    except httpx.RequestError as e:
        print(f"⚠️  Request failed: {e}", file=sys.stderr)
        sys.exit(1)
    except httpx.HTTPStatusError as e:
        print(f"⚠️  HTTP error: {e.response.status_code} {e.response.text}", file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    print("Response:")
    print(f"  link:   {data.get('link')}")
    print(f"  status: {data.get('status')}")
    if data.get("detail"):
        print(f"  detail: {data.get('detail')}")

if __name__ == "__main__":
    main()

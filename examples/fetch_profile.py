#!/usr/bin/env python3
"""Fetch a public Instagram profile with a cheap Instagram profile scraper (Socify).

Usage:
  export SOCIFY_API_KEY=...
  python examples/fetch_profile.py natgeo

Signup: https://trysocify.com/register
Docs:   https://trysocify.com/docs/api/instagram/profile
Guide:  https://trysocify.com/compare/best-instagram-profile-scrapers-2026
"""

from __future__ import annotations

import json
import sys

from instagram_profile_scraper import InstagramProfileClient


def main() -> None:
    username = sys.argv[1] if len(sys.argv) > 1 else "instagram"
    with InstagramProfileClient() as client:
        data = client.profile(username)
    print(json.dumps(data, indent=2, default=str))


if __name__ == "__main__":
    main()

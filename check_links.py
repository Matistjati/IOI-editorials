#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

def check_web_link(url):
    try:
        req = Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36')
        urlopen(req, timeout=10)
        return True
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False

links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', Path('readme.md').read_text())
links = [(t, u) for t, u in links if u.strip() and u != 'X']

broken = []
for text, url in links:
    if url.startswith('http://'):
        assert 0

    if url.startswith('https://'):
        status = check_web_link(url)
    else:
        status = Path(url).exists()
    
    if not status:
        broken.append((text, url))

print(f"✓ {len(links) - len(broken)}/{len(links)} links working")
if broken:
    print("\nBroken:")
    for text, url in broken:
        print(f"  [{text}]({url})")
    sys.exit(1)

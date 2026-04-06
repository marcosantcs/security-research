"""
Subdomain Enumeration Tool
Use ONLY on authorized targets.
"""
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

WORDLIST = [
    "www", "mail", "ftp", "api", "dev", "staging", "admin",
    "portal", "app", "test", "vpn", "remote", "cdn", "assets",
    "static", "blog", "shop", "auth", "login", "dashboard"
]

def resolve(subdomain: str, domain: str) -> dict | None:
    fqdn = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(fqdn)
        return {"subdomain": fqdn, "ip": ip}
    except socket.gaierror:
        return None

def enumerate_subdomains(domain: str, threads: int = 20) -> list:
    results = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(resolve, sub, domain): sub for sub in WORDLIST}
        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)
                print(f"[+] Found: {result['subdomain']} -> {result['ip']}")
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python subdomain_enum.py <domain>")
        print("Example: python subdomain_enum.py example.com")
        sys.exit(1)
    domain = sys.argv[1]
    print(f"[*] Enumerating subdomains for: {domain}\n")
    found = enumerate_subdomains(domain)
    print(f"\n[*] Total found: {len(found)}")

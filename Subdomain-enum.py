import requests

# You need to change the domain 
domain = "google.com"

# if you have domain list you can change from here 
file = open("subdomains.txt")
content = file.read()
subdomains = content.splitlines()
discovered_subdomains = []
for subdomain in subdomains:
   
    url = f"http://{subdomain}.{domain}"
    try:
        
        requests.get(url)
    except requests.ConnectionError:
        
        pass
    else:
        print("[+] Discovered subdomain:", url)
        
        discovered_subdomains.append(url)


with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)

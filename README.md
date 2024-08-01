# webhook-proxy
A Proxy server which forwards github webhooks requests to another server. This is intended to work with a Jenkins server instance that is behind a CGNAT and exposed through cloudflared without exposing the whole application to the internet. This is because cloudflare tunnels don't accept paths in the URL.

![image](https://github.com/user-attachments/assets/a3cdf371-e91a-42d3-8778-3e04e3b48792)


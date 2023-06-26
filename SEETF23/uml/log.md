The flag is in the same directory as the app. (through docker exec)

We're just sending a GET request to the internal service http://

Possible attacks are RCE but since getting RCE through a GET request seems unachievable tbh.

SSRF is a possibility and there is an open bug report for SSRF.


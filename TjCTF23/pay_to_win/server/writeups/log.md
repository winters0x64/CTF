When we login to the page our username is taken from the post request and create a users object, with the key as the username and value as the hash generated , but the hash generated is easy to bruteforce as we can see from here, 
```py
hex(random.getrandbits(24))[2:]
```

So here we'll get a string which is 24 bits in size,this gets assinged to data and it gets base64 encode and then the hash cookie is calculated by using this data + user[username], here we have control over data and if we could bruteforce the value of user[username]
then we could the hash check that is implemented on the server.

Now, we'll know the value of the random bits which could be used to forge a cookie with user_type=premium and now we could specify the theme we could pass in the flag directory to get the flag.

Not solved during the CTF


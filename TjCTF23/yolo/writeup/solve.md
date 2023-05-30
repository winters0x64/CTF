We have an admin bot so that means this is an XSS challenge

However there is CSP in the website prevents us from injecting arbitart javascript payload as the server has set script-src with a nonce
So we somehow needs to bypass this nonce check, To get code execution.

Lets look at how the Nonce is calculated

```py
    req.locals.nonce = req.locals.nonce ?? '47baeefe8a0b0e8276c2f7ea2f24c1cc9deb613a8b9c866f796a892ef9f8e65d';
    req.locals.nonce = crypto.createHash('sha256').update(req.locals.nonce).digest('hex');
    res.header('Content-Security-Policy', `script-src 'nonce-${req.locals.nonce}'; default-src 'self'; style-src 'self' 'nonce-${req.locals.nonce}';`);
```
If the nonce is not present then we start out with a nonce and then with every request we're updating the nonce. with the hexedn version of the sha256 of the previous hash. So that means if we know the number of requests that we are making then we can calculate the nonce value and make our script executable.

```html
<script nonce="f8c5a82d13fc3dd49597d4d292ab08f98c3a7845eb7268213ec6a0168fe3ce11">alert(1)</script>
```

This will work as it's the third request and the third nonce.

Now when the admin submits his note as the flag,

It's stored in the admins userId page.

So we need to decode the JWT token to get the userID and then send a fetch request to that userId using our XSS payload

And then we'll send the infected link to the admin hence we get the flag.
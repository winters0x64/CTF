In jwt.py we can see that if in the JWT token that we are sending if there is no algorithm of the form HS256 or RS256  it will just run our payload without any further checks.

So we need to need to decode the jwt cookie and then edit and add the algorithm as 'None' and the year in the payload section as less than  1970 to get the flag.
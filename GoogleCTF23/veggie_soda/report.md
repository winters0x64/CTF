# Veggie Soda


## On first Look 

-> There is an admin bot so an XSS challenge mostly.
-> Instead of node they are using deno js and typescript.
-> Dockerfile won't start for some reason.


## Functionality

-> We can register a user and then login as the same user.
-> Once logged in we can create a post with whatever content that we want, Stored under a unique url.
-> We can also send a veggie soda(just a vegetable) to any user that we want, The sodas that we get is stored under a unique url.
-> On logging in we can see a  soda that is send to us by the admin, This shows that there is an admin user.
-> The status feature of the website is only accessible by the admin only.


## Analyzing code



## The possible solution

-> We could get XSS on the websites in on of our posts and we can send this over to the admin so that we'll get the admin's cookie once we have that we can login as admin and then get to the second stage of the attack

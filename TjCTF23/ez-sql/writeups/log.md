# Writeup for ez sql

In the source code we can see that 
```js 
express.urlencoded({ extended: true })
``` 

Which means that we can send data as an array format in the get request as follows https://example.com/?name[0]=hello&name[1]=world

and this will get interpreted as

```js
name = [hello,world]
//here name.length returns 2
```

On the server side

Why is this relevant to us?

Well as we can see that the parameter name is directly passed into the sql query but the thing here is there is a length check, that means the name parameter can't be more than 6 letters in length inorder to bypass this we give name in the format of the above mentioned exploit.

We're using using sqlmap here (Just to advance my knowledge in it)

sqlmap --url "http://localhost:3000/search?name[0]=lol&name[1]=2" -p "name[0]" --level 5 --risk 3

and on the server inorder to be less noisy

we can use the following sqlmap query(reduce the level and risk values and we're mentioning a union based attack here)

sqlmap --url "http://localhost:3000/search?name[0]=lol&name[1]=2" -p "name[0]" --level 2 --risk 1 --dbms=sqlite --tables --technique=U

That's it

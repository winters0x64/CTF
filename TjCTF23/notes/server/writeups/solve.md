# Race condition Challenge
My first race condition challenge

Okay so here inorder to get the flag we just had to access a user which doesn't exist as can be seen here

```js
pool.query(`SELECT * FROM notes WHERE user_id = '${req.session.user_id}';`, (err, results) => {
        pool.query(`SELECT * FROM users WHERE id = '${req.session.user_id}';`, (err, users) => {
            res.render('index', { notes: results, user: users[0] || { username: flag } });
        });
    });
```

We can only pass in valid session user_id's here as there is a check if not we're just refirected back to the login page.
So our req.session.user_id should be valid, now if its valid, the sql query will always return a valid response. So this seems impossible but there's also a delete endpoint like so.

```js
app.post('/user/delete', (req, res) => {
    const id = req.session.user_id;
o
    pool.query(`DELETE FROM users WHERE id = '${id}' AND password = '${req.body.password}';`, (err, results) => {

        pool.query(`SELECT * FROM users WHERE id = '${id}' AND password != '${req.body.password}';`, (err, results) => {

            if (err)
                return res.redirect('/?e=an%20error%20occurred');

            if (results.length !== 0)
                return res.redirect('/?e=incorrect%20password');

            sessions[id].forEach(session => {
                session.destroy();
            });

            pool.query(`DELETE FROM notes WHERE user_id = '${id}';`, (err, results) => {
                if (err) {
                    res.json({ success: false, message: err });
                } else {
                    res.redirect('/');
                }
            });
        });
    });
});
```

So the idea here is to delete the user data by making use of the end point and before it destroys the user_session we'll fetch the home page 
to get the flag.


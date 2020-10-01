import requests
r = requests.get('https://api.github.com/events')
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(r.text, r.url)
print(r.content)
print(r.encoding)

r.json()
print(r.raise_for_status())

r = requests.get('https://api.github.com/events', stream=True)  
print(r.iter_content(100))
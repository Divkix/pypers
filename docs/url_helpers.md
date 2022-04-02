Refer from sample code here:

```python
from pypers.url_helpers import UrlHelpers
from pypers.url_helpers import AioHttp

new_url = await UrlHelpers.shorten_url('https://www.google.com')
print(new_url)

json, resp = AioHttp.get_json('https://www.google.com')
print(json, resp)

text, resp = AioHttp.get_text('https://www.google.com')
print(text, resp)

raw, resp = AioHttp.get_raw('https://www.google.com')
print(raw, resp)

json, resp = AioHttp.post_json('https://www.google.com')
print(json, resp)
```

# pypers

<p align="center">
    <a href="https://pypers.divkix.me"><img src="img/name.png"></a>
    </br></br>
    <a href="https://pypi.org/project/PyPers/"><img src="https://img.shields.io/pypi/v/PyPers" alt="PyPI"></a>
    <a href="https://github.com/Divkix/PyPers/actions"><img src="https://github.com/Divkix/PyPers/workflows/CI%20%28pip%29/badge.svg" alt="CI (pip)"></a>
    <a href="https://pypi.org/project/pypers/"><img src="https://img.shields.io/pypi/wheel/PyPers.svg" alt="PyPI - Wheel"></a>
    <a href="https://pypi.org/project/pypers/"><img src="https://img.shields.io/pypi/pyversions/PyPers.svg" alt="Supported Python Versions"></a>
    <a href="https://pepy.tech/project/PyPers"><img src="https://pepy.tech/badge/PyPers" alt="Downloads"></a>
</p>

Package with helper scripts.

Contains some helper function which make up its name: python+helpers = pypers.


## Usage:

### pypers.mongo_helpers:
```python
from pypers.mongo_helpers import AsyncMongoDB

db = AsyncMongoDB('localhost:27017', 'pypers')
db.collection = "test"

await db.insert_one({'name': 'pypers'})
results = await db.find_one({'name': 'pypers'})
print(results)
await db.delete_one({'name': 'pypers'})
```


### pypers.namespace:
```python
from pypers.namespace import Namespace

ns = Namespace(
    a=1,
    b=2,
    c=Namespace(
        d=3,
        e=4,
    ),
)

print(ns.a)
print(ns.b)
print(ns.c.d)
print(ns.c.e)
```

### pypers.url_helpers:
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

### pypers.image_tools:

```python
from pypers.image_tools import ImageTools

new_img = ImageTools.compress_image('/path/to/image.jpg', quality=50)
print(new_img)
```

### pypers.formatters:

```python
from pypers.formatters import Formatters

humanbytes_size = Formatters.humanbytes(1024*1024)
print(humanbytes_size)

human_time = Formatters.time_formatter(15000)
print(human_time)
```

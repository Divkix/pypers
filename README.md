# pypers

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
from pypers.url_helpers import shorten_url

new_url = await shorten_url('https://www.google.com')
print(new_url)
```

### pypers.image_tools:

```python
from pypers.image_tools import compress_image

new_img = compress_image('/path/to/image.jpg', quality=50)
print(new_img)
```

### pypers.formatters:

```python
from pypers.formatters import humanbytes, time_formatter

humanbytes_size = humanbytes(1024*1024)
print(humanbytes_size)

human_time = time_formatter(15000)
print(human_time)
```

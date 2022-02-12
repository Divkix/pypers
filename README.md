# pypers

Package with helper scripts.

Contains some helper function which make up its name: python+helpers = pypers.


## Usage:

### AsyncMongoDB:
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

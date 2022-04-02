Refer from sample code here:

```python
from pypers.mongo_helpers import AsyncMongoDB

db = AsyncMongoDB('localhost:27017', 'pypers')
db.collection = "test"

await db.insert_one({'name': 'pypers'})
results = await db.find_one({'name': 'pypers'})
print(results)
await db.delete_one({'name': 'pypers'})
```

Refer from sample code here:

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

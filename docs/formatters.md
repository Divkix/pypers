Refer from sample code here:

```python
from pypers.formatters import Formatters

humanbytes_size = Formatters.humanbytes(1024*1024)
print(humanbytes_size)

human_time = Formatters.time_formatter(15000)
print(human_time)
```

Refer from sample code here:

```python
from pypers.formatters import Formatters

# size being in bytes
humanbytes_size = Formatters.humanbytes(1024*1024)
print(humanbytes_size)

# time being in seconds
human_time = Formatters.time_formatter(15000)
print(human_time)

# time being in m/h/d/w/m/y.
seconds = Formatters.get_time_in_seconds("2w")
print(seconds)
```

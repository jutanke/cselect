# cselect
Selects reasonable colors for you.

## installing
```
pip install git+https://github.com/jutanke/cselect.git
```

## Types

### Linear coloring

```python
from cselect import color as cs

colors = cs.lincolor(25)
colors = cs.lincolor(25, random_sat=True, random_val=False)
colors = cs.lincolor(25, random_sat=False, random_val=True)
colors = cs.lincolor(25, random_sat=True, random_val=True)
```
![im1](https://user-images.githubusercontent.com/831215/34304903-14eeec30-e73c-11e7-8881-597d5c3a06c3.png)

## Poisson-disc sampling in Lab space

```python
from cselect import color as cs

colors = cs.poisson_disc_sampling_Lab(100)
```
![im2](https://user-images.githubusercontent.com/831215/34304902-14d46a7c-e73c-11e7-9e57-5aafb001b625.png)


## Choose color between range
```python
from cselect import color as cs

colors = cs.rangecolor(n, (255, 0, 0), (128, 128, 0))
```

![lincolor](https://user-images.githubusercontent.com/831215/41461513-3798b526-7090-11e8-85b0-0c812d98283f.png)

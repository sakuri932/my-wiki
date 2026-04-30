# Python 极速指南

> 这里收录了学习过程中积累的 Python 技能，按难度分层整理。每个主题尽量简明，以代码示例为主。

---

## 一、基础层

### 变量与类型

```python
# 动态类型，无需声明
x = 42
name = "Alice"
pi = 3.14
flag = True

# 查看类型
type(x)        # <class 'int'>
isinstance(x, int)  # True

# 多重赋值
a, b, c = 1, 2, 3
a, b = b, a    # 交换，无需临时变量
```

---

### 列表

```python
lst = [3, 1, 4, 1, 5, 9]

lst.append(2)       # 末尾追加
lst.insert(0, 0)    # 指定位置插入
lst.pop()           # 弹出末尾元素
lst.remove(1)       # 删除第一个匹配值
lst.sort()          # 原地排序
sorted(lst)         # 返回新列表，原列表不变
lst[::-1]           # 反转（不修改原列表）

# 列表推导式
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

---

### 字典

字典（`dict`）的内置方法可分为三类。基础操作：

```python
d = {"name": "Alice", "age": 25}
d["city"] = "Beijing"   # 直接赋值添加/修改
"name" in d             # 检查键是否存在 → True
```

#### 1. 访问与遍历数据

*   **`.get(key, default)` —— 安全地获取值**

    直接用 `dict[key]` 时若键不存在会 `KeyError`；`.get()` 不存在时返回默认值（默认 `None`），保证程序不崩溃。
    ```python
    d = {'name': 'Alice', 'age': 25}
    print(d.get('name'))           # 输出: Alice
    print(d.get('gender', '未知')) # 输出: 未知
    ```

*   **`.items()` —— 同时遍历键和值**

    调用 `.items()` 会返回一个视图对象，内容是所有键值对组成的元组：
    ```python
    raw_vocab = {'low': 5, 'lower': 2, 'newest': 6, 'widest': 3}
    # raw_vocab.items() 大致等于：
    # [('low', 5), ('lower', 2), ('newest', 6), ('widest', 3)]

    for word, freq in raw_vocab.items():
        print(word, freq)  # word='low', freq=5 ...
    ```
    `word, freq` 这种写法叫**解包（Unpacking）**：自动把元组的第一个元素赋给 `word`，第二个赋给 `freq`。

    如果只写 `for item in raw_vocab:`，Python 默认只遍历**键**，要拿值还需额外写 `freq = raw_vocab[item]`，远不如 `.items()` 简洁。

*   **`.keys()` —— 获取所有的键**

    返回包含所有键的视图，常用于判断键是否存在或遍历。
    ```python
    print(d.keys())  # dict_keys(['name', 'age'])
    ```

*   **`.values()` —— 获取所有的值**

    返回包含所有值的视图，通常用于数值统计（求和、找最大值等）。
    ```python
    print(d.values())  # dict_values(['Alice', 25])
    ```

#### 2. 添加与修改数据

*   **`.update(other_dict)` —— 批量更新合并**

    将另一个字典批量更新到当前字典。键已存在则覆盖，键不存在则新增。
    ```python
    d = {'a': 1, 'b': 2}
    d.update({'b': 99, 'c': 3})
    print(d)  # {'a': 1, 'b': 99, 'c': 3}
    ```

*   **`.setdefault(key, default)` —— 取值并设置默认值**

    键存在则返回其值；键不存在则插入 `key: default` 并返回 `default`。
    ```python
    d = {'a': 1}
    val = d.setdefault('b', 0)  # 'b' 不存在，插入 'b': 0 并返回 0
    ```

#### 3. 删除与清理数据

*   **`.pop(key, default)` —— 提取并删除**

    删除指定键并返回其值。不提供 `default` 且键不存在会报错。
    ```python
    d = {'a': 1, 'b': 2}
    val = d.pop('a')
    # val 等于 1，d 变成了 {'b': 2}
    ```

*   **`.popitem()` —— 弹出最后一项**

    删除并返回最后插入的键值对（`(key, value)` 元组）。常用于破坏性地遍历字典。
    ```python
    d = {'a': 1, 'b': 2}
    item = d.popitem()  # item 等于 ('b', 2)
    ```

*   **`.clear()` —— 清空字典**

    删除字典中所有元素，使其变为空字典 `{}`。

---

### 字符串操作

> **字符串是不可变的（Immutable）**：所有方法都不修改原字符串，而是返回一个新字符串。

**切片**（与列表通用的语法）：

```python
s = "Hello, World!"
s[0:5]    # 'Hello'
s[-6:]    # 'orld!'
s[::-1]   # 反转 → '!dlroW ,olleH'
```

**f-string**（推荐的格式化方式）：

```python
name, score = "Alice", 98.5
f"{name} 得了 {score:.1f} 分"  # 'Alice 得了 98.5 分'
```

字符串方法分为四类：

#### 1. 拆分与拼接

*   **`.split(sep)` —— 拆分成列表**

    按分隔符切分为列表，不传参数则按空白字符切分。
    ```python
    "a,b,c".split(",")  # ['a', 'b', 'c']
    ```

*   **`.join(iterable)` —— 将列表拼成字符串**

    `.split()` 的逆操作，用当前字符串作"胶水"拼合序列。
    ```python
    "-".join(['2024', '05', '01'])  # '2024-05-01'
    ```

#### 2. 清理与替换

*   **`.strip(chars)` —— 去除首尾字符**

    默认去除两端空白（空格、`\n`、`\t`）；可指定字符。`.lstrip()` / `.rstrip()` 只去一侧。
    ```python
    "  hello \n".strip()  # 'hello'
    ```

*   **`.replace(old, new, count)` —— 替换子串**

    将 `old` 替换为 `new`，`count` 可限制替换次数。
    ```python
    "I like apple".replace("apple", "banana")  # 'I like banana'
    ```

#### 3. 大小写转换

*   **`.lower()` / `.upper()` —— 全转小 / 大写**
    ```python
    "Hello".lower()  # 'hello'
    "Hello".upper()  # 'HELLO'
    ```

*   **`.capitalize()` / `.title()` —— 首字母大写**

    `.capitalize()` 只让整串第一个字母大写；`.title()` 每个单词首字母都大写。
    ```python
    "hello world".title()  # 'Hello World'
    ```

#### 4. 查找与判断

*   **`.find(sub)` —— 查找子串位置**

    返回子串起始索引（从 0 开始），找不到返回 `-1`。
    ```python
    "hello".find("e")  # 1
    "hello".find("x")  # -1
    ```

*   **`.startswith(prefix)` / `.endswith(suffix)` —— 判断开头 / 结尾**
    ```python
    "pic.jpg".endswith(".jpg")  # True
    ```

*   **`.isdigit()` / `.isalpha()` / `.isalnum()` —— 内容成分判断**

    依次判断字符串是否全由数字、全由字母、全由数字+字母组成。
    ```python
    "12345".isdigit()   # True
    "123.45".isdigit()  # False（含小数点）
    ```

---

### 条件与循环

```python
# 三元表达式
label = "偶数" if x % 2 == 0 else "奇数"

# for + enumerate（同时拿索引和值）
for i, v in enumerate(["a", "b", "c"]):
    print(i, v)

# for + zip（并行遍历）
for name, score in zip(names, scores):
    print(name, score)

# while + else（循环正常结束才执行 else）
i = 0
while i < 5:
    i += 1
else:
    print("循环结束")
```

---

### 函数基础

```python
def greet(name, greeting="你好"):
    """默认参数放在后面"""
    return f"{greeting}，{name}！"

# 可变位置参数
def total(*args):
    return sum(args)

# 可变关键字参数
def show(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

# 调用时强制关键字参数（* 后的参数必须用关键字传入）
def connect(host, *, port=8080, timeout=30):
    ...
```

---

## 二、进阶层

### 推导式进阶

```python
# 嵌套推导式（矩阵展平）
matrix = [[1,2,3],[4,5,6]]
flat = [x for row in matrix for x in row]  # [1,2,3,4,5,6]

# 集合推导式
unique_lens = {len(w) for w in ["hi", "hello", "hey"]}

# 字典推导式（反转键值）
inv = {v: k for k, v in d.items()}

# 生成器表达式（惰性求值，省内存）
gen = (x**2 for x in range(10**6))
next(gen)   # 按需取值
```

---

### 解包与星号

```python
first, *rest = [1, 2, 3, 4, 5]
# first=1, rest=[2,3,4,5]

*init, last = [1, 2, 3, 4, 5]
# init=[1,2,3,4], last=5

# 函数调用时解包
def add(a, b, c): return a + b + c
args = [1, 2, 3]
add(*args)          # 等价于 add(1,2,3)

kw = {"a":1, "b":2, "c":3}
add(**kw)           # 等价于 add(a=1,b=2,c=3)
```

---

### lambda 与高阶函数

```python
# lambda：单行匿名函数
square = lambda x: x ** 2

# sorted 自定义排序键
people = [{"name":"Bob","age":30},{"name":"Alice","age":25}]
sorted(people, key=lambda p: p["age"])

# map / filter（现代 Python 更推荐推导式，但要认识这两个）
list(map(lambda x: x*2, [1,2,3]))      # [2,4,6]
list(filter(lambda x: x>2, [1,2,3,4])) # [3,4]
```

---

### 文件操作

```python
# 推荐用 with，自动关闭文件
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()          # 全文读取
    lines = f.readlines()       # 按行读取为列表

with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.writelines(["a\n","b\n"])

# 逐行迭代（大文件友好）
with open("big.txt") as f:
    for line in f:
        process(line.rstrip())
```

---

### 异常处理

```python
try:
    result = 10 / x
except ZeroDivisionError:
    print("除数不能为零")
except (TypeError, ValueError) as e:
    print(f"类型或值错误：{e}")
else:
    print("没有异常时执行")     # try 成功才执行
finally:
    print("无论如何都执行")     # 清理资源用这里

# 主动抛出
raise ValueError("参数不合法")
```

---

### 常用标准库速查

```python
# collections
from collections import Counter, defaultdict, deque

Counter("abracadabra")          # {'a':5,'b':2,'r':2,'c':1,'d':1}
Counter(words).most_common(3)   # 最高频的 3 个

dd = defaultdict(list)          # 取不存在的键自动返回 []
dd["new_key"].append(1)         # 不会 KeyError

dq = deque([1,2,3], maxlen=5)
dq.appendleft(0)                # 两端 O(1) 操作

# itertools
from itertools import chain, product, combinations, permutations
list(chain([1,2],[3,4]))        # [1,2,3,4]
list(product("AB", repeat=2))   # AA AB BA BB

# pathlib（推荐替代 os.path）
from pathlib import Path
p = Path("data") / "input.txt"
p.exists()
p.read_text(encoding="utf-8")
p.parent / "output.txt"
```

---

## 三、高级层

### 装饰器

```python
import functools

def timer(func):
    @functools.wraps(func)      # 保留原函数签名
    def wrapper(*args, **kwargs):
        import time
        t = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} 耗时 {time.perf_counter()-t:.4f}s")
        return result
    return wrapper

@timer
def slow():
    import time; time.sleep(0.1)

# 带参数的装饰器（再包一层）
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello(): print("hi")
```

---

### 生成器

```python
# yield 把函数变成生成器
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5): print(x)

# send() 向生成器传值
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None: break
        total += value

gen = accumulator()
next(gen)           # 启动生成器
gen.send(10)        # 发送 10，返回累计值
gen.send(20)        # 返回 30
```

---

### 上下文管理器

```python
# 方式一：实现 __enter__ / __exit__
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self
    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start

with Timer() as t:
    expensive_op()
print(t.elapsed)

# 方式二：contextlib（更简洁）
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("获取资源")
    yield          # with 块在这里执行
    print("释放资源")
```

---

### 类与魔术方法

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):             # 开发者友好的字符串表示
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):       # v1 + v2
        return Vector(self.x+other.x, self.y+other.y)

    def __len__(self):              # len(v)
        return 2

    def __getitem__(self, idx):     # v[0], v[1]
        return (self.x, self.y)[idx]

# dataclass（省去样板代码）
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    tags: list = field(default_factory=list)  # 可变默认值必须用 field
```

---

### 类型注解

```python
# 基本注解（运行时不强制，但 IDE 和 mypy 会检查）
def add(a: int, b: int) -> int:
    return a + b

# 复杂类型
from typing import Optional, Union, List, Dict, Tuple

def search(query: str, top_k: int = 10) -> List[Dict[str, float]]:
    ...

def parse(val: Union[str, int]) -> Optional[float]:
    ...

# Python 3.10+ 可用 | 替代 Union
def f(x: str | int | None) -> float | None: ...
```

---

### 并发简介

```python
# threading：I/O 密集型任务
import threading

def task(name):
    print(f"{name} 开始")

threads = [threading.Thread(target=task, args=(f"T{i}",)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()

# multiprocessing：CPU 密集型任务（绕过 GIL）
from multiprocessing import Pool

with Pool(4) as p:
    results = p.map(heavy_compute, data_list)

# asyncio：高并发 I/O（协程）
import asyncio

async def fetch(url):
    await asyncio.sleep(1)   # 模拟 I/O 等待
    return url

async def main():
    results = await asyncio.gather(fetch("a"), fetch("b"), fetch("c"))

asyncio.run(main())
```

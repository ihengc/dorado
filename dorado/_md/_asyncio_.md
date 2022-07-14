# asyncio
## asyncio源码分析

相关概念:
1) 用`async`声明的方法会被包装成`Future`对象

从`asyncio.run()`方法开始：
1) 获取`_RunningLoop`，`_RunningLoop`此时必须为`None`
2) 判断传入的`main`方法是否为协程
3) 创建事件循环，并获取到时间循环对象
```python
def run(main):
    loop = events.new_event_loop()
    return loop.run_util_complete(main)
```


`Future`对象:
`Future`表示任务执行的结果，任务被放入事件循环中后，执行的时机是不确定的，因此何时能获取到执行的结果也是不确定的。
`Future`对象的构造很简单。
`asyncio`包中的`Future`与`concurrent`包中的`Future`类似。
1) `cancelled()`用于确定`Future`对象当前是否可以被取消。
    `Future`对象会被赋予多种状态,是否可以被取消就是状态的判断。
2) `add_done_callback`
3) ``

`run_util_complete`方法分析：  
```python
def run_util_complete(future):
    run_forever()
    return future.result()
```
```python
def run_forever():
    while True:
        run_once()

```
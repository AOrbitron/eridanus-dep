## 介绍
eridanus-dep是一个轻量化的onebot v11 sdk。

eridanus-dep是Eridanus的依赖包，它是Eridanus的核心库，提供了一系列的工具和模块，可以帮助开发者快速开发自己的onebot应用。

[Eridanus](https://github.com/avilliai/Eridanus)是基于eridanus-dep开发的onebot应用，你可以在Eridanus中找到很多有用的模块和工具，如函数调用、事件用例、插件管理、数据库连接等。

由于Eridanus是基于eridanus-dep开发的，所以你可以通过参考Eridanus的源码来学习eridanus-dep的使用方法。
## 安装
```cmd
pip install eridanus-dep
或
pip install --upgrade eridanus-dep
```
## 示例
```python

from Eridanus.adapters.websocket_adapter import WebSocketBot
from Eridanus.event.events import GroupMessageEvent

bot = WebSocketBot('ws://127.0.0.1:3001')
#bot = WebSocketBot('ws://127.0.0.1:3001',blocked_loggers=["DEBUG", "INFO_MSG"]) #像这样屏蔽指定logger

@bot.on(GroupMessageEvent)
async def _(event: GroupMessageEvent):
    print(event)
    await bot.send(event, 'Hello, world!')

bot.run()
```
## 文档
[Eridanus文档](https://eridanus-doc.netlify.app/)

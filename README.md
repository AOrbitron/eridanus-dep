## 介绍
eridanus-dep是一个轻量化的onebot v11 sdk，整体风格参考了[yirimirai](https://yiri-mirai.wybxc.cc/)

[Eridanus](https://github.com/avilliai/Eridanus)是基于eridanus-dep开发的onebot应用，你可以通过参考Eridanus的源码来了解eridanus-dep的使用方法。
## 安装
```cmd
pip install eridanus-dep
或
pip install --upgrade eridanus-dep
```
需要开启onebot实现的正向ws端口3001，access_token留空不要设置。
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

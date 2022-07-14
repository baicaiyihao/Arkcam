# Arkcam资产探测系统

* [前言](#前言)
* [环境配置](#环境配置)
  * [redis](#redis)
  * [mongodb](#mongodb)
* [开发日志](#开发日志)

## 前言

感觉现在不管是做些什么总会想到自动化工具能够帮助自己轻松完成任务，所以想根据自己的一些想法写一个自动化的系统来进行资产的收集和管理。

## 环境配置

### redis

redis免安装版下载
下载地址：https://github.com/tporadowski/redis/releases

redis图形化工具
下载地址：https://hub.fastgit.xyz/lework/RedisDesktopManager-Windows/releases/tag/2022.4

redis启动命令：
`redis-server.exe redis.windows.conf`

### mongodb

mongodb下载地址：https://www.mongodb.com/try/download/community

配置配置文件`mongod.cfg`

内容：

    systemLog:
    destination: file
    path: D:\MongoDB\log\mongod.log
    storage:
    dbPath: D:\MongoDB\data\db

然后进行cmd配置
`mongod.exe --config "D:\MongoDB\mongod.cfg" install`

后续使用

`net start MongoDB`

`net stop MongoDB`

进行开启和关闭

## 开发日志
这个项目也算是自己的一个学习过程，顺便记录一下开发中遇到的一些问题和自己的想法~

2022-06-14 内容会逐渐更新。。

2022-06-17 项目是想了一段时间打算开始的，最近花了几天时间理清楚了大概的系统模型是什么样的。主要包括django+mongodb+celery+redis，目前正在想前端和后端如何合理的交互问题，下周应该可以完成一个初始的系统功能。

功能主要为基于字典的子域名探测，大概构思是可以有以下自定义功能：

1. 自定义字典的上传
2. 自定义字典生成的规则
3. 自定义字典生成所需的关键字

再基于已有的关键字自我生成字典然后发现更多新的子域名信息。

2022-07-06

由于对前后端结合开发不太熟悉所以学习了一段时间，近期会慢慢开始更新。

2022-07-08

由于对前端不太熟悉，所以放弃了前端模板的自我开发采用了开源的前端模板，暂用当前的前端模板了。后续再进行修改。
目前主要将登录功能以及目录访问权限进行完善，后续就是各项功能的一个开发和完善了。

2022-07-12

由于对前端的不熟悉，所以走动的歪路有点多并且会有点迷茫不知道怎么做。
对于前后端数据交互的问题使用的ajax来进行前后端数据交互，也算是解决了目前来说最大的难题，因为一直都在迷茫怎么将前后端数据进行交互。现在解决前后端数据交互问题之后，后续的一些后端功能开发的话会慢慢跟上进度。

2022-07-13

由于之前用的前端对目前来说修改起来有点困难，所以更换了前端的模板。目前对后端的用户功能更基本开发完成，后续考虑的时资产的收录以及资产探测脚本的执行交互问题。
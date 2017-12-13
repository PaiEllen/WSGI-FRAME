## WSGI框架架构开发平台

> WSGI API 项目

## 目录 ##

>[项目简介](#项目简介)

>[开发依赖](#开发依赖)

>[目录结构](#目录结构)

## <span id="项目简介">项目简介</sapn>

	本框架是一个WSGI框架，主要开发组件有eventlet+Paste+Pastedeploy+route+webob,各模块功能如下:
	
- eventlet: python 的高并发网络库
- paste.deploy: 用于发现和配置 WSGI application 和 server 的库
- routes: 处理 http url mapping 的库
- webob: 处理HTTP请求并提供了一个对象来方便的处理返回response消息

settings 文件存放了一些全局变量

manager/urls 文件存放路由信息，按原格式来

conf/config.ini 为pastedeploy配置文件做application和server库的映射关系

主要依赖软件如下图所示


## <span id="开发依赖"> 开发依赖 </span> ##

1. webob==1.7.3
2. simplejson==3.11.1
3. paste==2.0.3
4. enum-compat==0.0.2
5. eventlet==0.21.0
6. greenlet==0.4.12
7. PasteDeploy==1.5.2
8. Python-memcached==1.58

** 详细参阅依赖文件 requirement.txt

## <span id="目录结构"> 项目目录结构介绍 </span>

wsgi_fram

> app
	
   - app     ——application处理存放目录
     
     - api   ——业务逻辑处理接口
     
     - controllers  ——业务逻辑处理程序
     
     - forms	——数据效验
     
     - models	——数据层处理程序
     
     - utils	--公用模块目录
     
> backend  --存放实现校验会话中间件的源代码存放目录

   - Log  --日志处理程序
   
   - form --数据校验源代码

   - middleware --过滤中间件源代码

   - session  --session 源代码

> conf  --存放所以pastedeloy配置文件（*.ini)

   - config.ini  


> manager  --主管理配置文件，服务文件，全局文件

   - urls.py --URL,访问路径
   - settings --全局环境
   - wsgi --中间件

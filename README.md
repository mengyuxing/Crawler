# OuterChain.py
1. 网站外链扫描功能
2. 输入网址格式检测及补全
3. 随机浏览器代理
4. 舍弃无用链接
5. 外链网页状态检测

# 使用方法
调用OuterChain模块中的run函数
```
a = OuterChain('www.xxx.com').run()
print(a)
```

# 返回结果
```
[{'url': 'http://www.xxxx.com', 'status': 200},
 {'url': 'http://www.xxxxxx.com', 'status': 404},]
```

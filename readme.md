# 中文车牌识别web

基于开源项目[HyperLPR](https://github.com/szad670401/HyperLPR)构建。

在其基础上提供了http调用的接口，便于你在其他的项目中调用。

并且提供了易于使用的web页面，便于调试或日常使用。

详情翻阅[https://github.com/szad670401/HyperLPR](https://github.com/szad670401/HyperLPR)

## 安装需求  
 
### 运行平台  
* ✔ Python 3.6+  
* ✔ Ubuntu 16.04
* ✔ ️Ubuntu 18.04
* ✔ CentOS 7   
* ✔ Docker   

Windows和MacOS系统下可通过构建Docker镜像来使用，暂不支持直接部署使用  
其他Linux平台暂未测试，可自行安装测试  

### 最低配置要求  
* CPU:    1核  
* 内存:    2G  
* SWAP:   2G  

## 安装说明  
### 服务器部署
1. 安装python3.7  
    推荐使用miniconda
    
2. 安装依赖包  
``` shell script
pip install -r requirements.txt
```  

3. 运行  
项目默认运行在8090端口：  
``` shell script
python backend/main.py [--port=8090]
# --port 指定运行时端口号 默认是8090
```

看到以下输出则代表安装成功： 
```shell script
Server is running: http://192.168.0.18:8090
```   

### Docker部署  
使用 Dockerfile 构建 或者直接 Pull镜像  
```shell script
# dockerfile 构建
docker build -t hyperlrweb:latest .

# 运行镜像
docker run -itd --rm -p 8090:8090 --name hyperlrweb hyperlrweb:latest 
```  

```shell script
# 从 dockerhub pull
docker pull litterguy/hyperlrweb:latest

# 运行镜像
docker run -itd --rm -p 8090:8090 --name hyperlrweb litterguy/hyperlrweb:latest 
```  
这里把容器的8090端口映射到了物理机的8090上，但如果你不喜欢映射，去掉run后面的`-p 8090:8090` 也可以使用docker的IP加`8090`来访问  


##pip 生成和安装requirements.txt

1. 生成文件

```
pip freeze > requirements.txt
```

2. 从requirements.txt安装依赖库
```
pip install -r requirements.txt
```

参考项目：

   - [HyperLPR](https://github.com/szad670401/HyperLPR)
   - [TrWebOCR](https://github.com/alisen39/TrWebOCR)
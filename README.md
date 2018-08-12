### 说明

事件中继的消费者客户端

### 环境

Openwrt + Python 2

### 部署方式

1. 先把 Openwrt 的串口配置好，驱动装好，确保 /dev 下有 ttyUSB0，这里我是用 Wrtnode 1 插了个 USB 转 UART （Wrtnode 1 只有一个串口还死活用不了）。
2. 安装 python, pip，还有 nohup。(Openwrt  下的安装方法具体自己搜搜吧- -没记录)
```
opkg install python python-pip coreutils-nohup
```
3. 安装依赖
```
pip install -r requirements.txt
```
4. 修改 config.py ，把里面的相关配置填好
5. 运行
```
./start.sh
```
6. 推荐在 crontab 里加上守护任务
```
crontab -e
```
```
* * * * * sh /root/eventbridge/deamon.sh
```

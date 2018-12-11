### docker-restart
- Docker for Windowsのテスト用コンテナを再起動するだけ。

### 使い方
```
$ py --version
Python 3.7.1

$ py docker-restart.py
############ SHOW CONTAINER ############
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                                        NAMES
167b60f682c3        master:0006         "/sbin/init"        6 minutes ago       Up 6 minutes        0.0.0.0:2222->22/tcp, 0.0.0.0:8080->80/tcp   master
cbd125ba6b0f        slave3:0005         "/sbin/init"        6 minutes ago       Up 6 minutes        0.0.0.0:2225->22/tcp, 0.0.0.0:8083->80/tcp   slave3
28509d5f430d        slave2:0005         "/sbin/init"        6 minutes ago       Up 6 minutes        0.0.0.0:2224->22/tcp, 0.0.0.0:8082->80/tcp   slave2
c37da914fce3        slave1:0005         "/sbin/init"        6 minutes ago       Up 6 minutes        0.0.0.0:2223->22/tcp, 0.0.0.0:8081->80/tcp   slave1
############ STOP CONTAINER ############
--- start ---
167b60f682c3
cbd125ba6b0f
28509d5f430d
c37da914fce3
--- end ---
############ REMOVE CONTAINER ############
--- start ---
167b60f682c3
cbd125ba6b0f
28509d5f430d
c37da914fce3
--- end ---
############ SHOW CONTAINER ############
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
############ START CONTAINER ############
e5a94b16b43b2b45897f90ad6aa527086ed1832f9c1ef77f5397bfaa36c6b80b
08bf757d0fb018e22ae011b34e85bc3d1986627bae6984813c0510641f87a3f0
6e83553323dfcc35a76936806994c3a6688d9b2bf7c189f0048e7617888c7079
81ebcb1dd2a1087d0a1e059360e96f7520e1baaa851de1966e472de63ac7ea2f

```
- うまくいかないときはDocker for Windows自体をrestartしてあげる

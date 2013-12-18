#coding: utf-8
#端口: 角色1位, 集群号1位, 实例号2位, 主从端口一样
#proxy      22xxx
#redis      20xxx
#sentinel   21xxx


#we will gen:
#port
#pidfile
#logfile
#dir

#path in the deploy machine
binarys = {
    'redis_server' : '/home/ning/idning-github/redis/src/redis-server',
    'redis_cli' : '/home/ning/idning-github/redis/src/redis-cli',
    'redis_sentinel' : '/home/ning/idning-github/redis/src/redis-sentinel',
    'nutcracker' : '/home/ning/Desktop/t/nutcracker-0.2.4/output/bin/nutcracker',
}

cluster0 = {
    'user': 'ning',
    'redis': [
        # host:port, install path
        ('127.0.0.5:20000', '/tmp/redis-20000'), ('127.0.0.5:30000', '/tmp/redis-30000'), #(示例配置, 主从端口分别用2xxxx/3xxxx)
        ('127.0.0.5:20001', '/tmp/redis-20001'), ('127.0.0.5:30001', '/tmp/redis-30001'),
        #('127.0.0.5:20002', '/tmp/redis-20002'), ('127.0.0.5:30002', '/tmp/redis-30002'),
        #('127.0.0.5:20003', '/tmp/redis-20003'), ('127.0.0.5:30003', '/tmp/redis-30003'),
        #('127.0.0.5:20004', '/tmp/redis-20004'), ('127.0.0.5:30004', '/tmp/redis-30004'),
    ],
    'sentinel':[
        ('127.0.0.5:21001', '/tmp/sentinel-21001'),
        ('127.0.0.5:21002', '/tmp/sentinel-21002'),
        ('127.0.0.5:21003', '/tmp/sentinel-21003'),
    ]
    'nutcracker': [
        # host:port, install path
        ('127.0.0.5:22000', '/tmp/nutcracker-22000'),
        ('127.0.0.5:22001', '/tmp/nutcracker-22001'),
        ('127.0.0.5:22002', '/tmp/nutcracker-22002'),
        #...
    ],
}


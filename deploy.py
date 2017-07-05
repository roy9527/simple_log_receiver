import os
import gevent.monkey
gevent.monkey.patch_all()
import multiprocessing

bind='127.0.0.1:8000' #绑定的端口

pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'
accesslog = 'log/access.log'

#启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1 
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'

debug=True
proc_name='gunicorn.pid'
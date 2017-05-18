import json


# s = "{'code': '906', 'MODEL': 'OPPO+R7s', 'BRAND': 'OPPO', 'VERSION': '4.4.4', 'token': '0'}"
# s = s.replace('\'', "\"")
# print(json.loads(s))

tokens = []
tokens_ = []
all_token=[]
models=[]
all_models=[]

with open('/home/ubuntu/workspace/simple_log_receiver/log/access.log', 'r') as f:
    while 1:
        line = f.readline()
        if not line:
            break
        else:
            line =  line.strip()
            if line.startswith('{'):
                line = line.replace('\'', "\"")
                lj = json.loads(line)
                code = lj['code']
                # print(code)
              	tt = lj['token']
                m = lj['MODEL']
                if not m in all_models:
                    all_models.append(m)
                if not tt in all_token:
                    all_token.append(tt)
                if code == '906':
                    if not m in models:
                        #print(lj)
                        models.append(m)
                    t = lj['token']
                    if not t in tokens:
                        tokens.append(t)
                elif code == '1024':
                    t = lj['token']
                    if not t in tokens_:
                        tokens_.append(t)
                elif code == '1025':
                    t = lj['token']
                    if not t in tokens_:
                        tokens_.append(t)

print('----------------')
print('success : ' + str(len(tokens)))
print('----------------')
print('failed  : '+ str(len(tokens_)))
print('----------------')
print('total   : '+ str(len(all_token)))
print('----------------')
print('success model : '+ str(len(models)))
print('----------------')
print('total model   : '+ str(len(all_models)))
print('----------------')
for m in models:
    print(m)

print('----------------')

for m in all_models:
    print(m)

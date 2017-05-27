import json


# s = "{'code': '906', 'MODEL': 'OPPO+R7s', 'BRAND': 'OPPO', 'VERSION': '4.4.4', 'token': '0'}"
# s = s.replace('\'', "\"")
# print(json.loads(s))

ok_token_s = set([])
all_token_s = set([])
ok_model_s = set([])
all_model_s = set([])
ok_version_s = set([])

json_s = set([])

tmp_s = set([])

error_s = set([])

retry_s = set([])
index = 0
with open('/home/ubuntu/workspace/simple_log_receiver/log/access.log', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('{'):
            line = line.replace('\'', "\"")
            lj = json.loads(line)
            t = lj['token']
            all_token_s.add(t)
        if '/v1get_file' in line:
            s = line[line.find('Android'):-1]
            tmp_s.add(s)
            print(line)
with open('/home/ubuntu/workspace/simple_log_receiver/log/05201246_json_list.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if '/v1get_file' in line:
            s = line[line.find('Android'):-1]
            tmp_s.add(s)

#    for line in f:
#        line = line.rstrip()
#        if line.startswith('{'):
#            line = line.replace('\'', "\"")
#            lj = json.loads(line)
#            code = lj['code']
#            t = lj['token']
#            m = 'model:' + lj['MODEL'] + ' | brand:'+ lj['BRAND'] + ' | version:' + lj['VERSION']
#            v = lj['VERSION'].decode('utf-8')
#            all_token_s.add(t)
#            all_model_s.add(m)
#            json_s.add(line)

#            if code == '906':
#                ok_token_s.add(t)
#                ok_model_s.add(m)
#            elif code == '1001' or code == '1002':
#                tmp_s.add(t)
#            elif code == '1025':
#                error_s.add(t)
#            elif code == '1024':
#                retry_s.add(t)

dup_s = set([])
#for t in all_token_s:
#    if t in ok_token_s and t in tmp_s:
#        dup_s.add(t)
print(index)
print('---------------------------')
print('download token  : ' + str(len(tmp_s) ))
print('---------------------------')
print('failed token  : ' + str(len(error_s)))
print('---------------------------')
print('retry failed token  : ' + str(len(retry_s)))
print('---------------------------')
print('retry success token  : ' + str(len(dup_s)))
print('---------------------------')
print('success_token / all_token : ' + str(len(ok_token_s)) + '/'+ str(len(all_token_s))) 
print('---------------------------')
print('success_model / all_model : ' + str(len(ok_model_s)) + '/'+ str(len(all_model_s)))
print('---------------------------')

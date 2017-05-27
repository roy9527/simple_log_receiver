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
with open('/home/ubuntu/workspace/simple_log_receiver/log/access05201246.log', 'r') as f:

    for line in f:
        line = line.rstrip()
        if line.startswith('{'):
            line = line.replace('\'', "\"")
            lj = json.loads(line)
            code = lj['code']
            t = lj['token']
            m = 'model:' + lj['MODEL'] + ' | brand:'+ lj['BRAND'] + ' | version:' + lj['VERSION']
            v = lj['VERSION'].decode('utf-8')
            all_token_s.add(t)
            all_model_s.add(m)
            json_s.add(line)
            if code == '906':
                ok_token_s.add(t)
                ok_model_s.add(m)
                if lj['MODEL'].startswith('OPPO+R7'):
                    tmp_s.add(t)
                if not v.startswith("4."):
                    ok_version_s.add('model:' + lj['MODEL'] + ' | brand:'+ lj['BRAND'] + ' | version:' + lj['VERSION'])            

with open('05201246_json_list.txt', 'a') as model:
    for m in json_s:
        model.write(m + '\n')
#for v in ok_version_s:
#    print(v + '\n')

print('---------------------------')

print('success_R7s:' + str(len(tmp_s)) + ' | success_Other:' + str(len(ok_token_s) - len(tmp_s)))

print('---------------------------')

print('success_token / all_token : ' + str(len(ok_token_s)) + '/'+ str(len(all_token_s))) 

print('---------------------------')

print('success_model / all_model : ' + str(len(ok_model_s)) + '/'+ str(len(all_model_s)))

print('---------------------------')

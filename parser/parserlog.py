import json


# s = "{'code': '906', 'MODEL': 'OPPO+R7s', 'BRAND': 'OPPO', 'VERSION': '4.4.4', 'token': '0'}"
# s = s.replace('\'', "\"")
# print(json.loads(s))

ok_token_s = set([])
all_token_s = set([])
ok_model_s = set([])
all_model_s = set([])
with open('/Users/roy/py_workspace/eiffelLog/log/access.log', 'r') as f:

    for line in f:
        line = line.rstrip()
        if line.startswith('{'):
            line = line.replace('\'', "\"")
            lj = json.loads(line)
            code = lj['code']
            t = lj['token']
            m = 'model:' + lj['MODEL'] + ' | brand:'+ lj['BRAND'] + ' | version:' + lj['VERSION']

            all_token_s.add(t)
            all_model_s.add(m)
            if code == '906':
                ok_token_s.add(t)
                ok_model_s.add(m)
            



print('success_token / all_token : ' + str(len(ok_token_s)) + '/'+ str(len(all_token_s))) 
print('success_model / all_model : ' + str(len(ok_model_s)) + '/'+ str(len(all_model_s)))
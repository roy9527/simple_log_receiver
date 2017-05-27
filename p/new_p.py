import json


# s = "{'code': '906', 'MODEL': 'OPPO+R7s', 'BRAND': 'OPPO', 'VERSION': '4.4.4', 'token': '0'}"
# s = s.replace('\'', "\"")
# print(json.loads(s))

success_tokens = []
all_tokens = []
success_model = []
tmp_model = []
tmp_all_model = []
with open('/home/ubuntu/workspace/simple_log_receiver/log/access.log', 'r') as f:

    for line in f:
        line = line.rstrip()
        line = line.replace('\'', "\"")
        if line.startswith('{'):
            lj = json.loads(line)
            code = lj['code']
            t = lj['token']
            m = lj['MODEL']
            if not t in all_tokens:
                all_tokens.append(t)
            else:
                if not t in tmp_model:
                    tmp_model.append(t)

print('success_token / all_token : ' + str(len(tmp_model)) + '/'+ str(len(all_tokens))) 

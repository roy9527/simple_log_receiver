
str = '127.0.0.1 - - [21/May/2017:00:11:20 +0000] "GET /log/v1get_file HTTP/1.0" 200 - "-" "Dalvik/1.6.0 (Linux; U; Android 4.4.4; OPPO R7s Build/KTU84P) | 135460651835791822"'

if 'Android' in str:
    s = str[str.find('Android'):-1]
    print(s)


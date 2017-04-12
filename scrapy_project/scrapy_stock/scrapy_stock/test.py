import json
import time

# if __name__ == '__main__':
#     with open('../../../temp/00001.jl') as f:
#         for line in f:
#             data = json.loads(line)
#             print(data['ticktime'],' ', data['trade'])


if __name__ == '__main__':
    t=time.localtime(1491803890)
    print(t)
    print(time.time())
"""
json : JavaScript对象标记，本质上是一种轻量级的数据交换格式
优势：易于阅读，易于解析，跨语言交换数据。传输效率高
字符串是json的载体（表现形式），符合json格式的字符串称为json字符串
反序列化
"""
import json
import re

json_str = '{"name":"yanzuwu", "age": 18}'  # 因为json是一种跨语言的格式，内部需用双引号
student = json.loads(json_str)  # loads函数作用是将json数据类型，转换为python的数据类型
print(student)  # 类型是字典，字典和json定义的格式相似，但有本质的区别
#  同一个json字符串，不同的语言可能会解释成不同的数据类型，如上述json字符串，python将它变为字典，但在javascript里是对象
json_str2 = '[{"name":"yanzuwu", "age": 18},{"name":"tingfeng", "age": 21}]'
# json_str2 这个json字符串代表着2个object对象的数组
person = json.loads(json_str2)
print(type(person), person)  # list，元素为dict
# 由字符串到某种语言的解析过程，称为反序列化

str1 = 'get callback msg: 20009_ISS_SR_MSG_Result, wParam: 0, lParam: {"intent":{"cid":"NULL","moreResults":[],' \
       '"normal_text":"车内太闷了","operation":"SET","rc":0,"score":0,"searchSemantic":{"action":"OPEN","name":"天窗",' \
       '"nameValue":"LITTLE","operation":"SET","service":"carControl"},"search_semantic":{"action":"OPEN",' \
       '"name":"天窗","nameValue":"LITTLE","operation":"SET","service":"carControl"},"semantic":{"slots":{' \
       '"action":"OPEN","name":"天窗","nameValue":"LITTLE"}},"service":"carControl",' \
       '"sid":"cida70b37bf@dx000b127c63ae01003c","text":"车内太闷了","uuid":"cida70b37bf@dx000b127c63ae01003c"}} '

# 处理语义实例


def print_result(str_result):
    result = re.search('"intent":({.*)}', str_result).group(1)
    nli_result = json.loads(result)
    text_result = nli_result['text']
    operation_result = nli_result['operation']
    semantic_result = nli_result['semantic']
    service_result = nli_result['service']
    sid_result = nli_result['sid']

    return text_result, operation_result, semantic_result, service_result, sid_result


text, operation, semantic, service, sid = print_result(str1)
print(' text:', text, '\n', 'operation:', operation, '\n', 'semantic:', semantic, '\n', 'service:', service, '\n', 'sid:', sid)




# 实现公共断言
def common_assert(obj,result,except_result=0):
    obj.assertEqual(except_result, result['errno'])
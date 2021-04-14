from api.user_manager import UserManager
import unittest

class TestUserManagerCase(unittest.TestCase):

    id01 = 1001


    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManager()
        cls.new_user = 'testy02'


    # case1:只输入用户名和密码，请求添加管理员接口
    def test01_add_user(self):
        # 1. 初始化数据
        username = 'testk02'
        password = 'testk02'

        # 2.请求接口(添加管理员)，输入的参数就是用户名和密码
        actul_result = self.user.add_user(username,password)
        data = actul_result.get('data')
        if data:
            user_id = data.get('id')
        if user_id:
            TestUserManagerCase.id01 = user_id
        # 3.进行断言
        self.assertEqual(0,actul_result['errno'])
        self.assertEqual(username,actul_result['data']['username'])


    # case2 : 编辑管理员
    def test02_edit_user(self):

        actual_result = self.user.edit_user(TestUserManagerCase.id01,self.new_user,'123456')
        self.assertEqual(0, actual_result['errno'])
        self.assertEqual(self.new_user, actual_result['data']['username'])


    # case3 : 查询管理员
    def test03_search_user(self):
        actual_result = self.user.get_user()
        self.assertEqual(0, actual_result['errno'])
        self.assertEqual(self.new_user,actual_result['data']['list'][0]['username'])


    # case4 :删除管理员
    def test04_delete(self):

        actual_result = self.user.delete_user(TestUserManagerCase.id01)
        self.assertEqual(0,actual_result['errno'])




if __name__ == '__main__':
    unittest.main()



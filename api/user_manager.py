"""
主要完成管理员接口的实现
"""
from loguru import logger
from api.base import Base


class UserManager(Base):



    def __init__(self):
        self.add_user_path = '/admin/admin/create'
        self.delete_user_path = '/admin/admin/delete'
        self.edit_user_path = '/admin/admin/update'
        self.get_user_path = '/admin/admin/list?page=1&limit=20&sort=add_time&order=desc'
        # self.b = Base()
        # self.login('admin123','admin123')    # 临时用来做测试 。




    #添加管理员
    def add_user(self,username,password,**kwargs):
        user_data = {'username':username,'password':password}
        if kwargs:
            logger.info("添加管理员接收可选参数为:{}".format(kwargs))
            user_data.update(**kwargs)
        add_path = self.get_url(self.add_user_path)
        return self.post(add_path,user_data)




    #删除管理员
    def delete_user(self,id,**kwargs):
        del_data = {'id':id}
        if kwargs:
            del_data.update(**kwargs)
        del_path = self.get_url(self.delete_user_path)
        return self.post(del_path,del_data)



    #编辑管理员
    def edit_user(self,id,username,password,**kwargs):
        edit_data = {'id':id,'username':username,'password':password}
        if kwargs:
            edit_data.update(**kwargs)
        edit_path = self.get_url(self.edit_user_path)
        return self.post(edit_path,edit_data)


    #查询管理员
    def get_user(self):
        search_path = self.get_url(self.get_user_path)
        return self.get(search_path)


if __name__ == '__main__':
    um = UserManager()
    um.add_user('testgg01','testgg01')
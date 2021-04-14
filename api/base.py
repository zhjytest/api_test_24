
"""
主要实现的是基础接口的封装 。
"""
import requests

from setting import BASE_URL
from loguru import logger
from cacheout import Cache

cache = Cache()

class Base():



    # 实现url拼接
    def get_url(self,path,params=None):
        """
        功能：返回一个完整的url
        eg :  http://ip:port/接口地址/参数
        :param path : 接口地址
        :param params : 查询参数
        :return:
        """
        if params:
            full_url  = BASE_URL + path +'?' + params
            logger.info("接口地址：{}".format(full_url))
            return full_url
        return BASE_URL + path


    # 定义get方法
    def get(self,url):
        """
        作用：主要是对requests.get()进行封装，目的就是满足我们后面的需求
        :return:
        """
        result = None
        response = requests.get(url,headers=self.get_headers())
        try:
            result = response.json()
            logger.debug("请求接口地址：{}，请求接口返回结果:{}".format(url,result))
            return result
        except Exception as e:
            logger.error("请求get方法异常，返回数据：{}".format(result))


    # 定义post方法
    def post(self,url,data):
        """
        作用：主要是对requests.post()进行封装，目的就是满足我们后面的需求
        :return:
        """
        result = None
        response = requests.post(url,json=data,headers=self.get_headers())
        try:
            result = response.json()
            logger.debug("请求接口地址:{}，请求接口返回结果:{}".format(url,result))
            return result
        except Exception as e:
            logger.error("请求post方法异常，返回数据：{}".format(result))


    # 定义请求头的处理
    def get_headers(self):
        headers = {'Content-Type':"application/json"}
        token = cache.get('token')
        if token:
            headers.update({'X-Litemall-Admin-Token':token})
        logger.warning("请求头信息返回数据:{},注意：多数接口时需要带着token参数".format(headers))
        return headers



    # 定义登录
    def login(self,username,password):
        login_path = '/admin/auth/login'
        login_url = self.get_url(login_path)
        login_data = {'username':username,'password':password}
        result = self.post(login_url,login_data)
        try:
            if 0 == result.get('errno'):
                logger.info("请求登录接口成功")
                token = result.get('data').get('token')
                cache.set('token',token)
            else:
                logger.error('请求登录接口失败:{}'.format(result))
        except Exception as e:
            logger.error('请求登录接口返回异常，异常数据:{}'.format(result))



if __name__ == '__main__':
    b = Base()
    # print(b.get_url('/admin/admin/list','q=iphone'))
    print(b.login('admin123','admin123'))
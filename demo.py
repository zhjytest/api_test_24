
"""
这是一个演示文件，不是框架内部的代码
"""

def demo():
    headers = {'Content-Type': "application/json"}
    header1 = {'X-Litemall-Admin-Token':'kfdsfdsfdsfksdfdskfkdsfjksdfkdsfsdf'}
    headers.update(header1)
    return headers


print(demo())
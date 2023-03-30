
def get_crazy_functionals():
    from crazy_functions.读文章写摘要 import 读文章写摘要
    from crazy_functions.生成函数注释 import 批量生成函数注释
    from crazy_functions.解析项目源代码 import 解析项目本身
    from crazy_functions.解析项目源代码 import 解析一个Python项目
    from crazy_functions.解析项目源代码 import 解析一个C项目的头文件
    from crazy_functions.解析项目源代码 import 解析一个C项目
    from crazy_functions.高级功能函数模板 import 高阶功能模板函数
    from crazy_functions.代码重写为全英文_多线程 import 全项目切换英文

    return {
        "[实验] Please parse and deconstruct the project itself": {
            "Function": 解析项目本身
        },
        "[Experiment] Parsing the whole py project (withinput输入框）": {
            "Color": "stop",    # 按钮颜色
            "Function": 解析一个Python项目
        },
        "[Experiment] Parsing the entire C++ project header file (withinput输入框）": {
            "Color": "stop",    # 按钮颜色
            "Function": 解析一个C项目的头文件
        },
        "[Experiment] Parsing an entire C++ project (withinput输入框）": {
            "Color": "stop",    # 按钮颜色
            "Function": 解析一个C项目
        },
        "[Lab] Read tex paper writing abstract (withinput输入框）": {
            "Color": "stop",    # 按钮颜色
            "Function": 读文章写摘要
        },
        "[Experiment] Batch Generation of Function Comments (withinput输入框）": {
            "Color": "stop",    # 按钮颜色
            "Function": 批量生成函数注释
        },
        "[Experiment] Switching the source code of this project to full English (multi-threaded)demo）": {
            "Function": 全项目切换英文
        },
        "[Experiment] Today in History (Higher Order Functional Template Functions)demo）": {
            "Function": 高阶功能模板函数
        },
    }




# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# 数据有类型,但是变量没有类型

print(type(print_hi))
# print(int("123.0"))
print(float("123.333"))
print(str(1234))
print("dsfds","dsfdsfdsfds")
# 标识符 变量 类 方法名字 大小写敏感 数字 英文 下划线 变量：全部小写 单词之间用_ 不是驼峰


print("dsds"*50)
print("%s" % "dsfd")
print("%34d" % 22.4)
 # 字符串拼接不能像java那样自动拼接 比如字符串和数字的+会报错
# print(f"dsfds"+11)  字符格式化所有的格式格式化为字符串 也可以进行精度控制 {heighe:10.5f} 10个宽度加上5位小数
name="DSSSSS"
message=f"dsfd{name}"
print(message)
# 比较运算符： 小写字母>大写字母>数字
print("a">str(12))

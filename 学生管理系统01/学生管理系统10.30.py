# 1.学生的信息（名字，学号，课程成绩）
#    功能类
# 1.添加学生信息包括删除
# 2.根据学号添加学生成绩
# 3.据学号查询学生成绩
# 4.计算学生成绩平均成绩
# 5.列出所用学生信息
# 6.提供菜单选项

# 定义一个学生类
class Student:
    def __init__(self, name, student_id, **course):
        self.name = name
        self.student_id = student_id
        self.course = course

    def __str__(self):
        return f'学生姓名：{self.name}\t学号：{self.student_id}\n学生学科{self.course}'

    def add_course_grade(self, course, grade):
        self.course[course] = grade


#  功能
class Way:
    # 保存学生信息
    def __init__(self):
        self.student_list = []

    # # 1.添加学生 姓名 学号
    # def add_student(self):
    #     name = input('请输入学生姓名：')
    #     student_id = input('请输入学生学号：')
    #     self.student_list.append(Student(name, student_id))
    # todo 用于测试
    # 1.添加学生 姓名 学号
    def add_student(self, name, student_id):
        name = name
        student_id = student_id
        self.student_list.append(Student(name, student_id))

    # 2.删除
    def delete(self):
        a = input('请输入删除学生姓名：')
        for i in self.student_list:
            if i.name == a:
                self.student_list.remove(i)
                print('删除成功')
            else:
                print('没有这个学生')

    # 3.添加学生成绩
    # def add_course(self):
    #
    #     a = input('请输入学生学号：')
    #     if len(self.student_list) != 0:
    #
    #         for i in self.student_list:
    #             if i.student_id == a:
    #                 course = input('请输入科目：')
    #                 course_grade = input('请输入科目成绩：')
    #                 i.add_course_grade(course, course_grade)
    #
    #
    #             else:
    #                 print('学号错误')
    #     else:
    #         print('目前没有学生信息')

    def add_course(self, id, course, course_grade):
        id = id
        if len(self.student_list) != 0:
            for i in self.student_list:
                if i.student_id == id:
                    course = course
                    course_grade = course_grade
                    i.add_course_grade(course, course_grade)


                else:
                    print('学号错误')
        else:
            print('目前没有学生信息')

    # 4.计算平均成绩（全部的）#todo 多个学生 计算的是全部平均值(没有意义)，如何实现对相同类的科目计算平均值
    #                     1.用字典 key为科目values为该科目的总分
    def x(self):
        total = 0
        num = 0
        for i in self.student_list:
            kind_course_grade_average = {}  # 存储key-科目 values-科目总成绩
            for key, values in i.course:
                #todo 11月4号 如何解决key的值计算并保留在字典中？
                kind_course_grade_average[key]=values
                total += int(values)
                num += 1
                # print(f'全部平均成绩{total / num}')
                print(f'全部平均成绩{"%.2f" % (total / num)}')

    # 5.列出所用学生信息
    def get(self):
        for i in self.student_list:
            print(i)

    # 提供菜单选项
    @staticmethod  # 静态方法   不会用到类的属性和方法  单独只为了输出一些字符串，跟类相关的信息
    def show_help():
        print('-' * 40)
        print('1.添加学员信息')
        print('2.删除学员信息')
        print('3.添加学员成绩')
        print('4.计算平均成绩')
        print('5.列出所用学生信息')
        print('6.退出系统')
        print('-' * 40)

    def user(self):
        while True:
            self.show_help()
            a = input('请输入你要执行的操作编号：')
            if a == '1':
                # self.add_student()
                # todo 下面三行代码用于测试
                self.add_student('小美', 12)
                self.add_student('小张', 13)
                self.add_student('小王', 14)
            elif a == '2':
                self.delete()
            elif a == '3':
                # self.add_course()
                # todo 下面三行代码用于测试
                self.add_course(12, '数学', 120)
                self.add_course(12, '语文', 97)
                self.add_course(13, '语文', 130)
                self.add_course(13, '数学', 125)
                self.add_course(14, '语文', 125)
                self.add_course(14, '数学', 75)
                self.add_course(14, '英语', 65)

            elif a == '4':
                self.x()
            elif a == '5':
                self.get()
            elif a == '6':
                break


w = Way()
w.user()

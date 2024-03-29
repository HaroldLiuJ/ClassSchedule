import random
import re

from dataStructure.CourseTable import CourseTable


class Class:

    noSchedule = []
    teacherList = []
    dayNum = 0
    lessonNum = 0
    def __init__(self, classNo, dayNum, lessonNum):
        self.teachers = []
        self.classNo = classNo
        self.courseTable = CourseTable(dayNum, lessonNum)
        self.dayNum = dayNum
        self.lessonNum = lessonNum

    @classmethod
    def setNoSchedule(cls, noSchedule):
        cls.noSchedule = noSchedule
    @classmethod
    def setTeacherList(cls, teacherList):
        cls.teacherList = teacherList
    @classmethod
    def getDayNum(cls):
        return cls.dayNum
    @classmethod
    def getLessonNum(cls):
        return cls.lessonNum

    def getTeachers(self, totalLessonNum):
        if not self.teacherList:
            raise Exception("老师列表未初始化")
        else:
            for teacher in self.teacherList:
                if self.classNo in teacher.Class:
                    self.teachers.append(teacher)
        lessonNum = 0
        for teacher in self.teachers:
            lessonNum += teacher.originTeachHour
        if lessonNum + len(self.noSchedule) == totalLessonNum:
            pass
        elif lessonNum + len(self.noSchedule) > totalLessonNum:
            raise Exception(str(self.classNo) + "班的课时数超过一周总课时数，差值为：" + str(lessonNum + len(self.noSchedule) - totalLessonNum))
        else:
            raise Exception(str(self.classNo) + "班的课时数不足一周总课时数，差值为：" + str(totalLessonNum - lessonNum - len(self.noSchedule)))

    def allocatable(self, day, teacher):
        num = 0
        for i in range(1, self.courseTable.lessonNum + 1):
            if self.courseTable.table[i][day] == teacher:
                num += 1
        if num > 2:
            return False
        else:
            return True

    def allocate(self, day, lesson, teacher):
        self.courseTable.table[lesson][day] = teacher

    def getARandomTeacher(self):
        if len(self.teachers) > 1:
            index = random.randint(0, len(self.teachers) - 1)
            return self.teachers[index], index
        else:
            return self.teachers[0], 0

    def getCourseTable(self):
        table = []
        for i in range(1, self.courseTable.lessonNum + 1):
            day = []
            for j in range(1, self.courseTable.dayNum + 1):
                day.append(self.courseTable.table[i][j].subject)
            table.append(day)
        return table

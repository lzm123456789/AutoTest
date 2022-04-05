# coding=utf-8
import openpyxl
from Log import log

log = log.MyLog


class ReadExcel:
    """读取excel文件"""

    def __init__(self, file, sheetName, headerList):
        """
        :param file: excel文件含绝对路径
        :param sheetName: sheet页名称
        :param headerList: excel表头组成的列表
        """

        self.file = file
        self.sheetName = sheetName
        self.headerList = headerList

    def get_dict_from_excel(self):
        """获取的数据结构为列表+字典，每一列是一个字典"""

        testdata = []
        try:
            keys = self.headerList
            workbook = openpyxl.load_workbook(self.file)
            sheet = workbook[self.sheetName]
            for row in sheet.rows:
                tempDict = {}
                for index, cell in enumerate(row):
                    tempDict[keys[index]] = cell.value
                testdata.append(tempDict)
            testdata = testdata[1:]
            return testdata
        except Exception as e:
            log.error('读取excel失败，具体原因：' + str(e))
            return testdata

    def get_tuple_from_excel(self):
        """ 获取的数据结构为列表+元组，每一列是一个元组"""

        testdata = []
        try:
            workbook = openpyxl.load_workbook(self.file)
            sheet = workbook[self.sheetName]
            for row in sheet.rows:
                tempList = []
                for cell in row:
                    tempList.append(cell.value)
                    tempTuple = tuple(tempList)
                testdata.append(tempTuple)
            testdata = testdata[1:]
            return testdata
        except Exception as e:
            log.error('读取excel失败，具体原因：' + str(e))
            return testdata

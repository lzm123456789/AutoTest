# coding=utf-8
import xlrd
import xlutils.copy


class RWExcel:
    def __init__(self, excel_file):
        self.excel = excel_file

    def get_information_from_excel(self, sheet_index, x, y):
        a = xlrd.open_workbook(self.excel)
        b = a.sheet_by_index(sheet_index)
        return b.cell(x, y).value

    def write_to_excel(self, sheet_index, x, y, text):
        xls_object = xlrd.open_workbook(self.excel, formatting_info=True)
        xls_copy = xlutils.copy.copy(xls_object)
        sheet = xls_copy.get_sheet(sheet_index)
        sheet.write(x, y, text)
        xls_copy.save(self.excel)

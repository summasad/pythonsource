from openpyxl import Workbook
#엑셀 저장 함수

def write_excel_template(filename,sheetname,listdata):
    wb = Workbook()
    ws = wb.active

    # 제목열 너비 조절
    ws.column_dimensions["A"].width = 100
    # 시트명 변경
    ws.title = sheetname
    # 데이터 추가
    for item in listdata:
        ws.append(item)

    wb.save("./" + filename)
    wb.close()

# test 코드
if __name__ == "__main__":
    listdata = [
        [1,10,8,5,14,26,12],
        [2,7,1,7,3,12,20],
        [3,5,7,9,2,8,19],
        [4,5,8,9,6,8,19],
    ]
    write_excel_template("temp1.xlsx","test",listdata)
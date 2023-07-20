# @Author  yuhaotian
# @date  2023/7/7 8:42
# @version  1.0


import xlrd

# def get_excel(filename,sheet_name):
#     work_book = xlrd.open_workbook(filename)
#     # 全部的sheet
#     res = work_book.sheets()
#     work_sheet = work_book.sheet_by_name(sheet_name)     #获取sheet页面
#     col_values = work_sheet.col_values(0)  #行
#
#     print(col_values)
#     row_values = work_sheet.row_values(0)  #列
#     print(row_values)




    # list1 = []
    # # res = work_sheet.cell(7,0)      #第7行第一列
    # # print(res)
    # # for i in range(1,8):
    # #     res1 = work_sheet.cell(i,9)     # 第一行第九列
    #     # print(res1)
    #     # res2 = work_sheet.cell(i,11)
    #     # print(res2)
    # for one in range(1,len(work_sheet.col_values(0))):
    #     res1 = work_sheet.cell(one, 9)
    #     res2 = work_sheet.cell(one, 11)
    #     list1.append((res1,res2))
    # print(list1)


    # get_excel()
# if __name__ == '__main__':
#     get_excel('../data/Delivery_System_V1.5.xls','登录模块')


# def get_excel(filename, sheet_name,rowname,*args):
#     work_book = xlrd.open_workbook(filename)
# #     # 全部的sheet
# #     res = work_book.sheets()
#     work_sheet = work_book.sheet_by_name(sheet_name)  # 获取sheet页面
# #     col_values = work_sheet.col_values(0)  # 行
# #     # print(col_values)
# #     row_values = work_sheet.row_values(0)  # 列
# #     # print(row_values)
#     collist = work_sheet.row_values(0)
#     indexlist = []
#     list3 = []
#     list2 = work_sheet.col_values(0)
#     for one in list2:
#         rowlist = []
#         if rowname in one:
#             index1 = list2.index(one)
#             for i in args:
#                 index3 = collist.index(i)
#                 res1 = work_sheet.cell(index1, index3)
#                 rowlist.append(res1)
#         if rowlist !=[]:
#             list3.append(tuple(rowlist))
#     print(list3)
# if __name__ == '__main__':
#     get_excel('../data/Delivery_System_V1.5.xls','我的商铺','listshopping',*['用例编号','标题','优先级'])







# def get_excel(filename, sheet_name,case_name,*args,run_case=None):
#     work_book = xlrd.open_workbook(filename)
#     work_sheet = work_book.sheet_by_name(sheet_name)  # 获取sheet页面
#     col_index = []
#     alls = work_sheet.row_values(0)
#     for i in args:
#         col_index.append(alls.index(i))
#     # print(col_index)
#     run_case_list=[]
#     if 'all' in run_case:
#         run_case_list = work_sheet.col_values(0)
#     else:
#         for one in run_case:
#             if '-' in one:
#                 start, end = one.split('-')
#                 for i in range(int(start),int(end)+1):
#                     run_case_list.append(case_name+f'{i:0>3}')
#             else:
#                 run_case_list.append(case_name+f'{one:0>3}')
#
#     all = []
#     row = 0
#     for name in work_sheet.col_values(0):
#         for i in run_case_list:
#             if case_name in name and name in i:
#                 sa = []
#                 for j in col_index:
#                     sa.append(work_sheet.cell(row,j).value)
#                 all.append(tuple(sa))
#         row+=1
#     print(all)
#
# if __name__ == '__main__':
#     get_excel('../data/Delivery_System_V1.5.xls','我的商铺','listshopping',*['用例编号','标题','优先级'],run_case=['001','003-005'])
#
#




import json
def get_excel(sheet_name,case_name,*args,run_case=None):
    if run_case is None:
        run_case = ['all']
    filename = '../data/Delivery_System_V1.5.xls'
    work_book = xlrd.open_workbook(filename)
    work_sheet = work_book.sheet_by_name(sheet_name)
    alls = work_sheet.row_values(0)
    col_index = []
    for i in args:
        if i in alls:
            col_index.append(alls.index(i))
    run_case_list = []
    if 'all' in run_case:
        run_case_list = work_sheet.col_values(0)
    else:
        for one in run_case:
            if '-' in one:
                start,end = one.split('-')
                for zz in range(int(start),int(end)+1):
                    run_case_list.append(case_name+f'{zz:0>3}')
            else:
                run_case_list.append(case_name+f'{one:0>3}')
    all = []
    row = 0
    for name in work_sheet.col_values(0):
        for i in run_case_list:
            if case_name in name and name in i:

                sa =[]
                for j in col_index:
                    need = is_json(work_sheet.cell(row,j).value)
                    # try:
                    #     need1 = json.loads(need)
                    # except:
                    #     sa.append(need)
                    # else:
                    #     sa.append(need1)
                    sa.append(need)
                all.append(tuple(sa))
        row+=1

    return all
def is_json(in_str):
    try:
        return json.loads(in_str)
    except:
        return in_str


if __name__ == '__main__':
    res = get_excel('登录模块', 'Login', *['请求参数', '响应预期结果'])
    # print(res)
    # get_excel('我的商铺','listshopping',*['用例编号','优先级','响应预期结果'],run_case=['001','003-005'])

































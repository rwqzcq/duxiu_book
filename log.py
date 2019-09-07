import os
import csv
import json
import time

class DuxiuLog:
    '''
    负责存储日志文件和数据文件
    '''
    def __init__(self, log_name):
        '''
        :Args:
         - log_name: 日志文件名字
         - full_name: csv文件名字
        '''

        self.csv_path = os.path.join(os.path.abspath('./dataset'), log_name + '.csv')
        self.is_exist = True
        

    # def get_log(self):
    #     '''
    #     获取日志文件
        
    #     :Returns:
    #      - Boolean False 不存在日志文件
    #     '''
    #     if self.is_exist == False:
    #         return False
    #     else:
    #         with open(self.log_path, encoding = "UTF-8") as f:
    #             data = f.read()
    #             return json.loads(data)

    # def check(self, filename):
    #     '''
    #     检查当前爬取的论文是否存在于日志中
    #     改方法不建议使用
    #     '''
    #     data = self.get_log()
    #     if data == False:
    #         return False # 不存在
    #     paper_log = data[filename]
    #     if paper_log['error'] == 1:
    #         return False # 存在但是出错了
    #     else:
    #         return True # 不存在
    
    # def write_log(self, data):
    #     '''
    #     写入日志文件
    #     '''
    #     data = json.dumps(data)
    #     with open(self.log_path, 'w+') as f:
    #         f.write(data)
    
    def get_full_csv(self):
        '''
        获取csv文件中的内容
        '''
        data = []
        try:
            with open(self.csv_path, encoding = "UTF-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
        finally:
            return data
        
    def update_csv(self, new_data):
        '''
        更新csv文件中的内容
        '''
        data = self.get_full_csv()
        # 合并
        data.extend(new_data) # 不用返回
        xuhao = 1
        headers = ["xuhao", "book_name", 'author', 'chubanshe', 'jianjie', 'zhutici', 'fenlei']
        with open(self.csv_path, 'w', newline='', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            for row in data:
                # 重新整理index
                row['xuhao'] = xuhao
                writer.writerow(row)
                xuhao += 1
    
    # def update_log(self, new_log):
    #     '''
    #     更新日志json文件
        
    #     :Args:
    #      - new_data: dict
    #     '''
    #     if new_log == {}:
    #         print("没有新日志数据")
    #         return False
    #     current_log = self.get_log() # 读取日志文件
    #     if current_log != False: # 当前有日志文件
    #         log = dict(current_log, **new_log) # 合并
    #     else: # 没有日志文件
    #         log = new_log # 新的日志当做总的
    #     if log != {}:
    #         self.write_log(log)
    #         return True


        

    # def use(self, obj_name):
    #     '''
    #     注入对象
    #     '''
    #     pass
    # def use_db(self):
    #     '''
    #     实例化一个数据库对象
    #     '''
    #     return JournalDb()
    
        

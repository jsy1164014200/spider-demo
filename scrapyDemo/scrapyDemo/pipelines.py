# Don't forget to add your pipeline to the ITEM_PIPELINES setting

import json


class ItcastPipeline(object):
    def __init__(self):
        self.filename = open("teacher.json","w",encoding="utf-8")
        
    def process_item(self,item,spider):
        jsontext = json.dumps(dict(item),ensure_ascii=False)
        self.filename.write(jsontext + '\n')
    # 结束时调用
    def close_spider(self,spider):
        self.filename.close()
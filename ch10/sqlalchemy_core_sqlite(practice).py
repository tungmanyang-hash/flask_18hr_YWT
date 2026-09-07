#----------practice start------------
import sqlalchemy as db

#連接資料庫
path_to_db = "./db/chinook.db"
table = 'genres'   # 表格名稱
# 建立資料庫引擎
engine = db.create_engine(f'sqlite:///{path_to_db}')
# 建立資料庫連線
connection  = engine.connect()

# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
metadata = db.MetaData()
print(f"metadata: \n{metadata.sorted_tables}")

# 取得 genres 資料表的 Python 對應操作物件
table_genres = db.Table(table, metadata, autoload_with=engine)
print(f"metadata: \n{metadata.sorted_tables}",end="\n"+("-"*80)+"\n")  # 比較Table建立前後的metadata 


# SELECT fetchall
query = db.select(table_genres).select_from(table_genres)
proxy = connection.execute(query)
results = proxy.fetchall()
print(results,end="\n"+("-"*80)+"\n")

# Close connection & engine
connection.close()
engine.dispose()
#----------practice end--------------





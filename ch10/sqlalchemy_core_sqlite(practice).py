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


# SELECT fetchone
query = db.select(table_genres).select_from(table_genres)
proxy = connection.execute(query)
for _ in range(30):
    results = proxy.fetchone()
    print(results)
print("-"*80)


# SELECT Specific Columns(抓特定欄位：Name/GenreId。大小寫有差)
query = db.select(table_genres.c.GenreId).select_from(table_genres)
proxy = connection.execute(query)
results = proxy.fetchall()
print(results,end="\n"+("-"*80)+"\n")

# SELECT where(找出特定哪一筆，如下：Latin)
query = db.select(table_genres).select_from(table_genres).where(table_genres.c.Name=="Latin")
proxy = connection.execute(query)
results = proxy.fetchall()
print(results,end="\n"+("-"*80)+"\n")

# SELECT limit & offset(跳過前兩個，取接下來的四個)
query = db.select(table_genres).select_from(table_genres).limit(4).offset(2)
proxy = connection.execute(query)
results = proxy.fetchall()
print(results,end="\n"+("-"*80)+"\n")


# INSERT(新增 Name=Funk 的欄位)
query = db.insert(table_genres).values(Name='Funk')
connection.execute(query)
connection.commit()

# UPDATE(把 GenreId=9 的 Name 改成 K-pop)
query = db.update(table_genres).where(table_genres.c.GenreId == 9).values(Name='K-pop')
connection.execute(query)
connection.commit()

# INSERT (新增 Funk2,Funk3,Funk4,Funk5,Funk6 的欄位)
for value in ['Funk2','Funk3','Funk4','Funk5','Funk6']:
    query = db.insert(table_genres).values(Name=value)
    connection.execute(query)
    connection.commit()


# DELETE
query = db.delete(table_genres).where(table_genres.c.GenreId > 28)
connection.execute(query)
connection.commit()


# Close connection & engine
connection.close()
engine.dispose()
#----------practice end--------------





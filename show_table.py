def show_table(cur, sp):
    print("<<テーブル一覧>>\n")
    cur.execute("select * from sqlite_master where type='table'")
    for item in cur.fetchall():
        print(item)
    print("="*sp)
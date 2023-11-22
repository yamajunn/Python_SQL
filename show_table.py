def show_table(cur, sp):
    print("<<テーブル一覧>>\n")
    cur.execute("select * from sqlite_master where type='table'")
    table_count = 0
    for item in cur.fetchall():
        print(item[1])
        table_count += 1
    print("-"*sp)
    print(f"テーブル数: {table_count}")
    print("="*sp)
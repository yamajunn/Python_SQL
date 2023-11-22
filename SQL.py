import sqlite3
import numpy as np
from create_table import create_table
from show_table import show_table
from show_help import show_help

# data.sqlite3を作成する
# すでに存在していれば、それにアスセスする。
dbname = 'data.sqlite3'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

sp = 100
OK_DICT = {
    "OK0": ["SQLを終了", "0", "exit", "終了"],
    "OK1": ["ヘルプ一覧を表示   ", "1", "help", "helps", "ヘルプ", "ヘルプ一覧"],
    "OK2": ["テーブル一覧を表示   ", "2", "table", "tables", "テーブル", "テーブル一覧"],
    "OK3": ["テーブルを作成   ", "3", "create table", "テーブル作成"],
    }

print("="*sp)
while True:
    num = input(">> ")
    if num in OK_DICT["OK0"]:
        print("<<バイバイ>>")
        break
    elif num in OK_DICT["OK1"]:
        show_help(OK_DICT, sp)
    elif num in OK_DICT["OK2"]:
        show_table(cur, sp)
    elif num in OK_DICT["OK3"]:
        create_table(cur, sp)
    else:
        print("<<無効な値>> 1 でヘルプ")
        print("="*sp)

# データベースへのコネクションを閉じる。(必須)
cur.close()
conn.close()
import sqlite3
import numpy as np
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
        print("<<テーブルを作成>>")
        column_list = np.array([])
        while True:
            table_name = input("テーブル名 >> ")
            print("<<カラム名を入力　';'で完了>>")

            while True:
                column_name = input("カラム名 >> ")
                if column_name == ";":
                    break
                column_list = np.append(column_list, column_name)

            while True:
                print("<<これで完了ですか？>>")
                create_bool = input("y/n >> ")
                if create_bool == "y" or create_bool == "n":
                    break
                else:
                    print("<< y か n を入力>>")
            if create_bool == "y":
                print("<<作成完了>>")
                break
            else:
                while True:
                    print("<<何か入力し直しますか？>>\n1: テーブル名\n2: カラム\n3: いいえ")
                    select_num = input("番号を入力 >> ")
                    if select_num == "1":
                        table_name = input("テーブル名 >> ")
                    elif select_num == "2":
                        while True:
                            print("<<どのカラムを修正しますか？>>")
                            for i, item in enumerate(column_list):
                                print(f"{i}: {item}")
                            print(f"{len(column_list)}: <新しく追加>")
                            print(f"{len(column_list)+1}: <修正しない>")
                            select_num = input("番号を入力 >> ")
                            if select_num.isdecimal():
                                if int(select_num) == len(column_list):
                                    print("<<カラム名を入力　';'で完了>>")
                                    while True:
                                        column_name = input("カラム名 >> ")
                                        if column_name == ";":
                                            break
                                        column_list = np.append(column_list, column_name)
                                elif int(select_num) == len(column_list)+1:
                                    break
                                else:
                                    column_name = input("カラム名 >> ")
                                    column_list[int(select_num)] = column_name
                            else:
                                print("<<無効な値>>")
                    elif select_num == "3":
                        break
                    else:
                        print("<<無効な値>>")
                print("<<作成完了>>")
                break
    else:
        print("<<無効な値>> 1 でヘルプ")
        print("="*sp)

# データベースへのコネクションを閉じる。(必須)
cur.close()
conn.close()
import numpy as np
def create_table(cur, sp):
    print("<<テーブルを作成>>")
    print("-"*sp)
    column_list = np.array([])
    while True:
        table_name = input("テーブル名 >> ")
        print("-"*sp)
        print("<<カラム名を入力　';'で完了>>")

        while True:
            column_name = input("カラム名 >> ")
            if column_name == ";":
                print("-"*sp)
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
            print("="*sp)
            break
        else:
            while True:
                print("-"*sp)
                print("<<何か入力し直しますか？>>\n1: テーブル名\n2: カラム\n3: いいえ")
                select_num = input("番号を入力 >> ")
                if select_num == "1":
                    print("-"*sp)
                    print("<<テーブル名を入力>>")
                    table_name = input("テーブル名 >> ")
                elif select_num == "2":
                    print("-"*sp)
                    while True:
                        print("-"*sp)
                        print("<<どのカラムを修正しますか？>>")
                        for i, item in enumerate(column_list):
                            print(f"{i}: {item}")
                        print(f"{len(column_list)}: <新しく追加>")
                        print(f"{len(column_list)+1}: <修正しない>")
                        select_num = input("番号を入力 >> ")
                        if select_num.isdecimal() and int(select_num) <= len(column_list)+1:
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
                                print("-"*sp)
                                column_name = input("カラム名 >> ")
                                column_list[int(select_num)] = column_name
                        else:
                            print("<<無効な値>>")
                elif select_num == "3":
                    print("-"*sp)
                    break
                else:
                    print("<<無効な値>>")
            print("<<作成完了>>")
            print("="*sp)
            break
    column_str = ""
    for i, item in enumerate(column_list):
        if i == len(column_list)-1:
            column_str += f"'{item}'"
        else:
            column_str += f"'{item}',"
    cur.execute(f"CREATE TABLE {table_name}({column_str});")
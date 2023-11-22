import numpy as np

def add_column(sp, column_list, second_bool):
    while True:
        while True:
            column_name = input("カラム名 >> ")
            if column_name == "" and second_bool:
                print("-"*sp)
                print("<<カラム名を入力して下さい(最低1つ)>>")
            elif not second_bool:
                break
            else:
                break
        if column_name == ";" and second_bool:
            if len(column_list) == 0:
                print("-"*sp)
                print("<<カラム名を入力して下さい(最低1つ)>>")
                continue
            else:
                print("-"*sp)
                break
        elif column_name != "" and column_name != ";" and column_name[len(column_name)-1] == ";" and second_bool:
            print("-"*sp)
            column_list = np.append(column_list, column_name[:len(column_name)-1])
            break
        elif column_name == "" and not second_bool:
            break
        elif column_name == ";" and not second_bool:
            break
        elif column_name != ";" and column_name[len(column_name)-1] == ";" and not second_bool:
            print("-"*sp)
            column_list = np.append(column_list, column_name[:len(column_name)-1])
            break
        column_list = np.append(column_list, column_name)
    return column_list


def create_table(cur, sp, table_list):
    print("<<テーブルを作成>>")
    print("-"*sp)
    column_list = np.array([])
    while True:
        while True:
            table_name = input("テーブル名 >> ")
            print("-"*sp)
            if table_name in table_list:
                print("<<このテーブル名はすでに使用されています。>>")
            else:
                break
        print("<<カラム名を入力　';'で完了>>")
        column_list = add_column(sp, column_list, True)
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
                    while True:
                        table_name = input("テーブル名 >> ")
                        print("-"*sp)
                        if table_name in table_list:
                            print("<<このテーブル名はすでに使用されています。>>")
                        else:
                            break
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
                                column_list = add_column(sp, column_list, False)
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
def show_help(OK_DICT, sp):
    print("<<ヘルプ一覧>>\n")
    for item in OK_DICT:
        print(f"{OK_DICT[item][1]}: {OK_DICT[item][0]}", end=f"{'　'*(15 - len(OK_DICT[item][0]))}")
        for i, list_item in enumerate(OK_DICT[item]):
            if i != 0:
                print(list_item, end=",  ")
        print()
    print("="*sp)
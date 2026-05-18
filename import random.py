todos=[]
while True:
    print("\n==============할 일 목록===============")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 완료 처리")
    print("4. 삭제")
    print("5. 종료")
    choices=input("매뉴 선택: ")
    if choices == "1":
        task=input("추가할 일 선택: ")
        todos.append({"task":task, "done":False})
        print("할 일이 추가되었습니다.")
    if choices == "2":
        if len(todos)==0:
            print("할 일이 추가되지 않았습니다.")
        else:
            print("\n[할일목록]")
            for i, todo in enumerate(todos):
                statues="완료" if todo["done"] else "미완료"
                print(f"")
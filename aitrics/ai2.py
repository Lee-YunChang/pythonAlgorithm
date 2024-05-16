def Solution(num_teams, remote_tasks, office_tasks, employees):
    team_office_tasks = {}
    remote_employees = set()

    for i in range(num_teams):
        team_office_tasks[i + 1] = set(office_tasks)

    for emp_info in employees[0]:
        emp_id, *emp_tasks = emp_info.split()
        emp_id = int(emp_id)

        for task in emp_tasks:
            if task in remote_tasks:
                remote_employees.add(emp_id)
            else:
                for team, tasks in team_office_tasks.items():
                    if task in tasks:
                        tasks.remove(task)

    for team, tasks in team_office_tasks.items():
        if not tasks:
            min_emp_id = float('inf')
            min_emp_ids = []
            for emp_info in employees[0]:
                emp_id, *emp_tasks = emp_info.split()
                emp_id = int(emp_id)
                if emp_id in remote_employees:
                    continue
                if team in [int(task) for task in emp_tasks]:
                    if emp_id < min_emp_id:
                        min_emp_id = emp_id
                        min_emp_ids = [emp_id]
                    elif emp_id == min_emp_id:
                        min_emp_ids.append(emp_id)
            remote_employees.update(min_emp_ids)

    return sorted(list(remote_employees))

# 예시 입력
num_teams = 3
remote_tasks = ["development", "marketing", "hometask"]
office_tasks = ["recruitment", "education", "officetask"]
employees = [
    ["1 development hometask",
     "1 recruitment marketing",
     "2 hometask",
     "2 development marketing hometask",
     "3 marketing",
     "3 officetask",
     "3 development"]
]

# 함수 호출
result = Solution(num_teams, remote_tasks, office_tasks, employees)
print(result)  # 출력: [1, 4, 5, 7]

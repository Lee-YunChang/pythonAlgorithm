from datetime import datetime, timedelta

# plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
complete_plans = []
proceed = []
complete = []


def add_minutes(time_str, minutes_to_add):

    time_format = "%H:%M"
    time_obj = datetime.strptime(time_str, time_format)
    new_time_obj = time_obj + timedelta(minutes=minutes_to_add)

    return new_time_obj.strftime(time_format)



for item in plans:
    subject, time_str, minutes_str = item
    minutes_to_add = int(minutes_str)
    new_time_str = add_minutes(time_str, minutes_to_add)
    complete_plans.append([subject, new_time_str])

print(complete_plans)

for i in range(len(complete_plans)-1):

    if complete_plans[i][1] < plans[i+1][1]:
        proceed.append(plans[i][0])
    else:
        complete.append(plans[i][0])

print(complete)
print(proceed)




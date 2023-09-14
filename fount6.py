
def solutions(reqs):

    bank = []
    res = []
    for operation in reqs:
        parts = operation.split()
        if len(parts) == 3:
            action, account, amount = parts
            if action == "DEPOSIT":
                if bank:
                    for item in bank:
                        if item.get("account") == account:
                            item["amount"] = int(item["amount"]) + int(amount)
                            res.append("200")
                        else:
                            res.append("404")
                else:
                    res.append("404")
            elif action == "CREATE":
                if bank:

                    for item in bank:
                        if item.get("account") == account:
                            res.append("403")
                        else:
                            create_dict = {"account": account, "amount": amount}
                            bank.append(create_dict)
                            res.append("200")
                else:
                    create_dict = {"account": account, "amount": amount}
                    bank.append(create_dict)
                    res.append("200")

            elif action == "WITHDRAW":
                if bank:
                    for item in bank:
                        if item.get("account") == account:

                            if int(item["amount"]) < int(amount):
                                res.append("403")
                            else:
                                item["amount"] = int(item["amount"]) - int(amount)
                                res.append("200")
                        else:
                            res.append("404")
                else:
                    res.append("404")

    return res




reps = ["DEPOSIT 3a 10000", "CREATE 3a 300000", "WITHDRAW 3a 150000", "WITHDRAW 3a 150001"]
result = solutions(reps)
print(result)
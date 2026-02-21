datas = ["java", "JAVA", "java"]

def cehck():
    for data in datas:
        if data.lower() != "java":
            return False
    return True

print(cehck())
def run_pipeline_1():
    print("Analysis1")


def run_pipeline_2():
    return "Analysis2"


def run_pipeline_3(num1, num2):
    print(num1 + num2)


def run_pipeline_4(num1, num2):
    return num1 + num2


run_pipeline_1()
res2 = run_pipeline_2()
print(res2)  # "Analysis2"
run_pipeline_3(2, 7)
res4 = run_pipeline_4(2, 3)
print(res4)

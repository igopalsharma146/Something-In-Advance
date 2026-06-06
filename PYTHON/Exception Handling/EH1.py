print("printing exact error name :")
try:
    x=5/0
except Exception as e:
    print(e.with_traceback())
    print("\n")
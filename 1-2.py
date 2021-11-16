seconds = int(input("enter some seconds: "))

hh = seconds // 3600
seconds = seconds - hh * 3600
mm = seconds // 60
ss = seconds - mm * 60

if hh < 10:
    hh = f"0{hh}"
if mm < 10:
    mm = f"0{mm}"
if ss < 10:
    ss = f"0{ss}"
print(f"{hh}:{mm}:{ss}")
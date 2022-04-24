import time
scale = 10
print("--------执行开始--------")
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    print(f"{c:^3.0f}%[{a}->{b}]")
    time.sleep(0.1)
print(f"{'执行开始':-^{scale*2}}")
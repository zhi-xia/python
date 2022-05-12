import time

scale = 10
start_time = time.perf_counter()
print("--------执行开始--------")
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    run_time = time.perf_counter() - start_time
    print(f"\r{c:^3.0f}%[{a}->{b}]", end="")
    time.sleep(0.1)
print(f"\n{'执行结束':-^{scale * 2}}")
print(f"运行时间：{run_time:.2f}s")

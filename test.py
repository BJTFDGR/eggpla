#TextProBarV3.py
import time
scale = 50

start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c= (i/scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)




def fun(number):
    loaded = number // 9
    loading = number % 9
    symbol = "  ,| ,▏,▎,▍,▌,▋,▊,▉,█".split(",")
    unloaded = (10 - loaded) * symbol[0]
    loaded = loaded * symbol[9]
    if number > 98:
        loading = ''
    else:
        loading = symbol[loading]
    print('\r%d%%' % number, '[' + loaded + loading + unloaded + '] 正在下载...', end="", flush=True)


for i in range(101):
    fun(i)
    time.sleep(0.1)


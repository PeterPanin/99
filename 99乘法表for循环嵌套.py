for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i} = {i*j}\t', end =' ')
    print()
#i=1时，i运行一次，j运行一次，形成1*1=1。i=2时，i运行两次，j运行两次，形成1*2=2，2*2=4以此类推。
#\t:转义字符
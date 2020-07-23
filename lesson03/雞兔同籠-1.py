n = int(input('請輸入共有幾隻雞和兔子:'))#共幾隻
f = int(input('請輸入共有幾隻腳:')) # 總腳數

c = 0 # 雞的個數
r = 0 # 兔子的個數

# block of code ...

r = (f-(n*2))/2
c = n-r
print("雞有 %d 隻, 兔子有 %d 隻" % (c, r))
class Gun:
    def __init__(self, model):
        # 1.枪的型号
        self.model = model

        # 2.枪的子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹的数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了..." % self.model)
            return
        # 2.发射子弹 子弹-1
        self.bullet_count -= 1
        # 3.提示发射情况
        print("[%s] 突突突...." % self.model)

class Soldier:

    def __init__(self, name):
        # 1.姓名
        self.name = name
        # 2.枪 --新兵没有枪
        self.gun = None

ak47 = Gun("AK47")
ak47.add_bullet(30)
ak47.shoot()

xusanduo = Soldier("许三多")
xusanduo.gun = ak47
print(xusanduo.gun.model)
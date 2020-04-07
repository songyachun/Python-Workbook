from sys import exit
from random import randint
from textwrap import dedent


class Scene():
    """ 方案 """

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine():
    """ 引擎 """

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):
    """ 死亡 """

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):
    """ 中央走廊 """

    def enter(self):
        print(dedent(""" 
        The Gothons of Planet Percal #25 have invaded your ship and
        destroyed your entire crew. You are the last surviving
        member and your last mission is to get the neutron destruct
        bomb from the Weapons Armory, put it in the bridge, and 
        blow the ship up after getting into an escape pod.

        You're running down the central corridor to the Weapons 
        Armory when a Gothon jumps out, red scaly skin, dark grimy 
        teeth, and evil clown costume flowing around his hate 
        filled body. He's blocking the door to the Armory and 
        about to pull a weapon to blast you.

        25号行星的野蛮人入侵了你的飞船，摧毁了你所有的船员。你是最后一个幸存的成员，你最后的任务是从武器库中取出中子毁灭炸弹，把它放在舰桥上，然后在进入逃生舱后炸毁飞船。
        
        当你沿着中央走廊跑向武器库的时候，一个怪兽跳了出来，红色的鳞状皮肤，黑色的脏牙，邪恶的小丑服装在他充满仇恨的身体周围流动。他挡住了军械库的门，正准备用武器干掉你。
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent(""" 
            Quick on the draw you yank out your blaster and fire 
            it at the Gothon. His clown costume is flowing and 
            moving around his body, which throws off your aim.
            Your laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his mother 
            bought him, which makes him fly into an insane rage 
            and blast you repeatedly in the face until you are 
            dead. Then he eats you.

            快拔出你的爆能枪，对准目标发射。他的小丑服装在他的身体周围流动和移动，这偏离了你的目标。你的激光击中了他的服装，但完全没有击中他。这完全毁了他妈妈给他买的新衣服，这让他暴跳如雷，不断地朝你的脸上猛轰，直到你死去。然后他吃了你。
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent(""" 
            Like a world class boxer you dodge, weave, slip and 
            slide right as the Gothon's blaster cranks a laser 
            past your head.In the middle of your artful dodge 
            your foot slips and you bang your head on the metal 
            wall and pass out. You wake up shortly after only to 
            die as the Gothon stomps on your head and eats you.

            就像一个世界级的拳击手，你躲闪、迂回、滑倒，当Gothon的激光发射器将一束激光从你的头上转动时，你就会向右滑动。在你巧妙的躲闪中，你的脚滑了一跤，你的头撞在了金属墙上，然后晕了过去。你醒来后不久就死了，因为巨蟒在你头上踩了几脚，把你吃掉了。

            """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
            Lucky for you they made you learn Gothon insults in 
            the academy. You tell the one Gothon joke you konw: 
            Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, 
            fur fvgf nebhaq gur ubhfr. The Gothon stops, tries 
            not to laugh, then busts out laughing and can't move.
            While he's laughing you run up and shoot him square in 
            the head putting him down, then jump through the 
            Weapon Armory door.

            你很幸运，他们让你在学院里学会了哥顿侮辱。你讲了一个你知道的哥特笑话:Lbhe zbgure vf fb sng，jura fur fvgf nebhaq gur ubhfr，fur fvgf nebhaq gur ubhfr。哥顿人停下来，尽量不笑，然后突然大笑起来，一动不动。当他笑的时候，你跑上来，朝他的头开一枪，把他放倒，然后从武器库的门跳过去。
            """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    """ 激光武器库 """

    def enter(self):
        print(dedent("""
        You do a dive roll into the Weapon Armory, crouch and scan 
        the room for more Gothons that might be hiding. It's dead 
        quiet, too quiet. You stand up and run to the far side of 
        the room and find the neutron bomb in its cintainer.
        There's a keypad lock on the box and you need the code to 
        get the bomb out. If you get the code wrong 10 times then 
        the lock closes forever and you can't get the bomb. The 
        code is 3 digits.

        你潜入武器库，蹲伏，扫视房间，寻找更多可能隐藏的怪物。太安静了，太安静了。你站起来，跑到房间的另一边，发现中子弹在烟筒里。盒子上有一个键盘锁，你需要密码把炸弹取出来。如果你的代码错了10次，那么锁就会永远关闭，你就不能得到炸弹了。代码是三位数。
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
            The container clicks open and the seal breaks, letting 
            gas out. You grab the neutron bomb and run as fast as 
            you can to the bridge where you must place it in the 
            right spot.

            容器咔哒一声打开了，封条裂开了，气体漏了出来。你拿起中子弹，以最快的速度跑到桥上，你必须把它放在正确的位置。
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            The lock buzzes one last time and then you hear a 
            sickening melting sound as the mechanism is fussed 
            together. You decide to sit there, and finally the 
            Gothons blow up the ship from their ship and you die.

            锁最后一次嗡嗡响，然后你听到一个令人作呕的融化的声音，因为机械装置被搅乱在一起了。你决定坐在那里，最后哥特人从他们的船上炸毁了这艘船，你死了。
            """))
            return 'death'


class TheBridge(Scene):
    """ 飞船主控舱 """

    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the netron destruct bomb
        under your arm and surprise 5 Gothons who are trying to 
        take control of the ship. Each of them has an even uglier
        clown costume than the last. They haven't pulled their 
        weapons out yet, as they see the active bomb under your
        arm and don't want to set it off.

        你腋下夹着一枚耐特龙毁灭炸弹冲进了舰桥，让试图控制飞船的5名哥特人大吃一惊。他们每个人的小丑服装都比上一个更丑。他们还没有拔出他们的武器，因为他们看到了你腋下的活动炸弹，不想引爆它。
        """))

        action = input("> ")

        if action == "thow the bomb":
            print(dedent("""
            In a panic you throw the bomb at the group of Gothons 
            and make a leap for the door. Right as you drop it a 
            Gothon shoots you right in the back killing you. As 
            you die you see another Gothon frantically try to 
            disarm the bomb. You die knowing they will probably 
            blow up when it goes off.

            在恐慌中，你把炸弹扔向哥顿一伙，然后向门口跳去。就在你放下枪的时候，一个哥特人从背后开枪打死了你。当你死时，你会看到另一个哥特人疯狂地试图拆除炸弹。你死的时候知道它们可能会爆炸。
            """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
            You point your blaster at the bomb under your arm and 
            the Gothons put their hands up and start to sweat. 
            You inch backward to the door, open it, and then 
            carefully place the bomb on the floor, pointing your 
            blaster at it. You then jump back through the door, 
            punch the close button and blast the lock so the 
            Gothons can't get out. Now that the bomb is placed 
            you run to the escape pod to get off this tin can.

            你用你的爆能枪对准你胳膊下的炸弹，哥顿人举起手开始流汗。你一步一步地向门后走，打开门，然后小心地把炸弹放在地板上，用你的冲击波瞄准它。然后你从门里跳回来，按下关闭按钮，打开锁，这样哥特人就不能出去了。既然炸弹已经放好了，你就跑到逃生舱，从这个锡罐上下来。
            """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):
    """ 救生舱 """

    def enter(self):
        print(dedent("""
        You rush through the ship desperately trying to make it to 
        the escape pod before the whole ship explodes. It seems 
        like hardly any Gothons are on the ship, so your run is 
        cleat of interference. You get to the chamber with the 
        escape pods, and now need to pick one to take. Some of 
        them could be damaged but you don't have time to look.
        There's 5 pods, which one do you take?

        在整艘船爆炸之前，你拼命穿过飞船，试图到达逃生舱。似乎几乎没有任何哥特人在船上，所以你的运行是干扰夹板。你带着逃生舱到了密室，现在需要挑选一个带走。其中一些可能会损坏，但你没有时间去看。有5个豆荚，你拿哪一个？
        """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
            You jump into pod {guess} and hit the eject button.
            The pod escapes out into the viod of space, then 
            implodes as the hull ruptures, crushing your body 
            into jam jelly.

            你跳进舱{guess}并按下弹出按钮。豆荚逃到太空中，随着外壳破裂而膨胀，把你的身体压成果酱果冻。
            """))
            return 'death'

        else:
            print(dedent("""
            You jump into pod {guess} and hit the eject button.
            The pod easily slides out into space heading to 
            the planet below. As it flies to the planet, you look 
            back and see your ship implode then explode like a 
            bright star, taking out the Gothon ship at the same 
            time. You won!

            你跳进舱{guess}并按下弹出按钮。太空舱很容易滑向太空，前往下面的星球。当它飞向行星时，你回头看到你的飞船爆炸了，然后像一颗明亮的星星一样爆炸，同时摧毁了哥顿飞船。你赢了！
            """))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map():
    """ 地图 """
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

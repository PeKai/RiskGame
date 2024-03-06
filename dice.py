import random


class Dice:
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)
        return self

    def getValue(self):
        return self.value


class Battle:
    def __init__(self, noAttackTroops: int, noDefenceTroops: int):
        if 0 < noAttackTroops <= 3:
            self.noAttackTroops = noAttackTroops
        else:
            raise ValueError("Number of attacking troops must be 1 to 3")
        if 0 < noDefenceTroops <= 2:
            self.noDefenceTroops = noDefenceTroops
        else:
            raise ValueError("Number of defending troops must be 1 or 2")

        self.attackDie = []
        self.defenceDie = []

    def rollAttack(self):
        die = [Dice() for i in range(self.noAttackTroops)]
        self.attackDie = [dice.roll() for dice in die]
        return self.attackDie

    def rollDefence(self):
        die = [Dice() for i in range(self.noDefenceTroops)]
        self.defenceDie = [dice.roll() for dice in die]
        return self.defenceDie

    def getAttackDie(self):
        if self.attackDie:
            return self.attackDie
        else:
            raise ValueError("Attempting to get die before rolling")

    def getDefenceDie(self):
        if self.defenceDie:
            return self.defenceDie
        else:
            raise ValueError("Attempting to get die before rolling")

    def getOutcome(self):
        attackDie = [d.getValue() for d in self.getAttackDie()]
        attackDie.sort()
        defenceDie = [d.getValue() for d in self.getDefenceDie()]
        defenceDie.sort()

        attackerLoss = 0
        defenderLoss = 0

        for i in range(min(len(attackDie), len(defenceDie))):
            attackMax = attackDie.pop()
            defenceMax = defenceDie.pop()

            if attackMax > defenceMax:
                defenderLoss += 1
            else:
                attackerLoss += 1

        return [attackerLoss, defenderLoss]


b = Battle(2, 2)
b.rollAttack()
b.rollDefence()

print("Attack:")
print([d.getValue() for d in b.getAttackDie()])
print("Defence:")
print([d.getValue() for d in b.getDefenceDie()])
print()
print("[attLoss, defLoss]:")
print(b.getOutcome())

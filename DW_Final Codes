import random
import time
import copy
import libdw.sm as sm

class You:
	def __init__(self, name, score):
		self.name = name
		self.trust_score = score
		self.alive = True

	def isDead(self):
		return not self.alive
    
	def Cheat(self,minus):
		self.trust_score = self.trust_score - minus
		if (self.trust_score < 0):
			print("{0} is a cheater!".format(self.name))
			self.alive = False
		print("Game Over")

	def __str__(self):
		str1 =  " You name: {0}".format(self.name)
		str2 = "score: {0}".format(self.trust_score)
		return str1 + '\n' + str2

class Trust:
	def __init__(self, netTrust):
		self.netTrust = netTrust

	def cast(self, netTrust):
		return self.netTrust + trust_core

class CooperateTrust(Trust):
	def __init__(self, trust_gain):
		self.type = "COOPERATE"
		super().__init__(trust_gain)

class CheatTrust(Trust):
	def __init__(self, trust_loss):
		self.type = "CHEAT"
		super().__init__(trust_loss)

## Composition and Inheritance
class Player(You):
	def __init__(self, name, trust_score):
		super().__init__(name, trust_score)
		if (Trust == "CHEAT"):
			self.trust = CheatTrust(self.trust_score - 2)
		elif (Trust == "COOPERATE"):
			self.trust = CooperateTrust(self.trust_score + 2)
		print("Player{0} is successfully trusted.".format(self.name))


def randomizer():
	i = random.randint(1,2)

	if (i == 1):
		type_trust = "CHEAT"
	elif (i == 2):
		type_trust = "COOPERATE"
	return type_trust



class GameWorld(sm.SM):

	def __init__(self):
		self.start_state = ["INIT", None, None]

	def get_next_values(self, state, inp):
		if inp == "S" and state[0] == "INIT":
			print('Please enter the name for your player who the computer can trust.')
			name = input(">>>")
			info_string = "Press A to cooperate, press B to Cheat:"
			new_state = ["READY", Player(name,randomizer()), Player("Computer",randomizer())]
			return new_state, info_string

		else:
			info_string = "You have lost. Please press Q."
			return state, info_string

	def done(self, state):
		if (state[0] == "Q" and state[0]!= "TERMINATED"):
			if (state[1].isDead() or state[2].isDead()):
				return True
		elif (state[0] == "TERMINATED"):
			return True
		else:
			return False

	def run(self):
		self.start()
		# get keyboard input
		print("Press S to start game, press Q to quit.")
		while(True):

			if (not self.done(self.state)):
				keyboard = input(">>>")
				output = self.step(keyboard)
				print(output)
			else:
				break

		print("Exiting GameWorld")


game = GameWorld()
game.run()

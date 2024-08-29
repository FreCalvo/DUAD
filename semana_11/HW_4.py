# Cree las siguientes clases:
#     1. `Head`
#     2. `Torso`
#     3. `Arm`
#     4. `Hand`
#     5. `Leg`
#     6. `Feet`
#     7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos.


class Head:
	def __init__(self):
		pass
	
class Torso:
	def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
		self.head = head
		self.right_arm = right_arm
		self.left_arm = left_arm
		self.right_arm = right_arm
		self.right_leg = right_leg
		self.left_leg = left_leg
		

class Arm:
	def __init__(self, hand):
		self.hand = hand

class Hand:
	pass

class Leg:
	def __init__(self, feet):
		self.feet = feet
		
class Feet:
	pass

class Human():
	def __init__(self, name, torso, height, weight):
		self.name = name
		self.torso = torso
		self.height = height
		self.weight = weight
        
	
    
right_hand = Hand()
left_hand = Hand()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
right_leg = Feet()
left_leg = Feet()
head = Head()
torso = (head, right_arm, left_arm, right_leg, left_leg)
human = Human('Roberto',torso, 1.80, 65)






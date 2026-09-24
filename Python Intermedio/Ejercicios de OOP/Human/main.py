from head import Head
from hand import Hand
from arm import Arm
from feet import Feet
from leg import Leg
from torso import Torso
from human import Human


# Create hands
right_hand = Hand()
left_hand = Hand()

# Create arms
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

# Create feet
right_feet = Feet()
left_feet = Feet()

# Create legs
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)

# Create head
head = Head()

# Create torso
torso = Torso(
    head,
    right_arm,
    left_arm,
    right_leg,
    left_leg
)

# Create human
human = Human(torso)
print("A human was born")
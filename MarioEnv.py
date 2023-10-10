# Import the game
import retro
# Import the Joypad wrapper
from nes_py.wrappers import JoypadSpace
# Import the SIMPLIFIED controls
from retro.actions import SIMPLE_MOVEMENT
# Setup game
env = retro.make(game='SuperMarioBros-Nes')
env = JoypadSpace(env, SIMPLE_MOVEMENT)
# Create a flag - restart or not
done = True
# Loop through each frame in the game
for step in range(100000):
    # Start the game to begin with
    if done:
        # Start the gamee
        env.reset()
    # Do random actions
    state, reward, done, info = env.step(env.action_space.sample())
    # Show the game on the screen
    env.render()
# Close the game
env.close()
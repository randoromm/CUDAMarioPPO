# Import Frame Stacker Wrapper and GrayScaling Wrapper
import retro
from gym.wrappers import GrayScaleObservation
from retro.actions import SIMPLE_MOVEMENT
from nes_py.wrappers import JoypadSpace
# Import Vectorization Wrappers
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
# Import Matplotlib to show the impact of frame stacking
from matplotlib import pyplot as plt
# 1. Create the base environment
env = retro.make(game='SuperMarioBros-Nes')
# 2. Simplify the controls
env = JoypadSpace(env, SIMPLE_MOVEMENT)
# 3. Grayscale
env = GrayScaleObservation(env, keep_dim=True)
# 4. Wrap inside the Dummy Environment
env = DummyVecEnv([lambda: env])
# 5. Stack the frames
env = VecFrameStack(env, 4, channels_order='last')
state = env.reset()
#state, reward, done, info = env.step([5])
#state, reward, done, info = env.step([5])
#state, reward, done, info = env.step([5])
#plt.figure(figsize=(20,16))
#for idx in range(state.shape[3]):
#    plt.subplot(1,4,idx+1)
#    plt.imshow(state[0][:,:,idx])
#plt.show()
import numpy as np
import retro
import gym
import time
from gym.wrappers import GrayScaleObservation, FrameStack

from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv

from RandomAgent import TimeLimitWrapper
from stable_baselines3 import PPO

model = PPO.load("tmp/best_model.zip")


def main():
    steps = 0

    # Use a single environment for both rendering and interaction
    env = retro.make(game='SuperMarioBros-Nes')
    env = TimeLimitWrapper(env)
    env = GrayScaleObservation(env)
    env = MaxAndSkipEnv(env, 4)
    env = FrameStack(env, 4)

    obs = env.reset()
    done = False
    total_reward = 0

    while not done:
        action, state = model.predict(np.array(obs).copy())
        obs, reward, done, info = env.step(action)

        total_reward += reward

        env.render()

        if done:
            obs = env.reset()
        steps += 1
        if steps % 200 == 0:
            print(f"Total Steps: {steps}")
            print(info)
    print("Final Info")
    print(info)
    print(f"Total Reward: {total_reward}")
    env.close()


if __name__ == "__main__":
    main()
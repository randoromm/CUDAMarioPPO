from stable_baselines3 import PPO

from PreProcessedMarioEnv import env

# Load model
model = PPO.load('./train/best_model_670000.zip')
state = env.reset()
# Start the game
state = env.reset()
# Loop through the game
while True:
    action, _ = model.predict(state)
    state, reward, done, info = env.step(action)
    env.render()
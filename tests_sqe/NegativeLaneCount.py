import gymnasium
import highway_env
from matplotlib import pyplot as plt

env = gymnasium.make('highway-v0', render_mode='rgb_array', config={
    "vehicles_count": 10,
    "lanes_count": -13,
})
env.reset(seed=0)
for _ in range(3):
    action = env.unwrapped.action_type.actions_indexes["IDLE"]
    obs, reward, done, truncated, info = env.step(action)

plt.imshow(env.render())
plt.show()
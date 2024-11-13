import sys
import os
import numpy as np
import gym

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from wildfire_environment.utils.misc import save_frames_as_gif


def test_wildfire() -> None:
    """Function to manually test the environment's functionality. Runs episodes with random agents in the Wildfire environment and save episode renders as GIFs."""
    # initialize environment. Set the arguments as desired.
    env = gym.make(
        "wildfire-v0",
        alpha=0.13,
        beta=0.9,
        delta_beta=0.7,
        max_steps=100,
        num_agents=2,
        agent_start_positions=((7, 3), (7, 7)),
        size=11,
        initial_fire_size=3,
        cooperative_reward=False,
        altruism_weight=0.2,
        render_selfish_region_boundaries=True,
        log_selfish_region_metrics=True,
        selfish_region_xmin=[6, 6],
        selfish_region_xmax=[8, 8],
        selfish_region_ymin=[2, 7],
        selfish_region_ymax=[4, 9],
    )

    # run episodes
    obs, _ = env.reset()
    frames = []
    frames.append(env.render())
    num_episodes = 1

    for ep in range(num_episodes):
        while True:
            actions = {
                f"{a.index}": np.random.choice(list(env.actions)) for a in env.agents
            }
            obs, reward, done, _ = env.step(actions)
            frames.append(env.render())
            if done:
                print(env.trees_on_fire+env.burnt_trees)
                break
        # save GIF for current episodes
        save_frames_as_gif(
            frames, path="./", filename="wildfire", ep=ep, fps=1, dpi=40
        )


test_wildfire()

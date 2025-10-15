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
        alpha=0.15,
        beta=0.95,
        delta_beta=0.7,
        use_wind=False,
        wind_alpha_base=0.1,
        wind_alpha_max=0.2,
        wind_alpha_min=0.05,
        max_steps=100,
        num_agents=6,
        agent_colors=("red", "blue", "purple"),
        agent_start_positions=((7, 10), (9, 10), (16,24), (17,24), (22,10), (24,10)),
        agent_groups=((0, 1), (2,3), (4, 5)),
        size=32,
        initial_fire_size=3,
        cooperative_reward=False,
        altruism_weight=0.2,
        render_selfish_region_boundaries=True,
        log_selfish_region_metrics=True,
        selfish_region_xmin=[5, 12, 20],
        selfish_region_xmax=[11, 19, 26],
        selfish_region_ymin=[7, 21, 7],
        selfish_region_ymax=[13, 27, 13],
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
                break
        # save GIF for current episodes
        save_frames_as_gif(
            frames, path="./", filename="wildfire", ep=ep, fps=5, dpi=40
        )


test_wildfire()

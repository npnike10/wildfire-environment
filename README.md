# wildfire-environment
This repository contains a gym-based multi-agent environment to simulate wildfire fighting. The wildfire process and the fire fighting using multiple autonomous aerial vehicles is modeled by a Markov decision process (MDP). The environment allows for three types of agents: team agents (single shared reward), grouped agents (each group has a shared reward), and individual agents (individual rewards). The provided reward function for team agents aims to prevent fire spread with equal preference for the entire forest while the grouped or individual agent rewards aim to prevent fire spread with higher preference given to prevent spread in regions of their selfish interest (selfish regions) than elsewhere in the forest.  

This environment was developed for use in a MARL project utilizing the [MARLlib](https://marllib.readthedocs.io/en/latest/) library and so is written to work with older Gym, NumPy, and Python versions to ensure compatibility. If you would like a version of this environment that works with newer versions of Gym, NumPy, and Python, please refer to the [gym-multigrid](https://github.com/Tran-Research-Group/gym-multigrid) repository.

## Installation
Prior to installation either as a package or from source, please ensure that Python v3.8 is in use. We also recommend the use of a virtual environment. To install the environment as a package, please run 
```
conda create -n wildfire-env python=3.8
conda activate wildfire-env
pip install pip==21 
pip install wildfire-environment
```

To install from source, please clone this GitHub repository and follow the steps:
```
cd wildfire-environment
conda create -n wildfire-env python=3.8
conda activate wildfire-env
poetry install
poetry run pip install gym==0.21
```
This repository uses [Poetry](https://python-poetry.org/docs/) library dependency management. 

**Note**: `poetry install` fails to install Gym v0.21. Given that the MARL library, for which this environment was developed to be used with, requires the use of Gym v0.20/0.21, we include an additional step after `poetry install` in above code. 

## Basic Usage

This repository provides a gym-based environment. The core contribution is the WildfireEnv class, which is a subclass of gym.Env (via MultiGridEnv class). Use of [Gym](https://github.com/openai/gym) environments is standard in RL community and this environment can be used in the same way as a typical gym environment. Note that Gym has now migrated to Gymnasium and to use a version of this environment that is compatible with Gymnasium, please refer to the [gym-multigrid](https://github.com/Tran-Research-Group/gym-multigrid) repository.

Here's a simple example for creating and interacting with the environment:

```
import gym
import wildfire_environment

env = gym.make("wildfire-v0", 
    num_agents=2,
    size=17,
    initial_fire_size=3,
    cooperative_reward=False,
    log_selfish_region_metrics=True,
    selfish_region_xmin=[7, 13],
    selfish_region_xmax=[9, 15],
    selfish_region_ymin=[7, 1],
    selfish_region_ymax=[9, 3],
    )
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    if done:
        observation, info = env.reset()
env.close()
```

Please ensure that path to wildfire_environment is present in PYTHONPATH before attempting to import it in your code. 

## Environment
### Wildfire
![WildfireEnv Example](./assets/wildfire-env-example.gif)

| Attribute             | Description    |
| --------------------- | -------------- |
| Actions               | `Discrete`  |
| Agent Action Space    | `Discrete(5)`  |
| Observations          | `Discrete`  |
| Observability          | `Fully observable`  |
| Agent Observation Space     | `Box([0,...],[1,...],(shape depends on number of agents,),float32)` |
| States                | `Discrete`  |
| State Space           | `Box([0,...],[1,...],(shape depends on number of agents,),float32)`  |
| Agents                | `Cooperative or Non-cooperative or Group`       |
| Number of Agents      | `>=1`            |
| Termination Condition | `No trees on fire exist`         |
| Truncation Steps      | `>=1`           |
| Creation              | `gym.make("wildfire-v0")` |

Agents move over trees on fire to dump fire retardant. Initial fire is randomly located. Agents can be cooperative (shared reward) or non-cooperative (individual/group rewards). A non-cooperative agent preferentially protects a region of selfish interest within the grid. Above GIF contains two groups of agents with their selfish regions shown in same color.
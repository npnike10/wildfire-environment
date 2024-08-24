# wildfire-environment
This repository contains a gym-based multi-agent environment to simulate wildfire fighting. The wildfire process and the fire fighting using multiple autonomous aerial vehicles is modeled by a Markov decision process (MDP). The environment allows for three types of agents: team agents (single shared reward), grouped agents (each group has a shared reward), and individual agents (individual rewards). The provided reward function for team agents aims to prevent fire spread with equal preference for the entire forest while the grouped or individual agent rewards aim to prevent fire spread with higher preference given to prevent spread in regions of their selfish interest (selfish regions) than elsewhere in the forest.  

This environment was developed for use in a MARL project utilizing the [MARLlib](https://marllib.readthedocs.io/en/latest/) library and so is written to work with older Gym, NumPy, and Python versions to ensure compatibility. If you would like a version of this environment that works with newer versions of Gym, NumPy, and Python, please refer to the [gym-multigrid](https://github.com/Tran-Research-Group/gym-multigrid) repository.

## Installation
To install the environment as a package, please use `pip install wildfire-environment`.

To install from source, please clone this GitHub repository, `cd wildfire-environment` and finally use `poetry install`. This repository uses [Poetry](https://python-poetry.org/docs/) library dependency management. 

**Note**: `poetry install` will likely fail for NumPy v1.21.0. This is an issue when installation is done via Poetry but installation works well with `pip install numpy==1.21.0`. Given that the MARL library, for which this environment was developed to be used with, requires the use of old NumPy versions and a clean solution to the installation issue with Poetry isn't known to us, we recommend the user to install NumPy v1.21.0 using `pip` first and then do `poetry install`. For users who use conda to manage virtual environments, they may follow the steps: clone this GitHub repository, `cd wildfire-environment`, create a conda virtual environment with Python 3.8 with `conda create -n wildfire-env python=3.8`, activate the venv with `conda activate wildfire-env`, install NumPy with `pip install numpy==1.21.0`, and finally run `poetry install` to complete the installation. 

## Basic Usage

This repository provides a gym-based environment. The core contribution is the WildfireEnv class, which is a subclass of gym.Env (via MultiGridEnv class). Use of [Gym](https://github.com/openai/gym) environments is standard in RL community and this environment can be used in the same way as a typical gym environment. Note that Gym has now migrated to Gymnasium and to use a version of this environment that is compatible with Gymnasium, please refer to the [gym-multigrid](https://github.com/Tran-Research-Group/gym-multigrid) repository.

Here's a simple example for creating and interacting with the environment:

```
import gym
import wildfire_environment

env = gym.make("wildfire-v0")
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
| Agents                | `Cooperative/Non-cooperative`       |
| Number of Agents      | `>=1`            |
| Termination Condition | `No trees on fire exist`         |
| Truncation Steps      | `>=1`           |
| Creation              | `gymnasium.make("multigrid-collect-respawn-clustered-v0")` |

Agents move over trees on fire to dump fire retardant. Initial fire is randomly located. Agents can be cooperative (shared reward) or non-cooperative (individual/group rewards). A non-cooperative agent preferentially protects a region of selfish interest within the grid. Above GIF contains two groups of agents with their selfish regions shown in same color.
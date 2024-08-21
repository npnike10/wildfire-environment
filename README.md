# wildfire-environment
This repository contains a gym-based multi-agent environment to simulate wildfire fighting. The wildfire process and the fire fighting using multiple autonomous aerial vehicles is modeled by a Markov decision process (MDP). The environment allows for three types of agents: team agents (single shared reward), grouped agents (each group has a shared reward), and individual agents (individual rewards). The provided reward function for team agents aims to prevent fire spread with equal preference for the entire forest while the grouped or individual agent rewards aim to prevent fire spread with higher preference given to prevent spread in regions of their selfish interest (selfish regions) than elsewhere in the forest.  

This environment was developed for use in a MARL project utilizing the [MARLlib](https://marllib.readthedocs.io/en/latest/) library and so is written to work with older Gym, NumPy, and Python versions to ensure compatibility. If you would like a version of this environment that works with newer versions of Gym, NumPy, and Python, please refer to the [gym-multigrid](https://github.com/Tran-Research-Group/gym-multigrid) repository.

## Installation
To install the environment as a package, please use `pip install wildfire-environment`.

To install from source, please clone this GitHub repository and use `poetry install`. This repository uses [poetry](https://python-poetry.org/docs/) library dependency management.

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
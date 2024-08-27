from gym.envs.registration import register


# Wildfire environment
# ----------------------------------------
register(id="wildfire-v0", entry_point="wildfire_environment.envs:WildfireEnv")

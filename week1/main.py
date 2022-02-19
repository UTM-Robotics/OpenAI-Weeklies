import gym
from time import sleep
from matplotlib import pyplot as plt
env = gym.make("CartPole-v1")
observation = env.reset()

for _ in range(1000):
    sleep(0.1)
    env.render()
    print(env.action_space.sample())
    env.step(env.action_space.sample()) # take a random action
env.close()

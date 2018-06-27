import gym

env = gym.make ('SpaceInvaders-v0')

env.reset()

env.render()

is_done = False
while not is_done:
	state, reward, is_done, info = env.step(env.action_space.sample())
	env.render() 
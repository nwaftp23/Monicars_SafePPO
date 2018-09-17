from monicars import Environment
from monicars.variables import global_var
import numpy as np
import sys
sys.path.insert(0, '/home/adaptation/lberry/Documents/HUAWEI_scenarios/ppo_monicars/src')
from train import * 


def rew_func(obs):
	if obs[-1] == 1:
		rew = -1000
	elif obs[1] <= 10:
		rew = -1000
	else:
		rew = -1
	return rew

env_name = "two_lanes"
obs_dim = 6
act_dim = 1  
batch_size = 20
num_episodes = 4000
gamma = 0.9995
lam = 0.98
HL1_mult = 10
Kl_targ = 0.003
make_plots = True

main(env_name, num_episodes, gamma, lam, Kl_targ, batch_size, HL1_mult, 1.0, make_plots, act_dim, obs_dim, obstacle = True, reward_function = rew_func, render = False)




from monicars import Environment
from monicars.variables import global_var
import numpy as np

env = Environment("round_a_bout")

env.reset()

done = False
while not done:
	accel_rand = np.random.normal(0,0.05)
	obs, reward, done = env.step([0, 0], npc_action = [[accel_rand,0]])
	env.clock.tick(global_var.FPS)

env.quit()
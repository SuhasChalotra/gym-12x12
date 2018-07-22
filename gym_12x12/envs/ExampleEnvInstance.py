from gym_12x12.envs.gym12x12_env import gym12x12_env, PlayerType as pt

env = gym12x12_env()

player_one = env.create_player(pt.AGENT)
player_two = env.create_player(pt.BOT)
obs = env.initiate_game(arg_player1=player_one, arg_player2=player_two, arg_int_boardsize=6)

# obs = env.reset()

import numpy
from scenario import *
import json
import time

'''parse command line'''
config_file_path = 'config/config.json'
scenario_file_path = 'scenario/mixture_cocktail.json'

""" init data structure """
config_buffer = get_config_buffer(trim_path_dir(config_file_path))
scenario = Scenario(scenario_file_path)
print('Done reading files')

taichi_init(config_buffer)
pre_config = Pre_config(config_buffer, scenario.scenario_buffer)
config = Config(pre_config, config_buffer, scenario.scenario_buffer)
print('Done configurating')

ngrid = Ngrid(config)
fluid = Fluid(config.fluid_max_part_num[None], pre_config, config)
bound = Fluid(config.bound_max_part_num[None], pre_config, config)
print('Done instancing')

init_scenario(fluid, bound, scenario, config)
print('Done pushing particles')

config.start_id[None], config.end_id[None] = bound.get_part_range_from_name('rod')
config.vel_down_np = np.array([0.0,-3.0,0.0])
config.vel_rot_np = np.zeros(3)

# config.tmp_scene_id = 'teabag'
if config.tmp_scene_id == "teabag":
    config.start_id[None], config.end_id[None] = bound.get_part_range_from_name('teabag')
    config.vel_down_np = np.array([0.0,-3.0,0.0])
    config.time_down[None] = 0.5

while 1:
    run_step(ngrid, fluid, bound, config)
    refresh_scenario(scenario, config)
    write_files(config, pre_config, fluid)

    if config.time_count[None] > 25:
        break


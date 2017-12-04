from slm_lab.spec import spec_util
from slm_lab.experiment import analysis
from slm_lab.experiment.control import Session, Trial
from slm_lab.lib import logger, util


def main():
    # logger.set_level('DEBUG')
    # spec = spec_util.get('base.json', 'base_case')
    # spec = spec_util.get('base.json', 'multi_env')
    spec = spec_util.get('dqn.json', 'dqn_base_case')
    trial = Trial(spec)
    trial_data = trial.run()


if __name__ == '__main__':
    main()
import shutil
import click
from pathlib import Path
from azureml.core import Workspace, Experiment, Dataset, Run, ComputeTarget
from azureml.train.sklearn import SKLearn


@click.command()
def main():

    workspace = Workspace.from_config()
    experiment = Experiment(workspace, 'linear_regression')
    compute_target = ComputeTarget(workspace, 'mlc-training-ml')

    root_folder = str(Path(__file__).parent)

    shutil.copy(Path(root_folder, '../../config.json'),
                Path(root_folder, 'config.json'))

    estimator = SKLearn(source_directory=root_folder,
                        compute_target=compute_target,
                        entry_script='train.py')

    experiment.submit(estimator)


if __name__ == '__main__':
    main()

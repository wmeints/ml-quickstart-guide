import logging
import click
from pathlib import Path
from azureml.core import Workspace, Dataset


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('dataset_name', type=str)
def main(input_filepath, dataset_name):
    ws = Workspace.from_config()
    datastore = ws.get_default_datastore()

    input_file = Path(input_filepath)

    logging.info(f'Uploading {input_filepath} to the workspace')

    datastore.upload(input_filepath, target_path=f'processed/{dataset_name}',
                     overwrite=True, show_progress=True)

    logging.info('Registering the uploaded data as a dataset')

    dataset = Dataset.Tabular.from_delimited_files(
        path=[(datastore, f'processed/{dataset_name}')])

    dataset.register(ws, dataset_name)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()

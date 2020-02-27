import click
import pickle
from azureml.core import Workspace, Experiment, Dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


@click.command()
def main():
    workspace = Workspace.from_config()
    dataset = Dataset.get_by_name(workspace, 'auto-mpg')

    df_milage = dataset.to_pandas_dataframe()

    X = df_milage[['cylinders', 'displacement', 'horsepower',
                   'weight', 'acceleration', 'model year', 'origin']]
    y = df_milage[['mpg']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    experiment = Experiment(workspace, 'linear_regression')

    with experiment.start_logging() as run:
        model = LinearRegression()
        model.fit(X_train, y_train)

        run.log('r_squared', model.score(X_test, y_test))


if __name__ == '__main__':
    main()

# The data set used in this example is from http://archive.ics.uci.edu/ml/datasets/Wine+Quality
import argparse
import warnings

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def parse_arguments(args):
    parser = argparse.ArgumentParser(description='Build a model to predict the wine quality')
    parser.add_argument('--alpha', type=float, default=0.5, help='alpha')
    parser.add_argument('--l1_ratio', type=float, default=0.5, help='l1 ratio')
    parser.add_argument('--wine_file', type=str, required=True, action=None, help='wine file to use to train the model')
    return parser.parse_args(args)


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def main(args=None):
    args = parse_arguments(args)

    warnings.filterwarnings("ignore")
    np.random.seed(40)

    wine_path = args.wine_file
    print('Wine Path [%s]' % wine_path)

    data = pd.read_csv(wine_path, delimiter=';')

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    for alpha in np.linspace(0, 1, 9):
        for l1_ratio in np.linspace(0.5, 0.5, 1):
            print(alpha, l1_ratio)

            alpha = round(alpha, 2)
            l1_ratio = round(l1_ratio, 2)

            with mlflow.start_run():
                lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
                lr.fit(train_x, train_y)

                predicted_qualities = lr.predict(test_x)

                (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

                print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
                print("  RMSE: %s" % rmse)
                print("  MAE: %s" % mae)
                print("  R2: %s" % r2)

                mlflow.log_param("source", wine_path)
                mlflow.log_param("alpha", alpha)
                mlflow.log_param("l1_ratio", l1_ratio)

                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)

                mlflow.set_tag('domain', 'wine')
                mlflow.set_tag('predict', 'quality')
                mlflow.sklearn.log_model(lr, "model")


if __name__ == "__main__":
    main()

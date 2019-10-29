import numpy as np
import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read the dataset into the program.')
    parser.add_argument("source_data", help="path to the source data file.")
    args = parser.parse_args()

    # Import data
    dataset = pd.read_csv('datingTestSet.txt', delimiter="\t")
    dataset.columns = ['miles', 'game', 'ice_cream', 'opinion']
    print(dataset.head())
    print(dataset.dtypes)
    print(np.unique(dataset['opinion']))
    print(len(dataset))

    # normalize of data

    # Analyze the dataset by drawing the graph
    sns.lmplot(x='ice_cream', y='game', data=dataset, hue='opinion', fit_reg=False, palette=dict(largeDoses="g", didntLike="m", smallDoses="y"))
    sns.lmplot(x='miles', y='game', data=dataset, hue='opinion', fit_reg=False)
    sns.lmplot(x='miles', y='ice_cream', data=dataset, hue='opinion', fit_reg=False)
    plt.show()



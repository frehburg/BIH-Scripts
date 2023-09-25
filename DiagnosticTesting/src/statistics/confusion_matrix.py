import numpy as np


def calc_confusion_matrix(x, y, y_hat):
    """
    Calculates the confusion matrix for a binary classification problem.

    Requires the true and false labels to be integers 1 and 0.

    :param x: The input data.
    :param y: The true labels.
    :param y_hat: The predicted labels.
    :return: The confusion matrix.
    """
    true_positives = np.sum(np.logical_and(y_hat == 1, y == 1))
    false_positives = np.sum(np.logical_and(y_hat == 1, y == 0))
    true_negatives = np.sum(np.logical_and(y_hat == 0, y == 0))
    false_negatives = np.sum(np.logical_and(y_hat == 0, y == 1))

    return true_positives, false_positives, false_negatives, true_negatives

def calc_sensitivity(tp, fn):
    return tp / (tp + fn)


def calc_specificity(tn, fp):
    return tn / (tn + fp)


def calc_precision(tp, fp):
    return tp / (tp + fp)


def calc_f1_score(tp, fp, fn):
    return 2 * tp / (2 * tp + fp + fn)


def calc_accuracy(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + fp + fn)


def calc_positive_predictive_value(sensitivity, specificity, prevalence):
    return (numerator := (sensitivity * prevalence)) / \
        (numerator + ((1 - specificity) * (1 - prevalence)))


def calc_negative_predictive_value(sensitivity, specificity, prevalence):
    return (numerator := (specificity * (1 - prevalence))) / \
        (numerator + ((1 - sensitivity) * prevalence))

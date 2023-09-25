import math
from typing import Tuple

import numpy as np

from . import calc_positive_predictive_value as calc_ppv
from . import calc_negative_predictive_value as calc_npv
from ..plot import plot_influence_of_prevalence


def influence_of_prevalence_on_diagnostic_testing(
        sensitivity: float = 0.95,
        specificity: float = 0.95,
        min_prevalence: float = 10e-5,
        max_prevalence: float = 1,
        save: bool = False,
        num_points: int = 1000
) -> None:
    """Plot the influence of prevalence on the positive and negative predictive
    values (PPV and NPV).

    :param sensitivity: Sensitivity of the diagnostic test.
    :type sensitivity: float
    :param specificity: Specificity of the diagnostic test.
    :type specificity: float
    :param min_prevalence: Minimum prevalence to plot, defaults to 10e-5.
    :type min_prevalence: float, optional
    :param max_prevalence: Maximum prevalence to plot, defaults to 1.
    :type max_prevalence: float, optional
    :param save: If True, the function will also save the plot as an image,
    defaults to False.
    :type save: bool, optional
    :param num_points: Number of points to plot, defaults to len(prevalences).
    :type num_points: int, optional
    """

    def round_down_to_power_of_ten(number: float) -> Tuple[float, int]:
        power = math.floor(math.log10(number))
        result = 10 ** power
        return result, power

    result_min, power_min = round_down_to_power_of_ten(min_prevalence)
    result_max, power_max = round_down_to_power_of_ten(max_prevalence)

    n = power_max - power_min + 1

    if num_points < n:
        # Plot a point for each prevalence, if num_points is not or wrongly specified
        num_points = 1000

    prevalences = np.logspace(power_min, power_max, num_points)

    # Calculate the PPVs and NPVs
    ppvs = []
    npvs = []
    for prevalence in prevalences:
        ppv = calc_ppv(sensitivity, specificity, prevalence)
        npv = calc_npv(sensitivity, specificity, prevalence)
        ppvs.append(ppv)
        npvs.append(npv)

    # Plot the PPVs and NPVs
    plotting_prevalences = np.logspace(power_min, power_max, n)  # x ticks for plot
    title = f'Influence of Disease Prevalence(π) on PPV and NPV \n' \
            f'(Sensitivity = {sensitivity:.3f}, Specificity = {specificity:.3f})'
    plot_influence_of_prevalence(
        ppvs=ppvs, npvs=npvs, prevalences=prevalences,
        x_ticks=plotting_prevalences,
        title=title,
        save=save,
        save_path=f'data/out/InfluenceOfPrevalence_sensitivity{sensitivity:.3f}'
                  f'_specificty{specificity:.3f}.png'
    )

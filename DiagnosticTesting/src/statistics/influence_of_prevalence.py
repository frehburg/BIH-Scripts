import math
from typing import Tuple, List

import numpy as np

from . import calc_positive_predictive_value as calc_ppv
from . import calc_negative_predictive_value as calc_npv
from ..plot import plot_influence_of_prevalence, plot_3ppv_influence_of_prevalence


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
    power_min, power_max, n = get_bounds_and_n(min_prevalence, max_prevalence)

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
    title = f'Influence of Disease Prevalence (π) on PPV and NPV \n' \
            f'(Sensitivity = {sensitivity:.3f}, Specificity = {specificity:.3f})'
    plot_influence_of_prevalence(
        ppvs=ppvs, npvs=npvs, prevalences=prevalences,
        x_ticks=plotting_prevalences,
        title=title,
        save=save,
        save_path=f'data/out/InfluenceOfPrevalence_sensitivity{sensitivity:.3f}'
                  f'_specificty{specificity:.3f}.png'
    )


def influence_3ppv_of_prevalence_on_diagnostic_testing(
        sensitivities: List[float],
        specificities: List[float],
        min_prevalence: float = 10e-5,
        max_prevalence: float = 1,
        save: bool = False,
        num_points: int = 1000
) -> None:
    power_min, power_max, n = get_bounds_and_n(min_prevalence, max_prevalence)

    if num_points < n:
        # Plot a point for each prevalence, if num_points is not or wrongly specified
        num_points = 1000

    prevalences = np.logspace(power_min, power_max, num_points)

    # Calculate the PPVs and NPVs
    ppvs1 = []
    ppvs2 = []
    ppvs3 = []
    for prevalence in prevalences:
        ppv1 = calc_ppv(sensitivities[0], specificities[0], prevalence)
        ppvs1.append(ppv1)
        ppv2 = calc_ppv(sensitivities[1], specificities[1], prevalence)
        ppvs2.append(ppv2)
        ppv3 = calc_ppv(sensitivities[2], specificities[2], prevalence)
        ppvs3.append(ppv3)

    # Plot the PPVs and NPVs
    plotting_prevalences = np.logspace(power_min, power_max, n)  # x ticks for plot
    title = 'Influence of Disease Prevalence (π) on PPV \n'
    plot_3ppv_influence_of_prevalence(
        ppvs1=ppvs1, ppvs2=ppvs2, ppvs3=ppvs3, prevalences=prevalences,
        label1=f'Sensitivity = {sensitivities[0]:.3f}, Specificity = '
               f'{specificities[0]:.3f}',
        label2=f'Sensitivity = {sensitivities[1]:.3f}, Specificity = '
               f'{specificities[1]:.3f}',
        label3=f'Sensitivity = {sensitivities[2]:.3f}, Specificity = '
               f'{specificities[2]:.3f}',
        x_ticks=plotting_prevalences,
        title=title,
        save=save,
        save_path=f'data/out/InfluenceOfPrevalence_{sensitivities[0]:.3f}-'
                  f'{specificities[0]:.3f}_{sensitivities[1]:.3f}-'
                  f'{specificities[1]:.3f}_{sensitivities[2]:.3f}-'
                  f'{specificities[2]:.3f}.png'
    )


def get_bounds_and_n(min_prevalence: float, max_prevalence: float):
    def round_down_to_power_of_ten(number: float) -> Tuple[float, int]:
        power = math.floor(math.log10(number))
        result = 10 ** power
        return result, power

    result_min, power_min = round_down_to_power_of_ten(min_prevalence)
    result_max, power_max = round_down_to_power_of_ten(max_prevalence)

    n = power_max - power_min + 1

    return power_min, power_max, n

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def plot_influence_of_prevalence(
        ppvs, npvs, prevalences,
        x_ticks, title,
        save, save_path
):
    # Create a new figure
    plt.figure()

    # x-axis
    plt.xscale('log')
    plt.xlim(0.7*np.min(prevalences), np.max(prevalences)*1.5)
    plt.xticks(x_ticks)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(  # setting 10^0 to 1
        lambda label, _: '{:g}'.format(label))
    )
    plt.xlabel('Prevalence (%)')

    # y-axis
    plt.ylim(-(offset := 0.05), 1 + offset)
    plt.yticks(np.arange(0, 1.1, 0.2))

    # Plot the PPVs and NPVs
    plt.plot(prevalences, ppvs, 'k-', label='PPV')
    plt.plot(prevalences, npvs, 'k--', label='NPV')

    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=2)

    plt.title(title)

    if save:
        save_path = Path(save_path).resolve()
        print(f'Saving plot to {save_path}...')
        plt.savefig(save_path, dpi=300)

    plt.show()

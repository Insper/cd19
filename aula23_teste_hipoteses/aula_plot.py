# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from scipy.stats import norm


def normal_plot(mu, dp, n, x_=None, abaixo=None, acima=None, intervalo = None ):
    """
        mu = média populacional
        scale = desvio padrão populacional
        n = tamanho da amostra
        x_ = x barra, média da amostra
        abaixo - região inferior a ser pintada
        acima - região superior a ser pintada
    """
    dp_x_ = dp/sqrt(n)
    amplitude = 5*dp_x_
    lim_inf = mu-amplitude
    lim_sup = mu+amplitude
    x_axis = np.linspace(lim_inf, lim_sup, 2000)
    y = norm.pdf(x_axis, loc=mu, scale=dp)
    y_amostral = norm.pdf(x_axis, loc=mu, scale=dp_x_)
    #plt.
    plt.figure(figsize=(15,8))
    ax = plt.subplot(111) # para depois arrumarmos a legend box
    
    plot_X_bar, = plt.plot(x_axis, y_amostral)
    plot_X_bar.set_label('Distribuição de $\overline{X}$')
    
    if abaixo is not None:
        plot_fill = plt.fill_between(x_axis, y1=y_amostral, where=(x_axis<abaixo))
        plot_fill.set_label("Região abaixo de {:.2f}".format(abaixo))
        

        
    if intervalo is not None:
        low = intervalo[0]
        high = intervalo[1]
        plot_fill = plt.fill_between(x_axis, y1=y_amostral, where=((x_axis>low) & (x_axis < high)))
        plot_fill.set_label("Região entre {:.3f} e {:.3f}".format(low, high))     
        
    if acima is not None:
        plot_fill = plt.fill_between(x_axis, y1=y_amostral, where=(x_axis>acima))
        plot_fill.set_label("Região acima de {:.2f}".format(acima))
        

    if x_ is not None:
        plot_x_  = plt.axvline(x_, linestyle="--")
        plot_x_.set_label("Linha da amostra $\overline{x}$=" + "{:.2f}".format(x_))
        
        
    
    # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
    #      ncol=3, fancybox=True, shadow=True)
    
    box = ax.get_position()
    legend_percent = 0.2
    ax.set_position([box.x0, box.y0, box.width * (1 - legend_percent), box.height])
    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
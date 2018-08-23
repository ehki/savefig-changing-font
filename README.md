# savefig_changing_font.py

## How to use

Simply replace plt.savefig with savefig_changing_font as follows:

    $ python
    >>> import matplotlib.pyplot as plt
    >>> from plot_changing_font import plot_chaging_font as savecf
    >>> x = [1,2,3]
    >>> y = [1,4,9]
    >>> plt.plot(x,y)
    >>> savecf(fmt="png") # default fmt is "pdf"


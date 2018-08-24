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

 Then you can see following three files:

![image with computer modern mathtext](https://github.com/ehki/savefig-changing-font/blob/master/out_cm.png?raw=true "out_cm.png")

![image with times new roman](https://github.com/ehki/savefig-changing-font/blob/master/out_times.png?raw=true "out_times.png")

![image with arial](https://github.com/ehki/savefig-changing-font/blob/master/out_arial.png?raw=true "out_arial.png")
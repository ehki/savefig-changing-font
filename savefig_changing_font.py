import matplotlib.pyplot as plt
def savefig_changing_font(basename="out", fmt="pdf",
                  savefig_options={"bbox_inches":"tight","pad_inches":0.02},
                  fontfamilies=["serif","serif","sans-serif"],
                  fontnames=["Times New Roman","Times New Roman","Arial"],
                  mathtexts=["cm","stix","stixsans"],
                  abbreviations=["cm","times","arial"],
                  **args):
    default = plt.rcParams
    savefig_options = dict(savefig_options, **args)
    for ff,fn,mt,ab in zip(fontfamilies,fontnames,mathtexts,abbreviations):
        plt.rcParams["font.family"] = ff
        plt.rcParams["font.sans-serif"] = fn
        plt.rcParams["font.serif"] = fn
        plt.rcParams["mathtext.fontset"] = mt
        plt.savefig(basename+"_"+ab+"."+fmt,**savefig_options)
    plt.rcParams = default
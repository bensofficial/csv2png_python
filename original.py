from matplotlib import pyplot as plt
import pandas as pd
import os

def main():
    filelist = os.listdir()
    for file in filelist:
        if not os.path.isdir(file) and file[-4:]==".csv":
            csv2png(file)


def csv2png(file):
    df = pd.read_csv(file, index_col=0)
    for i, dat in df.iteritems():
        # print(i,dat)
        plt.plot(df.index, dat, label = i)
    plt.title(file)
    plt.legend()
    plt.savefig(file+".png")
    plt.close()


if __name__ == '__main__':
    main()

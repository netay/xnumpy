import xnumpy as np


def main():
    print("""Loss of sin and cos exactness for big arguments:""")
    a = [1, 1e+5, 1e+10, 1e+15, 1e+20, 1e+25]
    print(f"arguments:\na={a}")
    print(f"sin(a):\n{np.sin(a)}")
    print(f"cos(a):\n{np.cos(a)}")


if __name__ == '__main__':
    main()


def main():
    ok = True
    while ok:
        decision = input("Choose the package: exp_root, factorial, logarithm: ")
        if decision == "factorial":
            import factorial.factorial
            try:
                a = int(input("Input number: "))
                if a>0:
                    print(factorial.factorial.fact(a))
            except ValueError: print("Bad input")
        elif decision == "exp_root":
            modul = input("Choose the module: root, exponentiation: ")
            if modul == "root":
                import exp_root.root
                a = input("Input the number and 2 if you want to find square root, 3 if you want to find the cubic root (e.g. 16 2): ")
                a = list(map(float, a.split()))
                if a[1]==2 and a[0]>0:
                    print(exp_root.root.root2(a[0]))
                elif a[1]==3:
                    print(exp_root.root.root3(a[0]))
                else:print("*input error*")
            elif modul == "exponentiation":
                import exp_root.exponentiation
                a =input("Input the number and 2 if you want to find the second power, 3 if you want to find the third (e.g. 4 3): ")
                a = list(map(float, a.split()))
                if a[1]==2:
                    print(exp_root.exponentiation.exp2(a[0]))
                elif a[1]==3:
                    print(exp_root.exponentiation.exp3(a[0]))
                else:print("*input error*")
            else: print("Module name Error")
        elif decision == "logarithm":
            import logarithm.logarithm
            a = input("Print one number if you want to find ln(a) or two numbers if you want to find log(a,b) (lg(b) should be b,10): ")
            a = list(map(float, a.split()))
            if len(a)==1 and a[0]>0 and a[0] != 1:
                print(logarithm.logarithm.ln(a))
            elif a[1]==10 and a[0]>0:
                print(logarithm.logarithm.lg(a[0]))
            elif a[1]>0 and a[0]>0:
                print(logarithm.logarithm.log(a[0],a[1]))
            else: print("Input error")
        else: print("Package name Error")      
if __name__=="__main__":
    main()
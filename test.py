import os

fileName = os.path.dirname(os.path.abspath(__file__))
[pathToDir, dire] = os.path.split(fileName)
programName = dire + ".cpp"
if (os.path.isfile(programName)):
    print("Testing " + programName)
    print("------------------------------")
    print("\n")
    os.system("rm -rf a.out")
    os.system("g++ " + programName)
    if (not(os.path.isfile("a.out"))):
        print("Compliation Error!")
    else:
        i = 0
        while True:
            i = i + 1
            inName = "in" + str(i)
            outName = "out" + str(i)
            outTemp = "out" + str(i) + "t"
            if (not(os.path.isfile(inName))):
                break
            print("Test " + str(i))
            print("------------------------------")
            os.system("./a.out < " + inName + " > " + outTemp)
            if (not(os.path.isfile(outTemp))):
                print("Running " + i + "th time fails!")
            else:
                os.system("diff " + outTemp + " " + outName)
            print("\n")
        for k in range(0, i):
            outTemp = "out" + str(k) + "t"
            if (os.path.isfile(outTemp)):
                os.system("rm -rf " + outTemp)

##import matplotlib.pyplot as pyplot # uninstall + reinstall py for pip

alphabet = [0,1,2,3,4,5,6,7,8,9," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def get_data_in():
    data_in = [["henry","dave","albert","danial","auther","ben","dylan"],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[["bunking"],["sent out","bunking"],["bunking","bunking","late"],["rep","late","sent out","rep"],["sent out","late","late","rep","sent out"],["late","late","rep","rep","rep","rep"],["rep","rep","rep","late","late","sent out","late"]]] # names(str), Hp(int), Bp(int), Bp reasons(2d)(str)
    return data_in

data_in = get_data_in()

#^^^ assumed data_in format may be inacurate

def sort(data_in,a):#for sorting by names, a = 0
    i = 0
    swaps = True
    while swaps == True:
        swaps = False
        for name_ndx in range(len(data_in[a])-1): # for name No. in first to penultimate
            for letter_ndx in range(len(data_in[a][name_ndx])): # for letter No. in name
                if alphabet.index(data_in[a][name_ndx][letter_ndx]) > alphabet.index(data_in[a][name_ndx+1][letter_ndx]): # if letter value(name 1) > letter value(name 2)
                    name_x = data_in[0][name_ndx] # Swap!
                    hp_x = data_in[1][name_ndx]
                    bp_x = data_in[2][name_ndx]
                    reasons_x = data_in[3][name_ndx]
                    data_in[0][name_ndx] = data_in[0][name_ndx+1]
                    data_in[1][name_ndx] = data_in[1][name_ndx+1]
                    data_in[2][name_ndx] = data_in[2][name_ndx+1]
                    data_in[3][name_ndx] = data_in[3][name_ndx+1]
                    data_in[0][name_ndx+1] = name_x
                    data_in[1][name_ndx+1] = hp_x
                    data_in[2][name_ndx+1] = bp_x
                    data_in[3][name_ndx+1] = reasons_x
                    swaps = True
                    break
                elif alphabet.index(data_in[a][name_ndx][letter_ndx]) < alphabet.index(data_in[a][name_ndx+1][letter_ndx]): # if letter value(name 1) < letter value(name 2)
                    break # No Swap!
        i += 1
        #print(f"pass number {i}: {data_in}")
    print(f"\nsorted by column({a+1}):\n{data_in[0]}\n{data_in[1]}\n{data_in[2]}\n{data_in[3]}\n")
    return data_in

def choose_graph(data_in):
##    pyplot.subplot(2,2,1)
##    pyplot.plot(data_in[1],data_in[2],marker = "*",mec = "darkcyan",mfc = "darkcyan")#student hps vs student bps *, no line, cyan
##    pyplot.grid
##    pyplot.subplot(2,2,2)
##    reasons = []
##    count = []
##    for element in data_in[3]: # counting raesons for bp
##        for reason in element:
##            if reason not in reasons:
##                reasons.append(reason)
##                count.append(1)
##            else:
##                count[reasons.index(reason)] += 1
##    pyplot.bar(reasons,count)
##    pyplot.subplot(2,2,3)
##    pyplot.pie(count,lables = reasons)
##    pyplot.subplot(2,2,4)
##    pyplot.show
    total = 0
    for n in data_in[1]:
        total += n
    print(f"Mean house-points per student: {total/len(data_in[0])}")
    total = 0
    for n in data_in[2]:
        total += n
    print(f"Mean behaviour-points per student: {total/len(data_in[0])}")

def start(data_in):
    data_in = sort(data_in,0) # try sort with dan and danial, Dan Auldry2son and Dan Blitherington, Danial Auldry2son and Dan Blitherington, 0 and 1, x and x
    choose_graph(data_in)

def user_input(text,arr):
    answer = input(text)
    coded_exceptions = ["restart","help"]
    while answer not in arr:
        if answer not in coded_exceptions:
            answer = input(f"Error\n{text}")
        else:
            while answer in coded_exceptions:
                if answer == "restart":
                    start(get_data_in())
                elif answer == "help":
                    print("\n#help info#\n")
                answer = input(text)
    return answer

start(data_in)


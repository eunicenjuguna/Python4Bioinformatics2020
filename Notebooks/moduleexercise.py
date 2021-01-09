# module for class exercises
def aa_pos():  
    AAseq = 'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'
    firstAA = AAseq[0]
    lastAA = AAseq[-1]
    fifthAA = AAseq[4]
    print('the first Amino Acid in Amino acid sequence is', firstAA)
    print('the last Amino Acid in Amino acid sequence is', lastAA)
    print('the fifth Amino Acid in Amino acid sequence is', fifthAA)
    
    seq = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
    def recog_site():   
        recSeq = 'TCCGGA'
        firstSit = seq.find(recSeq)
        print('The first restriction site is at index', firstSit)

    def rev_comp():
        seq = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
        comp = seq.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
        revComp = comp.upper()[::-1]
        print('The reverse complemment of my sequence is:', revComp)
        
    def atm_withdraw():   
        balance = 100
        options = input("please inter 'b' for balance, 'w' to withdraw, 'd' to deposite and 'q' to quit")
        while options != 'q':
            if options.lower() in ('b','w','d'):
                if options.lower() == 'b':
                    print('Your balance is:', balance)
                    print('anything else?')
                    options = input("please enter 'b' for balance, 'w' to withdraw, 'd' to deposite and 'q' to quit")
                elif options.lower()=='w':
                    withdraw = float(input('enter amount you want to withdraw:'))
                    if withdraw <= balance:
                        print('here is your:', withdraw)
                        balance = balance - withdraw
                        print('anything else?')
                        options = input("please enter 'b' for balance, 'w' to withdraw, 'd' to deposite and 'q' to quit")
                    else:
                        print('you dont have enough balance.')

                else:
                    options.lower()== 'd'
                    deposite = float(input('enter amount you want to deposite: '))
                    print('you deposited', deposite,)
                    balance = balance + deposite
                    print('anything else?')
                    options = input("please enter 'b' for balance, 'w' to withdraw, 'd' to deposite and 'q' to quit")
            else:
                print('bad choice')
                options = input("please enter 'b' for balance, 'w' to withdraw, 'd' to deposite and 'q' to quit")

def num_icrease(num):
    x=0
    while x <= 5:
        print(x)
        x += 1
        
def num_skip(num):    
    for x in range(10):
        if x==5:
            continue
        print(x)
num_skip(10)

def num_loop(num):    
    for x in range(4,11):
        if x>=4:
            print(x)
num_loop(10)

def GCcontent():
    tRNA = 'AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTT'
    A = tRNA.count('A')
    T = tRNA.count('T')
    C = tRNA.count('C')
    G = tRNA.count('G')
    tRNAleng = len(tRNA)
    GC = (G+C)
    GCperc = ((GC/tRNAleng)*100)
    print('The GC percent is %.2f' %(GCperc),'%')
GCcontent()
        
        
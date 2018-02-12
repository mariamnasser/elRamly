arr=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
print(arr[1],arr[2],arr[3],arr[4])
print(arr[5],arr[6],arr[7],arr[8])
print(arr[9],arr[10],arr[11],arr[12])
print(arr[13],arr[14],arr[15],arr[16])
turn = 1
while (True):
    m=int(input("Enter square 1:"))
    n=int(input("Enter square 2:"))   
    if (((m>0 and m<=16 and n>0 and n<=16)and(arr[m]!='x' and arr[n]!='x')))and(((n>m and n-m==1 and m%4!=0)or(n>m and n-m==4))or((m>n and m-n==1 and n%4!=0)or(m>n and m-n==4))) :
                arr[m]='x'
                arr[n]='x' 
                print(arr[1],arr[2],arr[3],arr[4])
                print(arr[5],arr[6],arr[7],arr[8])
                print(arr[9],arr[10],arr[11],arr[12])
                print(arr[13],arr[14],arr[15],arr[16])          
                
    else :
        
 
            while True:
                m=int(input("Enter another num ya DONKEY!!:"))
                n=int(input("Enter another num ya DONKEY!!"))
                
                if ((m>0 and m<16 and n>1 and n<=16)and(n>m and n-m==1 and m%4!=0)or(n>m and n-m==4 )and (arr[m]!='x' and arr[n]!='x')):
                    arr[m]='x'
                    arr[n]='x'
                    print(arr[1],arr[2],arr[3],arr[4])
                    print(arr[5],arr[6],arr[7],arr[8])
                    print(arr[9],arr[10],arr[11],arr[12])
                    print(arr[13],arr[14],arr[15],arr[16])  
                    break

    counter = 0
    
    for i in range (1,17):
        if( (i==16 or arr[i+1]=='x') and (i>=13 or arr[i+4]=='x')) or( arr[i]=='x'):
           counter = counter + 1
    if counter == 16 :
        if turn == 1:
            print("P1ayer 1 is the winner")
        else:
            print("Player 2 is the winner")
            
        break

    if turn == 1:
        turn = 2
    else:
        turn = 1

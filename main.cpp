  #include <iostream>
using namespace std;

int main()
{
//mas2ala bta3t Dr elramly >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    string arr[17]= {"0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"};
    cout<<arr[1]<<"\t"<<arr[2]<<"\t"<<arr[3]<<"\t"<<arr[4]<<endl<<arr[5]<<"\t"<<arr[6]<<"\t"<<arr[7]<<"\t"<<arr[8]<<endl<<arr[9]<<"\t"<<arr[10]<<"\t"<<arr[11]<<"\t"<<arr[12]<<endl<<arr[13]<<"\t"<<arr[14]<<"\t"<<arr[15]<<"\t"<<arr[16]<<endl;
    int turn=1;
    int m,s;
    while(true)
    {
        cout<<"enter the two numbers you want to replace them: ( "<<turn<<" ) ";
        cin>>m>>s;

        if((((m>0 && (m<=16)) && (s>0) && (s<=16))&&((arr[m]!="x") && (arr[s]!="x")))&&(((s>m) && (s-m==1) && (m%4!=0))||((s>m) && (s-m==4))||((m>s) && (m-s==1) && (s%4!=0))||((m>s) && (m-s==4))))
        {
            arr[m]="x";
            arr[s]="x";
            cout<<arr[1]<<"\t"<<arr[2]<<"\t"<<arr[3]<<"\t"<<arr[4]<<endl<<arr[5]<<"\t"<<arr[6]<<"\t"<<arr[7]<<"\t"<<arr[8]<<endl<<arr[9]<<"\t"<<arr[10]<<"\t"<<arr[11]<<"\t"<<arr[12]<<endl<<arr[13]<<"\t"<<arr[14]<<"\t"<<arr[15]<<"\t"<<arr[16]<<endl;

        }
        else
            while (true)
            {
                cout<< " enter another two numbers  ya DONKEY!! :  ";
                cin>>m>>s;
                if((((m>0 && (m<=16)) && (s>0) && (s<=16))&&((arr[m]!="x") && (arr[s]!="x")))&&(((s>m) && (s-m==1) && (m%4!=0))||((s>m) && (s-m==4))||((m>s) && (m-s==1) && (s%4!=0))||((m>s) && (m-s==4))))
                {
                    arr[m]="x";
                    arr[s]="x";
                    cout<<arr[1]<<"\t"<<arr[2]<<"\t"<<arr[3]<<"\t"<<arr[4]<<endl<<arr[5]<<"\t"<<arr[6]<<"\t"<<arr[7]<<"\t"<<arr[8]<<endl<<arr[9]<<"\t"<<arr[10]<<"\t"<<arr[11]<<"\t"<<arr[12]<<endl<<arr[13]<<"\t"<<arr[14]<<"\t"<<arr[15]<<"\t"<<arr[16]<<endl;
                    break;
                }
            }
            int counter=0;
            for(int i=1;i<17;i++){
                 if(( ((i==16 )||( arr[i+1]=="x")) && (i>=13 || (arr[i+4]=="x"))) ||( arr[i]=="x"))
                    counter++;
            }
            if (counter==16){
                if(turn==1)
                    cout<<" player 1 wins congratulation !! \n";

                else
                    cout<<" player 2 wins congratulation !! \n";
                break;
            }
            if (turn==1)
                turn=2;
            else
                turn=1;
    }



    return 0;
}

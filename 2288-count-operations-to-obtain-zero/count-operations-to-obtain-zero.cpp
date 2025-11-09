class Solution {
public:
    int countOperations(int num1, int num2) {
        int n1 = num1;
        int n2 = num2;
        int ops = 0;
        while(n1 > 0 && n2>0){
            if(n1 >= n2){
                n1-=n2;
            }else{
                n2-=n1;
            }
            ops++;
        }
        return ops;
    }
};
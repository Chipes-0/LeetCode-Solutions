class Solution {
    public int divide(int dividend, int divisor) {
        int res = 0;
        boolean flag = false;
        if(dividend < 0 ){
            dividend = -1 * dividend;
            flag = !flag;
        }
        if(divisor < 0 ){
            divisor = -1 * divisor;
            flag = !flag;
        }
        while(dividend >= divisor){
            dividend -= divisor;
            res++;
        }
        return flag ? -1 * res : res;
    }
}
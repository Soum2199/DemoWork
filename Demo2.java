import package.util.*;

class Main {
    public static void main(String[] args) {
        // System.out.println("Try programiz.pro");
        // int a  = 5;
        // a++;
        // System.out.print(a);
        // int hi = Math.floor(Math.random()*100);
        double hi = Math.random()*100;
        System.out.println(hi);
        System.out.println();
        // finding max/highest value from an array
        int[] arr = {2,4,3,5,1}; // not [2,4,3,5,1];
        int maxi = arr[0];
        for(int i=0; i<arr.length; i++){
            if( arr[i] > maxi){
               maxi = arr[i]; 
            }
        }
        // return maxi;
        System.out.println(maxi + " is the highest");
    }
}
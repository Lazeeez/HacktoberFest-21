class Reverse_the_array {
    
    public static void main(String [] args){

        int arr[]=new int[4];
       // int arr2[]=new int[4];

        arr[0]=10;
        arr[1]=20;
        arr[2]=30;
        arr[3]=40;
        /*
        for(int j=0,i=3; j<4;j++,i--){

            arr2[j]=arr[i];
            System.out.println(arr[i]);
        }*/
        int x=0;
        for(int i=0; i<arr.length;i++){
            x=arr[i];
            arr[i]=arr[(arr.length-1)-i];
            arr[(arr.length-1)-i]=x;
        }    
        System.out.println("Reversed Array: ");
        for(int i=0; i<arr.length;i++){
         
            System.out.println(arr[(arr.length-1)-i]);
        }
    }
}

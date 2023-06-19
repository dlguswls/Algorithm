// #include <stdio.h>
 
// int func1(int N){
//     int ret = 0;
//     for(int i = 1; i <= N; i++){
//         if(i % 3 == 0 || i % 5 == 0) ret += i;
//     }
//     return ret;
// }
 
 
// int main(void) {
//     printf("%d",func1(16));
//     return 0;
// }

#include <stdio.h>
 
int func2(int arr[], int N){
    for(int i = 0; i < N; i++)
        for (int j = i+1; j<N; j++)
            if(arr[i] + arr[j] == 100) return 1;
    return 0;
}
 
 
int main(void) {
    printf("%d",func2({1, 52, 48},3));
}


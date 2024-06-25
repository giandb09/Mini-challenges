#include <iostream>

void selectionSort(int arr[], int n) {
    int i, j, min_idx;


    for (i = 0; i < n-1; i++) {

        min_idx = i;
        for (j = i+1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

void imprimirArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int arr[] = {135, 43, 24, 13, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    std::cout << "Array original:" << std::endl;
    imprimirArray(arr, n);

    selectionSort(arr, n);

    std::cout << "Array ordenado en orden ascendente:" << std::endl;
    imprimirArray(arr, n);

    return 0;
}

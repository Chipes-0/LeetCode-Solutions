#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:

    struct Node {
        int maxVal;  // Valor máximo
        int index;   // Índice del valor máximo
    };
    vector<Node>tree;
    void build(const vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            // Nodo hoja: almacena el valor y el índice
            tree[node] = {arr[start], start};
        } else {
            int mid = (start + end) / 2;
            // Construir los hijos
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            // Almacenar el máximo de los hijos y el índice correspondiente
            Node left = tree[2 * node + 1];
            Node right = tree[2 * node + 2];
            
            if (left.maxVal > right.maxVal) {
                tree[node] = left;
            } else if (right.maxVal > left.maxVal) {
                tree[node] = right;
            } else {
                // Si los valores son iguales, tomamos el índice menor
                tree[node] = (left.index < right.index) ? left : right;
            }
        }
    }

    Node query(int node, int start, int end, int L, int R) {
        if (R < start || L > end) {
            // El rango consultado está fuera del rango actual
            return {-1, -1};  // Nodo inválido
        }
        if (L <= start && end <= R) {
            // El rango actual está completamente dentro del rango consultado
            return tree[node];
        }
        // Dividimos el rango y consultamos en los hijos
        int mid = (start + end) / 2;
        Node left = query(2 * node + 1, start, mid, L, R);
        Node right = query(2 * node + 2, mid + 1, end, L, R);

        if (left.maxVal > right.maxVal) {
            return left;
        } else if (right.maxVal > left.maxVal) {
            return right;
        } else {
            // Si los valores son iguales, tomamos el índice menor
            return (left.index < right.index) ? left : right;
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            // Nodo hoja: actualiza el valor y el índice
            tree[node] = {val, idx};
        } else {
            int mid = (start + end) / 2;
            if (start <= idx && idx <= mid) {
                // Actualizamos el hijo izquierdo
                update(2 * node + 1, start, mid, idx, val);
            } else {
                // Actualizamos el hijo derecho
                update(2 * node + 2, mid + 1, end, idx, val);
            }
            // Recalcular el valor del nodo actual
            Node left = tree[2 * node + 1];
            Node right = tree[2 * node + 2];

            if (left.maxVal > right.maxVal) {
                tree[node] = left;
            } else if (right.maxVal > left.maxVal) {
                tree[node] = right;
            } else {
                tree[node] = (left.index < right.index) ? left : right;
            }
        }
    }
    long long maxKelements(vector<int>& nums, int k) {
        int N = nums.size();
        tree.resize(4 * N);
        build(nums, 0, 0, N - 1);
        int out = 0;
        Node biggest;
        while(k--){
            biggest = query(0, 0, N - 1, 0, N);
            out += biggest.maxVal;
            update(0, 0, N - 1, biggest.index, ceil(biggest.maxVal / 3.0));
        }      
        return out;
    }
};
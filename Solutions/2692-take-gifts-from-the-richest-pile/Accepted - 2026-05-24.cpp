#include <cmath>

using namespace std;

class Solution {
public:
    // Maximum Segment Tree
    struct Node
    {
        int maxVal;  
        int index;   
    };

    // SegmentTree Global
    vector<Node> segtree;

    // Función para construir el Segment Tree
    // arr  =    arreglo original
    // node =    indice actual
    // start =   limite inferior del arreglo
    // end   =   limite superior del arreglo  
    void build(const vector<int> &arr, int node, int start, int end){
        // Caso base: si el rango contiene solo un elemento
        if (start == end){
            // Asigna el valor de ese único elemento y su índice al nodo actual
            segtree[node] = {arr[start], start};
        } else {
            // Calcular el punto medio del rango
            int m = (start + end) / 2;
            // Construir el subárbol izquierdo
            build(arr, 2 * node + 1, start, m);
            // Construir el subárbol derecho
            build(arr, 2 * node + 2, m + 1, end);
            // Combinar los resultados de los hijos y almacenar el mayor en el nodo actual
            Node left = segtree[2 * node + 1];
            Node right = segtree[2 * node + 2];

            // Almacena el mayor valor entre los hijos en el nodo actual
            if (left.maxVal > right.maxVal){
                segtree[node] = left;
            } else {
                segtree[node] = right;
            }
        }
    }

    // Función para consultar el valor máximo en el intervalo [L, R]
    // node =    indice actual
    // start =   limite inferior del arreglo
    // end   =   limite superior del arreglo  
    // L =       Limite inferior de la consulta
    // R =       Limite superior de la consulta
    Node query(int node, int start, int end, int L, int R){
        // Si el rango actual está completamente dentro del rango de consulta
        if (L <= start && end <= R){
            return segtree[node];  // Devolver el nodo actual
        }
        // Calcular el punto medio del rango
        int m = (start + end) / 2;
        // Consultar los hijos izquierdo y derecho
        Node left = query(2 * node + 1, start, m, L, R);
        Node right = query(2 * node + 2, m + 1, end, L, R);

        // Devolver el mayor valor entre los dos hijos
        if (left.maxVal > right.maxVal){
            return left;
        } else {
            return right;
        }
    }

    // Función para actualizar un valor en el arreglo original
    // node =    indice actual
    // start =   limite inferior del arreglo
    // end   =   limite superior del arreglo  
    // i     =   indice a actualizar
    // val   =   nuevo valor
    void update(int node, int start, int end, int i, int val){
        // Si el rango actual corresponde a una hoja (el elemento a actualizar)
        if (start == end){
            segtree[node] = {val, i};  // Actualizar el nodo con el nuevo valor y su índice
        } else {
            // Calcular el punto medio del rango
            int m = (start + end) / 2;
            // Determinar si actualizar el hijo izquierdo o derecho
            if (start <= i && i <= m){
                update(2 * node + 1, start, m, i, val);  // Actualizar el subárbol izquierdo
            } else {
                update(2 * node + 2, m + 1, end, i, val);  // Actualizar el subárbol derecho
            }
            // Recalcular el valor máximo del nodo actual tras la actualización
            Node left = segtree[2 * node + 1];
            Node right = segtree[2 * node + 2];

            // Almacena el mayor valor entre los hijos
            if (left.maxVal > right.maxVal){
                segtree[node] = left;
            } else if (right.maxVal > left.maxVal){
                segtree[node] = right;
            }
        }
    }
    long long pickGifts(vector<int>& gifts, int k) {
        int N = gifts.size();
        segtree.resize(4 * N);
        build(gifts, 0, 0, N - 1);
        long long out = 0;
        Node biggest;
        int new_val;
        while(k--){
            biggest = query(0, 0, N - 1, 0, N);
            new_val = floor(sqrt(biggest.maxVal));
            out += biggest.maxVal - new_val;
            update(0, 0, N - 1, biggest.index, new_val);
        }      
        int total = 0;
        for(int a: gifts){
            total += a;
        }
        return total - out;
    }
};
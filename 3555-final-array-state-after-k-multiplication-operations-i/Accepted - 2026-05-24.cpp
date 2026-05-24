class Solution {
public:
    // Minimum Segment Tree
    struct Node
    {
        int minVal; // Almacena el valor mínimo
        int index;  // Almacena el índice correspondiente
    };

    // SegmentTree Global
    vector<Node> segtree;

    // Función para construir el Segment Tree
    // arr  =    arreglo original
    // node =    índice actual
    // start =   límite inferior del arreglo
    // end   =   límite superior del arreglo
    void build(const vector<int> &arr, int node, int start, int end)
    {
        // Caso base: si el rango contiene solo un elemento
        if (start == end)
        {
            // Asigna el valor de ese único elemento y su índice al nodo actual
            segtree[node] = {arr[start], start};
        }
        else
        {
            // Calcular el punto medio del rango
            int m = (start + end) / 2;
            // Construir el subárbol izquierdo
            build(arr, 2 * node + 1, start, m);
            // Construir el subárbol derecho
            build(arr, 2 * node + 2, m + 1, end);
            // Combinar los resultados de los hijos y almacenar el menor en el nodo actual
            Node left = segtree[2 * node + 1];
            Node right = segtree[2 * node + 2];

            // Almacena el menor valor entre los hijos en el nodo actual
            if (left.minVal < right.minVal)
            {
                segtree[node] = left;
            }
            else if (right.minVal < left.minVal)
            {
                segtree[node] = right;
            }
            else
            {
                segtree[node] = (left.index < right.index) ? left : right;
            }
        }
    }

    // Función para consultar el valor mínimo en el intervalo [L, R]
    // node =    índice actual
    // start =   límite inferior del arreglo
    // end   =   límite superior del arreglo
    // L =       Límite inferior de la consulta
    // R =       Límite superior de la consulta
    Node query(int node, int start, int end, int L, int R)
    {
        // Si el rango actual está completamente dentro del rango de consulta
        if (L <= start && end <= R)
        {
            return segtree[node]; // Devolver el nodo actual
        }

        // Si el rango actual está completamente fuera del rango de consulta
        if (end < L || start > R)
        {
            return {INT_MAX, -1}; // Retorna un valor "infinito" para ignorar
        }

        // Calcular el punto medio del rango
        int m = (start + end) / 2;
        // Consultar los hijos izquierdo y derecho
        Node left = query(2 * node + 1, start, m, L, R);
        Node right = query(2 * node + 2, m + 1, end, L, R);

        // Devolver el menor valor entre los dos hijos
        if (left.minVal < right.minVal)
        {
            return left;
        }
        else if (right.minVal < left.minVal)
        {
            return right;
        }
        else
        {
            return (left.index < right.index) ? left : right;
        }
    }

    // Función para actualizar un valor en el arreglo original
    // node =    índice actual
    // start =   límite inferior del arreglo
    // end   =   límite superior del arreglo
    // i     =   índice a actualizar
    // val   =   nuevo valor
    void update(int node, int start, int end, int i, int val)
    {
        // Si el rango actual corresponde a una hoja (el elemento a actualizar)
        if (start == end)
        {
            segtree[node] = {val, i}; // Actualizar el nodo con el nuevo valor y su índice
        }
        else
        {
            // Calcular el punto medio del rango
            int m = (start + end) / 2;
            // Determinar si actualizar el hijo izquierdo o derecho
            if (start <= i && i <= m)
            {
                update(2 * node + 1, start, m, i, val); // Actualizar el subárbol izquierdo
            }
            else
            {
                update(2 * node + 2, m + 1, end, i, val); // Actualizar el subárbol derecho
            }
            // Recalcular el valor mínimo del nodo actual tras la actualización
            Node left = segtree[2 * node + 1];
            Node right = segtree[2 * node + 2];

            // Almacena el menor valor entre los hijos
            if (left.minVal < right.minVal)
            {
                segtree[node] = left;
            }
            else if (right.minVal < left.minVal)
            {
                segtree[node] = right;
            }
            else
            {
                segtree[node] = (left.index < right.index) ? left : right;
            }
        }
    }

    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        int N = nums.size();
        segtree.resize(4 * N);
        build(nums, 0, 0, N - 1);
        Node smallest;
        while(k--){
            smallest = query(0, 0, N - 1, 0, N-1);
            update(0, 0, N - 1, smallest.index, smallest.minVal * multiplier);
        }
        for(int i = 0; i < N; i++){
            smallest = query(0, 0, N - 1, i, i);
            nums[i] = smallest.minVal;
        }
        return nums;
    }
};
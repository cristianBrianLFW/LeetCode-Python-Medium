# include <stdio.h>
# include <stdlib.h>


int main (){

    int n, m;
    int *vA;
    int i, j, elem;

    printf ("Digite o numero de linhas e colunas ");

    scanf ("%d %d", &n, &m);

    vA = ( int *) malloc ( sizeof ( int ) * n * m);

    for ( i = 0; i < n; i++ ){
        for ( j = 0; j < m; j++){
            printf ("Digite elem [ %d ] [ %d ] ", i, j); 
            scanf ("%d", &elem);

            vA[ i * m + j] = elem;
        }
    }

    for ( i = 0; i < m; i++){

        printf ("%d ", vA[ ( n / 2)* m + i]);
    }

    return 0;

}
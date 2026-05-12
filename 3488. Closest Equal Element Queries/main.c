# include <stdio.h>
# include <stdlib.h>

// função auxiliar ( so de visualização mesmo )

void imprime_matriz_padrao ( int * vA, int n, int m){
    
    
    int i, j;
    printf ("------- IMPRIMINDO MATRIZ PADRAO ----------\n\n");
    
    for ( i = 0; i < n; i++ ){
        printf ("[ ");
        for ( j = 0; j < m; j++){
            printf ("%d ", vA[ i * m + j]);
        }
        printf ("]\n");
    }
    printf ("\n");
}

void imprime_matriz_vetor ( int *vA, int n, int m){

    int i, j;

    printf ("------- IMPRIMINDO MATRIZ COMO VETOR ----------\n\n");
    
    printf ("[ ");
    for ( i = 0; i < n; i++ ){
        for ( j = 0; j < m; j++){
            printf ("%d ", vA[ i * m + j]);
        }
    }
    printf ("]\n");

    printf ("\n");

}


// seu código

int main (){

    int n, m;
    int *vA;
    int i, j, elem;

    printf ("Digite o numero de linhas e colunas ");

    scanf ("%d %d", &n, &m);

    vA = ( int *) malloc ( sizeof ( int ) * n * m);

    for ( i = 0; i < n; i++ ){

        printf ("Linha [ %d ] da Matriz\n", i);

        for ( j = 0; j < m; j++){
            printf ("Digite elem [ %d ] [ %d ] ", i, j); // ajustando os indices

            scanf ("%d", &elem);

            vA[ i * m + j] = elem;
        }
        printf ("\n");
    }

    // função minha para visualizar a matriz ( forma padrão )

    imprime_matriz_padrao ( vA, n, m);

    imprime_matriz_vetor ( vA, n, m);

    printf ("--------- Resultado -----------\n\n");

    printf ("[ ");

    for ( i = 0; i < m; i++){
        printf ("%d ", vA[ ( n / 2)*m + i]);
    }

    printf ("]\n\n");

    return 0;

}
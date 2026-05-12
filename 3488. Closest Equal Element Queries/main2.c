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
            printf ("Digite elem [ %d ] [ %d ] ", n, m); // ajuste meu apenas para comparar as saídas 
                                                         // não precisa disso na prova e nem nas outras atividades
                                                         // é só uma coisa minha para corrigir nesse contexto msm
            scanf ("%d", &elem);

            vA[ i * m + j] = elem;
        }
    }

    printf ("\n\n------- RESULTADO ----------\n\n"); // só ajuste para deixar mais
                                                    // claro a correção

    printf ("[ ");

    for ( i = 0; i < m; i++){

        printf ("%d ", vA[ ( n / 2) + i]);
    }

    printf ("]\n\n");

    return 0;

}

// caso teste matriz 3 x 3

// [ 0, 1, 2] [ 3, 4, 5 ] [ 6, 7, 8 ] --> formato padrão

// [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] --> em vetor

// saida esperada : [ 3, 4, 5 ]

// saída obtida : [ 1, 2, 3 ]
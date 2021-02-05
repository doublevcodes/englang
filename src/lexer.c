#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "../include/lexing.h"

int array_len;

char *to_char_array(char filename[]) {

    int initial_length_of_array = 32, array_ptr = 0;
    char ch, *array = calloc(initial_length_of_array, 1);
    FILE *fp;
  
    fp = fopen(filename, "r");
    if(NULL == fp){
        perror("TO_CHAR_ARRAY: Fopen error");
        array = NULL;
        goto cleanup;
  }

    while(1){
        ch = getc(fp);
        if (EOF == ch) { break; } 
        if(array_ptr >= initial_length_of_array){
            initial_length_of_array += 32;
            array = realloc(array, initial_length_of_array);
        }
        array[array_ptr] = ch;
        //printf("%c  --> POSITION %d\n", array[array_ptr], array_ptr);
        array_ptr++;
  }
  
    array_len = array_ptr;
    
    array = realloc(array, array_len);

    cleanup:
        return array;
}

void lex(char *ptr) {
    for(int i=0; i<array_len; i++){
   		char cur = ptr[i];
        if (NEWLINE(cur)) {
            printf("\\n      : NEWLINE\n");
        } else if (SPACE(cur)) {
            printf("        : SPACE\n");
        } else if (DOUBLEQUOTE(cur)) {
            printf("\"       : STRING DELIMITER - DOUBLE QUOTES\n");
        } else if (PLUS(cur, ptr, i)) {
            printf("PLUS    : ARITHMETIC OPERATOR - ADDITION\n");
            i += 3;
        } else if (MINUS(cur, ptr, i)){
            printf("MINUS   : ARITHMETIC OPERATOR - SUBTRACTION");
            i += 4;
        } else if (SINGLEQUOTE(cur)) {
            printf("'       : STRING DELIMITER - SINGLE QUOTES\n");
        } else if (SAY(cur, ptr, i)) {
            printf("SAY     : OUTPUT STATEMENT\n");
            i += 2;
        } else if (isdigit(cur)) {
            printf("%c       : INTEGER\n", cur);
        } else {
            printf("%c       : UNRECOGNISED TOKEN\n", cur);
        }
	}
}

int main(int argc, char ** argv) {
  if(argc < 2){
    printf("Usage: %s <file>", argv[0]);
    goto cleanup;
  }

  char *code_array = to_char_array(argv[1]);
  lex(code_array);

cleanup:
  return 0;
}
#include <stdio.h>
#include <stdlib.h>

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
    
    cleanup:
        return array;
}

void lex(char *ptr) {
    for(int i=0; i<array_len; i++){
   		char cur = ptr[i];
        if (cur == '\n') {
            printf("\\n      : NEWLINE\n");
        } else if (cur == ' ') {
            printf("        : SPACE\n");
        } else if (cur == 34) {
            printf("\"       : STRING DELIMITER - DOUBLE QUOTES\n");
        } else if (cur == 39) {
            printf("'       : STRING DELIMITER - SINGLE QUOTES\n");
        } else if (cur == 's' && ptr[i + 1] == 'a' && ptr[i + 2] == 'y' && ptr[i + 3] == ' ') {
            printf("SAY     : OUTPUT STATEMENT\n");
            i += 2;
        }
        else {
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

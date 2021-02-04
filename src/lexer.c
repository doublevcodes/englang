#include <stdio.h>
#include <stdlib.h>

int array_len;

char *to_char_array(char filename[]) {
  int initial_length_of_array = 32;
  FILE *fp;
  char ch;
  char *array = calloc(initial_length_of_array, 1);
  int array_ptr = 0;
  
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
      array_ptr++;
  }
  array_len = array_ptr;

    cleanup:
        return array;
}

char *scan_string(char *ptr, int i){
    int j = 0;
    char cur = ptr[i];
    char ret[32] = {};
    while(!strcmp(cur, "'")) {
        ret[j] = cur;
        i++;
        j++;
    }
    return ret;
}

void lex(char *ptr) {
    for(int i=0; i<array_len; i++){
   		char cur = ptr[i];
        if (cur == '\n') {
            printf("\\n : NEWLINE\n");
        } else if (strcmp(cur, "'")) {
            char string[] = scan_string(ptr, i);
            printf(string);
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

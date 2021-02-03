#include <stdio.h>
#include <stdlib.h>

char *to_char_array(char filename[]) {
    char length = 32;
    FILE *fp;
    char ch;
    char *array = calloc(1, length);
    int array_ptr = 0;
    fp = fopen(filename, "r");
    while(1){
        ch = getc(fp);
        if (EOF == ch) {
            break;
        } 
        if(array_ptr >= length){
            length += 32;
            array = realloc(array, length);
        }
        array[array_ptr] = ch;
        array_ptr++;
    }
    return array;
}



int main() {
    char *code_array = to_char_array("filename.txt");
    return 0;
}

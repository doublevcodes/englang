int NEWLINE(char cur) {
    if (cur == '\n') {
        return 1;
    } else {
        return 0;
    }
}

int SPACE(char cur) {
    if (cur == ' ') {
        return 1;
    } else {
        return 0;
    }
}

int SINGLEQUOTE(char cur) {
    if (cur == 39) {
        return 1;
    } else {
        return 0;
    }
}

int DOUBLEQUOTE(char cur) {
    if (cur == 34) {
        return 1;
    } else {
        return 0;
    }
}

int SAY(char cur, char *ptr, int i) {
    if ((cur == 's' || cur == 'S') && (ptr[i + 1] == 'a' || ptr[i + 1] == 'A') && (ptr[i + 2] == 'y' || ptr[i + 2] == 'Y') && ptr[i + 3] == ' ' && (ptr[i - 1] == ' ' || ptr[i - 1] == 0)) {
        return 1;
    } else {
        return 0;
    }
}

int PLUS(char cur, char *ptr, int i) {
    if ((cur == 'p' || cur == 'P') && (ptr[i + 1] == 'l' || ptr[i + 1] == 'L') && (ptr[i + 2] == 'u' ||ptr[i + 2] == 'U') && (ptr[i + 3] == 's' || ptr[i + 3] == 'S') && (ptr[i + 4] == ' ') && (ptr[i - 1] == ' ')) {
        return 1;
    } else {
        return 0;
    }
}

int MINUS(char cur, char *ptr, int i) {
    if ((cur == 'm' || cur == 'M') && (ptr[i + 1] == 'i' || ptr[i + 1] == 'I') && (ptr[i + 2] == 'n' ||ptr[i + 2] == 'N') && (ptr[i + 3] == 'u' || ptr[i + 3] == 'U') && (ptr[i + 4] == 's' || ptr[i + 4] == 'S') && (ptr[i + 5] == ' ') && (ptr[i - 1] == ' ')) {
        return 1;
    } else {
        return 0;
    }
}


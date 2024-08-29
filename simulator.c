
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//gcc simulador.c -o simulador
// Função para limpar o buffer de entrada
void clear_input_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

// Função para esperar o Enter do usuário
void wait_for_enter() {
    printf("press enter to continue...");
    clear_input_buffer();
}

// Função para simular as instruções
void execute_instruction(char *operation, char *reg, char *value, long *rax, long *rbx, long *rcx, long *rdx) {
    long *register_ptr = NULL;

    // Determina qual registrador está sendo referenciado
    if (strcmp(reg, "rax") == 0) {
        register_ptr = rax;
    } else if (strcmp(reg, "rbx") == 0) {
        register_ptr = rbx;
    } else if (strcmp(reg, "rcx") == 0) {
        register_ptr = rcx;
    } else if (strcmp(reg, "rdx") == 0) {
        register_ptr = rdx;
    }

    if (register_ptr == NULL) {
        printf("Registrador desconhecido: %s\n", reg);
        return;
    }

    if (strcmp(operation, "mov") == 0) {
        // Operação MOV
        if (value[0] == 'r') {
            // Copia o valor de outro registrador
            if (strcmp(value, "rax") == 0) *register_ptr = *rax;
            else if (strcmp(value, "rbx") == 0) *register_ptr = *rbx;
            else if (strcmp(value, "rcx") == 0) *register_ptr = *rcx;
            else if (strcmp(value, "rdx") == 0) *register_ptr = *rdx;
            else printf("no x86 register: %s\n", value);
        } else {
            // Move um valor direto para o registrador
            *register_ptr = atol(value);
        }
    } else if (strcmp(operation, "add") == 0) {
        // Operação ADD
        if (value[0] == 'r') {
            // Adiciona o valor de outro registrador
            if (strcmp(value, "rax") == 0) *register_ptr += *rax;
            else if (strcmp(value, "rbx") == 0) *register_ptr += *rbx;
            else if (strcmp(value, "rcx") == 0) *register_ptr += *rcx;
            else if (strcmp(value, "rdx") == 0) *register_ptr += *rdx;
            else printf("no x86 register : %s\n", value);
        } else {
            // Adiciona um valor direto ao registrador
            *register_ptr += atol(value);
        }
    }
}

int main() {
    char filename[256];
    FILE *file;
    char line[256];
    char *operation, *reg, *value;
    long rax = 0, rbx = 0, rcx = 0, rdx = 0;
    printf("\033c\033[47;30m");
    // Pergunta o nome do ficheiro ao usuário
    printf("file name: ");
    scanf("%255s", filename);
    clear_input_buffer();

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Erro on file: %s\n", filename);
        return 1;
    }

    // Lê cada linha do ficheiro e processa as instruções
    while (fgets(line, sizeof(line), file)) {
        operation = strtok(line, " ,\n");
        reg = strtok(NULL, " ,\n");
        value = strtok(NULL, " ,\n");

        if (operation != NULL && reg != NULL && value != NULL) {
            execute_instruction(operation, reg, value, &rax, &rbx, &rcx, &rdx);
            printf("rax: %ld, rbx: %ld, rcx: %ld, rdx: %ld\n", rax, rbx, rcx, rdx);
            wait_for_enter();
        }
    }

    fclose(file);
    return 0;
}

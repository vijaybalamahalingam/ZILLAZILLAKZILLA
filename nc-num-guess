#include <stdio.h>
int main() {
    int num, guess;
    int attempts = 0;
    printf("Welcome to the Number Guessing Game!\n");
    printf("User A, Enter a number between 1 and 100:\n");
    scanf("%d", &num);
    printf("User B, Try to guess the number between 1 and 100.\n");

    do {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        attempts++;

        if (guess < num) {
            printf("Too low! Try again.\n");
        } else if (guess > num) {
            printf("Too high! Try again.\n");
        } else {
            printf("Congratulations! You guessed the number %d in %d attempts.\n", num,attempts);
        }
    } while (guess != num);

    return 0;
}

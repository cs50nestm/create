#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

#define ALPHASIZE 26
char substitution[ALPHASIZE];

bool alphabet(string key);

int main(int argc, string argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Validate key length
    string key = argv[1];
    if (strlen(key) != ALPHASIZE)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Validate key and add chars to the substitution array
    if (!alphabet(key))
    {
        printf("Key must contain non-repeating alpha characters.\n");
        return 1;
    }

    // Prompt user for plaintext
    string plaintext = get_string("plaintext:  ");

    // Encrypt plaintext with substitution
    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        char c = plaintext[i];
        if (isupper(c))
        {
            printf("%c", substitution[c - 'A']);
        }
        else if (islower(c))
        {
            printf("%c", tolower(substitution[c - 'a']));
        }
        else
        {
            printf("%c", c);
        }
    }

    printf("\n");
    return 0;
}

bool alphabet(string key)
{
    // Initialze used to keep track of used chars
    bool used[ALPHASIZE] = {false};
    for (int i = 0; i < ALPHASIZE; i++)
    {
        char c = toupper(key[i]);

        // Validate key
        if (!isalpha(key[i]) || used[c -'A'] == true)
        {
            return false;
        }

        // Add chars to be substituted
        substitution[i] = c;
        used[c - 'A'] = true;
    }

    // Key is valid and substitution array complete
    return true;
}

#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>

int     curl_easy_test(void);

int     main(int argc, char **argv)
{
        (void) argc;
        (void) argv;
        int exit;


        exit = curl_easy_test();
        return(exit);
}

int curl_easy_test(void)
{
        CURL *curl = curl_easy_init();

        if (!curl)
        {
                fprintf(stderr, "init failed!");
                return (EXIT_FAILURE)
        }

        curl_easy_cleanup(curl);
        return (EXIT_SUCCESS);
}

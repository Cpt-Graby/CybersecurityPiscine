#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
//#include <curl/curl.h>

typedef struct arguments {
	int rec;
	//char *path;
} argu;


int     curl_easy_test(void);
int		check_input(int ac, char **av, argu *args);

int     main(int argc, char **argv)
{
        (void) argc;
        (void) argv;
        int exit;
		argu args;

		exit = check_input(argc, argv, &args);
		if (!exit)
			return (exit);

        //exit = curl_easy_test();
		//if (!exit)
		return (EXIT_SUCCESS);
}

int	check_input(int ac, char **av, argu *args)
{
	// Cas gerer:
	// - pas d'argument
	// - argument de recusivit
	int c = -1;

	if (ac == 1)
	{
			fprintf(stderr, "No arguments\n");
			return (EXIT_FAILURE);
	}
	while (c = getopt(ac, av, "rlp") != -1)
	{
		switch (c)
		{
			case 'r':
				args->rec = atoi(optarg);
				break;
			default:
				break;
		}
	}
	return (EXIT_SUCCESS);
}

//int curl_easy_test(void)
//{
//        CURL *curl = curl_easy_init();
//
//        if (!curl)
//        {
//                fprintf(stderr, "init failed!");
//                return (EXIT_FAILURE);
//        }
//
//        curl_easy_cleanup(curl);
//        return (EXIT_SUCCESS);
//}

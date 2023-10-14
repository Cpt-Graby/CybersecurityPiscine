/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agonelle <marvin@42lausanne.ch>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/14 17:16:42 by agonelle          #+#    #+#             */
/*   Updated: 2023/10/14 18:01:22 by agonelle         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>

int	main(void)
{
	CURL				*curl;
	CURLcode			res;

	curl = curl_easy_init();
	if (!curl)
		return (-1);
	curl_easy_setopt(curl, CURLOPT_URL, "https://www.google.com");
	res = curl_easy_perform(curl);
	if (res != CURLE_OK)
		return (-1);
	curl_easy_cleanup(curl);
	return (0);
}
	//curl_easy_strerror(res);
	// https://www.youtube.com/watch?v=KSc4zf5t6I4

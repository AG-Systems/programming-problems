#include <iostream>

int main()
{
//	int input;
//	std::cin >> input;

	std::cout << "Please insert the top number: " << std::endl;
	int first;
	std::cin >> first;
/*	for (int loop = 1; loop <= input; loop++)
	{
		std::cout << "Please insert the top number: " << std::endl;
	}
*/	
	std::cout << "Please insert the next top number: " << std::endl;
	int two;
	std::cin >> two;
	std::cout << "Please insert the bottom number: " << std::endl;
	int bot1;
	std::cin >> bot1;
	std::cout << "Please insert the 2nd bottom number: " << std::endl;
	int bot2;
	std::cin >> bot2;
	int test = 5;

	if ( bot1 != bot2)
	{
		test++;
		if (test = 6 )
			{
			int final;
			int firstF;
			int twoF;
			final = bot1 * bot2;
			firstF = bot2 * first;
			twoF = bot2 * two;
			int finalA = first + two;
			std::cout << "\n" << "\n " << "------------------------------------------------------" << std::endl;
			std::cout << finalA << "\n" << final << std::endl;

		}
	}


	
	if ( bot1 == bot2)
	{
		int finalB = first + two;
		std::cout << "\n" << "\n " << "------------------------------------------------------" << std::endl;
		std::cout << finalB << "\n" << bot1 << std::endl;
	}


	system("PAUSE");
}

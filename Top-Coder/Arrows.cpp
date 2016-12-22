#include <iostream>
#include <string>  
#include <vector>
class Arrows
{
public:
	int longestArrow(std::string);
	int arrowFinder(std::string,std::string, std::string,int);
	int revarrowFinder(std::string,std::string,std::string,int);
};
int Arrows::arrowFinder(std::string str1,std::string str2,std::string str3,int counter)
{
	for(int z = 0; z < str1.size(); z++)
	{
		std::size_t found = str1.find(str2);
		if(found!=std::string::npos)
		{
			counter++;
			str1 += str3;
		}
		else
		{
			break;
		}
	}
	return counter;
}

int Arrows::revarrowFinder(std::string str1,std::string str2, std::string str3, int counter)
{
	for(int z = 0; z < str1.size(); z++)
	{
		std::size_t found = str1.find(str2);
		if(found!=std::string::npos)
		{
			counter++;
			str1 = str3 + str1;
		}
		else
		{
			break;
		}
	}
	return counter;	
}
int Arrows::longestArrow(std::string str)
{
	int counter = 0;
	std::vector <int> list;
	int highnum = str[0];
	std::string frontarrow = "<";
	std::string backarrow = ">";
	std::string dash = "-";
	std::string equal = "=";
	Arrows::arrowFinder(str,frontarrow,dash,counter);
	list.push_back(counter);
	Arrows::arrowFinder(str,frontarrow,equal,counter);
	list.push_back(counter);
	Arrows::revarrowFinder(str,backarrow,dash,counter);
	list.push_back(counter);
	Arrows::revarrowFinder(str,backarrow,equal,counter);
	for(int c = 0; c < list.size(); c++)
	{
		std::cout << list[c] << " ";
		if(highnum < str[c])
		{
			highnum = str[c];
		}
	}
	std::cout << "The longest arrow is: " << highnum << std::endl;
	return highnum;
}

int main()
{
	std::string str = "<----=====>";
	Arrows a;
	a.longestArrow(str);
}

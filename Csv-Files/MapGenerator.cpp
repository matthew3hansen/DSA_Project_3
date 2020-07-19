#include <iostream>
#include <fstream>
#include <time.h>
#include <queue>

#define GRIDSIZE 500
#define PERCENTBUILDINGS 20
#define RANGEOFCRIMEVALUES 9 //works up to 9 only due to "char" nature of this program which originally did not handle digits
#define OUTPUTFILENAME "randomizedCityMap.csv"



bool checkIfNotEnclosed(char storeArray[GRIDSIZE][GRIDSIZE], int, int);
void floodfill(char storeArray[GRIDSIZE][GRIDSIZE], int, int);

int main()
{
    srand(time(NULL));

    char storeArray[GRIDSIZE][GRIDSIZE * 2];


    //randomize data
    for (int i = 0; i < GRIDSIZE; i++)
    {
        for (int j = 0; j < GRIDSIZE; j++)
        {
            //1 through 100
            int randomNumber = rand() % 100 + 1;

            if (randomNumber <= PERCENTBUILDINGS)
            {
                storeArray[i][j] = '0';
            }
            else
            {
                int randomInt = rand() % RANGEOFCRIMEVALUES + 1;
                storeArray[i][j] = randomInt + '0';
            }
        }
    }
    //make borders clear
    for (int i = 0; i < GRIDSIZE; i++)
    {
        int randomInt = rand() % RANGEOFCRIMEVALUES + 1;
        storeArray[0][i] = randomInt + '0';
        randomInt = rand() % RANGEOFCRIMEVALUES + 1;
        storeArray[GRIDSIZE - 1][i] = randomInt + '0';
        randomInt = rand() % RANGEOFCRIMEVALUES + 1;
        storeArray[i][0] = randomInt + '0';
        randomInt = rand() % RANGEOFCRIMEVALUES + 1;
        storeArray[i][GRIDSIZE - 1] = randomInt + '0';
    }

    char temp[GRIDSIZE][GRIDSIZE];

    for (int i = 0; i < GRIDSIZE; i++)
    {
        for (int j = 0; j < GRIDSIZE; j++)
        {
            temp[i][j] = storeArray[i][j];
        }
    }
    //escape out enclosed streets
    for (int i = 1; i < GRIDSIZE - 1; i++)
    {
        for (int j = 1; j < GRIDSIZE - 1; j++)
        {
            if (temp[i][j] == '0' || temp[i][j] == 'A')
                continue;

            //reset temp array
            for (int i = 0; i < GRIDSIZE; i++)
            {
                for (int j = 0; j < GRIDSIZE; j++)
                {
                    temp[i][j] = storeArray[i][j];
                }
            }

            int shiftCount = 1;
            while (!checkIfNotEnclosed(temp, i, j))
            {
                std::cout << "Found index " << i << " " << j << " that is completely enclosed, blindly opening up one block to the left and checking again.\n";

                int randomInt = rand() % RANGEOFCRIMEVALUES + 1;
                storeArray[i - shiftCount][j] = randomInt + '0';
                shiftCount++;
                //reset temp array
                for (int i = 0; i < GRIDSIZE; i++)
                {
                    for (int j = 0; j < GRIDSIZE; j++)
                    {
                        temp[i][j] = storeArray[i][j];
                    }
                }
            }
        }
    }


    //put in commas
    for (int i = 0; i < GRIDSIZE; i++)
    {
        for (int j = GRIDSIZE - 1; j != -1; j--)
        {
            storeArray[i][2 * j] = storeArray[i][j];
            storeArray[i][2 * j + 1] = ',';
        }
    }
    

    //print out
    std::ofstream outFile;
    outFile.open(OUTPUTFILENAME);
    for (int i = 0; i < GRIDSIZE; i++)
    {
        for (int j = 0; j < GRIDSIZE * 2; j++)
        {
            outFile << storeArray[i][j];
        }
        outFile << "\n";
    }
    outFile.close();
    

    return 0;
}

bool checkIfNotEnclosed(char storeArray[GRIDSIZE][GRIDSIZE], int i, int j)
{
    floodfill(storeArray, i, j);

    if (storeArray[0][0] == 'A')
        return true;
    else
        return false;
}

void floodfill(char storeArray[GRIDSIZE][GRIDSIZE], int i, int j)
{
    if (storeArray[i][j] == '0' || storeArray[i][j] == 'A')
    {
        return;
    }
    else
    {
        storeArray[i][j] = 'A';
    }
    std::queue<int> xStack;
    std::queue<int> yStack;

    if (i - 1 >= 0)
    {
        xStack.push(i - 1);
        yStack.push(j);
    }
    if (i + 1 < GRIDSIZE)
    {
        xStack.push(i + 1);
        yStack.push(j);
    }
    if (j - 1 >= 0)
    {
        xStack.push(i);
        yStack.push(j-1);
    }
    if (j + 1 < GRIDSIZE)
    {
        xStack.push(i);
        yStack.push(j + 1);
    }

    while (!xStack.empty())
    {
        if (storeArray[xStack.front()][yStack.front()] == 'A' || storeArray[xStack.front()][yStack.front()] == '0')
        {
            xStack.pop();
            yStack.pop();
        }
        else
        {
            storeArray[xStack.front()][yStack.front()] = 'A';

            if (xStack.front() - 1 >= 0)
            {
                xStack.push(xStack.front() - 1);
                yStack.push(yStack.front());
            }
            if (xStack.front() + 1 < GRIDSIZE)
            {
                xStack.push(xStack.front() + 1);
                yStack.push(yStack.front());
            }
            if (yStack.front() - 1 >= 0)
            {
                xStack.push(xStack.front());
                yStack.push(yStack.front() - 1);
            }
            if (yStack.front() + 1 < GRIDSIZE)
            {
                xStack.push(xStack.front());
                yStack.push(yStack.front() + 1);
            }

            xStack.pop();
            yStack.pop();
        }
    }
}
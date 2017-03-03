//	  -*- coding: UTF-8 -*-
//
//    Copyright(C) 2017 Vitaly Yaroshenko <yarokha@gmail.com>
//
//    This program is free software : you can redistribute it and / or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with this program.If not, see <http://www.gnu.org/licenses/>.


#include<iostream>
#include<fstream>

bool RowCheck(int *mat[], int x, int y, int num);		// Search a number in a row (x) of the whole matrix
bool ColumnCheck(int *mat[], int x, int y, int num);		// Search a number in a column (y) of the whole matrix
bool SubCheck(int *mat[], int x, int y, int num);		// Search a number in a submatrix (n) 3x3
bool FullCheck(int *mat[], int x, int y, int num);		// Search a number in a row and a column of the whole matrix
bool Search(int *mat[], int &a, int &b);			// Search an empty cell
void PRINT(int *mat[]);						// Print the whole matrix
void Copy(int *from[], int *to[]);				// Copy a matrix to another matrix
bool solve(int *mat[]);						// Solve the sudoku

void main() {
	std::ifstream f;
	f.open("sudoku.txt");
	int **mat = new int*[9];
	for (int i = 0; i < 9; i += 1)
		mat[i] = new int[9];
	for (int x = 0; x < 9; x += 1) 
		for (int y = 0; y < 9; y +=1)
			f >> mat[x][y];
	PRINT(mat);
	std::cout << solve(mat) << std::endl;
	PRINT(mat);

	delete[]mat;
	f.close();
	system("pause");
}

bool RowCheck(int *mat[], int x, int y, int num) {
	for (int i = 0; i < 9; i += 1) {
		if (mat[x][i] == num)
			return 1;
	}
	return 0;
}
bool ColumnCheck(int *mat[], int x, int y, int num) {
	for (int i = 0; i < 9; i += 1) {
		if (mat[i][y] == num)
			return 1;
	}
	return 0;
}
bool SubCheck(int *mat[], int x, int y, int num) {
	int n = 3 * (x / 3) + y / 3,
		a = 3 * (n / 3),
		b = 3 * (n - a);
	for (int k = a; k < a + 3; k += 1) {
		for (int l = b; l < b + 3; l += 1) {
			if (mat[k][l] == num)
				return 1;
		}
	}
	return 0;
}
bool FullCheck(int *mat[], int x, int y, int num) {
	return ColumnCheck(mat, x, y, num) || RowCheck(mat, x, y, num) || SubCheck(mat, x, y, num);
}
bool Search(int *mat[], int &a, int &b) {
	for (int x = 0; x < 9; x += 1) {
		for (int y = 0; y < 9; y += 1) {
			if (mat[x][y] == 0) {
				a = x;
				b = y;
				return 1;
			}
		}
	}
	return 0;
}
void PRINT(int *mat[]) {
	for (int x = 0; x < 9; x += 1) {
		for (int y = 0; y < 9; y += 1) {
			std::cout << mat[x][y];
			if ((y+1)%3 == 0 && y!=8)
				std::cout << '|';
				std::cout << ' ';
		}
		std::cout << std::endl;
		if ((x + 1) % 3 == 0 && x != 8) {
			for (int i = 0; i < 19; i += 1)
				std::cout << '-';
			std::cout << std::endl;
		}
	}

}
void Copy(int *from[], int *to[]) {
	for (int x = 0; x < 9; x += 1) {
		for (int y = 0; y < 9; y += 1) {
			to[x][y] = from[x][y];
		}
	}
}
bool solve(int *mat[]) {
	int x = 0, y = 0;
	bool check, ch = false;
	int **temp = new int*[9];
	for (int i = 0; i < 9; i += 1)
		temp[i] = new int[9];
	Copy(mat, temp);
	if (Search(mat, x, y)) {
		int n = 3 * (int(x / 3)) + int(y / 3);
		for (int i = 1; i < 10; i += 1) {
			if (!FullCheck(mat, x, y, i)) {
				ch = true;
				mat[x][y] = i;
			}
			if (ch) {
				check = solve(mat);
				if (check)
					return true;
				else {
					Copy(temp, mat);
					ch = false;
				}
			}
		}
		if (!ch) {
			return false;
			delete[] temp;
		}
	}
	else {
		return true;
		delete[] temp;
	}
}
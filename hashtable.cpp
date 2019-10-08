//#include "stdafx.h"
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <cctype>
//#include <Windows.h>
#include <stack>
#include <queue>


#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>
#include <stdbool.h>

#define SIZE 20
int hashCode(int key);



struct DataItem {
	/*int data;
	int key;*/

	char data;
	char key;
};

struct DataItem* hashArray[SIZE];
struct DataItem* hashArray2[SIZE];

struct DataItem* dummyItem;
struct DataItem* dummyItem2;

struct DataItem* item;


struct DataItem *del(struct DataItem* item) {
	int key = item->key;

	//get the hash 
	int hashIndex = hashCode(key);

	//move in array until an empty
	while (hashArray[hashIndex] != NULL) {

		if (hashArray[hashIndex]->key == key) {
			struct DataItem* temp = hashArray[hashIndex];

			//assign a dummy item at deleted position
			hashArray[hashIndex] = dummyItem;
			return temp;
		}

		//go to next cell
		++hashIndex;

		//wrap around the table
		hashIndex %= SIZE;
	}

	return NULL;
}


int hashCode(int key) {
	return key % SIZE;
}

struct DataItem *search(int key) {
	//get the hash 
	int hashIndex = hashCode(key);

	//move in array until an empty 
	while (hashArray[hashIndex] != NULL) {

		if (hashArray[hashIndex]->key == key)
			return hashArray[hashIndex];

		//go to next cell
		++hashIndex;

		//wrap around the table
		hashIndex %= SIZE;
	}

	return NULL;
}


//void insert(int key, int data) {
void insert2(char key, char data) {

	struct DataItem *item = (struct DataItem*) malloc(sizeof(struct DataItem));
	item->data = data;
	item->key = key;

	//get the hash
	int intParsed_char_key = int(key);
	int hashIndex = hashCode(intParsed_char_key);

	//move in array until an empty or deleted cell
	while (hashArray2[hashIndex] != NULL && hashArray2[hashIndex]->key != -1) {
		//go to next cell
		++hashIndex;

		//wrap around the table
		hashIndex %= SIZE;
	}

	hashArray2[hashIndex] = item;
}


//void insert(int key, int data) {
void insert(char key, char data) {

	struct DataItem *item = (struct DataItem*) malloc(sizeof(struct DataItem));
	item->data = data;
	item->key = key;

	//get the hash
	int intParsed_char_key = int(key);
	int hashIndex = hashCode(intParsed_char_key);

	//move in array until an empty or deleted cell
	while (hashArray[hashIndex] != NULL && hashArray[hashIndex]->key != -1) {
		//go to next cell
		++hashIndex;

		//wrap around the table
		hashIndex %= SIZE;
	}

	hashArray[hashIndex] = item;
}


void display() {
	int i = 0;

	for (i = 0; i < SIZE; i++) {

		if (hashArray[i] != NULL)
			printf(" (%d,%d)", hashArray[i]->key, hashArray[i]->data);
		else
			printf(" ~~ ");
	}

	printf("\n");
}


void display2() {
	int i = 0;

	for (i = 0; i < SIZE; i++) {

		if (hashArray2[i] != NULL)
			printf(" (%d,%d)", hashArray2[i]->key, hashArray2[i]->data);
		else
			printf(" ~~ ");
	}

	printf("\n");
}

int main() {
	dummyItem = (struct DataItem*) malloc(sizeof(struct DataItem));
	dummyItem->data = -1;
	dummyItem->key = -1;

	/*insert(1, 20);
	insert(2, 70);
	insert(42, 80);
	insert(4, 25);
	insert(12, 44);
	insert(14, 32);
	insert(17, 11);
	insert(13, 78);
	insert(37, 97);*/
	insert('a', 'a');
	insert('b', 'b');
	insert('c', 'c');
	insert('d', 'd');
	insert('3', '3');
	display();

	dummyItem2 = (struct DataItem*) malloc(sizeof(struct DataItem));
	dummyItem2->data = -1;
	dummyItem2->key = -1;

	insert2('a', 'a');
	insert2('b', 'b');
	insert2('c', 'c');
	insert2('d', 'd');
	insert2('3', '3');

	// BOTH ARE INSERTED IN THE SAME WAY IN THE TABLE.



	//insert(14, 32);
	//insert(17, 11);
	//insert(13, 78);
	//insert(37, 97);

	display2();
	item = search(37);

	if (item != NULL) {
		printf("Element found: %d\n", item->data);
	}
	else {
		printf("Element not found\n");
	}

	del(item);

	printf("delete operation for, (key: %d, value: %d)\n", item->key,item->data);
	item = search(37);

	if (item != NULL) {
		printf("Element found: %d\n", item->data);
	}
	else {
		printf("Element not found\n");
	}
}

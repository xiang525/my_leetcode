/*---------------------------------------------
Data structure: interval tree
note: the followings are what I can do for today. 
I implemented the interval tree's three functions:
buildTree(), addition() and deletion(). If you really want 
to use these APIs, some conversions from characters to ASCII
are needed. 
-----------------------------------------------*/
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 10

// declare interval tree node
struct IntervalTreeNode{
    int left,right,mid;    
    bool cover; // flag for coverage check
};


IntervalTreeNode intervalTree[3 * MAX];

// build interval tree 
void buildTree(int left,int right,int num){
    intervalTree[num].left = left;
    intervalTree[num].right = right;
    intervalTree[num].mid = (left + right) / 2;
    intervalTree[num].cover = false;
    if(left + 1 != right){
        buildTree(left,intervalTree[num].mid,2*num);
        buildTree(intervalTree[num].mid,right,2*num+1);
    }
}

// implement addition
void Addition(int left,int right,int num){    
    if(intervalTree[num].left == left && intervalTree[num].right == right){
        intervalTree[num].cover = 1;
        return;
    }
    if(right <= intervalTree[num].mid){
        Addition(left,right,2*num);
    }
    else if(left >= intervalTree[num].mid){
        Addition(left,right,2*num+1);
    }
    else{
        Addition(left,intervalTree[num].mid,2*num);
        Addition(intervalTree[num].mid,right,2*num+1);
    }
}
// implement deletion
bool Deletion(int left,int right,int num){    
    if(intervalTree[num].left + 1 == intervalTree[num].right){
        int cover = intervalTree[num].cover;
        intervalTree[num].cover = 0;
        return cover;
    }
    if(intervalTree[num].cover == 1){
        intervalTree[num].cover = 0;
        intervalTree[2*num].cover = 1;
        intervalTree[2*num+1].cover = 1;
    }
    // left nodes
    if(right <= intervalTree[num].mid){
        return Deletion(left,right, 2*num);
    }
    // right nodes
    else if(left >= intervalTree[num].mid){
        return Deletion(left,right,2*num+1);
    }
    // span left and right nodes
    else{
        return Deletion(left,intervalTree[num].mid,2*num) &&
        Deletion(intervalTree[num].mid,right,2*num+1);
    }
}



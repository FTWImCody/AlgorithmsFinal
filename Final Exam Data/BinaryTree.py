import csv
import re
import os

class Node: #class holding the process id and process length values and the tick method
    def __init__(self, val = 0, fn = None, ln = None, ph = 0, ss = 0, a = None, rank = 0, s = 0, l = None, r = None): #Constructor for Node class
        self.value = val
        self.fName = fn
        self.lName = ln
        self.phone = ph
        self.social = ss
        self.address = a
        self.rank = rank
        self.salary = s
        self.l_child = l
        self.r_child = r
    
    def __str__(self): #overriding the __str__ to print more useful information
        output=""
        output+="Employee ID: "+self.value+"\n"
        output+="Name: "+self.lName+", "+self.fName+"\n"
        output+="Phone#: "+re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', self.phone)+"\n"
        output+="Social: "+re.sub(r'(\d{3})(\d{2})(\d{4})', r'\1-\2-\3', self.social)+"\n"
        output+="Address: "+self.address+"\n"
        output+="Rank: "+self.rank+"\n"
        output+="Salary: "+"$"+self.salary+".00"
        return output

class BinaryTree:
    def __init__(self, r = None, s = 0): #constructor for BinaryTree class
        self.root = r
        self.size = s
    
    def put(self, value, fName, lName, phone, social, address, rank, salary): #method for checking if the root exists or not, if not it calls the _put method
        if self.root == None:
            self.root = Node(value, fName, lName, phone, social, address, rank, salary)
            self.size+=1
        elif self.root != False:
            self._put(self.root, value, fName, lName, phone, social, address, rank, salary)
    
    def _put(self, root, value, fName, lName, phone, social, address, rank, salary): #method for determining where to place the new node
        if value < root.value and root.l_child == None:
            root.l_child = Node(value, fName, lName, phone, social, address, rank, salary) #place node with value as root.l_child
            self.size+=1
        elif value < root.value and root.l_child != None:
            self._put(root.l_child, value, fName, lName, phone, social, address, rank, salary) #call _put() with l.child as root
        elif value > root.value and root.r_child == None:
            root.r_child = Node(value, fName, lName, phone, social, address, rank, salary) #place node with value as root.r_child
            self.size+=1
        elif value > root.value and root.r_child != None:
            self._put(root.r_child, value, fName, lName, phone, social, address, rank, salary) #call _put() with r.child as root
        else:
            print("Value already in tree!")
    
    def printTree(self, root): #prints off the basic tree to determine if it is inputting the nodes properly
        print(root)
        if root.l_child:
            print("Left")
            self.printTree(root.l_child)
        if root.r_child:
            print("Right")
            self.printTree(root.r_child)
    
    def searchTree(self, root, value): #searches the value the user input, if it is equal it will print off the employee info
        if value < int(root.value) and root.l_child == None:
            print("Employee ID not on Binary Tree!")
        elif value < int(root.value) and root.l_child != None:
            self.searchTree(root.l_child, value) #call _put() with l.child as root
        elif value > int(root.value) and root.r_child == None:
            print("Employee ID not on Binary Tree!")
        elif value > int(root.value) and root.r_child != None:
            self.searchTree(root.r_child, value) #call _put() with r.child as root
        else:
            print(root)
    
    def buildTree(self, filename):
        with open(filename+".csv", newline='') as csvfile: #opens csv file and inserts all the elements of the csv rows into a node element on the BinaryTree
            csvReader = csv.reader(csvfile)
            for row in csvReader:
                self.put(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
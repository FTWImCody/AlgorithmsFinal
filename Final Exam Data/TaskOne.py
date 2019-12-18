import BinaryTree
import os

def main():
        bt = BinaryTree.BinaryTree() #creating an empty Binary Tree

        bt.buildTree("EmployeeList") #building the Binary Tree
        file_dict = {} #empty dictionary for the employeeID DNA to go into


        for filename in os.listdir(os.getcwd()+'\\Task One'): #read in each ID#.txt and kid.txt with the ID# as the dictionary key for each dna strand
                with open(os.path.join(os.getcwd()+'\\Task One', filename)) as file_object:
                        filename = filename.split(".") #split to remove .txt from the dictionary key
                        row = file_object.read()
                        row = row.replace("GAATTC", "G/AATTC") #cut the DNA strings using the 3 methods in assignment
                        row = row.replace("GGATCC", "G/GATCC")
                        row = row.replace("AAGCTT", "A/AGCTT")
                        row = row.split("/") #split on the "/" after replacing
                        rowList = [len(i) for i in row] #list comprehension
                        file_dict[filename[0]] = rowList

        y = set(file_dict['kidDNA'])
        maxSize = 0
        for key in file_dict: #looping through the employeeIds in file_dict
                if key != 'kidDNA':
                        x = set(file_dict[key]) #set algebra to compare the employee to the kidw
                        z = x.intersection(y)
                        if len(z) > maxSize:
                                maxLength = key
                                maxSize = len(z)

        bt.searchTree(bt.root, int(maxLength)) #search tree for the EmployeeId that matched the most lengths
main()
input()
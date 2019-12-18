import os
import csv

class DNA: #stores all the DNA information for each hash
    def __init__(self, H, R, S, C):
        self.Hash = H
        self.Region = R
        self.Site = S
        self.Class = C

def FileWalk(path, file_Dict): #walks through all files/folders and analyzes the DNA in tripletts to determine the max amount of continuous CAGs there are
    for item in os.listdir(path): #item is the files in the current directory
        fullPath = os.path.join(path, item) #setting up a full path to check if it a folder or opening the file to scan it
        if os.path.isdir(fullPath): #if fullpath is a folder then it will open it in recursion
            FileWalk(fullPath, file_Dict)
        else:
            with open(fullPath) as file_object: #opens the file so we can analyze it
                file = file_object.read() #reads the file into a object
                filename = item.split(".") #splits filename so we can save the hash
                total = 0 #keeps track of the total continuous CAGs
                maxNum = 0 #stores the max number of continuous CAGs
                fileDir = fullPath.split("\\") #splits fullpath on \\ to determine the Region and Site names
                Region = fileDir[10] #index 10 is the Region Name
                Site = fileDir[11] #index 11 is the Site Name
                for i in range(0, len(file), 3): #keeps the triplett to determine how many continuous CAGs there are
                    dna = file[i] + file[i+1] + file[i+2]
                    if dna == 'CAG': #compares dna to "CAG"
                        total += 1 #if true then it ticks the total up
                    else: 
                        if total > maxNum:
                            maxNum = total
                            total = 0
                        else:
                            total = 0
                if maxNum <= 26: #assigns a classification determined by how many continuous CAGs there were
                    classification = "Normal"
                elif maxNum <= 35:
                    classification = "Intermediate"
                elif maxNum <= 39:
                    classification = "Reduced Penetrance"
                else:
                    classification = "Full Penetrance"
                file_Dict[filename[0]] = DNA(filename[0], Region, Site, classification) #adds a DNA class to the file_Dict dictionary
    return file_Dict
def main():
    file_Dict = {} #empty dicitonary to plug into the args for FileWalk
    file_Dict = FileWalk(os.getcwd()+"\\Set", file_Dict) 

    with open('hash_file.csv', mode='w', newline='') as employee_file: #open CSV
        employee_writer = csv.writer(employee_file, delimiter=',')

        for i in file_Dict: #loop through the list adding self.Hash, self.Region, self.Site, self.Class of any hash with class > 26 into a CSV
            if file_Dict[i].Class != "Normal":
                employee_writer.writerow([file_Dict[i].Hash, file_Dict[i].Region, file_Dict[i].Site, file_Dict[i].Class])

main()
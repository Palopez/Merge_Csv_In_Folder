import glob
#Modify
#place the route of the folder where are the csv files
directory = "C:\yourRoute\FolderContainingTheCsvFiles"
#Name of the merged csv files
name = "merged.csv"
#place the route of destiny to the merged csv
outputfile = "C:\yourRoute\FolderContainingTheCsvFiles/FolderOfMergedCsv/"+name

print("collecting files...")
#NO modify
#Takes all the .csv files of the var directory
to_merge = glob.glob(directory+"/*.csv")
to_merge.sort()
header_saved = False
inicial = 0;
with open(outputfile,'w', encoding = 'utf-8-sig') as mergedfile:
    for filename in to_merge:
        inicial = inicial + 1;
        n = inicial;
        print(str(n)+")"+filename)
        print("")
        with open(filename, encoding = 'utf-8-sig') as infiles:
            header = next(infiles)
            if not header_saved:
                mergedfile.write(header)
                header_saved = True
            for line in infiles:
                mergedfile.write(line)
print("file merged on route "+ directory + "/" + outputfile)

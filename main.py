import glob
import json

filenamesEn = glob.glob(".\\en\\*\\")
filenamesSr = glob.glob(".\\rs\\*\\")

with open("./en/en-meta.json", 'r') as file:
    metaEn = json.load(file)

with open("./rs/rs-meta.json", 'r') as file:
    metaRs = json.load(file)

allFilesEn = []
allFilesRs = []

for x in filenamesEn:
    print(x.split("\\")[-2]);
    allFilesEn.append(x.split("\\")[-2]);


for x in filenamesSr:
    print(x.split("\\")[-2]);
    allFilesRs.append(x.split("\\")[-2]);

metaEn["pages"] = allFilesEn;
metaRs["pages"] = allFilesRs;

with open("./en/en-meta.json", 'w') as file:
    json.dump(metaEn, file, indent=4)

with open("./rs/rs-meta.json", 'w') as file:
    json.dump(metaRs, file, indent=4)
import glob
import os
import json
import numpy as np

filenamesEn = glob.glob("./en/*/*.html", recursive=True)
filenamesRs = glob.glob("./rs/*/*.html", recursive=True)

with open("./en/en-meta.json", 'r+') as file:
    metaEn = json.load(file)

with open("./rs/rs-meta.json", 'r+') as file:
    metaRs = json.load(file)

allFilesEn = []
allFilesRs = []

delim = "/"
if os.name == 'nt':
    delim = "\\"

for x in filenamesEn:
    allFilesEn.append(x.split(delim)[-2]);

for x in filenamesRs:
    allFilesRs.append(x.split(delim)[-2]);

originalMetaEn = metaEn["pages"]
originalMetaRs = metaRs["pages"]
metaEn["pages"] = allFilesEn;
metaRs["pages"] = allFilesRs;

with open("./en/en-meta.json", 'w') as file:
    json.dump(metaEn, file, indent=4)

with open("./rs/rs-meta.json", 'w') as file:
    json.dump(metaRs, file, indent=4)

with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:

    rsDiff = np.setdiff1d(originalMetaRs, allFilesRs)
    enDiff = np.setdiff1d(originalMetaEn, allFilesEn)

    if len(originalMetaEn) < len(allFilesEn) and len(enDiff) != 0:
        fh.write("msg=Created page -" + enDiff[0] + "\n")
    elif len(originalMetaEn) > len(allFilesEn) and len(enDiff) != 0:
        fh.write("msg=Deleted page - " + enDiff[0] + "\n")
        
    elif len(originalMetaRs) < len(allFilesRs) and len(enDiff) != 0:
        fh.write("msg=Stvorena stranica - " + rsDiff[0] + "\n")
    elif len(originalMetaRs) > len(allFilesRs) and len(enDiff) != 0:
        fh.write("msg=Obrisana stranica - " + rsDiff[0] + "\n")
        
    else:
        fh.write("msg=Update of site meta-data")

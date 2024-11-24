import glob
import json
import numpy as np

def main():
    filenamesEn = glob.glob("./en/*/")
    filenamesSr = glob.glob("./rs/*/")

    with open("./en/en-meta.json", 'r+') as file:
        metaEn = json.load(file)

    with open("./rs/rs-meta.json", 'r+') as file:
        metaRs = json.load(file)

    allFilesEn = []
    allFilesRs = []

    for x in filenamesEn:
        allFilesEn.append(x.split("/")[-2]);

    for x in filenamesSr:
        allFilesRs.append(x.split("/")[-2]);

    originalMetaEn = metaEn["pages"]
    originalMetaRs = metaRs["pages"]
    metaEn["pages"] = allFilesEn;
    metaRs["pages"] = allFilesRs;

    with open("./en/en-meta.json", 'w') as file:
        json.dump(metaEn, file, indent=4)

    with open("./rs/rs-meta.json", 'w') as file:
        json.dump(metaRs, file, indent=4)

    if len(originalMetaEn) < len(allFilesEn):
        return "Created page: \"" + np.setdiff1d(originalMetaEn, allFilesEn)[0] + '"'
    else if len(originalMetaEn) > len(allFilesEn):
        return "Deleted page: \"" + np.setdiff1d(originalMetaEn, allFilesEn)[0] + '"'
        
    else if len(originalMetaRs) < len(allFilesRs):
        return "Stvorena stranica: \"" + np.setdiff1d(originalMetaRs, allFilesRs)[0] + '"'
    else if len(originalMetaRs) > len(allFilesRs):
        return "Obrisana stranica: \"" + np.setdiff1d(originalMetaRs, allFilesRs)[0] + '"'

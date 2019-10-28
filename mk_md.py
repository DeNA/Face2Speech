import sys
import os
import re

fnames_list_path = sys.argv[1]
fp = open(fnames_list_path, 'r')
fnames_list = fp.readlines()
fp.close()

# header
print("# Audio samples")
print("")
print("* Face images were provided to subjects in evaluation.")
print("* However, we can't provide the face images and original audio on this page because of copyrights.")
print("* You can confirm the face images by clicking on the speaker name linking to wikipedia.")
print("")
print("| Id in VGGFace2 | Speaker name | Gender |  SYNTH-FACE (Proposed) | SYNTH-SPEECH (baseline)  |")
print("|---|---|---|---|---|")
for fname in fnames_list:
    voxcelebid, vggid, spkname, gender, link = fname.rstrip().split()
    vggid = vggid.rstrip()
    spkname = spkname.rstrip()
    gender = gender.rstrip()
    link = link.rstrip()
    spkname = re.sub("_", " ", spkname)
    spkname = re.sub("\"", " ", spkname)

    print("| {} | [{}]({}) | {} | <audio controls=\"controls\" > <source src=\"wav/SYNTH-FACE/{}.wav\" autoplay/> Your browser does not support the audio element. </audio> | <audio controls=\"controls\" > <source src=\"wav/SYNTH-SPEECH/{}.wav\" autoplay/> Your browser does not support the audio element. </audio> |".format(vggid, spkname, link, gender, voxcelebid, voxcelebid))

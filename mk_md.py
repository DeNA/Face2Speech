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
print("* We can't provide face images on this page because of copyrights.")
print("* However, the face images were provided to subjects in evaluation.")

print("| Id in VGGFace2 | Speaker name | Gender  |  SYNTH-FACE | SYNTHE-SPEECH  |")
print("|---|---|---|---|---|")
for fname in fnames_list:
    vggid, voxcelbif, spkname, gender = fname.rstrip().split()
    vggid = vggid.rstrip()
    spkname = spkname.rstrip()
    gender = gender.rstrip()
    spkname = re.sub("_", " ", spkname)
    spkname = re.sub("\"", " ", spkname)

    print("| {} | {}  | {} | <audio controls=\"controls\" > <source src=\"wav/SYNTH-FACE/{}.wav\" autoplay/> Your browser does not support the audio element. </audio> | <audio controls=\"controls\" > <source src=\"wav/SYNTH-SPEECH/{}.wav\" autoplay/> Your browser does not support the audio element. </audio> |".format(vggid, spkname, gender, vggid, vggid))

'''
for fname in fnames_list:
    vggid, voxcelbif, spkname, gender = fname.rstrip().split()
    vggid = vggid.rstrip()
    spkname = spkname.rstrip()
    gender = gender.rstrip()
    spkname = re.sub("_", " ", spkname)
    spkname = re.sub("\"", " ", spkname)

    print("| ")
    print(" {} |".format(vggid))
    print(" {} |".format(spkname))
    print(" {} |".format(gender))
    print("<audio controls=\"controls\" >")
    print("<source src=\"wav/SYNTH-FACE/{}.wav\" autoplay/>".format(vggid))
    print("Your browser does not support the audio element.")
    print("</audio>")
    print(" | ")

    print("<audio controls=\"controls\" >")
    print("<source src=\"wav/SYNTH-SPEECH/{}.wav\" autoplay/>".format(vggid))
    print("Your browser does not support the audio element.")
    print("</audio>")
    print(" |")

print("")
'''


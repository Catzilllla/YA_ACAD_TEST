import json

# read json
with open("data_54ea06a7cf.json", encoding="UTF-8") as file_in:
    rec_json = json.load(file_in)

# change element
# ensure_ascii - change ascii to symb if True
# sort_keys - sort elements
rec_json[1]["group_number"] = 2
with open ("data_54ea06a7cf.json", "w", encoding="UTF-8") as file_out:
    json.dump(rec_json, file_out, ensure_ascii=False, indent=2, sort_keys=True)

# read json for output into the string
with open("data_54ea06a7cf.json", encoding="UTF-8") as file2_in:
    out_json = json.load(file2_in)
print(out_json)
file_in.close
file_out.close
file2_in.close

print("\n\n ========================== \n\n")


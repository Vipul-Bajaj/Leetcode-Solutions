import os, urllib.parse
files_to_ignored = ["README.md"]
root_folder = "."
root_readme = open(os.path.join(root_folder,"README.md"),"w+")
root_readme.write("# Index\n")
company_idx = 1
for company_folder in sorted(os.listdir(root_folder)):
    if os.path.isdir(os.path.join(root_folder, company_folder)):
        comapany_level = os.path.join(root_folder, company_folder)
        company_readme = open(os.path.join(comapany_level,"README.md"),"w+")
        company_readme.write("# Index\n")
        difficulty_idx = 1
        for difficulty_folder in os.listdir(comapany_level):
            if os.path.isdir(os.path.join(company_folder,difficulty_folder)):
                difficulty_level = os.path.join(company_folder,difficulty_folder)
                difficulty_readme = open(os.path.join(difficulty_level,"README.md"),"w+")
                difficulty_readme.write("# Index\n")
                file_idx = 1
                for files in sorted(os.listdir(difficulty_level)):
                    if files not in files_to_ignored:
                        file_name,file_extension = os.path.splitext(files)
                        difficulty_readme.write(str(file_idx) + ". [" + file_name + "](" + urllib.parse.quote(os.path.join('.',files)) + ")\n")
                        file_idx +=1
                company_readme.write(str(difficulty_idx) + ". [" + difficulty_folder + "](" + urllib.parse.quote(os.path.join('.',difficulty_folder)) + ")\n")
                difficulty_idx+=1
        root_readme.write(str(company_idx) + ". [" + company_folder + "](" + urllib.parse.quote(os.path.join(root_folder, company_folder)) + ")\n")
        company_idx+=1
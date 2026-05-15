import os

#Get list of all visible files in task2_data folder
files = [f for f in os.listdir('./task2_data') if not f.startswith('.')]

#Check how many files are in the folder
if len(files) >= 5:

    count = 1

    for f in files:

        #Only rename image files (.jpg, .png, .jpeg)
        if f.endswith(('.jpg', '.jpeg', '.png')):

            #Separate file name from extension, so only pathname is changed and extension is preserved
            name, ext = os.path.splitext(f)

            #Create a naming template for all files to follow
            new_name = f"Hawaii_Trip_{count:02}{ext}"

            #Rename file
            os.rename(
                f"./task2_data/{f}",
                f"./task2_data/{new_name}"
            )

            #Increase counter so each file is given a different number
            count +=1

#If there are not enough files in the folder, give an error
else:
    print("Not enough files in task2_data to run script. Add at least 5 files and try again.")
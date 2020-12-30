
import os
import shutil

def main():
	

		for count, filename in enumerate(os.listdir(dir)):
			src = dir + filename
			date_str = filename
			date_path = date_str[0:10]
			date_path_dir = dir + date_path;
			

			if not os.path.exists(dir + date_path):
				os.makedirs(dir + date_path)


			if os.path.exists(dir + date_path):
				if date_path in filename:
					shutil.move(os.path.join(src), date_path_dir)

		print("Organized " + str(count) + " items" )
			

if __name__ == '__main__':
		print("")
		print("")
		print("================================================================================================================================")
		print("Welcome to My Photo / Video Organizer, This tool will take all filenames in a directory and create folders to go with each file.")
		print("")
		print("")
		print("")
		print("Best case scenario filename with naming structure of : YEAR-DD-MM or anything with similar idea")
		print("If you wish to change length of 'Folder Name/Naming Structure Length please find date_path = date_str[0:10]")
		print("")
		print("")
		print("Thanks for using my first python tool!")
		print("================================================================================================================================")
		print("")
		print("")
		dir = input("Directory to Organize - Please use / backslash when typing in directory - Example: C:/User/Username/Photos/ :")
		main()

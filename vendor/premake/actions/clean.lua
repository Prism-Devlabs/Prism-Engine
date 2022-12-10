newaction{
	trigger = "clean",
	description = "Cleans up the project",
	execute = function()
		print("Removing bin and bin-int directories")
		os.rmdir("./bin")
		os.rmdir("./bin-int")
		print("Removing MakeFiles")
		os.remove("**Makefile")
		print("Removing Visual Studio Files")
		os.remove("**.vcxproj")
		os.remove("**.vcxproj.**")
		os.remove("**.sln")
		print("Done")
	end
}

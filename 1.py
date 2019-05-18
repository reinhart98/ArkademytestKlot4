import json


hobby = ["Video Editing","Watching Tv"] #array in python

biodata = {
	"name" : "Reinhart",
	"address" : "Gowa",
	"hobbies" : hobby,
	"is_Married" : False,
	"school" : {"HighSchool":"SMAN 2 Parepare", "University":"UNHAS"},
	"SKILLS" : [{"Name" : "English"},{"Score":523}]
}

cvtJson = json.dumps(biodata)

print(cvtJson)
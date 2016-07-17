from DBConnection import DBConnection
from Fragment import Fragment
import zipfile, os, csv
import datetime
import modex


db = DBConnection()

#---Fragment--------------------------------------------------------------
class Project(object):

	
	# Statics---------------------------------------------------------------------------------

	@staticmethod
	def saveFragmentsDb():
		for file in os.listdir('fragments/'):
			f = open('fragments/' + file)
			newfile = db.projectfiles.ProjectFiles()
			newfile['referenceId'] = file
			newfile.save()
			newfile.fs.file.put(f)

		return #for file in os.listdir('fragments/'):

	@staticmethod
	def getFragmentsList():
		for file in db.projectfiles.find():
			print file
		return

	@staticmethod
	def getFragments():
		for file in db.projectfiles.ProjectFiles.fs.find():
			print file

		for f in db.projectfiles.ProjectFiles.find({'referenceId' : 'Codes_Cluster_1.zip'}):
			ff =  f.fs.file.get_last_version()
			print ff.read()

		return

	# Objects---------------------------------------------------------------------------------
	def __init__(self, filename, admin):

		# initialize class variables to default state
		self.id = 0
		self.name = filename
		self.fileSize = os.path.getsize('upload/' + filename)
		self.admin = admin
		self.startDate = datetime.datetime.now()
		self.endDate = datetime.datetime.now()
		self.volunteers = []
		self.fragments = []
		self.state = 'started'
		self.files = 'upload/' + filename

		#initialize project id
		number = 0
		for project in db.projects.find():
			number = number + 1

		self.id = number + 1

		# Create project fragments using Fragments class
		Fragment.fragments(filename)
		
		# Create Fragment class instances and save in Project class fragments list variable
		#for index, file in enumerate(os.listdir('fragments/')):
		#	if file[-3:] == 'zip':
		#		fragment = Fragment()
		#		fragment.id = index
		#		fragment.size = os.path.getsize('fragments/' + file)
		#		self.fragments.append(fragment)

		#create fragments list to store in project class
		for index, file in enumerate(os.listdir('fragments/')):
			if file[-3:] == 'zip':
				fragment = dict()
				fragment['id'] = index
				fragment['size'] = os.path.getsize('fragments/' + file)
				fragment['time'] =datetime.datetime.now()
				self.fragments.append(fragment)
				#fragment.append(index)
				#fragment.append(os.path.getsize('fragments/' + file))
				#fragment.append(datetime.datetime.now())
				#fragment.append()

		#Save the project and files in the mongodb
		project = db.projects()
		project['id'] = self.id
		project['name'] = self.name
		project['fileSize'] = self.fileSize
		project['admin'] = self.admin
		project['startDate'] = self.startDate
		project['endDate'] = self.endDate 
		project['volunteers'] = self.volunteers
		project['fragments'] = self.fragments
		#for fragment in 
		project['state'] = self.state
		project.save()
		#self.project = project

		# get _id of the saved project
		for project in db.projects.find({ 'id' : self.id }):
			docid = str(project['_id'])

		#Save project files in mongodb in Project Document
		file = open('upload/' + filename)
		project.fs.put(file)
		#project.files = self.files = 'upload/' + filename

		#Save fragments in mongodb
		for file in os.listdir('fragments/'):
			fragment = db.files()
			fragment['projectid'] = self.id
			fragment['name'] = file
			fragment['docid'] = docid
			fragment['type'] = 'fragment'
			fragment.save()
			open_file = open('fragments/' + file, 'rb')
			fragment.fs.file.put(open_file)

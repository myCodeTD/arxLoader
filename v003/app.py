#Import python modules
import sys, os, re, shutil, urllib, subprocess, time

# from PyQt4 import QtCore
# from PyQt4 import QtGui
# import sip
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *

#Import GUI
from PySide import QtCore
from PySide import QtGui

from shiboken import wrapInstance


# import ui
from arxLoader import ui as ui
reload(ui)

from arxLoader import mayaHook as hook
reload(hook)

from utils import config, fileUtils
reload(config)
reload(fileUtils)

from sgUtils import sgUtils
reload(sgUtils)

moduleDir = sys.modules[__name__].__file__


# If inside Maya open Maya GUI
def getMayaWindow():
	ptr = mui.MQtUtil.mainWindow()
	return wrapInstance(long(ptr), QtGui.QWidget)
	# return sip.wrapinstance(long(ptr), QObject)

import maya.OpenMayaUI as mui
getMayaWindow()


class MyForm(QtGui.QMainWindow):

	def __init__(self, parent=None):
		self.count = 0
		#Setup Window
		super(MyForm, self).__init__(parent)
		# QtGui.QWidget.__init__(self, parent)
		self.ui = ui.Ui_loaderWindow()
		self.ui.setupUi(self)


		# custom variable
		self.configPath = '%s/config.txt' % os.path.split(moduleDir)[0]
		self.configData = config.readSetting(self.configPath)
		self.moduleDir = moduleDir
		self.iconPath = '%s/%s' % (os.path.split(self.moduleDir)[0], 'icons')
		self.root = eval(self.configData['root'])['windowRoot']
		self.rootProject = '%s/%s' % (self.root, self.configData['rootProject'])
		self.assetRoot = '%s/%s' % (self.root, self.configData['assetRoot'])
		self.fileExt = eval(self.configData['ext'])['maya']
		self.noPreviewIcon = '%s/%s' % (self.iconPath, 'noPreview.png')
		self.thumbnail = self.configData['thumbnail']
		self.itemColor = [0, 0, 0]
		self.textItemColor = [[200, 200, 200], [120, 120, 120], [100, 100, 100]]
		self.sceneInfo = None
		self.shotAssets = None

		# init connections
		self.initConnections()

		# init functions
		self.initFunctions()



	def initConnections(self) : 
		self.ui.shotgun_radioButton.toggled.connect(self.setWindowMode)
		self.ui.createReference_pushButton.clicked.connect(self.doCreateReference)
		self.ui.search_lineEdit.textChanged.connect(self.listAllAsset)
		self.ui.type_checkBox.stateChanged.connect(self.setFilterSignal1)
		self.ui.parent_checkBox.stateChanged.connect(self.setFilterSignal2)
		self.ui.variation_checkBox.stateChanged.connect(self.setFilterSignal3)
		self.ui.showSceneAsset_checkBox.stateChanged.connect(self.refreshUI)
		self.ui.main_listWidget.customContextMenuRequested.connect(self.showMenu)
		self.ui.thumbnail_checkBox.stateChanged.connect(self.refreshUI)
		self.ui.selectedReference_checkBox.stateChanged.connect(self.setReferenceButton)


	def initFunctions(self) : 
		# set the correct layout window
		self.loadData()
		self.setWindowMode()
		


	# window area =========================================================================

	def setWindowMode(self) : 
		# check what mode is checked 
		if self.ui.shotgun_radioButton.isChecked() : 
			value = False
			w = 550
			h = 640
			lPos = 320
			text = 'Shotgun Asset List'
			value2 = True
			mode = 'shotgun'
			buttonText = 'Create All Reference'
			value3 = False


		if self.ui.manualBrowser_radioButton.isChecked() : 
			value = True
			# w = 850
			# h = 640
			# lPos = 620
			w = 550
			h = 640
			lPos = 320
			text = 'All Asset List'
			value2 = False
			mode = 'browser'
			buttonText = 'Create Reference'
			value3 = False
		
		# show / hide
		self.ui.add_pushButton.setVisible(value3)
		self.ui.remove_pushButton.setVisible(value3)
		self.ui.clear_pushButton.setVisible(value3)
		self.ui.search_frame.setVisible(value)
		self.ui.filter_frame.setVisible(value)
		self.ui.list_frame.setVisible(value3)
		self.ui.main_label.setText(text)
		self.ui.projectInfo_frame.setVisible(value2)
		self.ui.selectedReference_checkBox.setVisible(value2)
		self.ui.showSceneAsset_checkBox.setVisible(value)

		# resizing window
		self.ui.frame.resize(w, h)
		self.resize(w + 14, h + 14)
		self.ui.logo_label.setGeometry(lPos, 10, 221, 61)
		self.setLogo()

		# button text
		self.ui.createReference_pushButton.setText(buttonText)

		# set all UI
		self.ui.information_label.setText('Processing ...')
		QtGui.QApplication.processEvents()
		self.setUI(mode)


	def setLogo(self) : 
		# set company logo
		logo = self.configData['logo']
		iconPath = '%s/%s' % (self.iconPath, logo)
		self.ui.logo_label.setPixmap(QtGui.QPixmap(iconPath).scaled(200, 40, QtCore.Qt.KeepAspectRatio))



	def refreshUI(self) : 
		# check what mode is checked 
		if self.ui.shotgun_radioButton.isChecked() : 
			mode = 'shotgun'


		if self.ui.manualBrowser_radioButton.isChecked() : 
			mode = 'browser'

		# set all UI
		self.ui.information_label.setText('Processing ...')
		QtGui.QApplication.processEvents()
		self.setUI(mode)



	def setReferenceButton(self) : 

		if self.ui.selectedReference_checkBox.isChecked() : 
			self.ui.createReference_pushButton.setText('Create Selected Reference')

		else : 
			self.ui.createReference_pushButton.setText('Create All References')


	# load data ==================================================================================================


	def loadData(self) : 
		# load scene name
		sceneName = hook.getSceneName()

		if sceneName : 
			self.sceneInfo = self.getSceneInfo(sceneName)

			# load shotgun shot
			self.shotAssets = self.loadShotgunAsset()

		# load all shotgun asset
		self.allSgAssets = self.loadAllShotgunAsset()

		# asset info
		if self.allSgAssets : 
			self.assetInfo = self.getAssetInfo(self.allSgAssets)



	def getSceneInfo(self, sceneName) : 
		# layout ex.
		# U:/projects/ttv/episodes/e100/work/sq010/layout/maya/ttv_e100_010_layout.v002.ma
		eles = sceneName.replace('%s/' % self.rootProject, '').split('/')

		if len(eles) > 6 : 
			episode = eles[0]
			level = eles[1]
			sequence = eles[2]
			fileName = eles[-1]
			shot = ''
			project = 'ttv_%s' % episode

			if 'layout' in eles : 
				step = eles[3]

			if 'anim' in eles : 
				shot = eles[3]
				step = eles[4]


			info = {'project': project, 'episode': episode, 'step': step, 'sequence': sequence, 'shot': shot}

			return info


	def loadShotgunAsset(self) : 
		sceneName = hook.getSceneName()
		sceneInfo = self.getSceneInfo(sceneName)

		if sceneInfo : 
			step = sceneInfo['step']
			projName = sceneInfo['project']
			episode = sceneInfo['episode']
			sequenceName = sceneInfo['sequence']
			shotName = sceneInfo['shot']

			if step == 'layout' : 
				shotCode = '%s_%s_layout' % (episode, sequenceName.replace('sq', ''))

			if step == 'anim' : 
				shotCode = '%s_%s_%s' % (episode, sequenceName.replace('sq', ''), shotName.replace('sh', ''))

			shots = sgUtils.sgGetShot(projName, sequenceName)

			if shots : 
				for eachShot in shots : 
					if shotCode == eachShot['code'] : 
						assets = eachShot['assets']

						return assets


	def loadAllShotgunAsset(self) : 
		# using asset from this project
		# sceneName = hook.getSceneName()
		# sceneInfo = self.getSceneInfo(sceneName)
		# projName = sceneInfo['project']

		# using ttv_assets as a master asset project
		projName = self.configData['assetProject']

		assets = sgUtils.sgGetAllAssets(projName, fields=['code', 'id', 'sg_origin_id', 'sg_asset_type', 'sg_parent', 'sg_folder', 'sg_status_list', 'image'])

		return assets



	def downloadThumbnail(self) : 
		if self.thumbnail == 'auto' : 
			print 'Checking Thumbnail ...'
			countImage = 0
			
			for each in self.assetInfo : 
				image = self.assetInfo[each]['image']
				thumbnailFile = self.assetInfo[each]['thumbnailFile']
				thumbnailPath = os.path.dirname(thumbnailFile)
				code = self.assetInfo[each]['code']

				if image : 
					if not os.path.exists(thumbnailFile) : 
						if not os.path.exists(thumbnailPath) : 
							os.makedirs(thumbnailPath)

						print 'Downloading %s ...' % code
						self.ui.information_label.setText('Downloading %s...' % code)
						QtGui.QApplication.processEvents()

						urllib.urlretrieve(image, thumbnailFile)


			print 'Done'





	def getAssetInfo(self, sgAssets) : 
		assetInfo = dict()

		for each in sgAssets : 
			id = each['id']
			originID = each['sg_origin_id']
			code = each['code']
			assetType = each['sg_asset_type']
			parent = each['sg_parent']
			variation = each['sg_folder']
			pullFile = None
			publishFile = str()
			publishPxyFile = str()
			fileType = 'No File'
			image = each['image']

			if assetType and parent and variation : 
				approvedPath = os.path.join(self.assetRoot, 'approved', assetType, parent, variation, 'rig', 'maya').replace('\\', '/')
				publishPath = os.path.join(self.assetRoot, 'publish', assetType, parent, variation, 'rig', 'maya').replace('\\', '/')
				thumbnailPath = os.path.join(self.assetRoot, 'publish', assetType, parent, variation, '_shotgun').replace('\\', '/')
				thumbnailFile = '%s/%s' % (thumbnailPath, '%s.jpg' % code)

				# pxy file ======================================================
				aprvPxyFile = '%s/ttv_%s_%s_%s_rig_mr.%s' % (approvedPath, assetType, parent, variation, self.fileExt)
				masterPxyFile = '%s/ttv_%s_%s_%s_rig_mr.MASTER.%s' % (publishPath, assetType, parent, variation, self.fileExt)

				maxPublishPxyFile = self.findMaxVersion(publishPath, 'ttv_%s_%s_%s_rig_pxy' % (assetType, parent, variation), self.fileExt)

				if maxPublishPxyFile : 
					publishPxyFile = '%s/%s' % (publishPath, maxPublishPxyFile)

				# mr file ========================================================
				aprvFile = '%s/ttv_%s_%s_%s_rig_mr.%s' % (approvedPath, assetType, parent, variation, self.fileExt)
				masterFile = '%s/ttv_%s_%s_%s_rig_mr.MASTER.%s' % (publishPath, assetType, parent, variation, self.fileExt)

				maxPublishFile = self.findMaxVersion(publishPath, 'ttv_%s_%s_%s_rig_mr' % (assetType, parent, variation), self.fileExt)

				if maxPublishFile : 
					publishFile = '%s/%s' % (publishPath, maxPublishFile)

				# ================================================================

				# check apprv -> master -> publishVersion 
				if os.path.exists(aprvPxyFile) : 
					pullFile = aprvPxyFile
					fileType = 'approved'

				elif os.path.exists(masterPxyFile) : 
					pullFile = masterPxyFile
					fileType = 'master'

				elif os.path.exists(publishPxyFile) : 
					pullFile = publishPxyFile
					fileType = 'publish'

				elif os.path.exists(aprvFile) : 
					pullFile = aprvFile
					fileType = 'approved'

				elif os.path.exists(masterFile) : 
					pullFile = masterFile
					fileType = 'master'

				elif os.path.exists(publishFile) : 
					pullFile = publishFile
					fileType = 'publish'

				else : 
					print '%s has no assosiated file' % code

			else : 
				print 'Missing field %s %s %s' % (assetType, parent, variation)


			assetInfo[code] = {'id': id, 'code': code, 'assetType': assetType, 'parent': parent, 'variation': variation, 'pullFile': pullFile, 'fileType': fileType, 'aprvFile': aprvFile, 'masterFile': masterFile, 'publishPath': publishPath, 'aprvPxyFile': aprvPxyFile, 'masterPxyFile': masterPxyFile, 'thumbnailFile': thumbnailFile, 'image': image}

		return assetInfo


			# U:\projects\ttv\assets\approved\charmain\angela\base\rig\maya\ttv_charmain_angela_base_rig_mr.v004.ma
			# "U:\projects\ttv\assets\publish\charmain\angela\base\rig\maya\ttv_charmain_angela_base_rig_mr.MASTER.ma"


	# set UI =======================================================================================================


	def setUI(self, mode) : 

		if mode == 'shotgun' : 

			if self.sceneInfo : 
				self.setSceneInfo(self.sceneInfo)

			if self.shotAssets : 
				self.downloadThumbnail()
				self.listShotAsset(self.shotAssets)

			else : 
				self.ui.main_listWidget.clear()
				self.ui.information_label.setText('No Shotgun data')

		if mode == 'browser' : 

			if self.assetInfo : 
				self.downloadThumbnail()
				self.setFilter()				
				self.listAllAsset()



	def setSceneInfo(self, sceneInfo) : 
		# set UI shot Info
		self.ui.step_label.setText(sceneInfo['step'])
		self.ui.episode_label.setText(sceneInfo['episode'])
		self.ui.sequence_label.setText(sceneInfo['sequence'])
		self.ui.shot_label.setText(sceneInfo['shot'])


	def listShotAsset(self, assets) : 

		self.ui.main_listWidget.clear()
		aprvCount = 0
		masterCount = 0
		publishCount = 0
		missingCount = 0
		i = 0
		info = []
		addIcon = 0
		textColors = self.textItemColor

		scenePathInfo = self.getSceneAssets()


		if self.ui.thumbnail_checkBox.isChecked() : 
			addIcon = 1


		for each in assets : 
			
			if each['name'] in self.assetInfo.keys() : 
				pullFile = self.assetInfo[each['name']]['pullFile']
				fileType = self.assetInfo[each['name']]['fileType']
				# display = '%s - %s' % (self.assetInfo[each['name']]['code'], fileType)
				display = '%s' % (self.assetInfo[each['name']]['code'])
				color = [100, 0, 0]
				thumbnailFile = self.assetInfo[each['name']]['thumbnailFile']
				iconPath = self.noPreviewIcon

				numberDisplay = 'In scene x 0'
				number = 0

				if pullFile in scenePathInfo.keys() : 
					number = scenePathInfo[pullFile]['number']
					
				if number : 
					numberDisplay = 'In scene x %s' % number

				textColors[2] = [200, 100, 100]

				if number > 0 : 
					textColors[2] = [100, 200, 0]

				if number == 0 : 
					textColors[2] = [200, 200, 0]

				if os.path.exists(thumbnailFile) : 
					iconPath = thumbnailFile

				if fileType == 'approved' : 
					color = [0, 0, 0]
					aprvCount+=1

				if fileType == 'master' : 
					color = [0, 0, 0]
					masterCount+=1

				if fileType == 'publish' : 
					color = [0, 0, 0]
					publishCount+=1

				if fileType == 'No File' : 
					print each['name']
					print 'Approved file missing %s' % self.assetInfo[each['name']]['aprvFile']
					print 'Master file missing %s' % self.assetInfo[each['name']]['masterFile']
					print '------------------------' 
					missingCount+=1

				self.addListWidgetItem(display, fileType, numberDisplay, iconPath, color, textColors, addIcon, size = 90)

			i+=1


		info.append('	%s 	approved asset' % aprvCount)
		info.append('	%s 	master asset' % masterCount)
		info.append('	%s 	publish asset' % publishCount)
		info.append('	-----------------------------------')
		info.append('	%s/%s available (%s Missing)' % ((aprvCount + masterCount + publishCount), i, missingCount))
		info.append('')
		displayInfo = ('\n\r').join(info)

		print '%s asset missing' % missingCount

		self.ui.information_label.setText(displayInfo)



	def setFilterSignal1(self) : 

		if self.ui.type_checkBox.isChecked() : 
			self.ui.type_comboBox.currentIndexChanged.connect(self.listAllAsset)

		else : 
			self.ui.type_comboBox.currentIndexChanged.disconnect(self.listAllAsset)

		self.refreshUI()

	def setFilterSignal2(self) : 

		if self.ui.parent_checkBox.isChecked() : 
			self.ui.parent_comboBox.currentIndexChanged.connect(self.listAllAsset)

		else : 
			self.ui.parent_comboBox.currentIndexChanged.disconnect(self.listAllAsset)

		self.refreshUI()


	def setFilterSignal3(self) : 

		if self.ui.variation_checkBox.isChecked() : 
			self.ui.variation_comboBox.currentIndexChanged.connect(self.listAllAsset)

		else : 
			self.ui.variation_comboBox.currentIndexChanged.disconnect(self.listAllAsset)

		self.refreshUI()


	def setFilter(self) : 

		assetTypes = []
		parents = []
		variations = []

		for each in self.assetInfo : 
			assetType = self.assetInfo[each]['assetType']
			parent = self.assetInfo[each]['parent']
			variation = self.assetInfo[each]['variation']

			if not assetType in assetTypes : 
				assetTypes.append(assetType)

			if not parent in parents : 
				parents.append(parent)

			if not variation in variations : 
				variations.append(variation)

		self.ui.type_comboBox.clear()

		for each in assetTypes : 
			self.ui.type_comboBox.addItem(each)

		self.ui.parent_comboBox.clear()

		for each in parents : 
			self.ui.parent_comboBox.addItem(each)

		self.ui.variation_comboBox.clear()

		for each in variations : 
			self.ui.variation_comboBox.addItem(each)



	def listAllAsset(self) : 
		assetInfo = self.assetInfo
		info = []
		self.ui.information_label.setText('Working ...')

		# keyword in search field
		kw = str(self.ui.search_lineEdit.text())
		assetTypeKw = str(self.ui.type_comboBox.currentText())
		parentKw = str(self.ui.parent_comboBox.currentText())
		variationKw = str(self.ui.variation_comboBox.currentText())

		# get in scene reference
		scenePathInfo = self.getSceneAssets()

		self.ui.main_listWidget.clear()
		color = [100, 0, 0]
		assetCount = 0
		aprvCount = 0
		masterCount = 0
		publishCount = 0
		missingCount = 0
		addIcon = 0

		textColors = self.textItemColor


		if self.ui.thumbnail_checkBox.isChecked() : 
			addIcon = 1

		for each in sorted(assetInfo.keys()) : 
			fileType = assetInfo[each]['fileType']
			pullFile = assetInfo[each]['pullFile']
			assetType = assetInfo[each]['assetType']
			parent = assetInfo[each]['parent']
			variation = assetInfo[each]['variation']
			thumbnailFile = assetInfo[each]['thumbnailFile']
			iconPath = self.noPreviewIcon
			numberDisplay = 'In scene x 0'
			number = 0
			assetNo = 100

			if pullFile in scenePathInfo.keys() : 
				number = scenePathInfo[pullFile]['number']

			if number : 
				numberDisplay = 'In scene x %s' % number

			if os.path.exists(thumbnailFile) : 
				iconPath = thumbnailFile

			if not self.ui.type_checkBox.isChecked() : 
				assetTypeKw = assetType

			if not self.ui.parent_checkBox.isChecked() : 
				parentKw = parent

			if not self.ui.variation_checkBox.isChecked() : 
				variationKw = variation

			if self.ui.showSceneAsset_checkBox.isChecked() : 
				assetNo = number


			if kw in each : 			
				if assetTypeKw == assetType :  
					if parentKw == parent : 
						if variationKw == variation : 
							if assetNo > 0 : 
								if fileType == 'approved' : 
									color = [0, 0, 0]
									aprvCount+=1

								if fileType == 'master' : 
									color = [0, 0, 0]
									masterCount+=1

								if fileType == 'publish' : 
									color = [0, 0, 0]
									publishCount+=1

								if fileType == 'No File' : 
									color = [100, 0, 0]
									missingCount+=1
								

								textColors[2] = [200, 100, 100]

								if number > 0 : 
									textColors[2] = [100, 200, 0]

								if number == 0 : 
									textColors[2] = [200, 200, 0]

								self.addListWidgetItem(each, fileType, numberDisplay, iconPath, color, textColors, addIcon, 90)
								assetCount+=1

		info.append('	%s	assets' % assetCount)
		info.append('	---------------------------------')
		info.append('	%s 	approved asset' % aprvCount)
		info.append('	%s	master asset' % masterCount)
		info.append('	%s	publish asset' % publishCount)
		info.append('	%s	missing asset' % missingCount)
		display = ('\n\r').join(info)

		self.ui.information_label.setText(display)


	def showMenu(self,pos):
		menu1, state = self.getMenu1()
		if self.ui.main_listWidget.currentItem() : 
			menu=QtGui.QMenu(self)
			menu.addAction(menu1)
			menu.setEnabled(state)
			
			menu.popup(self.ui.main_listWidget.mapToGlobal(pos))
			result = menu.exec_(self.ui.main_listWidget.mapToGlobal(pos))

			if result : 
				self.menuCommand(result.text(), 'main_listWidget')

	# open in explorer command
	def getMenu1(self) : 
		text = self.getSelectedWidgetItem(1)
		item = text[-1]
		menu = None

		heroFile = self.assetInfo[item]['pullFile']

		if heroFile : 
			path = heroFile.replace('/', '\\')

		else : 
			path = self.assetInfo[item]['publishPath'].replace('/', '\\')
			
		if os.path.exists(path) : 
			menu = 'Open in Explorer'
			status = True

		else : 
			menu = 'Path not exists'
			status = False

		return menu, status


	def menuCommand(self, command, listWidget) : 
		cmd = 'self.ui.%s.currentItem().text()' % listWidget
		item = str(eval(cmd))

		if ' - ' in item : 
			item = item.split(' - ')[0]

		heroFile = self.assetInfo[item]['pullFile']

		if heroFile : 
			path = heroFile.replace('/', '\\')

		else : 
			path = self.assetInfo[item]['publishPath'].replace('/', '\\')
			print path

		subprocess.Popen(r'explorer /select,"%s"' % path)
			


	# signal call button command
	def doCreateReference(self) : 

		# check allow multiple asset
		multipleAsset = True

		# get what exists in the scene
		scenePathInfo = self.getSceneAssets()

		# check create all or selected
		selOnly = self.ui.selectedReference_checkBox.isChecked()

		# read from shotgun

		if self.ui.shotgun_radioButton.isChecked() : 

			if selOnly : 
				readAssetList = self.getSelectedWidgetItem(1)

			else : 
				readAssetList = self.getAllListWidgetItem()

		if self.ui.manualBrowser_radioButton.isChecked() : 
			readAssetList = self.getSelectedWidgetItem(1)

		if readAssetList : 

			for each in readAssetList : 
				assetName = self.assetInfo[each]['code']
				namespace = assetName
				path = self.assetInfo[each]['pullFile']

				if path : 
					if not path in scenePathInfo.keys() : 
						result = hook.createReference(namespace, path)

					else : 
						# asking if want to create another reference
						title = 'Confirm create multiple reference'
						description = '%s already exists in the scene, do you still want to create reference?' % assetName
						result = self.messageBox(title, description)

						if result == QtGui.QMessageBox.Ok : 
							result = hook.createReference(namespace, path)

				else : 
					if selOnly : 
						title = 'Asset not exists'
						dialog = '%s has no approved, MASTER or published file' % assetName
						self.completeDialog(title, dialog)


		self.refreshUI()

		# read from list
		# if self.ui.manualBrowser_radioButton.isChecked() : 
		# 	readAssetList = self.getSelectedWidgetItem(1)

		

	'''
	this function get all reference in the scene and return path and number of references
	'''

	def getSceneAssets(self) : 
		allRefs = hook.getAllReferencePath()
		paths = []
		sceneAssetPathInfo = dict()

		for each in allRefs : 
			namespace = hook.getNamespace(each)
			path = each.split('{')[0]
			number = 1

			if not path in paths : 
				paths.append(path)

			else : 
				number = sceneAssetPathInfo[path]['number'] + 1

			sceneAssetPathInfo[path] = {'namespace': namespace, 'number': number}

		return sceneAssetPathInfo






	# utils =================================================================

	def getSelectedWidgetItem(self, lineText) : 
		items = self.ui.main_listWidget.selectedItems()
		allItems = []

		for item in items : 
			customWidget = self.ui.main_listWidget.itemWidget(item)

			if lineText == 1 : 
				text = customWidget.text1()

			if lineText == 2 : 
				text = customWidget.text2()

			if lineText == 3 : 
				text = customWidget.text3()
			
			allItems.append(text)

		return allItems


	def getAllListWidgetItem(self) : 
		count = self.ui.main_listWidget.count()
		items = []

		for i in range(count) : 
			item = self.ui.main_listWidget.item(i)
			customWidget = self.ui.main_listWidget.itemWidget(item)
			text1 = customWidget.text1()

			items.append(text1)


		return items


	def findMaxVersion(self, path, fileName, ext) : 
		files = fileUtils.listFile(path, ext)

		max = 0
		targetFile = str()

		for each in files : 
			if fileName in each : 
				version = each.split('.')[-2].replace('v', '')
				if version.isdigit() : 
					num = int(version)
					if num > max : 
						max = num
						targetFile = each
					
		return targetFile


	def addListWidgetItem(self, text1, text2, text3, iconPath, color, textColors, addIcon = 1, size = 90) : 		

		myCustomWidget = customQWidgetItem()
		myCustomWidget.setText1(text1)
		myCustomWidget.setText2(text2)
		myCustomWidget.setText3(text3)
		# myCustomWidget.setText4(text4)

		myCustomWidget.setTextColor1(textColors[0])
		myCustomWidget.setTextColor2(textColors[1])
		myCustomWidget.setTextColor3(textColors[2])

		if addIcon : 
			myCustomWidget.setIcon(iconPath, size)

		item = QtGui.QListWidgetItem(self.ui.main_listWidget)

		item.setSizeHint(myCustomWidget.sizeHint())
		self.ui.main_listWidget.addItem(item)
		self.ui.main_listWidget.setItemWidget(item, myCustomWidget)
		item.setBackground(QtGui.QColor(color[0], color[1], color[2]))

		
		# QtGui.QApplication.processEvents()


	def addListWidgetItem2(self, text1, text2, text3, iconPath, color, textColors, addIcon = 1, size = 90) : 		

		myCustomWidget = customQWidgetItem()
		myCustomWidget.setText1(text1)
		myCustomWidget.setText2(text2)
		myCustomWidget.setText3(text3)

		myCustomWidget.setTextColor1(textColors[0])
		myCustomWidget.setTextColor2(textColors[1])
		myCustomWidget.setTextColor3(textColors[2])

		if addIcon : 
			myCustomWidget.setIcon(iconPath, size)

		item = QtGui.QListWidgetItem(self.ui.list_listWidget)

		item.setSizeHint(myCustomWidget.sizeHint())
		self.ui.list_listWidget.addItem(item)
		self.ui.list_listWidget.setItemWidget(item, myCustomWidget)
		item.setBackground(QtGui.QColor(color[0], color[1], color[2]))


	def messageBox(self, title, description) : 
		result = QtGui.QMessageBox.question(self,title,description ,QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)

		return result



	def completeDialog(self, title, dialog) : 
		QtGui.QMessageBox.information(self, title, dialog, QtGui.QMessageBox.Ok)

		

class customQWidgetItem(QtGui.QWidget) : 
	def __init__(self, parent = None) : 
		super(customQWidgetItem, self).__init__(parent)
		# set label 
		self.textQVBoxLayout = QtGui.QVBoxLayout()
		self.text1Label = QtGui.QLabel()
		self.text2Label = QtGui.QLabel()
		self.text3Label = QtGui.QLabel()
		# self.text4Label = QtGui.QLabel()
		self.textQVBoxLayout.addWidget(self.text1Label)
		self.textQVBoxLayout.addWidget(self.text2Label)
		self.textQVBoxLayout.addWidget(self.text3Label)
		# self.textQVBoxLayout.addWidget(self.text4Label)

		# set icon
		self.allLayout = QtGui.QHBoxLayout()
		self.iconQLabel = QtGui.QLabel()
		self.allLayout.addWidget(self.iconQLabel, 0)
		self.allLayout.addLayout(self.textQVBoxLayout, 1)
		self.allLayout.setContentsMargins(2, 2, 2, 2)
		self.setLayout(self.allLayout)

		# set font
		font = QtGui.QFont()
		font.setPointSize(9)
		# font.setWeight(70)
		font.setBold(True)
		self.text1Label.setFont(font)


	def setText1(self, text) : 
		self.text1Label.setText(text)


	def setText2(self, text) : 
		self.text2Label.setText(text)


	def setText3(self, text) : 
		self.text3Label.setText(text)


	def setText4(self, text) : 
		self.text4Label.setText(text)


	def setTextColor1(self, color) : 
		self.text1Label.setStyleSheet('color: rgb(%s, %s, %s);' % (color[0], color[1], color[2]))


	def setTextColor2(self, color) : 
		self.text2Label.setStyleSheet('color: rgb(%s, %s, %s);' % (color[0], color[1], color[2]))


	def setTextColor3(self, color) : 
		self.text3Label.setStyleSheet('color: rgb(%s, %s, %s);' % (color[0], color[1], color[2]))


	def setIcon(self, iconPath, size) : 
		self.iconQLabel.setPixmap(QtGui.QPixmap(iconPath).scaled(size, size, QtCore.Qt.KeepAspectRatio))


	def text1(self) : 
		return self.text1Label.text()


	def text2(self) : 
		return self.text2Label.text()


	def text3(self) : 
		return self.text3Label.text()




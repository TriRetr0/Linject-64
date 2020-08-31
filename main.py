#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
from hashlib import sha256
from PIL import Image
import shutil
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon , QPixmap
from PyQt5.QtWidgets import QFileDialog
import GUI

if not os.path.exists("tmp"):
    os.mkdir("tmp")
NUSPackerConfig = open("./Tools/encryptKeyWith", "r")
Sha256Check2 = NUSPackerConfig.read()

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = GUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('./Ressources/meta/logo.png'))
        self.setWindowTitle('Linject-64')
        icon = "tmp/iconTex.png"
        Bootlogo = "tmp/bootLogoTex.png"
        BootTv = "tmp/bootTvTex.png"
        BootDrc = "tmp/bootDrcTex.png"
        Image.open("./Ressources/meta/iconTex.tga").save("./tmp/iconTex.png")
        image = Image.open('tmp/iconTex.png')
        new_image = image.resize((64, 64))
        new_image.save('tmp/iconTex.png')
        image = Image.open('Ressources/meta/boot.png')
        new_image = image.resize((231, 121))
        new_image.save('tmp/bootTvTex.png')
        image = Image.open('Ressources/meta/boot.png')
        new_image = image.resize((211, 121))
        new_image.save('tmp/bootDrcTex.png')
        Image.open("./Ressources/meta/bootLogoTex.tga").save("./tmp/bootLogoTex.png")
        image = Image.open('tmp/bootLogoTex.png')
        pixmap = QPixmap("tmp/iconTex.png")
        pixmap_2 = QPixmap("tmp/bootLogoTex.png")
        pixmap_3 = QPixmap("tmp/bootTvTex.png")
        pixmap_4 = QPixmap("tmp/bootDrcTex.png")
        self.ui.label_12.setPixmap(pixmap)
        self.ui.label_14.setPixmap(pixmap_2)
        self.ui.label_13.setPixmap(pixmap_3)
        self.ui.label_15.setPixmap(pixmap_4)
        self.resize(pixmap.width(), pixmap.height())
        longname1 = self.ui.lineEdit_6.text()
        longname2 = self.ui.lineEdit_6.text()
        shortname = self.ui.lineEdit_5.text()
        self.ui.toolButton.clicked.connect(self.openFile)
        self.ui.toolButton_2.clicked.connect(self.openFile_2)
        self.ui.toolButton_3.clicked.connect(self.openFile_3)
        self.ui.toolButton_4.clicked.connect(self.openFile_4)
        self.ui.pushButton.clicked.connect(self.openFile_5)
        self.ui.pushButton_2.clicked.connect(self.openFile_6)
        self.ui.pushButton_3.clicked.connect(self.openFile_7)
        self.ui.pushButton_4.clicked.connect(self.openFile_8)
        self.ui.checkBox.clicked.connect(self.longname)
        self.ui.lineEdit_4.setText(Sha256Check2)
        self.ui.lineEdit_4.editingFinished.connect(self.check)
        self.ui.pushButton_5.clicked.connect(self.copy)
        self.ui.comboBox.currentIndexChanged.connect(self.combo)

    def combo(self):
        inifile = open("./Ressources/ini configs/UCZLE0.z64.ini", "w")
        iniFile = "./Ressources/ini configs/UCZLE0.z64.ini"
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.0 US" :
            inifile.write(";Ocarina US 1.0\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801DA5CB\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.1 US" :
            inifile.write(";Ocarina US 1.1\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801DA78B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.2 US" :
            inifile.write(";Ocarina US 1.2\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801DAE8B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.0 E" :
            inifile.write(";Ocarina EU 1.0\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801D860B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.1 E" :
            inifile.write(";Ocarina EU 1.1\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801D864B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time J" :
            inifile.write(";Ocarina JAP 1.0\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801D864B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time MQ" :
            inifile.write(";Ocarina MQ\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801D8F4B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "None" :
            self.ui.lineEdit_8.setText("")

    def combo_2(self):
        inifile = open("./Ressources/ini configs/UCZLE0.z64.ini", "w")
        iniFile = "./Ressources/ini configs/UCZLE0.z64.ini"
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.0 US" :
            inifile.write(";Ocarina US 1.0\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801DA5CB\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.1 US" :
            inifile.write(";Ocarina US 1.1\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801DA78B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.2 US" :
            inifile.write(";Ocarina US 1.2\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801DAE8B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.0 E" :
            inifile.write(";Ocarina EU 1.0\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801D860B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time 1.1 E" :
            inifile.write(";Ocarina EU 1.1\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801D864B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time J" :
            inifile.write(";Ocarina JAP 1.0\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801D864B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "Zelda Ocarina of time MQ" :
            inifile.write(";Ocarina MQ\n[Cheat]\n;pause menu\nCheat0 = 2\nCheat0_Addr = 0x801D8F4B\nCheat0_Value = 0x02\nCheat0_Bytes = 1")
            self.ui.lineEdit_8.setText(f"{iniFile}")
        if self.ui.comboBox.currentText() == "None" :
            self.ui.lineEdit_8.setText("")

    def openFile(self):
        filter = "Nintendo 64 Rom(*.z64 *.v64 *.n64)"
        filename = QFileDialog.getOpenFileName(self, 'Select N64 Rom', "", filter)
        Romfile = filename[0]
        print(Romfile)
        self.ui.lineEdit.setText(f"{Romfile}")
    def openFile_2(self):
        Base = QFileDialog.getExistingDirectory(self, 'Select Base VC title (NUS Format)')
        print(Base)
        self.ui.lineEdit_2.setText(f"{Base}")
    def openFile_3(self):
        OutDir = QFileDialog.getExistingDirectory(self, 'Select output directory')
        print(OutDir)
        self.ui.lineEdit_3.setText(f"{OutDir}")
    def openFile_4(self):
        filter = "Ini(*.ini)"
        filename_4 = QFileDialog.getOpenFileName(self, 'Select .ini config file (Optional but Required for some games)', "", filter)
        iniFile = filename_4[0]
        print(iniFile)
        self.ui.lineEdit_8.setText(f"{iniFile}")
    def openFile_5(self):
        filter = "Images(*.tga *.png *.jpg .jpeg)"
        filename = QFileDialog.getOpenFileName(self, 'Select icon', "", filter)
        icon = filename[0]
        print(icon)
        image = Image.open(icon)
        new_image = image.resize((64, 64))
        new_image.save('tmp/iconTex.png')
        pixmap = QPixmap('tmp/iconTex.png')
        self.ui.label_12.setPixmap(pixmap)

    def openFile_6(self):
        filter = "Images(*.tga *.png *.jpg .jpeg)"
        filename = QFileDialog.getOpenFileName(self, 'Select Boot Tv image', "", filter)
        BootTv = filename[0]
        print(BootTv)
        image = Image.open(BootTv)
        new_image = image.resize((231, 121))
        new_image.save('tmp/bootTvTex.png')
        pixmap_3 = QPixmap('tmp/bootTvTex.png')
        self.ui.label_13.setPixmap(pixmap_3)

    def openFile_7(self):
        filter = "Images(*.tga *.png *.jpg .jpeg)"
        filename = QFileDialog.getOpenFileName(self, 'Select Boot Gamepad image', "", filter)
        BootDrc = filename[0]
        print(BootDrc)
        image = Image.open(BootDrc)
        new_image = image.resize((211, 121))
        new_image.save('tmp/bootDrcTex.png')
        pixmap_4 = QPixmap('tmp/bootDrcTex.png')
        self.ui.label_15.setPixmap(pixmap_4)

    def openFile_8(self):
        filter = "Images(*.tga *.png *.jpg .jpeg)"
        filename = QFileDialog.getOpenFileName(self, 'Select Boot logo image', "", filter)
        BootLogo = filename[0]
        print(BootLogo)
        image = Image.open(BootLogo)
        new_image = image.resize((170, 42))
        new_image.save('tmp/bootLogoTex.png')
        pixmap_2 = QPixmap('tmp/bootLogoTex.png')
        self.ui.label_14.setPixmap(pixmap_2)
        

    def check(self):
        ComKey = self.ui.lineEdit_4.text()
        Sha256Check = sha256(ComKey.rstrip().encode('utf-8')).hexdigest()
        if Sha256Check == 'ef7a8003bce6ef3243ee507dd9277f5e84e80721dd7730a3420eb5c93093d3c7':
            pixmap_5 = QPixmap("Ressources/meta/Correct.png")
            self.ui.lineEdit_4.setDisabled(True)
            CommmunKey = open("./Tools/encryptKeyWith","w")
            CommmunKey.write(ComKey)
            self.ui.label_11.setPixmap(pixmap_5)
        else:
            pixmap_5 = QPixmap("Ressources/meta/Wrong.png")
            self.ui.label_11.setPixmap(pixmap_5)

    def longname(self):
        if self.ui.checkBox.isChecked() == True :
            self.ui.lineEdit_6.setDisabled(False)
            self.ui.lineEdit_7.setDisabled(False)
        else:
            self.ui.lineEdit_6.setDisabled(True)
            self.ui.lineEdit_7.setDisabled(True)

    def copy(self):
        if os.path.exists("tmp/INJECTION TEMP") == False :
            os.mkdir("tmp/INJECTION TEMP")
        shutil.rmtree("./tmp/INJECTION TEMP")
        shortname = self.ui.lineEdit_5.text()
        longname1 = self.ui.lineEdit_6.text()
        longname2 = self.ui.lineEdit_7.text()
        Base = self.ui.lineEdit_2.text()
        Output = self.ui.lineEdit_3.text()
        Ini = self.ui.lineEdit_8.text()
        Rom = self.ui.lineEdit.text()
        Encrypt = self.ui.lineEdit_4.text()
        DstT = "./tmp/INJECTION TEMP"
        cpBase = shutil.copytree(Base, DstT)
        DstR = "./tmp/INJECTION TEMP/content/rom/UCZLE0.z64"
        cpRom = shutil.copy2(Rom, DstR)
        shutil.rmtree("./tmp/INJECTION TEMP/content/data-sync/images")
        DstC = "./tmp/INJECTION TEMP/content/data-sync/images"
        print(self.ui.comboBox_2.currentText())
        if self.ui.comboBox_2.currentText() == "Blue (default)" :
            Color = "BLUE"
        if self.ui.comboBox_2.currentText() == "Green" :
            Color = "GREEN"
        if self.ui.comboBox_2.currentText() == "Orange" :
            Color = "ORANGE"
        if self.ui.lineEdit_8.text() == '' :
            print("Default ini file will be used")
        else :
            DstI = "./tmp/INJECTION TEMP/content/config/UCZLE0.z64.ini"
            cpIni = shutil.copy2(Ini, DstI)
        ColorD = f"./Ressources/meta/{Color}/images"
        print(ColorD)
        shutil.copytree(ColorD, DstC)
        TID = '{:04X}'.format(random.randint(0,32767))
        TIDExt = '{:02X}'.format(random.randint(0,255))
        metaxml = open("./tmp/INJECTION TEMP/meta/meta.xml", "w")
        metaxml.write(f'<?xml version="1.0" encoding="utf-8"?>\n<menu type="complex" access="777">\n  <version type="unsignedInt" length="4">33</version>\n  <product_code type="string" length="32">WUP-N-CZLE</product_code>\n  <content_platform type="string" length="32">WUP</content_platform>\n  <company_code type="string" length="8">0001</company_code>\n  <mastering_date type="string" length="32"></mastering_date>\n  <logo_type type="unsignedInt" length="4">0</logo_type>\n  <app_launch_type type="hexBinary" length="4">00000000</app_launch_type>\n  <invisible_flag type="hexBinary" length="4">00000000</invisible_flag>\n  <no_managed_flag type="hexBinary" length="4">00000000</no_managed_flag>\n  <no_event_log type="hexBinary" length="4">00000000</no_event_log>\n  <no_icon_database type="hexBinary" length="4">00000000</no_icon_database>\n  <launching_flag type="hexBinary" length="4">00000005</launching_flag>\n  <install_flag type="hexBinary" length="4">00000000</install_flag>\n  <closing_msg type="unsignedInt" length="4">0</closing_msg>\n  <title_version type="unsignedInt" length="4">16</title_version>\n  <title_id type="hexBinary" length="8">00050000{TID}{TIDExt}FF</title_id>\n  <group_id type="hexBinary" length="4">0000{TID}</group_id>\n  <boss_id type="hexBinary" length="8">0000000000000000</boss_id>\n  <os_version type="hexBinary" length="8">000500101000400A</os_version>\n  <app_size type="hexBinary" length="8">0000000000000000</app_size>\n  <common_save_size type="hexBinary" length="8">0000000000000000</common_save_size>\n  <account_save_size type="hexBinary" length="8">0000000002000000</account_save_size>\n  <common_boss_size type="hexBinary" length="8">0000000000000000</common_boss_size>\n  <account_boss_size type="hexBinary" length="8">0000000000000000</account_boss_size>\n  <save_no_rollback type="unsignedInt" length="4">0</save_no_rollback>\n  <join_game_id type="hexBinary" length="4">00000000</join_game_id>\n  <join_game_mode_mask type="hexBinary" length="8">0000000000000000</join_game_mode_mask>\n  <bg_daemon_enable type="unsignedInt" length="4">1</bg_daemon_enable>\n  <olv_accesskey type="unsignedInt" length="4">1343397927</olv_accesskey>\n  <wood_tin type="unsignedInt" length="4">0</wood_tin>\n  <e_manual type="unsignedInt" length="4">1</e_manual>\n  <e_manual_version type="unsignedInt" length="4">0</e_manual_version>\n  <region type="hexBinary" length="4">00000006</region>\n  <pc_cero type="unsignedInt" length="4">128</pc_cero>\n  <pc_esrb type="unsignedInt" length="4">6</pc_esrb>\n  <pc_bbfc type="unsignedInt" length="4">192</pc_bbfc>\n  <pc_usk type="unsignedInt" length="4">0</pc_usk>\n  <pc_pegi_gen type="unsignedInt" length="4">3</pc_pegi_gen>\n  <pc_pegi_fin type="unsignedInt" length="4">192</pc_pegi_fin>\n  <pc_pegi_prt type="unsignedInt" length="4">4</pc_pegi_prt>\n  <pc_pegi_bbfc type="unsignedInt" length="4">3</pc_pegi_bbfc>\n  <pc_cob type="unsignedInt" length="4">0</pc_cob>\n  <pc_grb type="unsignedInt" length="4">128</pc_grb>\n  <pc_cgsrr type="unsignedInt" length="4">128</pc_cgsrr>\n  <pc_oflc type="unsignedInt" length="4">0</pc_oflc>\n  <pc_reserved0 type="unsignedInt" length="4">192</pc_reserved0>\n  <pc_reserved1 type="unsignedInt" length="4">192</pc_reserved1>\n  <pc_reserved2 type="unsignedInt" length="4">192</pc_reserved2>\n  <pc_reserved3 type="unsignedInt" length="4">192</pc_reserved3>\n  <ext_dev_nunchaku type="unsignedInt" length="4">0</ext_dev_nunchaku>\n  <ext_dev_classic type="unsignedInt" length="4">0</ext_dev_classic>\n  <ext_dev_urcc type="unsignedInt" length="4">0</ext_dev_urcc>\n  <ext_dev_board type="unsignedInt" length="4">0</ext_dev_board>\n  <ext_dev_usb_keyboard type="unsignedInt" length="4">0</ext_dev_usb_keyboard>\n  <ext_dev_etc type="unsignedInt" length="4">0</ext_dev_etc>\n  <ext_dev_etc_name type="string" length="512"></ext_dev_etc_name>\n  <eula_version type="unsignedInt" length="4">0</eula_version>\n  <drc_use type="unsignedInt" length="4">1</drc_use>\n  <network_use type="unsignedInt" length="4">1</network_use>\n  <online_account_use type="unsignedInt" length="4">0</online_account_use>\n  <direct_boot type="unsignedInt" length="4">0</direct_boot>\n  <reserved_flag0 type="hexBinary" length="4">00010001</reserved_flag0>\n  <reserved_flag1 type="hexBinary" length="4">00000000</reserved_flag1>\n  <reserved_flag2 type="hexBinary" length="4">00000000</reserved_flag2>\n  <reserved_flag3 type="hexBinary" length="4">00000000</reserved_flag3>\n  <reserved_flag4 type="hexBinary" length="4">00000000</reserved_flag4>\n  <reserved_flag5 type="hexBinary" length="4">00000000</reserved_flag5>\n  <reserved_flag6 type="hexBinary" length="4">00000003</reserved_flag6>\n  <reserved_flag7 type="hexBinary" length="4">00000001</reserved_flag7>\n  <longname_ja type="string" length="512">{longname1}\n{longname2}</longname_ja>\n  <longname_en type="string" length="512">{longname1}\n{longname2}</longname_en>\n  <longname_fr type="string" length="512">{longname1}\n{longname2}</longname_fr>\n  <longname_de type="string" length="512">{longname1}\n{longname2}</longname_de>\n  <longname_it type="string" length="512">{longname1}\n{longname2}</longname_it>\n  <longname_es type="string" length="512">{longname1}\n{longname2}</longname_es>\n  <longname_zhs type="string" length="512">{longname1}\n{longname2}</longname_zhs>\n  <longname_ko type="string" length="512">{longname1}\n{longname2}</longname_ko>\n  <longname_nl type="string" length="512">{longname1}\n{longname2}</longname_nl>\n  <longname_pt type="string" length="512">{longname1}\n{longname2}</longname_pt>\n  <longname_ru type="string" length="512">{longname1}\n{longname2}</longname_ru>\n  <longname_zht type="string" length="512">{longname1}\n{longname2}W</longname_zht>\n  <shortname_ja type="string" length="256">{shortname}</shortname_ja>\n  <shortname_en type="string" length="256">{shortname}</shortname_en>\n  <shortname_fr type="string" length="256">{shortname}</shortname_fr>\n  <shortname_de type="string" length="256">{shortname}</shortname_de>\n  <shortname_it type="string" length="256">{shortname}</shortname_it>\n  <shortname_es type="string" length="256">{shortname}</shortname_es>\n  <shortname_zhs type="string" length="256">{shortname}</shortname_zhs>\n  <shortname_ko type="string" length="256">{shortname}</shortname_ko>\n  <shortname_nl type="string" length="256">{shortname}</shortname_nl>\n  <shortname_pt type="string" length="256">{shortname}</shortname_pt>\n  <shortname_ru type="string" length="256">{shortname}</shortname_ru>\n  <shortname_zht type="string" length="256">{shortname}</shortname_zht>\n  <publisher_ja type="string" length="256"></publisher_ja>\n  <publisher_en type="string" length="256">Nintendo</publisher_en>\n  <publisher_fr type="string" length="256"></publisher_fr>\n  <publisher_de type="string" length="256"></publisher_de>\n  <publisher_it type="string" length="256"></publisher_it>\n  <publisher_es type="string" length="256"></publisher_es>\n  <publisher_zhs type="string" length="256"></publisher_zhs>\n  <publisher_ko type="string" length="256"></publisher_ko>\n  <publisher_nl type="string" length="256"></publisher_nl>  <publisher_pt type="string" length="256"></publisher_pt>\n  <publisher_ru type="string" length="256"></publisher_ru>\n  <publisher_zht type="string" length="256"></publisher_zht>\n  <add_on_unique_id0 type="hexBinary" length="4">00000000</add_on_unique_id0>\n  <add_on_unique_id1 type="hexBinary" length="4">00000000</add_on_unique_id1>\n  <add_on_unique_id2 type="hexBinary" length="4">00000000</add_on_unique_id2>\n  <add_on_unique_id3 type="hexBinary" length="4">00000000</add_on_unique_id3>\n  <add_on_unique_id4 type="hexBinary" length="4">00000000</add_on_unique_id4>\n  <add_on_unique_id5 type="hexBinary" length="4">00000000</add_on_unique_id5>\n  <add_on_unique_id6 type="hexBinary" length="4">00000000</add_on_unique_id6>\n  <add_on_unique_id7 type="hexBinary" length="4">00000000</add_on_unique_id7>\n  <add_on_unique_id8 type="hexBinary" length="4">00000000</add_on_unique_id8>\n  <add_on_unique_id9 type="hexBinary" length="4">00000000</add_on_unique_id9>\n  <add_on_unique_id10 type="hexBinary" length="4">00000000</add_on_unique_id10>\n  <add_on_unique_id11 type="hexBinary" length="4">00000000</add_on_unique_id11>\n  <add_on_unique_id12 type="hexBinary" length="4">00000000</add_on_unique_id12>\n  <add_on_unique_id13 type="hexBinary" length="4">00000000</add_on_unique_id13>\n  <add_on_unique_id14 type="hexBinary" length="4">00000000</add_on_unique_id14>\n  <add_on_unique_id15 type="hexBinary" length="4">00000000</add_on_unique_id15>\n  <add_on_unique_id16 type="hexBinary" length="4">00000000</add_on_unique_id16>\n  <add_on_unique_id17 type="hexBinary" length="4">00000000</add_on_unique_id17>\n  <add_on_unique_id18 type="hexBinary" length="4">00000000</add_on_unique_id18>\n  <add_on_unique_id19 type="hexBinary" length="4">00000000</add_on_unique_id19>\n  <add_on_unique_id20 type="hexBinary" length="4">00000000</add_on_unique_id20>\n  <add_on_unique_id21 type="hexBinary" length="4">00000000</add_on_unique_id21>\n  <add_on_unique_id22 type="hexBinary" length="4">00000000</add_on_unique_id22>\n  <add_on_unique_id23 type="hexBinary" length="4">00000000</add_on_unique_id23>\n  <add_on_unique_id24 type="hexBinary" length="4">00000000</add_on_unique_id24>\n  <add_on_unique_id25 type="hexBinary" length="4">00000000</add_on_unique_id25>\n  <add_on_unique_id26 type="hexBinary" length="4">00000000</add_on_unique_id26>\n  <add_on_unique_id27 type="hexBinary" length="4">00000000</add_on_unique_id27>\n  <add_on_unique_id28 type="hexBinary" length="4">00000000</add_on_unique_id28>\n  <add_on_unique_id29 type="hexBinary" length="4">00000000</add_on_unique_id29>\n  <add_on_unique_id30 type="hexBinary" length="4">00000000</add_on_unique_id30>\n  <add_on_unique_id31 type="hexBinary" length="4">00000000</add_on_unique_id31>\n</menu>')
        os.system(f'java -jar ./Tools/NUSPacker.jar -in "{Base}" -out "{Output}" -tID 00050000{TID}{TIDExt}FF -encryptKeyWith {Encrypt}')
        print(Encrypt)
        

        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

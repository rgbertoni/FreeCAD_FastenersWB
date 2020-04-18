# -*- coding: utf-8 -*-
##########################################################################
#
#  InitGui.py
#
#  Copyright 2015 Shai Seger <shaise at gmail dot com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
##########################################################################

import fnwb_locator
fnWBpath = os.path.dirname(fnwb_locator.__file__)
fnWB_icons_path = os.path.join(fnWBpath, 'Icons')

global main_fnWB_Icon
main_fnWB_Icon = os.path.join(fnWB_icons_path, 'FNLogo.svg')

FASTENERSWB_VERSION = 'V0.3.13'


class FastenersWorkbench (Workbench):

    global main_fnWB_Icon

    MenuText = "Fasteners"
    ToolTip = "Create ISO Fasteners"
    Icon = main_fnWB_Icon

    def Initialize(self):
        "This function is executed when FreeCAD starts"
        import os
        import FastenerBase
        import FSScrewCalc
        import PEMInserts
        import FastenersCmd
        import FSNuts
        import CountersunkHoles
        import FSChangeParams
        self.list = []
        cmdlist = FastenerBase.FSGetCommands("command")
        self.appendToolbar("FS Commands", cmdlist)
        self.list.extend(cmdlist)
        screwlist1 = FastenerBase.FSGetCommands("screws")
        screwlist = []
        for cmd in screwlist1:
            if isinstance(cmd, tuple):  # group in sub toolbars
                #FreeCAD.Console.PrintLog("Append toolbar " + str(cmd) + "\n")
                self.appendToolbar(cmd[0], cmd[1])
                self.list.extend(cmd[1])
            else:
                screwlist.append(cmd)
        if len(screwlist) > 0:
            # creates main screw toolbar
            self.appendToolbar("FS Screws", screwlist)
            self.list.extend(screwlist)
        FreeCADGui.addIconPath(FastenerBase.iconPath)
        FreeCADGui.addPreferencePage(os.path.join(
            FastenerBase.__dir__, 'FSprefs.ui'), 'Fasteners')

        # self.appendMenu("My New Menu",self.list) # creates a new menu
        # self.appendMenu(["An existing Menu","My submenu"],self.list) #
        # appends a submenu to an existing menu

    def Activated(self):
        "This function is executed when the workbench is activated"
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def ContextMenu(self, recipient):
        "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        # add commands to the context menu
        self.appendContextMenu("My commands", self.list)

    def GetClassName(self):
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"

Gui.addWorkbench(FastenersWorkbench())


# coding: utf-8
# Python 3.11.1
'''
    tracePtLas3D 1.0

    Trace in Autocad the extent of the .las files.

    No install

    Requirements: Autocad
    External Modules: pyautocad, laspy

    Only for Windows
    Tested on Windows 10 and Autocad 2015

    :No copyright: (!) 2023 by Frédéric Coulon.
    :No license: Do with it what you want.
'''
from pyautocad import Autocad, APoint
import laspy
from tkinter import Tk, filedialog, messagebox
import time

# Connect to Autocad.
acad = Autocad(create_if_not_exists=True)

def tracePtLas(acad):
    doc = acad.ActiveDocument
    #  Start message.
    acad.prompt('\ntracePtLas connected\n')
    # Files explorer
    root = Tk()
    # Hides the root window.
    root.withdraw()
    file_path = filedialog.askopenfilenames(initialdir = 'c:/',
                                        title = 'Select LAS files',
                                        filetypes = [('LAS files', '*.las')])
    # If files were found.
    if file_path:
        acad.prompt('In Progress ...\n')
        # Counters
        cpt = 0 # number of .las
        cptI = 0 # number of .las ignored
        # Loop over files.
        for fil in file_path:
            # Extract file path name.
            nf = '/'.join(fil.split('/')[-1:])[:-4]
            # Insertion unit in meter.
            doc.SetVariable('insunits', 6)
            # Counters.
            cptt = 0 # total number of points
            npt = 0 # final number of points
            # Decreased density (1 point ou of 32)
            sens = 12
            # Las reading.
            las = laspy.read(fil)
            # number of points.
            ptCount = las.header.point_count
            # We ignore files containing less than 1000 points.
            if ptCount > 1000:
                # Create layer
                doc.layers.Add('LAS_POINTS').Color = 6
                # Get Coordinates
                lx = las.X
                ly = las.Y
                lz = las.Z
                # Get scale and offset to convert coordinates.
                xscale = las.header.scales[0]
                xoffset = las.header.offsets[0]
                yscale = las.header.scales[1]
                yoffset = las.header.offsets[1]
                zscale = las.header.scales[2]
                zoffset = las.header.offsets[2]
                # Theorical coordinates of .las for block insertion.
                xm = int(((min(lx) * xscale) + xoffset) /100) * 100
                ym = int(((min(ly) * yscale) + yoffset) /100) * 100 + 100
                zm = int(((min(lz) * zscale) + zoffset) /100) * 100
                # Create a block in collection.
                bloc = doc.Blocks.Add(APoint(0, 0, 0), nf)
                # loop over points.
                while cptt < ptCount :
                    if sens == 12:
                        # Add point to relative coordinates.
                        bloc.AddPoint(APoint((lx[cptt]* xscale)+ xoffset - xm,
                                    (ly[cptt] * yscale) + yoffset - ym,
                                    (lz[cptt] * zscale) + zoffset - zm))
                        sens = 0
                        npt += 1
                    else:
                        sens += 1
                    cptt += 1
                # Inserting the block into the drawing.
                ibloc = acad.model.InsertBlock(APoint(xm, ym, zm),
                                       nf, 1, 1, 1, 0)
                ibloc.Layer = 'LAS_POINTS'
                # Focus
                acad.app.ZoomExtents()
                # Save with .las name.
                try:
                    doc.SaveAs(fil[:-3] + 'dwg')
                except:
                    doc.SaveAs(fil[:-4] + '_exc.dwg')
                # Let's calm things down.
                time.sleep(2)
                # If the file is not the latest.
                if fil != file_path[-1]:
                    ibloc.Delete()
                    doc.PurgeAll()
                cpt += 1
            else: # Add 1 to the ignored.
                cptI += 1
        # Final message.
        acad.prompt(f'\n {str(cpt)} .las processed\n\
 {str(cptI)} .las ignored\n')
    else:
        messagebox.showerror(title='Error',
                    message='No file, or you lost your way ...')
# Autocad check.
if acad:
    tracePtLas(acad)
else:
    messagebox.showerror(title='Error',
                    message='Autocad must be installed, or unknown error')

# cd c:/Data/Python/tracePtLas/
# pyinstaller --noconsole --onefile tracePtLas3D.py

# coding: utf-8
# Python 3.11.1
'''
    tracePtLas 1.0

    Trace in Autocad the extent of the .las files.

    No install

    Requirements: Autocad
    External Modules: pyautocad, laspy

    Only for Windows
    Tested on Windows 10 and Autocad 2015, 2022

    :No copyright: (!) 2023 by Frédéric Coulon.
    :No license: Do with it what you want.
'''
from pyautocad import Autocad, APoint
import laspy
from tkinter import Tk, filedialog, messagebox
import time

# Connect to Autocad
acad = Autocad(create_if_not_exists=True)

def tracePtLas(acad):
    doc = acad.ActiveDocument
    #  Start message
    acad.prompt('tracePtLas connected\n')
    # Files explorer
    root = Tk()
    # Hides the root window
    root.withdraw()
    file_path = filedialog.askopenfilenames(initialdir='c:/',
                                        title='Select LAS files',
                                        filetypes=[('LAS files', '*.las')])
    # If files were found
    if file_path:
        cpt = 0
        cptI = 0
        cptt = 0
        # Loop over files
        for fil in file_path:
            cptt = 0
            sens = 33
            step = 0
            time.sleep(2)
            doc.SendCommand('(vla-open (vla-get-documents (vlax-get-acad-object)) "c:/Data/Python/tracePtLas/dwg/Lambert93.dwg")\n')
            time.sleep(4)
            doc.SendCommand('(vla-activate (vla-item (vla-get-documents (vlax-get-acad-object)) "Lambert93.dwg"))\n')
            time.sleep(3)
            # Reconnect to Autocad in the new draw.
            acad = Autocad()            
            doc = acad.ActiveDocument
            # Las reading.
            las = laspy.read(fil)
            # number of points
            ptCount = las.header.point_count
            # We ignore files containing less than 1000 points.
            if ptCount > 1000:
                # Get Coordinates
                lx = las.X
                ly = las.Y
                # Get scale and offset to convert coordinates.
                xscale = las.header.scales[0]
                xoffset = las.header.offsets[0]
                yscale = las.header.scales[1]
                yoffset = las.header.offsets[1]
                # loop over points.
                while cptt < ptCount:
                    if sens == 33:
                        acad.model.AddPoint(APoint((lx[cptt] * xscale)+xoffset,
                                        (ly[cptt] * yscale) + yoffset, 0.0))
                        sens = 0
                        step += 1
                    else:
                        sens += 1
                    cptt += 1
                acad.app.ZoomExtents()
                doc.SaveAs(fil[:-3] + 'dwg')
                time.sleep(2)
                doc.close()
                time.sleep(4)
                # Reconnect to Autocad in the drawing1.
                acad = Autocad()            
                doc = acad.ActiveDocument
                cpt += 1
            else: # Add 1 to the ignored.
                cptI += 1
        # Final message.
        acad.prompt(f'\n {str(cpt)} .las processed\n {str(cptI)} .las ignored\n')
    else:
        messagebox.showerror(title='Error',
                    message='No file, or abandonment',)
# Autocad check.
if acad:
    tracePtLas(acad)
else:
    messagebox.showerror(title='Error',
                    message='Autocad must be installed, or unknown error',)

# cd c:/Data/Python/tracePtLas/
# pyinstaller --noconsole --onefile tracePtLas.py
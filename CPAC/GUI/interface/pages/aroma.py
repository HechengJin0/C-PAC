import wx
import wx.html
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator
import pkg_resources as p


class AROMA_ICA(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile(p.resource_filename('CPAC', 'GUI/resources/html/aroma.html'))            
            
    def get_counter(self):
        return self.counter

class AromaSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Aroma_ICA Options")
        
        self.page.add(label="Run Aroma-ICA ", 
                 control=control.CHOICE_BOX, 
                 name='runICA', 
                 type=dtype.LSTR, 
                 comment="Calculate Amplitude of Low Frequency Fluctuations (ALFF) and and fractional ALFF (f/ALFF) for all voxels.", 
                 values=["Off","On"],
                 wkf_switch = True)
        
        self.page.add(label= "TR(s)",
                 control=control.TEXT_BOX, 
                 name='aroma_TR', 
                 type=dtype.NUM, 
                 values= "0.01",
                 validator = CharValidator("no-alpha"),
                 comment="Repeatation time of the input file.")


        self.page.add(label= "Dimensions",
                 control=control.TEXT_BOX, 
                 name='aroma_dim', 
                 type=dtype.NUM, 
                 values= "1",
                 validator = CharValidator("no-alpha"),
                 comment="Number of dimensions you would wish to perform analysis on.")

        
        self.page.add(label= "Denoise type",
                 control=control.CHOICE_BOX, 
                 name='aroma_denoise_type', 
                 type=dtype.STR, 
                 values= ["nonaggr","aggr"],
                 validator = CharValidator("no-alpha"),
                 comment="Types of denoising strategy:i)nonaggr-patial component regression,ii)aggr-aggressive denoising,full component regression")


        self.page.add(label="Use fnirt warp file",
                 control=control.CHOICE_BOX,
                 name='warp_file_boolean',
                 type=dtype.LSTR,
                 comment="Uses the warp file obtained from linear FNIRT transformation",
                 values=["Off","On"])
                 
        #self.page.add(label=".mat file path",
        #			  control=control.COMBO_BOX,
        #			  name='aroma_mat_file',
        #			  type=dtype.STR,
        #			  comment="Specify the path to the matfile describing the affine registration of the functional data to structural data.")
        
        #self.page.add(label="MELODIC dir",
        #			  control= control.DIR_COMBO_BOX,
        #              name ='melodic_dir',
        #			  type=dtype.STR,
        #			  comment="Specify the path to the melodic directory if you do not specify any other functional file")        
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
            
import os
import shutil

#Set this to directory path to sort files.
directory_path = "E:\\Enc\\Users\\Downloads"
image_extensions = ["jpg", "jpeg", "jpe","jif", "jfif", "jfi","png","gif","webp","tiff","tif","raw", "arw", "cr2", "nrw", "k25","bmp"]
video_extensions = ['264', '3g2', '3gp', '3gp2', '3gpp', '3gpp2', '3mm', '3p2', '60d', '787', '89', 'aaf', 'aec', 'aep', 'aepx', 'aet', 'aetx', 'ajp', 'ale', 'am', 'amc', 'amv', 'amx', 'anim', 'aqt', 'arcut', 'arf', 'asf', 'asx', 'avb', 'avc', 'avd', 'avi', 'avp', 'avs', 'avs', 'avv', 'axm', 'bdm', 'bdmv', 'bdt2', 'bdt3', 'bik', 'bin', 'bix', 'bmk', 'bnp', 'box', 'bs4', 'bsf', 'bvr', 'byu', 'camproj', 'camrec', 'camv', 'ced', 'cel', 'cine', 'cip', 'clpi', 'cmmp', 'cmmtpl', 'cmproj', 'cmrec', 'cpi', 'cst', 'cvc', 'cx3', 'd2v', 'd3v', 'dat', 'dav', 'dce', 'dck', 'dcr', 'dcr', 'ddat', 'dif', 'dir', 'divx', 'dlx', 'dmb', 'dmsd', 'dmsd3d', 'dmsm', 'dmsm3d', 'dmss', 'dmx', 'dnc', 'dpa', 'dpg', 'dream', 'dsy', 'dv', 'dv-avi', 'dv4', 'dvdmedia', 'dvr', 'dvr-ms', 'dvx', 'dxr', 'dzm', 'dzp', 'dzt', 'edl', 'evo', 'eye', 'ezt', 'f4p', 'f4v', 'fbr', 'fbr', 'fbz', 'fcp', 'fcproject', 'ffd', 'flc', 'flh', 'fli', 'flv', 'flx', 'gfp', 'gl', 'gom', 'grasp', 'gts', 'gvi', 'gvp', 'h264', 'hdmov', 'hkm', 'ifo', 'imovieproj', 'imovieproject', 'ircp', 'irf', 'ism', 'ismc', 'ismv', 'iva', 'ivf', 'ivr', 'ivs', 'izz', 'izzy', 'jss', 'jts', 'jtv', 'k3g', 'kmv', 'ktn', 'lrec', 'lsf', 'lsx', 'm15', 'm1pg', 'm1v', 'm21', 'm21', 'm2a', 'm2p', 'm2t', 'm2ts', 'm2v', 'm4e', 'm4u', 'm4v', 'm75', 'mani', 'meta', 'mgv', 'mj2', 'mjp', 'mjpg', 'mk3d', 'mkv', 'mmv', 'mnv', 'mob', 'mod', 'modd', 'moff', 'moi', 'moov', 'mov', 'movie', 'mp21', 'mp21', 'mp2v', 'mp4', 'mp4v', 'mpe', 'mpeg', 'mpeg1', 'mpeg4', 'mpf', 'mpg', 'mpg2', 'mpgindex', 'mpl', 'mpl', 'mpls', 'mpsub', 'mpv', 'mpv2', 'mqv', 'msdvd', 'mse', 'msh', 'mswmm', 'mts', 'mtv', 'mvb', 'mvc', 'mvd', 'mve', 'mvex', 'mvp', 'mvp', 'mvy', 'mxf', 'mxv', 'mys', 'ncor', 'nsv', 'nut', 'nuv', 'nvc', 'ogm', 'ogv', 'ogx', 'osp', 'otrkey', 'pac', 'par', 'pds', 'pgi', 'photoshow', 'piv', 'pjs', 'playlist', 'plproj', 'pmf', 'pmv', 'pns', 'ppj', 'prel', 'pro', 'prproj', 'prtl', 'psb', 'psh', 'pssd', 'pva', 'pvr', 'pxv', 'qt', 'qtch', 'qtindex', 'qtl', 'qtm', 'qtz', 'r3d', 'rcd', 'rcproject', 'rdb', 'rec', 'rm', 'rmd', 'rmd', 'rmp', 'rms', 'rmv', 'rmvb', 'roq', 'rp', 'rsx', 'rts', 'rts', 'rum', 'rv', 'rvid', 'rvl', 'sbk', 'sbt', 'scc', 'scm', 'scm', 'scn', 'screenflow', 'sec', 'sedprj', 'seq', 'sfd', 'sfvidcap', 'siv', 'smi', 'smi', 'smil', 'smk', 'sml', 'smv', 'spl', 'sqz', 'srt', 'ssf', 'ssm', 'stl', 'str', 'stx', 'svi', 'swf', 'swi', 'swt', 'tda3mt', 'tdx', 'thp', 'tivo', 'tix', 'tod', 'tp', 'tp0', 'tpd', 'tpr', 'trp', 'ts', 'tsp', 'ttxt', 'tvs', 'usf', 'usm', 'vc1', 'vcpf', 'vcr', 'vcv', 'vdo', 'vdr', 'vdx', 'veg', 'vem', 'vep', 'vf', 'vft', 'vfw', 'vfz', 'vgz', 'vid', 'video', 'viewlet', 'viv', 'vivo', 'vlab', 'vob', 'vp3', 'vp6', 'vp7', 'vpj', 'vro', 'vs4', 'vse', 'vsp', 'w32', 'wcp', 'webm', 'wlmp', 'wm', 'wmd', 'wmmp', 'wmv', 'wmx', 'wot', 'wp3', 'wpl', 'wtv', 'wve', 'wvx', 'xej', 'xel', 'xesc', 'xfl', 'xlmv', 'xmv', 'xvid', 'y4m', 'yog', 'yuv', 'zeg', 'zm1', 'zm2', 'zm3', '.zmv']
ppt_extensions = ["ppt","pptx"]
document_extensions = ["doc","rtf","txt","docx","odt"]
pdf_extensions = ["pdf"]
csv_extensions = ["xls","xlsx","csv"]

config_extensions = ["dll","ini","cfg","dtd","env","ppk","pem","yaml","yml","toml","json","crt","key","log"]
programs_extensions = ["c","cpp","java","asp","aspx","js","class","py","php","go","sh","html"]
archive_extensions = ["zip","rar","tar","tgz","gz","7z"]


def getDirectoryPath(extension):
    if extension.lower() in image_extensions:
        return os.path.join(directory_path,"IMAGES")
    elif extension.lower() in video_extensions:
        return os.path.join(directory_path,"VIDEOS")
    elif extension.lower() in ppt_extensions:
        return os.path.join(directory_path,"PPT")
    elif extension.lower() in document_extensions:
        return os.path.join(directory_path,"DOCS")
    elif extension.lower() in pdf_extensions:
        return os.path.join(directory_path,"PDF")
    elif extension.lower() in csv_extensions:
        return os.path.join(directory_path,"EXCEL")
    elif extension.lower() in config_extensions:
        return os.path.join(directory_path,"CONFIGS_AND_SYS")
    elif extension.lower() in programs_extensions:
        return os.path.join(directory_path,"PROGRAMS")
    elif extension.lower() in archive_extensions:
        return os.path.join(directory_path,"ARCHIVE")
    else:
        return os.path.join(directory_path,"OTHERS", extension.upper())

def move_file(file_name):
    extension = file_name.split(".")[-1]
    destination_path = getDirectoryPath(extension)
    if(not os.path.exists(destination_path)):
        os.mkdir(destination_path)
    shutil.move(os.path.join(directory_path,file_name),os.path.join(destination_path,file_name))

def getArchiveList():
    archive_list = os.listdir(os.path.join(directory_path,"ARCHIVE"))
    archive_list_modified = []
    for archive_name in archive_list:
        tarch = archive_name.split(".")
        tarch = tarch[:len(tarch)-1]
        tarch = "".join(tarch)
        archive_list_modified.append(tarch)
    return archive_list_modified


def check_exists_and_move(file_name,archive_list):
    if file_name in archive_list:
        shutil.move(os.path.join(directory_path,file_name),os.path.join(directory_path,"CAN_DELETE",file_name))


if(not os.path.exists(os.path.join(directory_path,"CAN_DELETE"))):
    os.mkdir(os.path.join(directory_path,"CAN_DELETE"))
    print("CAN_DELETE CREATED")
if(not os.path.exists(os.path.join(directory_path,"OTHERS"))):
    os.mkdir(os.path.join(directory_path,"OTHERS"))
    print("OTHERS CREATED")
    

for path in os.listdir(directory_path):
    try:
        if os.path.isfile(os.path.join(directory_path,path)):
            move_file(path)
    except Exception as e:
        print("Exception occurent")
        print(e)

archive_list = getArchiveList()
#print(archive_list)
print("Files moved, moving on to directory archive matching...")  

for file_name in os.listdir(directory_path):
    if os.path.isdir(os.path.join(directory_path,file_name)):
        check_exists_and_move(file_name,archive_list)
print("Archives Copied...")  
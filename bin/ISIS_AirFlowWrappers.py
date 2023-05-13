from airflow.decorators import task
from kalasiris import (cam2map, 
    mroctx2isis, spiceinit, ctxcal, ctxevenodd, moc2isis, 
    moccal, mocnoise50, mocevenodd, catlab,
    footprintinit, caminfo)


#global vars
si_from = ''
mr_from = ''
mr_to = ''
ctxcal_from = ''
ctxcal_to = ''
ctxevenodd_from = ''
ctxevenodd_to = ''
rename_src = ''
rename_dest = ''
cam_from = ''
cam_to = ''
cam_map = ''
moc_from = ''
moc_to = ''
moccal_from = ''
moccal_to = ''
mocnoise_from = ''
mocnoise_to = ''
mocevenodd_from = ''
mocevenodd_to = ''
matchmap = 'no'
pixres = ''
defaultrange = ''
catlab_from = ''
catlab_to = ''
fp_from = ''
fp_increase = ''
fp_inc = ''
fp_vtx = ''
fp_em = ''
fp_incedidence = ''


#CTX POW
@task(task_id='mroctx2isis')
def runmroctx2isis(ds=None, **kwargs):
    try:
        mroctx2isis(from_=mr_from, to=mr_to)
    except:
        #console warning of fail here
        pass

@task(task_id='spiceinit')
def runspiceinit(ds=None, **kwargs):
    try:
        spiceinit(from_=si_from, ckandir='yes', cksmithed='yes')
    except:
        #console warning of fail here
        pass

@task(task_id='ctxcal')
def runctxcal(ds=None, **kwargs):
    try:
        ctxcal(from_=ctxcal_from,
        to=ctxcal_to)
    except:
        #console warning of fail here
        pass

@task(task_id='ctxevenodd')
def runctxevenodd(ds=None, **kwargs):
    try:
        ctxevenodd(from_=ctxevenodd_from,
        to=ctxevenodd_to)
    except:
        #console warning of fail here
        pass

@task(task_id='cube_rename')
def runcube_rename(ds=None, **kwargs):
    try:
        #cuberename(src=rename_src,
        #dest=rename_dest)
        pass
    except:
        #console warning of fail here
        pass

@task(task_id='cam2map')
def runcam2map(ds=None, **kwargs):
    try:
        cam2map(from_=cam_to,
        to=cam_to, map=cam_map,
        matchmap='no', pixres=pixres, defaultrange=defaultrange)
    except:
        #console warning of fail here
        pass

#MOC POW
@task(task_id='moc2isis')
def runmoc2isis(ds=None, **kwargs):
    try:
        moc2isis(from_=moc_from, to=moc_to)
    except:
        #console warning of fail here
        pass

@task(task_id='spiceinit')
def runspiceinit(ds=None, **kwargs):
    try:
        spiceinit(from_=si_from, ckandir='yes', cksmithed='yes')
    except:
        #console warning of fail here
        pass

@task(task_id='moccal')
def runmoccal(ds=None, **kwargs):
    try:
        moccal(from_=moccal_from,
        to=moccal_to)
    except:
        #console warning of fail here
        pass

@task(task_id='mocnoise50')
def runmocnoise50(ds=None, **kwargs):
    try:
        mocnoise50(from_=mocnoise_from,
        to=mocnoise_to)
    except:
        #console warning of fail here
        pass

@task(task_id='mocevenodd')
def runmocevenodd(ds=None, **kwargs):
    try:
        mocevenodd(from_=mocevenodd_from,
        to=mocevenodd_to)
    except:
        #console warning of fail here
        pass

@task(task_id='cube_rename')
def runcube_rename(ds=None, **kwargs):
    try:
        #cube_rename(src=rename_src,
        #dest=rename_dest)
        pass
    except:
        #console warning of fail here
        pass

@task(task_id='catlab')
def runcatlab(ds=None, **kwargs):
    try:
        catlab(from_=catlab_from, to=catlab_to)
    except:
        pass

@task(task_id='footprint_init')
def runfootprintinit(ds=None, **kwargs):
    try:
        footprintinit(from_=fp_from, increaseprecision=fp_increase,
                      inctype=fp_inc, numvertices=fp_vtx, maxemission=fp_em,
                      maxincidence=fp_incedidence)
    except:
        pass

ci_from = ''
ci_to = ''
ci_geo = ''
ci_isislbl = ''
ci_originlbl = ''
ci_stats = ''
ci_camstats = ''
ci_linc = ''
ci_sinc = ''
ci_polygon = ''
ci_inctype = ''
ci_increase = ''
ci_vtx = ''
ci_maxemission = ''
ci_maxincidence = ''
ci_spice = ''

@task(task_id='caminfo')
def runcaminfo(ds=None, **kwargs):
    try:
        caminfo(
            from_=ci_from,
            to=ci_to,
            geometry = ci_geo,
            isislabel = ci_isislbl,
            originallabel = ci_originlbl,
            statistics = ci_stats,
            camstats = ci_camstats,
            linc = ci_linc,
            sinc = ci_sinc,
            polygon = ci_polygon,
            inctype = ci_inctype,
            increaseprecision = ci_increase,
            numverticies = ci_vtx,
            maxemission = ci_maxemission,
            maxincidence = ci_maxincidence,
            spice = ci_spice
        )
    except:
        pass

gd_outputType = ''
gd_format = ''
gd_scaleParams = ''
gd_width = ''
gd_height = ''
gd_src = ''
gd_dest = ''

@task(task_id='gdal_translate')
def rungdal_translate(ds=None, **kwargs):
    try:
        #gdal_translate(outputType=gd_outputType,
        #               format=gd_format,
        #               scaleParams=gd_scaleParams,
        #               width=gd_width,
        #               height=gd_height,
        #               src=gd_src,
        #               dest=gd_dest
        #               )
        pass
    except:
        pass
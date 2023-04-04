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
moc_from = ''
moc_to = ''
moccal_from = ''
moccal_to = ''
mocnoise_from = ''
mocnoise_to = ''
mocevenodd_from = ''
mocevenodd_to = ''


#CTX POW
@task(task_id='mroctx2isis')
    def runmroctx2isis(ds=None, **kwargs):
        try:
            mroctx2isis(from=mr_from, to=mr_to)
        except:
            #console warning of fail here
            pass

@task(task_id='spiceinit')
    def runspiceinit(ds=None, **kwargs):
        try:
            spiceinit(from=si_from, ckandir='yes', cksmithed='yes')
        except:
            #console warning of fail here
            pass

@task(task_id='ctxcal')
    def runctxcal(ds=None, **kwargs):
        try:
            ctxcal(from=ctxcal_from,
            to=ctxcal_to)
        except:
            #console warning of fail here
            pass

@task(task_id='ctxevenodd')
    def runctxevenodd(ds=None, **kwargs):
        try:
            ctxevenodd(from=ctxevenodd_from,
            to=ctxevenodd_to)
        except:
            #console warning of fail here
            pass

@task(task_id='cube_rename')
    def runcube_rename(ds=None, **kwargs):
        try:
            cube_rename(src=rename_src,
            dest=rename_dest)
        except:
            #console warning of fail here
            pass

@task(task_id='cam2map')
    def runcam2map(ds=None, **kwargs):
        try:
            cam2map(from=cam_to,
            to=cam_to, map=value,
            matchmap='no', pixres=value, defaultrange=value)
        except:
            #console warning of fail here
            pass

#MOC POW
@task(task_id='moc2isis')
    def runmoc2isis(ds=None, **kwargs):
        try:
            moc2isis(from=moc_from, to=moc_to)
        except:
            #console warning of fail here
            pass

@task(task_id='spiceinit')
    def runspiceinit(ds=None, **kwargs):
        try:
            spiceinit(from=si_from, ckandir='yes', cksmithed='yes')
        except:
            #console warning of fail here
            pass

@task(task_id='moccal')
    def runmoccal(ds=None, **kwargs):
        try:
            moccal(from=moccal_from,
            to=moccal_to)
        except:
            #console warning of fail here
            pass

@task(task_id='mocnoise50')
    def runmocnoise50(ds=None, **kwargs):
        try:
            mocnoise50(from=mocnoise_from,
            to=mocnoise_to)
        except:
            #console warning of fail here
            pass

@task(task_id='mocevenodd')
    def runmocevenodd(ds=None, **kwargs):
        try:
            mocevenodd(from=mocevenodd_from,
            to=mocevenodd_to)
        except:
            #console warning of fail here
            pass

@task(task_id='cube_rename')
    def runcube_rename(ds=None, **kwargs):
        try:
            cube_rename(src=rename_src,
            dest=rename_dest)
        except:
            #console warning of fail here
            pass

@task(task_id='cam2map')
    def runcam2map(ds=None, **kwargs):
        try:
            cam2map(from=cam_from,
            to=cam_to, map=value,
            matchmap='no', pixres=value, defaultrange=value)
        except:
            #console warning of fail here
            pass
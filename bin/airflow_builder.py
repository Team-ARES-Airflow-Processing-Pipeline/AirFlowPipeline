from airflow import DAG
from airflow.decorators import task
from json_parser import parse_data, read_file
import json, ISIS3_Mods
from datetime import datetime
from ISIS3_Enums import ISIS_DAGS
import ISIS_AirFlowWrappers as wrap

def main():
    data = read_file("/home/isaiahr/src/AirFlowPipeline/bin/example_recipes.json")
    dags = parse_data(data)

    for node in dags:
        with DAG(
            dag_id=node[0],
            schedule=None, start_date=datetime.now(),
            catchup=False
        ) as dag:
            
            node.remove(node[0])
            set_order = []
            

            for (id, mod) in node:

                isis_mroctx2isis = 1
                isis_catlab = 2
                isis_spiceinit = 3
                isis_footprintinit = 4
                isis_caminfo = 5
                isis_ctxcal = 6
                isis_ctxevenodd = 7
                cube_rename = 8
                isis_cam2map = 9
                gdal_translate = 10


                def mon(func):
                    if len(set_order) == 0:
                        x = func()
                        set_order.append(x)
                    else:
                        x = func(ds=set_order[len(set_order) - 1])
                        set_order.append(x)

                if int(id) == isis_mroctx2isis: #mr
                    wrap.mr_from = mod.from_
                    wrap.mr_to = mod.to
                    mon(wrap.runmroctx2isis)

                elif int(id) == isis_spiceinit:
                    wrap.si_from = mod.from_
                    mon(wrap.runspiceinit)

                elif int(id) == isis_ctxcal:
                    wrap.ctxcal_from = mod.from_
                    wrap.ctxcal_to = mod.to
                    mon(wrap.runctxcal)

                elif int(id) == isis_ctxevenodd:
                    wrap.ctxevenodd_from = mod.from_
                    wrap.ctxevenodd_to = mod.to
                    mon(wrap.runctxevenodd)
                    
                elif int(id) == isis_cam2map:
                    wrap.cam_from = mod.from_
                    wrap.cam_to = mod.to
                    wrap.cam_map = mod.map
                    wrap.matchmap = mod.matchmap
                    wrap.pixres = mod.pixres
                    wrap.defaultrange = mod.defaultrange

                    mon(wrap.runcam2map)

                elif int(id) == isis_catlab:
                    wrap.catlab_from = mod.from_
                    wrap.catlab_to = mod.to
                    
                    mon(wrap.runcatlab)

                elif int(id) == isis_footprintinit:
                    wrap.fp_from = mod.from_
                    wrap.fp_increase = mod.increaseprecision
                    wrap.fp_inc = mod.inctype
                    wrap.fp_vtx = mod.numvertices
                    wrap.fp_em = mod.maxemission
                    wrap.fp_incedidence = mod.maxincidence

                    mon(wrap.runfootprintinit)

                elif int(id) == isis_caminfo:
                    wrap.ci_from = mod.from_
                    wrap.ci_to = mod.to
                    wrap.ci_geo = mod.geometry
                    wrap.ci_isislbl = mod.isislabel
                    wrap.ci_originlbl = mod.originallabel
                    wrap.ci_stats = mod.statistics
                    wrap.ci_camstats = mod.camstats
                    wrap.ci_linc = mod.linc
                    wrap.ci_sinc = mod.sinc
                    wrap.ci_polygon = mod.polygon
                    wrap.ci_inctype = mod.inctype
                    wrap.ci_increase = mod.increaseprecision
                    wrap.ci_vtx = mod.numvertices
                    wrap.ci_maxemission = mod.maxemission
                    wrap.ci_maxincidence = mod.maxincidence
                    wrap.ci_spice = mod.spice

                    mon(wrap.runcaminfo)
                    
                elif int(id) == cube_rename:
                    wrap.rename_src = mod.src
                    wrap.rename_dest = mod.dest
                    mon(wrap.runcube_rename)

                elif int(id) == gdal_translate:
                    wrap.gd_outputType = mod.outputType
                    wrap.gd_format = mod.format
                    wrap.gd_scaleParams = mod.scaleParams
                    wrap.gd_width = mod.width
                    wrap.gd_height = mod.height
                    wrap.gd_src = mod.src
                    wrap.gd_dest = mod.dest

                    mon(wrap.rungdal_translate)

main()
from airflow import DAG
from airflow.decorators import task
from json_parser import parse_data, read_file
import json, ISIS3_Mods
from datetime import datetime
from ISIS3_Enums import ISIS_DAGS

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
                # if len(set_order) == 0:
                #     @task(task_id=("task"+str(id)))
                #     def report_init(*kwargs):
                #         print("did it")
                #     x = report_init()
                #     set_order.append(x)
                # else:
                #     @task(task_id=("task"+str(id)))
                #     def report_init(*kwargs):
                #         print("did it")
                #     x = report_init(set_order[len(set_order) - 1])
                #     set_order.append(x)

                enum = ISIS_DAGS

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
                        x = func(set_order[len(set_order) - 1])
                        set_order.append(x)

                if int(id) == isis_mroctx2isis: #mr
                    @task(task_id="mroctx2isis")
                    def report_init(*args):
                        print("did it")
                    mon(report_init)

                elif int(id) == isis_spiceinit:
                    @task(task_id="spiceinit")
                    def spice_init(*args):
                        print("complete")
                    mon(spice_init)
                elif int(id) == isis_ctxcal:
                    @task(task_id="ctxcal")
                    def ctxcal(*args):
                        print("did it")
                    mon(ctxcal)
                elif int(id) == isis_ctxevenodd:
                    @task(task_id="ctxevenodd")
                    def ctxcal(*args):
                        print("did it")
                    mon(ctxcal)
                elif int(id) == isis_cam2map:
                    @task(task_id="cam2map")
                    def ctxcal(*args):
                        print("did it")
                    mon(ctxcal)
                elif int(id) == isis_catlab:
                    @task(task_id="catlab")
                    def ctxcal(*args):
                        print("did it")
                    mon(ctxcal)
                elif int(id) == isis_cam2map:
                    @task(task_id="cam2map")
                    def ctxcal(*args):
                        print("did it")
                    mon(ctxcal)
                elif int(id) == isis_footprintinit:
                    @task(task_id="footprintinit")
                    def footprintinit(*args):
                        print("did it")
                    mon(footprintinit)
                elif int(id) == isis_caminfo:
                    @task(task_id="caminfo")
                    def caminfo(*args):
                        print("did it")
                    mon(caminfo)
                elif int(id) == cube_rename:
                    @task(task_id="cube_rename")
                    def cuberename(*args):
                        print("did it")
                    mon(cuberename)
                elif int(id) == gdal_translate:
                    @task(task_id="gdal_translate")
                    def gdaltranslate(*args):
                        print("did it")
                    mon(gdaltranslate)

main()
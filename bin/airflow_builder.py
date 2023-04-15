from airflow import DAG
from airflow.decorators import task
from json_parser import parse_data, read_file
import ISIS_AirFlowWrappers, json, ISIS3_Enums, ISIS3_Mods
from datetime import datetime
def main():
    data = read_file("example_recipes.json")
    dags = parse_data(data)

    for node in dags:
        with DAG(
            dag_id=node[0],
            schedule=None, start_date=datetime.now(),
            catchup=False
        ) as dag:
            
            try:
                for mod in node:
                    if mod.isinstance(ISIS3_Mods.isis_mroctx2isis):
                        pass
                    elif mod.isinstance(ISIS3_Mods.isis_spiceinit):
                        pass
                    elif mod.isinstance(ISIS3_Mods.isis_ctxcal):
                        pass
                    elif mod.isinstance(ISIS3_Mods.isis_ctxevenodd):
                        pass
                    elif mod.isinstance(ISIS3_Mods.isis_ctxcal):
                        pass
                    elif mod.isinstance(ISIS3_Mods.isis_caminfo):
                        pass
                    elif mod.isinstance(ISIS3_Mods.isis_cam2map):
                        pass
                    elif mod.isinstance(ISIS3_Mods.cube_rename):
                        pass
                    elif mod.isinstance(ISIS3_Mods.gdal_translate):
                        pass
                    elif mod.isinstance(ISIS3_Mods.isis_footprintinit):
                        pass
            except:
                pass
            
            @task(task_id="print")
            def report_init():
                print("did it")
            start=report_init()
            start

main()
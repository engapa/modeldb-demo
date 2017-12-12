from modeldb.basic.ModelDbSyncerBase import *

# Create a syncer, specifying project values
syncer_obj = Syncer.create_syncer("AI - Demo Project2",  # Project Name
                                  "engapa",              # Author name
                                  "Other Demo project"   # Description
                                  )

# Sync all data from yaml file
syncer_obj.sync_all("YamlExperimentMetrics.yaml")

syncer_obj.sync()

from modeldb.basic.ModelDbSyncerBase import *

syncer_obj = Syncer.create_syncer_from_config(
  "syncer.json",  # Syncer configuration
  "sha_A1B2C3D4"  # UID, git commit sha
  )

# Create a syncer, specifying project values
# syncer_obj = Syncer.create_syncer("Sample Project",  # Project Name
#                                   "engapa",          # Author name
#                                   "Demo project"     # Description
#                                   )

# Sync all data from yaml file
syncer_obj.sync_all("YamlExperimentMetrics.yaml")

syncer_obj.sync()
